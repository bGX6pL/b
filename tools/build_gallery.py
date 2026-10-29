"""Writes research/competitors/gallery-data.js for gallery.html: our 4 samples + every competitor page we captured.

Source: research/competitors/competitors.json (+ the ad-funnel variants inside it) and screenshots/ for our samples.
Run: .venv/Scripts/python -X utf8 -I tools/build_gallery.py
"""
import json
import pathlib
import sys

from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parents[1]
COMP = ROOT / "research" / "competitors"
OUT = COMP / "gallery-data.js"
THUMBS = COMP / "gallery"  # small WebP copies so every page can be on screen at once

# Pages whose cookie popup covers about half the first mobile screen or more, or dims the whole page, are left out:
# a visitor from an ad would bounce, so they are not examples worth looking at. A bottom bar below this is fine.
MAX_COOKIE_COVER = 45

GROUPS = [
    ("ours", "Our samples"),
    ("lead", "CZ/SK lead magnets"),
    ("content", "CZ content & screeners"),
    ("broker", "Brokers & robo-advisors"),
    ("intl", "International"),
]

# Our samples. Weight = bytes transferred on a mobile load before consent; cookie bar = 90 px of 844 (both measured 2026-10-29).
OURS = [
    ("a", "a-dvojce", "A · Dvojče", "Chcete VOO? Tady je jeho evropské dvojče.", "Pick a US fund → its buyable European twin with ISIN. For ad 1.", 266),
    ("b", "b-poplatky", "B · Účtenka", "Kolik vám za 20 let sebere poplatek?", "Fee calculator as a 20-year receipt: bank fund vs. VOO vs. twin. For ad 2.", 234),
    ("c", "c-srovnani", "C · Žebříček", "Srovnali jsme 20 ETF z NYSE. Tady je výsledek.", "Sortable league table; the twin column unlocks with an e-mail.", 317),
    ("d", "d-portfolio", "D · Přeložit portfolio", "Složte si portfolio z amerických ETF. Přeložíme ho do evropských.", "A US portfolio from YouTube/Reddit → a European shopping list.", 360),
]

# One card per captured landing page: (card id, record slug, screenshot prefix, short label, group, ad-funnel variant url or None).
CARDS = [
    ("xtb-ebook", "xtb-etf-ebook", "xtb-ebook", "XTB · ETF e-book", "lead", None),
    ("xtb-nemovitosti", "xtb-etf-ebook", "xtb-nemovitosti", "XTB · Nemovitosti vs. ETF", "lead", "https://vzdelavani.xtb.com/nemovitosti-vs-akcie-a-etf"),
    ("xtb-kurz", "xtb-etf-ebook", "xtb-kurz", "XTB · Portfolio course", "lead", "https://cz.xtb.com/tvorba-akcioveho-portfolia"),
    ("portu-ebook", "portu", "portu-ebook", "Portu · e-book", "lead", None),
    ("ipholky", "investovani-pro-holky", "ipholky", "Investování pro holky · e-book", "lead", None),
    ("ipholky-webinar", "investovani-pro-holky", "ipholky-webinar", "Investování pro holky · webinar", "lead",
     "https://vzdelavani.investovaniproholky.cz/pages/webinar-zdarma-investovani-jednoduse"),
    ("specialista", "specialista-na-investovanie", "specialista", "Špecialista na investovanie (SK)", "lead", None),
    ("pruvodce", "pruvodce-investicemi", "pruvodce", "Průvodce investicemi", "lead", None),
    ("finorum", "finorum", "finorum", "Finorum · US ETF → twins", "content", None),
    ("finex", "finex", "finex", "Finex · ETF screener", "content", None),
    ("finex-sp500", "finex", "finex-sp500", "Finex · S&P 500 article", "content", "https://finex.cz/nejzajimavejsi-etf-fondy-kopirujici-sp-500/"),
    ("investicniweb", "investicniweb", "investicniweb", "Investiční web · ETF", "content", None),
    ("penize", "penize", "penize", "Peníze.cz · ETF", "content", None),
    ("kurzy", "kurzy", "kurzy", "Kurzy.cz · S&P 500 UCITS", "content", None),
    ("bankovnipoplatky", "bankovnipoplatky", "bankovnipoplatky", "Bankovní poplatky", "content", None),
    ("portu-home", "portu", "portu", "Portu · homepage calculator", "broker", "https://www.portu.cz/"),
    ("fondee", "fondee", "fondee", "Direct Fondee", "broker", None),
    ("xtb-plany", "xtb-investicni-plany", "xtb-plany", "XTB · Investiční plány", "broker", None),
    ("degiro", "degiro", "degiro", "DEGIRO · Nákup ETF", "broker", None),
    ("lynx", "lynx", "lynx", "LYNX · ETF broker", "broker", None),
    ("trading212", "trading212", "trading212", "Trading 212", "broker", None),
    ("revolut", "revolut", "revolut", "Revolut · Robo poradce", "broker", None),
    ("isj", "isj-invest", "isj", "Investiční spoření jednoduše", "broker", None),
    ("euetfscan", "eu-etf-scan", "euetfscan", "EU ETF Scan · VOO", "intl", None),
    ("fec", "financial-expert-class", "fec", "Financial Expert Class", "intl", None),
    ("justetf", "justetf", "justetf", "justETF", "intl", None),
    ("extraetf", "extraetf", "extraetf", "extraETF", "intl", None),
    ("finanzfluss", "finanzfluss", "finanzfluss", "Finanzfluss · ETF-Suche", "intl", None),
    ("indexmasterclass", "index-masterclass", "indexmasterclass", "Index Masterclass", "intl", None),
]

