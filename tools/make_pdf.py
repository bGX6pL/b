"""Render the lead magnet: site/tahak/tahak.html -> site/tahak/etf-tahak-2026.pdf + nahled-1.png (page-1 preview
used on the landing pages). Uses the local static server on :8765 if running, else starts one."""
import pathlib, subprocess, sys, time, urllib.request
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
PORT = 8767
srv = subprocess.Popen([sys.executable, "-m", "http.server", str(PORT), "--bind", "127.0.0.1"], cwd=SITE,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
try:
    url = f"http://127.0.0.1:{PORT}/tahak/tahak.html"
    for _ in range(50):
        try:
            urllib.request.urlopen(url); break
        except Exception:
            time.sleep(0.1)
    with sync_playwright() as pw:
        b = pw.chromium.launch(channel="msedge")
        p = b.new_page(viewport={"width": 900, "height": 1200}, device_scale_factor=2)
        p.goto(url); p.wait_for_timeout(900)
        overflow = p.evaluate("""() => [...document.querySelectorAll('.page')].map(pg => pg.scrollHeight - pg.clientHeight)""")
        if any(o > 1 for o in overflow):
            print("WARNING: page content overflows A4 by", overflow, "px")
        p.pdf(path=str(SITE / "tahak" / "etf-tahak-2026.pdf"), format="A4", print_background=True, prefer_css_page_size=True)
        p.locator("#p1").screenshot(path=str(SITE / "tahak" / "nahled-1.png"))
        p.locator("#p2").screenshot(path=str(SITE / "tahak" / "nahled-2.png"))
        b.close()
    # Light preview for the landing pages (the PNG is ~340 KB; a 640 px WebP is a fraction of that).
    from PIL import Image
    for n in (1, 2):
        im = Image.open(SITE / "tahak" / f"nahled-{n}.png").convert("RGB")
        im = im.resize((640, round(im.height * 640 / im.width)), Image.LANCZOS)
        im.save(SITE / "tahak" / f"nahled-{n}.webp", "WEBP", quality=82, method=6)
    for f in ("etf-tahak-2026.pdf", "nahled-1.png", "nahled-1.webp", "nahled-2.webp"):
        print(f, round((SITE / "tahak" / f).stat().st_size / 1024), "KB")
finally:
    srv.terminate()
