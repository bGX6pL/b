/* Lead endpoint for the live site: one Vercel function, no dependencies.
 *
 *   POST /api/lead            e-mail form → Ecomail list "PDF" (+ Meta Conversions API "Lead", only with cookie consent)
 *   POST /api/lead/consent    "Ano, posílejte" on the thank-you page → Ecomail list "tips", double opt-in
 *   POST /api/lead/profile    broker answer on the thank-you page → custom field "broker"
 * vercel.json rewrites /api/lead/:action to this function as ?action=:action.
 *
 * Environment variables (Vercel → Settings → Environment Variables):
 *   ECOMAIL_API_KEY       required. Ecomail → Manage your account → For developers
 *   ECOMAIL_LIST_PDF      required. List ID for everyone who asked for the PDF. No double opt-in (they asked for it);
 *                         an Ecomail automation on "subscribed to this list" sends e-mail 0 with the PDF. No campaigns.
 *   ECOMAIL_LIST_TIPS     required for /consent. List ID of the newsletter (4 tips + quarterly update); Ecomail sends
 *                         its double opt-in e-mail, the tips automation starts on confirmation.
 *   META_PIXEL_ID, META_CAPI_TOKEN   optional: server copy of the Lead event, de-duplicated with the Pixel by event_id
 *   META_TEST_EVENT_CODE  optional: route server events to Events Manager → Test Events while checking
 *   META_GRAPH_VERSION    optional, default v26.0
 *   LEAD_SECRET           optional: key for the token handed to the thank-you page (default: derived from ECOMAIL_API_KEY)
 *   ALLOWED_ORIGINS       optional, comma-separated extra origins allowed to post (the site's own host always is)
 *
 * The response to the form is {"id": token}: the e-mail encrypted (AES-256-GCM) with a timestamp, valid 24 h. The
 * thank-you page sends it back with /consent and /profile, so those calls work without the page ever holding the
 * e-mail and nobody can sign up someone else's address there. Logs never contain e-mail addresses.
 */
import crypto from "node:crypto";

const ECOMAIL = "https://api2.ecomailapp.cz";
const TOKEN_TTL_MS = 24 * 3600 * 1000;
const BROKERS = new Set(["xtb", "t212", "degiro", "ibkr", "fio", "revolut", "robo", "other", "none"]);
const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[a-z]{2,}$/i;
const UTM = ["utm_source", "utm_medium", "utm_campaign", "utm_content", "utm_term"];
const hits = new Map(); // per-instance rate limit; add a Vercel Firewall rule for a global one

export default {
  async fetch(request) {
    const url = new URL(request.url);
    const action = url.searchParams.get("action") || url.pathname.replace(/\/+$/, "").split("/").pop();
    if (request.method !== "POST") return json({ error: "method" }, 405, { Allow: "POST" });
    if (!originOk(request, url)) return json({ error: "origin" }, 403);
    if (!env("ECOMAIL_API_KEY") || !env("ECOMAIL_LIST_PDF")) return json({ error: "not_configured" }, 503);
    if (Number(request.headers.get("content-length") || 0) > 16384) return json({ error: "too_large" }, 413);
    let body;
    try { body = await request.json(); } catch { return json({ error: "body" }, 400); }
    if (!body || typeof body !== "object") return json({ error: "body" }, 400);
    const ip = clientIp(request);
    if (limited(action + "|" + ip, action === "lead" ? 5 : 20)) return json({ error: "rate" }, 429, { "Retry-After": "600" });
    try {
      if (action === "lead") return await lead(body, request, url, ip);
      if (action === "consent") return await consent(body);
      if (action === "profile") return await profile(body);
      return json({ error: "not_found" }, 404);
    } catch (e) {
      console.error(redact(String((e && e.message) || e)));
      return json({ error: "upstream" }, 502);
    }
  },
};

