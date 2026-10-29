"""Renders gallery.html in fit-to-screen mode as two still images (mobile and desktop first screens of every page).

Output: screenshots/_sheet-gallery-mobile.jpg and _sheet-gallery-desktop.jpg. Serves the repo itself on a free port.
Run: .venv/Scripts/python tools/gallery_sheet.py
"""
import functools
import http.server
import pathlib
import threading

from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parents[1]


class Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a):
        pass


def main():
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), functools.partial(Quiet, directory=str(ROOT)))
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    base = f"http://127.0.0.1:{srv.server_port}/gallery.html"
    with sync_playwright() as p:
        b = p.chromium.launch(channel="msedge")
        # 2400×1500 CSS px at 2× keeps every thumbnail readable when zoomed on a phone.
        ctx = b.new_context(viewport={"width": 2400, "height": 1500}, device_scale_factor=2)
        pg = ctx.new_page()
        for view, name in [("m1", "mobile"), ("d1", "desktop")]:
            pg.goto(f"{base}?sheet=1&view={view}", wait_until="networkidle")
            pg.evaluate("document.fonts.ready")
            pg.wait_for_timeout(400)
            out = ROOT / "screenshots" / f"_sheet-gallery-{name}.jpg"
            bottom = pg.evaluate("Math.ceil(Math.max(...[...document.querySelectorAll('.card')].map(c => c.getBoundingClientRect().bottom))) + 16")
            pg.screenshot(path=str(out), type="jpeg", quality=86, clip={"x": 0, "y": 0, "width": 2400, "height": bottom})
            print(out.relative_to(ROOT), out.stat().st_size // 1024, "KB")
        b.close()
    srv.shutdown()


if __name__ == "__main__":
    main()
