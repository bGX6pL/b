"""End-to-end check of the ad tracking on the live site (public/), with test IDs and no real requests to Meta or Google.

Swaps assets/config.js for test keys, stubs the Meta Pixel and gtag scripts so every call is logged, mocks the form
endpoint, then walks three visitors through landing page → form → thank-you page:
  1. accepts cookies on the landing page,
  2. refuses cookies (must produce zero requests to Meta/Google),
  3. ignores the bar on the landing page and accepts on the thank-you page (the Lead must still be counted),
  4. the whole chain against the real function (api/lead.mjs via tools/dev_server.mjs, fake Ecomail/Meta upstream):
     form → Ecomail PDF list → token → newsletter opt-in → broker answer, plus the server-side Lead.
Run: .venv/Scripts/python -X utf8 tools/check_tracking.py   (exit code 1 on any failed check; scenario 4 needs node)
"""
import functools
import http.server
import json
import pathlib
import socket
import subprocess
import sys
import threading
import time
import urllib.request

from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parents[1]
ENDPOINT = "https://api.example.test/lead"
CONFIG = f'window.LEAD_CONFIG = {{ metaPixel: "000000000000001", ga4: "G-TEST000001", endpoint: "{ENDPOINT}" }};'
# Stand-ins for the vendor scripts: they log what the page asked for instead of sending it anywhere.
FB_STUB = ("fbq.callMethod = function () { console.log('FBQ ' + JSON.stringify([].slice.call(arguments))); };"
           "fbq.queue.forEach(function (a) { fbq.callMethod.apply(fbq, a); }); fbq.queue = [];")
GA_STUB = ("(function () { function log(a) { a = [].slice.call(a); if (a[0] === 'event' || a[0] === 'config') console.log('GTAG ' + JSON.stringify(a)); }"
           "dataLayer.forEach(log); var push = dataLayer.push; dataLayer.push = function (a) { log(a); return push.apply(dataLayer, arguments); }; })();")
MOBILE = {"viewport": {"width": 390, "height": 844}, "device_scale_factor": 1, "is_mobile": True, "has_touch": True}

fails = []


def check(ok, what):
    print(("  ok    " if ok else "  FAIL  ") + what)
    if not ok:
        fails.append(what)


class Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a):
        pass


def visitor(browser, base, consent_on):
    ctx = browser.new_context(**MOBILE)
    log, vendor_requests, posts = [], [], []
    ctx.route("**/assets/config.js", lambda r: r.fulfill(body=CONFIG, content_type="text/javascript"))
    ctx.route("https://connect.facebook.net/**", lambda r: (vendor_requests.append(r.request.url), r.fulfill(body=FB_STUB, content_type="text/javascript")))
    ctx.route("https://www.googletagmanager.com/**", lambda r: (vendor_requests.append(r.request.url), r.fulfill(body=GA_STUB, content_type="text/javascript")))

    def api(route):
        posts.append((route.request.url, json.loads(route.request.post_data or "{}")))
        route.fulfill(status=200, body=json.dumps({"id": "srv-123"}), content_type="application/json",
                      headers={"Access-Control-Allow-Origin": "*", "Access-Control-Allow-Headers": "Content-Type"})
    ctx.route(ENDPOINT + "**", api)
    pg = ctx.new_page()
    pg.on("console", lambda m: log.append(m.text) if m.text.startswith(("FBQ ", "GTAG ")) else None)
    errors = []
    pg.on("pageerror", lambda e: errors.append(str(e)))

    pg.goto(base + "/?m=5000&y=30&utm_source=meta&utm_medium=paid_social&utm_campaign=etf_tahak_2026&utm_content=ad2_uctenka&fbclid=TESTCLID")
    check(pg.locator(".consent").is_visible(), "cookie bar shows on first visit")
    check(pg.locator('[data-seg="amount"] [aria-pressed="true"]').inner_text() == "5 000"
          and pg.locator('[data-seg="years"] [aria-pressed="true"]').inner_text() == "30", "ad parameters ?m=5000&y=30 preset the receipt")
    if consent_on == "landing":
        pg.click('.consent [data-c="yes"]')
    elif consent_on == "never":
        pg.click('.consent [data-c="no"]')
    pg.locator('[data-seg="amount"] [data-v="3000"]').click()
    pg.fill("#email-hero", "jana.novakova@seznam.cz")
    pg.click('#email-hero ~ button, [data-placement="hero"] button[type="submit"]')
    pg.wait_for_url("**/dekujeme/**")
    pg.wait_for_load_state("networkidle")
    if consent_on == "thankyou":
        check(pg.locator(".consent").is_visible(), "cookie bar asks again on the thank-you page when ignored before")
        pg.click('.consent [data-c="yes"]')
    pg.wait_for_timeout(300)
    lead = json.loads(pg.evaluate("sessionStorage.getItem('lead')"))
    pg.reload(wait_until="networkidle")  # a reload must not count a second lead
    pg.wait_for_timeout(300)
    ctx.close()
    check(not errors, "no JavaScript errors" + (f": {errors}" if errors else ""))
    return log, vendor_requests, posts, lead