# Stats that competitors.json notes for one page of a multi-page record (cookie_banner.note, page_weight.impression, variant notes).
OVERRIDE = {
    "xtb-nemovitosti": {"fields": 4, "cookie": 29},  # "same 4-field form … cookie bar ~29%"
    "xtb-kurz": {"fields": 4},                       # same template as the e-book page (README §1)
    "portu-ebook": {"cookie": 0, "cookie_note": "E-book LP (magazín) showed no banner."},
    "portu-home": {"cookie": 33, "kb": 2300, "fields": 0,
                   "cookie_note": "Sheet 'Dáte si k investicím koláček?' with equal-weight 'Jen nezbytné'/'Souhlasím'."},
    "ipholky-webinar": {"cookie": 0, "kb": 3000, "fields": 1, "cookie_note": "Webinar LP had none."},
    "revolut": {"cookie": 36, "dims": True},  # light entries: from first_screen
    "pruvodce": {"cookie": 48},
    # Not measured in competitors.json; read from the m1 capture (2026-10-29).
    "finex-sp500": {"cookie": 57, "dims": True, "cookie_note": "Same consent modal as the Finex screener; page dimmed."},
    "isj": {"cookie": 4, "cookie_note": "Small cookie pill at the bottom (visual estimate)."},
    **{k: {"cookie": 0, "cookie_note": "No banner in this capture."} for k in ("xtb-kurz", "investicniweb", "penize", "kurzy", "bankovnipoplatky")},
}

# Threat column of the overview table in research/competitors/README.md.
THREAT = {
    "xtb-etf-ebook": "Highest – same offer, biggest ad spend", "portu": "High – best form UX", "investovani-pro-holky": "Medium – Instagram-native",
    "specialista-na-investovanie": "Low", "finex": "Medium – SEO, brand", "finorum": "High on content – same twins pitch",
    "fondee": "Low", "xtb-investicni-plany": "Low – destination, not rival", "degiro": "Low", "lynx": "Low", "trading212": "Low",
    "justetf": "Medium – reference", "extraetf": "Reference", "finanzfluss": "Reference", "financial-expert-class": "Best-practice model",
    "eu-etf-scan": "High on concept", "index-masterclass": "Low – different price point",
}


def rel(p):
    """Path relative to the repo root (gallery.html lives there)."""
    return f"research/competitors/{p}"


def shot(prefix, kind):
    names = {"m1": [f"{prefix}-m1-raw.webp"], "full": [f"{prefix}-m-full.webp"], "d1": [f"{prefix}-d1.webp"]}[kind]
    if prefix == "finanzfluss" and kind == "m1":
        names.insert(0, "finanzfluss-m1-wait8s.webp")  # the 2.5 s capture was still blank
    for n in names:
        if (COMP / "shots" / n).exists():
            return rel(f"shots/{n}")
    return None


def as_list(v):
    if not v:
        return []
    return v if isinstance(v, list) else [v]


def make_thumbs(it):
    """t_m1 = first screen as captured, t_clean = first screen after the cookie choice, t_d1 = desktop first screen."""
    def save(im, name, width):
        im = im.convert("RGB")
        im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
        im.save(THUMBS / name, "WEBP", quality=80, method=6)
        return f"research/competitors/gallery/{name}"

    it["t_m1"] = save(Image.open(ROOT / it["m1"]), f"{it['id']}-m1.webp", 480)
    if it.get("clean"):
        it["t_clean"] = save(Image.open(ROOT / it["clean"]), f"{it['id']}-clean.webp", 480)
    elif it.get("full"):  # top of the full-page capture, which was taken after the privacy-preserving cookie click
        full = Image.open(ROOT / it["full"])
        it["t_clean"] = save(full.crop((0, 0, full.width, round(full.width * 844 / 390))), f"{it['id']}-clean.webp", 480)
    if it.get("d1"):
        it["t_d1"] = save(Image.open(ROOT / it["d1"]), f"{it['id']}-d1.webp", 800)


