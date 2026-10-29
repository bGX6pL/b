"""Compose review sheets from screenshots/: all mobile first screens side by side, desktop first screens 2×2."""
import pathlib
from PIL import Image, ImageDraw

ROOT = pathlib.Path(__file__).resolve().parents[1]
S = ROOT / "screenshots"
BG = (236, 233, 225)


def row(files, out, h=1200, gap=24):
    ims = [Image.open(S / f).convert("RGB") for f in files]
    ims = [im.resize((round(im.width * h / im.height), h), Image.LANCZOS) for im in ims]
    W = sum(i.width for i in ims) + gap * (len(ims) + 1)
    sheet = Image.new("RGB", (W, h + 2 * gap), BG)
    x = gap
    for im in ims:
        sheet.paste(im, (x, gap)); x += im.width + gap
    sheet.save(S / out, optimize=True)


def grid(files, out, w=1100, gap=24):
    ims = [Image.open(S / f).convert("RGB") for f in files]
    ims = [im.resize((w, round(im.height * w / im.width)), Image.LANCZOS) for im in ims]
    h = max(i.height for i in ims)
    sheet = Image.new("RGB", (2 * w + 3 * gap, 2 * h + 3 * gap), BG)
    for k, im in enumerate(ims):
        sheet.paste(im, (gap + (k % 2) * (w + gap), gap + (k // 2) * (h + gap)))
    sheet.save(S / out, optimize=True)


row([f"{s}-mobile-first.png" for s in "abcd"], "_sheet-mobile-first.png")
row([f"{s}-mobile-first-clean.png" for s in "abcd"], "_sheet-mobile-first-clean.png")
grid([f"{s}-desktop-first.png" for s in "abcd"], "_sheet-desktop-first.png")
row(["state-a-qqq-selected.png", "state-b-10000-30y.png", "state-c-sorted-fee.png", "state-d-three-fund.png", "state-email-typo.png", "thankyou-mobile-first.png"],
    "_sheet-states.png", h=1000)
print("ok")