def endpoint_chain(browser):
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        port = s.getsockname()[1]
    srv = subprocess.Popen(["node", str(ROOT / "tools" / "dev_server.mjs"), "--port", str(port), "--fake-upstream"],
                           stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
    base = f"http://127.0.0.1:{port}"
    try:
        for _ in range(100):
            try:
                urllib.request.urlopen(base + "/__calls"); break
            except Exception:
                time.sleep(0.05)
        ctx = browser.new_context(**MOBILE)
        ctx.route("**/assets/config.js", lambda r: r.fulfill(
            body='window.LEAD_CONFIG = { metaPixel: "000000000000001", ga4: "", endpoint: "/api/lead" };', content_type="text/javascript"))
        ctx.route("https://connect.facebook.net/**", lambda r: r.fulfill(body=FB_STUB, content_type="text/javascript"))
        log = []
        pg = ctx.new_page()
        pg.on("console", lambda m: log.append(m.text) if m.text.startswith("FBQ ") else None)
        pg.goto(base + "/?m=5000&y=30&utm_source=meta&utm_content=ad2_uctenka&fbclid=E2ECLID")
        pg.click('.consent [data-c="yes"]')
        pg.fill("#email-hero", "Jana.Novakova@seznam.cz")
        pg.click('[data-placement="hero"] button[type="submit"]')
        pg.wait_for_url("**/dekujeme/**")
        pg.wait_for_load_state("networkidle")
        check("J•••@seznam.cz" in pg.locator("[data-mailnote]").inner_text(), "thank-you page shows the masked address")
        consent_text = pg.locator("[data-consent-text]").inner_text().strip()
        pg.click('[data-optin="yes"]')
        pg.click('[data-b="xtb"]')
        pg.wait_for_timeout(600)
        calls = json.loads(urllib.request.urlopen(base + "/__calls").read())
        ctx.close()
        lead = next((c for c in calls if c["path"] == "/lists/11/subscribe"), None)
        cf = lead["body"]["subscriber_data"]["custom_fields"] if lead else {}
        check(lead is not None and lead["body"]["subscriber_data"]["email"] == "jana.novakova@seznam.cz", "form → Ecomail PDF list (11) with the e-mail")
        check(cf.get("calc_amount", {}).get("value") == 5000 and cf.get("calc_years", {}).get("value") == 30 and cf.get("utm_content") == "ad2_uctenka",
              "calculator state from the ad link and UTM stored on the contact")
        fb = [json.loads(x[4:]) for x in log]
        pixel_lead = next((c for c in fb if c[:2] == ["track", "Lead"]), None)
        capi = next((c for c in calls if c["host"] == "graph.facebook.com"), None)
        check(pixel_lead is not None and capi is not None and capi["body"]["data"][0]["event_id"] == pixel_lead[3]["eventID"],
              "server Lead (Conversions API) and browser Pixel Lead share one event_id")
        check(capi is not None and capi["body"]["data"][0]["user_data"].get("fbc", "").endswith(".E2ECLID"), "fbclid from the ad reaches Meta as fbc")
        tips = next((c for c in calls if c["path"] == "/lists/12/subscribe"), None)
        check(tips is not None and tips["body"]["skip_confirmation"] is False and tips["body"]["subscriber_data"]["email"] == "jana.novakova@seznam.cz",
              "'Ano, posílejte' → tips list (12) with double opt-in, e-mail recovered from the token")
        check(tips is not None and tips["body"]["subscriber_data"]["custom_fields"].get("consent_text") == consent_text, "exact consent wording from the page stored")
        puts = [c for c in calls if c["method"] == "PUT" and c["body"]["subscriber_data"]["custom_fields"].get("broker") == "xtb"]
        check(len(puts) == 2, "broker answer stored on both lists")
    finally:
        srv.terminate()
        err = srv.communicate(timeout=5)[1].decode("utf-8", "replace").strip()
        check(not err, "dev server ran without errors" + (f": {err[:300]}" if err else ""))


def main():
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), functools.partial(Quiet, directory=str(ROOT / "public")))
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    base = f"http://127.0.0.1:{srv.server_port}"
    with sync_playwright() as p:
        b = p.chromium.launch(channel="msedge")

        print("1) accepts cookies on the landing page")
        log, vendor, posts, lead = visitor(b, base, "landing")
        fb = [json.loads(x[4:]) for x in log if x.startswith("FBQ ")]
        ga = [json.loads(x[5:]) for x in log if x.startswith("GTAG ")]
        leads = [c for c in fb if c[:2] == ["track", "Lead"]]
        check(["init", "000000000000001"] in fb, "Meta Pixel initialised with the ID from config.js")
        check(sum(c[:2] == ["track", "PageView"] for c in fb) >= 2, "PageView on landing and thank-you page")
        check(any(c[:2] == ["track", "ViewContent"] for c in fb), "ViewContent on the landing page")
        check(len(leads) == 1, f"exactly one Lead event (got {len(leads)}, page reloaded once)")
        check(any(c[:2] == ["trackCustom", "LeadFormStart"] for c in fb), "LeadFormStart custom event when the e-mail field is focused")
        lead_post = [b_ for u, b_ in posts if u == ENDPOINT]
        check(len(lead_post) == 1, "form POSTs once to the endpoint")
        if lead_post and leads:
            body = lead_post[0]
            check(leads[0][3] == {"eventID": body["event_id"]}, "Pixel Lead eventID == event_id sent to the endpoint (Conversions API de-dup)")
            check(body.get("utm_source") == "meta" and body.get("utm_content") == "ad2_uctenka" and body.get("fbclid") == "TESTCLID",
                  "UTM parameters and fbclid reach the endpoint")
            check(body.get("context", {}).get("calc_amount") == 3000 and body.get("context", {}).get("calc_years") == 30,
                  "calculator state (3 000 Kč, 30 let) reaches the endpoint")
            check(body.get("variant") == "B" and body.get("placement") == "hero", "variant and placement reach the endpoint")
        check(lead.get("id") == "srv-123", "id returned by the endpoint is kept for the thank-you page")
        check(["config", "G-TEST000001"] == ga[0][:2] if ga else False, "GA4 configured with the ID from config.js")
        check(sum(g[:2] == ["event", "generate_lead"] for g in ga) == 1, "GA4 generate_lead exactly once")
        check(any(g[:2] == ["event", "lp_view"] for g in ga) and any(g[:2] == ["event", "calc_change"] for g in ga), "GA4 lp_view and calc_change")

        print("2) refuses cookies")
        log, vendor, posts, lead = visitor(b, base, "never")
        check(not vendor, f"no request to Meta or Google ({len(vendor)} made)")
        check(not log, "no Pixel or gtag calls")
        check(len([1 for u, _ in posts if u == ENDPOINT]) == 1, "the form still works and sends the lead")

        print("3) ignores the bar on the landing page, accepts on the thank-you page")
        log, vendor, posts, lead = visitor(b, base, "thankyou")
        fb = [json.loads(x[4:]) for x in log if x.startswith("FBQ ")]
        leads = [c for c in fb if c[:2] == ["track", "Lead"]]
        check(len(leads) == 1, f"Lead still counted once (got {len(leads)})")

        print("4) real function, fake Ecomail/Meta upstream")
        endpoint_chain(b)
        b.close()
    srv.shutdown()
    print(f"\n{'ALL CHECKS PASS' if not fails else str(len(fails)) + ' FAILED'}")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
