/* Unit checks for api/lead.mjs with Ecomail and Meta replaced by a local fake (no network).
 * Run: node tools/check_endpoint.mjs   (exit code 1 on any failed check)
 */
import crypto from "node:crypto";

const calls = [];
let ecomailStatus = 200, subscriberStatus = null;
globalThis.fetch = async (url, opts = {}) => {
  const u = new URL(String(url));
  calls.push({ method: opts.method || "GET", host: u.host, path: u.pathname, query: Object.fromEntries(u.searchParams),
    key: opts.headers && opts.headers.key, body: opts.body ? JSON.parse(opts.body) : null });
  if (u.host === "graph.facebook.com") return Response.json({ events_received: 1 });
  if ((opts.method || "GET") === "GET") {
    return subscriberStatus ? Response.json({ subscriber: { status: subscriberStatus } }) : Response.json({ errors: ["Subscriber with email a@b.cz was not found"] }, { status: 404 });
  }
  return ecomailStatus === 200 ? Response.json({ id: 1 }) : new Response("Ecomail down for jana@seznam.cz", { status: ecomailStatus });
};
const errors = [];
console.error = (...a) => errors.push(a.join(" "));
const { default: api } = await import("../api/lead.mjs");

let fails = 0, ipN = 0;
const check = (ok, what) => { console.log((ok ? "  ok    " : "  FAIL  ") + what); if (!ok) fails++; };
const BASE = "https://etf-tahak.example";
async function post(path, body, { origin = BASE, ip, cookie, method = "POST", raw } = {}) {
  const headers = { "content-type": "application/json", "x-forwarded-for": ip || `10.0.0.${++ipN}`, "user-agent": "TestUA/1.0" };
  if (origin) headers.origin = origin;
  if (cookie) headers.cookie = cookie;
  const [p, action] = path.split("/").filter(Boolean).slice(1); // /api/lead/consent → action via rewrite
  const url = new URL(BASE + "/api/lead" + (action ? `?action=${action}` : ""));
  const res = await api.fetch(new Request(url, { method, headers, body: method === "GET" ? undefined : raw ?? JSON.stringify(body) }));
  return { status: res.status, body: await res.json().catch(() => null) };
}
const set = (o) => { for (const k of Object.keys(process.env)) if (/^(ECOMAIL|META|LEAD_SECRET|ALLOWED)/.test(k)) delete process.env[k]; Object.assign(process.env, o); };
const KEYS = { ECOMAIL_API_KEY: "test-key", ECOMAIL_LIST_PDF: "11", ECOMAIL_LIST_TIPS: "12" };
const LEAD = { email: " Jana.Novakova@Seznam.cz ", variant: "B", placement: "hero", page: "/", event_id: "lead-abc", consent: "denied",
  context: { calc_amount: 3000, calc_years: 20, calc_case: "typical", calc_save_czk: 346000 }, utm_source: "meta", utm_content: "ad2_uctenka", fbclid: "CLID" };

console.log("configuration and guards");
set({});
check((await post("/api/lead", LEAD)).status === 503, "no keys → 503 not_configured (the form shows 'try again')");
set(KEYS);
check((await post("/api/lead", null, { method: "GET" })).status === 405, "GET → 405");
check((await post("/api/lead", LEAD, { origin: "https://evil.example" })).status === 403, "post from another website → 403");
check((await post("/api/lead", null, { raw: "{not json" })).status === 400, "malformed JSON → 400");
calls.length = 0;
check((await post("/api/lead", { ...LEAD, email: "jana@seznam" })).status === 400 && calls.length === 0, "invalid e-mail → 400, Ecomail not called");
const ip = "10.9.9.9";
let last;
for (let i = 0; i < 6; i++) last = await post("/api/lead", LEAD, { ip });
check(last.status === 429, "6th lead from one IP within 10 min → 429");

console.log("lead");
calls.length = 0;
let r = await post("/api/lead", LEAD);
const sub = calls.find((c) => c.path === "/lists/11/subscribe");
check(r.status === 200 && typeof r.body.id === "string", "200 with an id");
check(!r.body.id.includes("jana") && !Buffer.from(r.body.id, "base64url").toString("latin1").includes("jana"), "the id does not contain the e-mail in clear");
check(sub && sub.host === "api2.ecomailapp.cz" && sub.method === "POST" && sub.key === "test-key", "Ecomail POST /lists/11/subscribe with the key header");
check(sub && sub.body.subscriber_data.email === "jana.novakova@seznam.cz", "e-mail trimmed and lower-cased");
check(sub && sub.body.skip_confirmation === true && sub.body.trigger_autoresponders === true && sub.body.update_existing === true,
  "PDF list: no double opt-in, starts the PDF automation, updates repeat requests");
const cf = sub ? sub.body.subscriber_data.custom_fields : {};
check(cf.calc_amount && cf.calc_amount.value === 3000 && cf.calc_amount.type === "int" && cf.calc_save_czk.value === 346000 && cf.calc_years.value === 20,
  "calculator values stored as int custom fields");