async function lead(b, request, url, ip) {
  const email = String(b.email || "").trim().toLowerCase();
  if (email.length > 254 || !EMAIL_RE.test(email)) return json({ error: "email" }, 400);
  const ctx = b.context && typeof b.context === "object" ? b.context : {};
  const fields = {
    lp_variant: str(b.variant, 10), lp_placement: str(b.placement, 20), lp_page: str(b.page, 100),
    calc_amount: int(ctx.calc_amount), calc_years: int(ctx.calc_years), calc_case: str(ctx.calc_case, 20), calc_save_czk: int(ctx.calc_save_czk),
    lead_at: new Date().toISOString(),
  };
  UTM.forEach((k) => { fields[k] = str(b[k], 200); });
  await ecomail("POST", `/lists/${env("ECOMAIL_LIST_PDF")}/subscribe`, {
    subscriber_data: { email, source: "etf-tahak-lp", custom_fields: clean(fields) },
    trigger_autoresponders: true, // the automation that sends e-mail 0 with the PDF
    update_existing: true, resubscribe: true, skip_confirmation: true, // a repeat request still gets the PDF
  });
  // A failed server event must never cost the lead; it is capped at 3 s and only logged.
  await metaLead(b, email, request, url, ip).catch((e) => console.error(redact(String(e.message || e))));
  return json({ id: seal(email) });
}

async function consent(b) {
  const email = unseal(b.id);
  if (!email) return json({ error: "token" }, 400);
  const list = env("ECOMAIL_LIST_TIPS");
  if (!list) return json({ error: "not_configured" }, 503);
  // Evidence of consent (GDPR art. 7(1)): the exact wording shown, when, where. Ecomail logs the double opt-in click.
  const fields = { consent_text: str(b.consent_text, 1000), consent_at: new Date().toISOString(), consent_page: "/dekujeme/" };
  const current = await ecomail("GET", `/lists/${list}/subscriber/${encodeURIComponent(email)}`).catch(() => null);
  if (current && current.subscriber && current.subscriber.status === 1) {
    // Already confirmed: record the renewed consent, don't send another opt-in e-mail or reset the status.
    await ecomail("PUT", `/lists/${list}/update-subscriber`, { email, subscriber_data: { custom_fields: clean(fields) } });
  } else {
    await ecomail("POST", `/lists/${list}/subscribe`, {
      subscriber_data: { email, source: "etf-tahak-dekujeme", custom_fields: clean(fields) },
      trigger_autoresponders: true, update_existing: true, resubscribe: true, skip_confirmation: false,
    });
  }
  return json({ ok: true });
}

async function profile(b) {
  const email = unseal(b.id);
  if (!email) return json({ error: "token" }, 400);
  const broker = String(b.broker || "");
  if (!BROKERS.has(broker)) return json({ error: "broker" }, 400);
  const lists = [env("ECOMAIL_LIST_PDF"), env("ECOMAIL_LIST_TIPS")].filter(Boolean);
  const done = await Promise.allSettled(lists.map((l) =>
    ecomail("PUT", `/lists/${l}/update-subscriber`, { email, subscriber_data: { custom_fields: { broker } } })));
  done.filter((r) => r.status === "rejected").forEach((r) => console.error(redact(String(r.reason && r.reason.message))));
  if (!done.some((r) => r.status === "fulfilled")) throw new Error("profile: no list updated");
  return json({ ok: true });
}

// Meta Conversions API: same event_name + event_id as the Pixel's Lead on the thank-you page, so Meta counts it once.
// Sent only when the visitor clicked "Povolit" in the cookie bar (the form sends that state as body.consent).
async function metaLead(b, email, request, url, ip) {
  const pixel = env("META_PIXEL_ID"), token = env("META_CAPI_TOKEN");
  if (!pixel || !token || b.consent !== "granted" || !b.event_id) return;
  const cookies = parseCookies(request.headers.get("cookie"));
  const fbclid = str(b.fbclid, 500);
  const event = {
    event_name: "Lead",
    event_time: Math.floor(Date.now() / 1000),
    event_id: String(b.event_id).slice(0, 100),
    action_source: "website",
    event_source_url: (request.headers.get("origin") || url.origin) + (str(b.page, 100) || "/"),
    user_data: clean({
      em: [sha256(email)],
      client_ip_address: ip,
      client_user_agent: request.headers.get("user-agent") || undefined,
      fbc: cookies._fbc || (fbclid ? `fb.1.${Date.now()}.${fbclid}` : undefined),
      fbp: cookies._fbp,
    }),
    custom_data: clean({ content_name: "ETF tahák 2026", lp_variant: str(b.variant, 10) }),
  };
  const payload = { data: [event] };
  if (env("META_TEST_EVENT_CODE")) payload.test_event_code = env("META_TEST_EVENT_CODE");
  const res = await fetch(`https://graph.facebook.com/${env("META_GRAPH_VERSION") || "v26.0"}/${encodeURIComponent(pixel)}/events?access_token=${encodeURIComponent(token)}`, {
    method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(payload), signal: AbortSignal.timeout(3000),
  });
  if (!res.ok) throw new Error(`Meta CAPI ${res.status} ${(await res.text().catch(() => "")).slice(0, 300)}`);
}