def main():
    data = json.loads((COMP / "competitors.json").read_text(encoding="utf-8"))
    recs = {c["slug"]: c for c in data["competitors"] + data["light_entries"]}
    missing = []
    items = []
    for key, folder, label, h1, pitch, kb in OURS:
        items.append({
            "id": f"ours-{key}", "group": "ours", "label": label, "url": f"site/{folder}/", "local": True,
            "h1": h1, "type": "Our sample", "market": "CZ", "pitch": pitch,
            "fields": 1, "cookie": 11, "dims": False, "kb": kb,
            "m1": f"screenshots/{key}-mobile-first.png", "clean": f"screenshots/{key}-mobile-first-clean.png",
            "full": f"screenshots/{key}-mobile-full.png", "d1": f"screenshots/{key}-desktop-first.png",
        })
    for cid, slug, prefix, label, group, variant in CARDS:
        r = recs.get(slug)
        if not r:
            missing.append(slug)
            continue
        var = next((v for v in r.get("ad_funnel_variants") or [] if v.get("url") == variant), None) if variant else None
        form = r.get("form") if isinstance(r.get("form"), dict) else {}
        cb = r.get("cookie_banner") if isinstance(r.get("cookie_banner"), dict) else {}
        pw = r.get("page_weight") or {}
        lm = r.get("lead_magnet")
        it = {
            "id": cid, "group": group, "label": label, "url": variant or r["url"], "local": False,
            "name": r["name"], "market": r.get("market", ""), "type": r.get("type", ""),
            "h1": (var or {}).get("h1") or r.get("h1", ""),
            "pitch": (var or {}).get("note") or r.get("first_screen_3s") or r.get("first_screen") or r.get("note", ""),
            "note": "" if variant else r.get("note", ""),
            "lead": lm.get("name") if isinstance(lm, dict) else (lm or ""),
            "fields": form.get("field_count"), "field_names": form.get("fields") or [],
            "cookie": cb.get("mobile_cover_pct"), "dims": bool(cb.get("dims_page")), "cookie_note": cb.get("note", ""),
            # Funnel variants and light entries only have weight for their own page when it was measured.
            "kb": None if variant else pw.get("transfer_kb"),
            "threat": THREAT.get(slug, ""), "steal": as_list(r.get("steal")), "avoid": as_list(r.get("avoid")),
            "m1": shot(prefix, "m1"), "full": shot(prefix, "full"), "d1": shot(prefix, "d1"),
        }
        if variant:  # the record's stats describe its main page; a variant keeps only what was noted for it
            it.update(fields=None, field_names=[], cookie=None, dims=False, cookie_note="", steal=[], avoid=[], parent=r["name"])
        it.update(OVERRIDE.get(cid, {}))
        if it["fields"] and not it["field_names"] and it["fields"] == form.get("field_count"):
            it["field_names"] = form.get("fields") or []  # same template as the parent page
        if not it["m1"]:
            missing.append(f"{cid}: m1")
        if it["cookie"] is None:
            missing.append(f"{cid}: cookie cover")
        items.append(it)
    if missing:
        print("missing:", ", ".join(missing))
        sys.exit(1)
    hidden = [i for i in items if i["cookie"] >= MAX_COOKIE_COVER or i["dims"]]
    items = [i for i in items if i not in hidden]
    print("left out (cookie popup):", ", ".join(f"{i['label']} {i['cookie']}%{' dimmed' if i['dims'] else ''}" for i in hidden))
    THUMBS.mkdir(exist_ok=True)
    for old in THUMBS.glob("*.webp"):  # this folder holds only generated thumbnails
        old.unlink()
    for it in items:
        make_thumbs(it)
    payload = {"captured": data["meta"]["captured"], "groups": [{"id": g, "label": l} for g, l in GROUPS], "items": items,
               "hidden": [{"label": i["label"], "cookie": i["cookie"], "dims": i["dims"]} for i in hidden]}
    OUT.write_text("// Generated by tools/build_gallery.py from competitors.json – do not edit.\nwindow.GALLERY = "
                   + json.dumps(payload, ensure_ascii=False, separators=(",", ":")) + ";\n", encoding="utf-8", newline="\n")
    print(f"{len(items)} pages ({len(OURS)} ours) → {OUT.relative_to(ROOT)} ({OUT.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
