"""Capture the review screenshots of all four samples into screenshots/.

Per sample:  <id>-mobile-first.png        iPhone-size first screen exactly as a visitor from an ad sees it (cookie bar included)
             <id>-mobile-first-clean.png  same after "Odmítnout" (what remains on screen)
             <id>-mobile-full.png         whole page on mobile (fixed bars hidden so they don't repeat)
             <id>-desktop-first.png       1440×900 first screen
             <id>-desktop-full.png        whole page on desktop
plus interaction states (state-*.png) and the thank-you page.
Run with the repo root served:  .venv/Scripts/python tools/capture.py
"""
import pathlib, subprocess, sys, time, urllib.request
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / "screenshots"
OUT.mkdir(exist_ok=True)
PORT = 8768
BASE = f"http://127.0.0.1:{PORT}"
MOBILE = dict(viewport={"width": 390, "height": 844}, device_scale_factor=3, is_mobile=True, has_touch=True, locale="cs-CZ",
              user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Mobile/15E148 Safari/604.1")
DESKTOP = dict(viewport={"width": 1440, "height": 900}, device_scale_factor=1, locale="cs-CZ")
SAMPLES = [("a", "a-dvojce"), ("b", "b-poplatky"), ("c", "c-srovnani"), ("d", "d-portfolio")]
HIDE_FIXED = "<style>.sticky-cta,.consent{display:none!important}</style>"


def page(b, ctx_opts, path):
    ctx = b.new_context(**ctx_opts)
    p = ctx.new_page()
    p.goto(BASE + path)
    p.wait_for_timeout(900)
    return ctx, p


def decline(p):
    btn = p.get_by_role("button", name="Odmítnout")
    if btn.count():
        btn.first.click()
        p.wait_for_timeout(400)


def full(p, out, dpr_note=""):
    p.add_style_tag(content=HIDE_FIXED.replace("<style>", "").replace("</style>", ""))
    p.wait_for_timeout(200)
    p.screenshot(path=str(out), full_page=True)


srv = subprocess.Popen([sys.executable, "-m", "http.server", str(PORT), "--bind", "127.0.0.1"], cwd=ROOT / "site",
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
try:
    for _ in range(50):
        try:
            urllib.request.urlopen(BASE + "/a-dvojce/"); break
        except Exception:
            time.sleep(0.1)
    with sync_playwright() as pw:
        b = pw.chromium.launch(channel="msedge")
        shots = []
        for sid, path in SAMPLES:
            ctx, p = page(b, MOBILE, f"/{path}/")
            p.screenshot(path=str(OUT / f"{sid}-mobile-first.png")); shots.append(f"{sid}-mobile-first.png")
            decline(p)
            p.screenshot(path=str(OUT / f"{sid}-mobile-first-clean.png")); shots.append(f"{sid}-mobile-first-clean.png")
            ctx.close()
            ctx, p = page(b, dict(MOBILE, device_scale_factor=2), f"/{path}/?noconsent=1")
            full(p, OUT / f"{sid}-mobile-full.png"); shots.append(f"{sid}-mobile-full.png")
            ctx.close()
            ctx, p = page(b, DESKTOP, f"/{path}/")
            p.screenshot(path=str(OUT / f"{sid}-desktop-first.png")); shots.append(f"{sid}-desktop-first.png")
            decline(p)
            full(p, OUT / f"{sid}-desktop-full.png"); shots.append(f"{sid}-desktop-full.png")
            ctx.close()

        # interaction states (mobile, after declining cookies)
        def state(name, path, actions):
            ctx, p = page(b, MOBILE, path)
            decline(p)
            actions(p)
            p.wait_for_timeout(500)
            p.screenshot(path=str(OUT / f"state-{name}.png")); shots.append(f"state-{name}.png")
            ctx.close()

        state("a-qqq-selected", "/a-dvojce/", lambda p: p.locator('.chip[data-t="QQQ"]').click())
        state("a-sheet-open", "/a-dvojce/", lambda p: (p.mouse.wheel(0, 1400), p.wait_for_timeout(600), p.locator("[data-open-sheet='sticky']").click()))
        state("b-10000-30y", "/b-poplatky/", lambda p: (p.locator('[data-seg="amount"] [data-v="10000"]').click(), p.locator('[data-seg="years"] [data-v="30"]').click()))
        state("c-sorted-fee", "/c-srovnani/?sort=ter", lambda p: None)
        state("c-unlock-sheet", "/c-srovnani/", lambda p: p.locator(".twin--locked").nth(1).click())
        state("d-three-fund", "/d-portfolio/?p=three", lambda p: None)
        state("email-typo", "/a-dvojce/", lambda p: (p.fill("#email-hero", "jana.novakova@sezanm.cz"), p.locator("#email-hero").blur()))

        # thank-you page after a real submit from A (context echo)
        ctx, p = page(b, MOBILE, "/a-dvojce/?t=SPY")
        decline(p)
        p.fill("#email-hero", "jana@seznam.cz"); p.press("#email-hero", "Enter")
        p.wait_for_url("**/dekujeme/**"); p.wait_for_timeout(700)
        p.screenshot(path=str(OUT / "thankyou-mobile-first.png")); shots.append("thankyou-mobile-first.png")
        full(p, OUT / "thankyou-mobile-full.png"); shots.append("thankyou-mobile-full.png")
        ctx.close()
        b.close()
    print("\n".join(shots))
finally:
    srv.terminate()