async function ecomail(method, path, body) {
  const res = await fetch(ECOMAIL + path, {
    method, headers: { key: env("ECOMAIL_API_KEY"), "Content-Type": "application/json" },
    body: body === undefined ? undefined : JSON.stringify(body), signal: AbortSignal.timeout(8000),
  });
  if (!res.ok) {
    const text = await res.text().catch(() => "");
    throw new Error(`Ecomail ${method} ${path.replace(/\/subscriber\/.*/, "/subscriber/…")} → ${res.status} ${text.slice(0, 300)}`);
  }
  return res.json().catch(() => ({}));
}

function tokenKey() {
  return crypto.createHash("sha256").update("etf-tahak/lead-token/" + (env("LEAD_SECRET") || env("ECOMAIL_API_KEY"))).digest();
}

function seal(email) {
  const iv = crypto.randomBytes(12), c = crypto.createCipheriv("aes-256-gcm", tokenKey(), iv);
  const data = Buffer.concat([c.update(JSON.stringify({ e: email, t: Date.now() }), "utf8"), c.final()]);
  return Buffer.concat([iv, c.getAuthTag(), data]).toString("base64url");
}

function unseal(token) {
  try {
    const raw = Buffer.from(String(token || ""), "base64url");
    if (raw.length < 29) return null;
    const d = crypto.createDecipheriv("aes-256-gcm", tokenKey(), raw.subarray(0, 12));
    d.setAuthTag(raw.subarray(12, 28));
    const p = JSON.parse(Buffer.concat([d.update(raw.subarray(28)), d.final()]).toString("utf8"));
    return Date.now() - p.t < TOKEN_TTL_MS && EMAIL_RE.test(p.e) ? p.e : null;
  } catch {
    return null;
  }
}

function originOk(request, url) {
  const origin = request.headers.get("origin");
  if (!origin) return true; // non-browser clients; this check only stops other websites' pages from posting
  let host;
  try { host = new URL(origin).host; } catch { return false; }
  const own = [url.host, request.headers.get("host"), request.headers.get("x-forwarded-host")];
  const extra = (env("ALLOWED_ORIGINS") || "").split(",").map((s) => s.trim()).filter(Boolean);
  return own.includes(host) || extra.includes(origin);
}

function limited(key, max, windowMs = 600000) {
  const now = Date.now(), recent = (hits.get(key) || []).filter((t) => now - t < windowMs);
  recent.push(now);
  if (hits.size > 5000) hits.clear();
  hits.set(key, recent);
  return recent.length > max;
}

function clientIp(request) {
  const xff = request.headers.get("x-forwarded-for");
  return (xff ? xff.split(",")[0] : request.headers.get("x-real-ip") || "").trim() || undefined;
}

function parseCookies(header) {
  const out = {};
  String(header || "").split(";").forEach((part) => {
    const i = part.indexOf("=");
    if (i > 0) out[part.slice(0, i).trim()] = decodeURIComponent(part.slice(i + 1).trim());
  });
  return out;
}

function json(obj, status = 200, headers = {}) {
  return Response.json(obj, { status, headers: { "Cache-Control": "no-store", ...headers } });
}

const env = (k) => (process.env[k] || "").trim();
const sha256 = (s) => crypto.createHash("sha256").update(s).digest("hex");
const str = (v, max) => (v === undefined || v === null || v === "" ? undefined : String(v).slice(0, max));
const int = (v) => (Number.isFinite(Number(v)) && v !== "" && v !== null ? { value: Math.round(Number(v)), type: "int" } : undefined);
const clean = (o) => Object.fromEntries(Object.entries(o).filter(([, v]) => v !== undefined && v !== ""));
const redact = (s) => s.replace(/[^\s"'<>@]+@[^\s"'<>]+/g, "[email]");
