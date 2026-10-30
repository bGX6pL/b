"""Full-page captures of the live site (public/): landing + thank-you, mobile and desktop.

Output: screenshots/final-*.jpg. Serves public/ itself on a free port, so absolute paths (/assets/…) resolve as on Vercel.
Run: .venv/Scripts/python tools/capture_final.py
"""
import functools
import http.server
import json
import pathlib
import threading

from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / "screenshots"
MOBILE = {"viewport": {"width": 390, "height": 844}, "device_scale_factor": 2, "is_mobile": True, "has_touch": True}
DESKTOP = {"viewport": {"width": 1440, "height": 900}, "device_scale_factor": 1}


class Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a):
        pass


def main():
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), functools.partial(Quiet, directory=str(ROOT / "public")))
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    base = f"http://127.0.0.1:{srv.server_port}"
    lead = {"id": None, "eid": "lead-demo", "variant": "B", "masked": "j•••@seznam.cz", "placement": "hero",
            "context": {"calc_amount": 3000, "calc_years": 20, "calc_case": "typical", "calc_save_czk": 346000}}
    with sync_playwright() as p:
        b = p.chromium.launch(channel="msedge")
        for name, dev in [("mobile", MOBILE), ("desktop", DESKTOP)]:
            ctx = b.new_context(**dev)
            pg = ctx.new_page()
            errors = []
            pg.on("pageerror", lambda e: errors.append(str(e)))
            for page, path in [("landing", "/?noconsent=1"), ("thankyou", "/dekujeme/?noconsent=1")]:
                if page == "thankyou":
                    pg.evaluate(f"sessionStorage.setItem('lead', {json.dumps(json.dumps(lead))})")
                pg.goto(base + path, wait_until="networkidle")
                pg.evaluate("document.fonts.ready")
                pg.wait_for_timeout(500)
                out = OUT / f"final-{page}-{name}.jpg"
                pg.screenshot(path=str(out), full_page=True, type="jpeg", quality=82)
                over = pg.evaluate("document.documentElement.scrollWidth - innerWidth")
                print(out.relative_to(ROOT), out.stat().st_size // 1024, "KB", "overflow" if over > 0 else "", *errors)
            ctx.close()
        b.close()
    srv.shutdown()


if __name__ == "__main__":
    main()
