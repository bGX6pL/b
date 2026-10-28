"""Render the two ad creatives (feed 4:5 and story 9:16) from ads/creative.html to PNG.
Served over the local static server rooted at the repo (fonts need http://, not file://)."""
import pathlib, subprocess, sys, time, urllib.request
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parents[1]
PORT = 8766
SIZES = {"feed": (1080, 1350), "story": (1080, 1920)}
NAMES = {"1": "ad-1-dvojce", "2": "ad-2-uctenka"}

srv = subprocess.Popen([sys.executable, "-m", "http.server", str(PORT), "--bind", "127.0.0.1"], cwd=ROOT,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
try:
    for _ in range(50):
        try:
            urllib.request.urlopen(f"http://127.0.0.1:{PORT}/ads/creative.html"); break
        except Exception:
            time.sleep(0.1)
    with sync_playwright() as pw:
        b = pw.chromium.launch(channel="msedge")
        for ad, name in NAMES.items():
            for f, (w, h) in SIZES.items():
                p = b.new_page(viewport={"width": w, "height": h}, device_scale_factor=1)
                p.goto(f"http://127.0.0.1:{PORT}/ads/creative.html?ad={ad}&f={f}")
                p.wait_for_timeout(700)
                out = ROOT / "ads" / f"{name}-{f}.png"
                p.screenshot(path=str(out))
                print("saved", out.relative_to(ROOT))
                p.close()
        b.close()
finally:
    srv.terminate()
