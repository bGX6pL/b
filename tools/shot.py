"""Screenshot helper (Playwright + the locally installed Microsoft Edge).

Usage:
  .venv/Scripts/python tools/shot.py URL OUT.png [--device mobile|desktop] [--full] [--consent]
                                     [--wait MS] [--scroll] [--dpr N] [--max-height PX]

  --device   mobile  = iPhone-14-like viewport 390x844 @3x, touch, mobile UA (default)
             desktop = 1440x900 @1x
  --full     capture the whole page instead of the first screen only
  --consent  try to dismiss cookie banners with the most privacy-preserving button
             (Odmítnout / Pouze nezbytné / Reject all ...) before capturing
  --scroll   scroll through the page first so lazy-loaded content renders
  --wait     extra wait in ms after load (default 2500)
  --dpr      device pixel ratio for mobile (default 3 for first screen, 2 with --full)
  --max-height  with --full, clip the capture to this many CSS px (default 7000)

URL may also be a local file path; it is converted to a file:// URL.
"""
import argparse
import pathlib
import sys
import time

from playwright.sync_api import sync_playwright

MOBILE_UA = (
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 "
    "(KHTML, like Gecko) Version/17.5 Mobile/15E148 Safari/604.1"
)

# Most privacy-preserving choices first. Matched case-insensitively against button text.
REJECT_LABELS = [
    "odmítnout vše", "odmítnout všechny", "odmítnout", "zamítnout vše", "zamítnout",
    "pouze nezbytné", "jen nezbytné", "pouze nutné", "pouze technické", "nesouhlasím",
    "odmietnuť všetko", "odmietnuť", "len nevyhnutné",
    "reject all", "reject", "decline all", "decline", "only necessary", "necessary only",
    "use necessary cookies only", "alle ablehnen", "ablehnen", "nur das nötigste",
    "nur notwendige", "nur erforderliche",
]


def dismiss_consent(page):
    frames = [page.main_frame] + [f for f in page.frames if f is not page.main_frame]
    for label in REJECT_LABELS:
        for frame in frames:
            try:
                loc = frame.get_by_role("button", name=label, exact=False)
                if loc.count() and loc.first.is_visible():
                    try:
                        loc.first.click(timeout=2000)
                    except Exception:  # covered/animating: fall back to a DOM click
                        loc.first.evaluate("e => e.click()")
                    time.sleep(0.8)
                    return label
            except Exception as e:
                print(f"consent attempt '{label}': {str(e).splitlines()[0]}", file=sys.stderr)
            try:
                loc = frame.locator(f"a:text-is('{label}'), [role=button]:text-matches('{label}', 'i')")
                if loc.count() and loc.first.is_visible():
                    loc.first.click(timeout=2000)
                    time.sleep(0.8)
                    return label
            except Exception as e:
                print(f"consent attempt '{label}': {str(e).splitlines()[0]}", file=sys.stderr)
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("url")
    ap.add_argument("out")
    ap.add_argument("--device", default="mobile", choices=["mobile", "desktop"])
    ap.add_argument("--full", action="store_true")
    ap.add_argument("--consent", action="store_true")
    ap.add_argument("--scroll", action="store_true")
    ap.add_argument("--wait", type=int, default=2500)
    ap.add_argument("--dpr", type=float, default=None)
    ap.add_argument("--max-height", type=int, default=7000)
    a = ap.parse_args()

    url = a.url
    p = pathlib.Path(url)
    if not url.startswith(("http://", "https://", "file://")) and p.exists():
        url = p.resolve().as_uri()

    out = pathlib.Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as pw:
        browser = pw.chromium.launch(channel="msedge", headless=True)
        if a.device == "mobile":
            ctx = browser.new_context(
                viewport={"width": 390, "height": 844},
                device_scale_factor=a.dpr or (2 if a.full else 3),
                is_mobile=True, has_touch=True, user_agent=MOBILE_UA, locale="cs-CZ",
            )
        else:
            ctx = browser.new_context(
                viewport={"width": 1440, "height": 900}, device_scale_factor=a.dpr or 1,
                locale="cs-CZ",
            )
        page = ctx.new_page()
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=45000)
        except Exception as e:  # still try to capture what loaded
            print(f"goto warning: {e}", file=sys.stderr)
        page.wait_for_timeout(a.wait)
        clicked = dismiss_consent(page) if a.consent else None
        if a.scroll:
            h = page.evaluate("document.body.scrollHeight")
            y = 0
            while y < h:
                y += 700
                page.evaluate(f"window.scrollTo(0, {y})")
                page.wait_for_timeout(250)
                h = page.evaluate("document.body.scrollHeight")
            page.evaluate("window.scrollTo(0, 0)")
            page.wait_for_timeout(600)
        if a.full:
            w = page.viewport_size["width"]
            h = min(page.evaluate("document.documentElement.scrollHeight"), a.max_height)
            page.screenshot(path=str(out), full_page=True, clip={"x": 0, "y": 0, "width": w, "height": h})
        else:
            page.screenshot(path=str(out))
        print(f"saved {out} (consent: {clicked})")
        browser.close()


if __name__ == "__main__":
    main()