check(cf.utm_source === "meta" && cf.utm_content === "ad2_uctenka" && cf.lp_variant === "B" && cf.lp_placement === "hero", "UTM, variant, placement stored");
check(!("tags" in sub.body.subscriber_data), "no tags sent (Ecomail would overwrite the client's own tags)");
check(!calls.some((c) => c.host === "graph.facebook.com"), "consent denied → no Conversions API call");
const token = r.body.id;

console.log("Conversions API");
set({ ...KEYS, META_PIXEL_ID: "000000000000001", META_CAPI_TOKEN: "capi-token", META_TEST_EVENT_CODE: "TEST123" });
calls.length = 0;
r = await post("/api/lead", { ...LEAD, consent: "granted" }, { cookie: "_fbp=fb.1.1700000000000.123; other=1" });
const capi = calls.find((c) => c.host === "graph.facebook.com");
const ev = capi && capi.body.data[0];
check(r.status === 200 && capi && capi.path === "/v26.0/000000000000001/events" && capi.query.access_token === "capi-token", "consent granted → POST graph.facebook.com/v26.0/<pixel>/events");
check(ev && ev.event_name === "Lead" && ev.event_id === "lead-abc" && ev.action_source === "website", "event Lead with the Pixel's event_id");
check(ev && ev.user_data.em[0] === crypto.createHash("sha256").update("jana.novakova@seznam.cz").digest("hex"), "e-mail sent only as SHA-256 hash");
check(ev && ev.user_data.fbp === "fb.1.1700000000000.123" && /^fb\.1\.\d+\.CLID$/.test(ev.user_data.fbc), "fbp from cookie, fbc built from fbclid");
check(ev && ev.user_data.client_user_agent === "TestUA/1.0" && ev.user_data.client_ip_address, "IP and user agent included");
check(capi && capi.body.test_event_code === "TEST123", "test event code passed through");
calls.length = 0;
r = await post("/api/lead", { ...LEAD, consent: null });
check(r.status === 200 && !calls.some((c) => c.host === "graph.facebook.com"), "no cookie answer → no Conversions API call");
set(KEYS);

console.log("consent (newsletter, double opt-in)");
calls.length = 0; subscriberStatus = null;
r = await post("/api/lead/consent", { id: token, consent_text: "Během 10 dnů 4 e-maily…", newsletter: true });
const tips = calls.find((c) => c.path === "/lists/12/subscribe");
check(r.status === 200 && tips && tips.body.subscriber_data.email === "jana.novakova@seznam.cz", "token → subscribe to the tips list");
check(tips && tips.body.skip_confirmation === false, "tips list: double opt-in e-mail is sent (skip_confirmation false)");
check(tips && tips.body.subscriber_data.custom_fields.consent_text === "Během 10 dnů 4 e-maily…" && tips.body.subscriber_data.custom_fields.consent_at,
  "exact consent wording and time stored");
calls.length = 0; subscriberStatus = 1;
r = await post("/api/lead/consent", { id: token, consent_text: "x" });
check(r.status === 200 && calls.some((c) => c.method === "PUT" && c.path === "/lists/12/update-subscriber") && !calls.some((c) => c.path === "/lists/12/subscribe"),
  "already confirmed → fields updated, no second opt-in e-mail");
subscriberStatus = null;
const forged = Buffer.from(token, "base64url"); forged[forged.length - 1] ^= 1;
check((await post("/api/lead/consent", { id: forged.toString("base64url"), consent_text: "x" })).status === 400, "tampered token → 400");
check((await post("/api/lead/consent", { id: "jana@seznam.cz", consent_text: "x" })).status === 400, "plain e-mail instead of token → 400");
set({ ...KEYS, LEAD_SECRET: "other-secret" });
check((await post("/api/lead/consent", { id: token, consent_text: "x" })).status === 400, "token from another key → 400");
set(KEYS);
const realNow = Date.now;
Date.now = () => realNow() + 25 * 3600 * 1000;
check((await post("/api/lead/consent", { id: token, consent_text: "x" })).status === 400, "token older than 24 h → 400");
Date.now = realNow;

console.log("profile");
calls.length = 0;
r = await post("/api/lead/profile", { id: token, broker: "xtb" });
const puts = calls.filter((c) => c.method === "PUT");
check(r.status === 200 && puts.length === 2 && puts.every((c) => c.body.subscriber_data.custom_fields.broker === "xtb" && c.body.email === "jana.novakova@seznam.cz"),
  "broker stored as custom field in both lists");
check((await post("/api/lead/profile", { id: token, broker: "<script>" })).status === 400, "unknown broker → 400");

console.log("upstream failure");
ecomailStatus = 500; errors.length = 0;
r = await post("/api/lead", LEAD);
check(r.status === 502, "Ecomail error → 502 (the form says 'try again')");
check(errors.length > 0 && errors.every((e) => !/jana|seznam/i.test(e)), "error logged without the e-mail address");
ecomailStatus = 200;

console.log(fails ? `\n${fails} FAILED` : "\nALL CHECKS PASS");
process.exit(fails ? 1 : 0);
