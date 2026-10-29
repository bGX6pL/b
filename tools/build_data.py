"""Build the single source of truth for every number on the pages, the PDF and the ads.

Inputs  (research, each value with its sources):  data/raw/us-etfs-part1.json, us-etfs-part2.json,
                                                   ucits-twins.json, cz-context.json
Outputs: data/etfs.json        ground truth (chosen value + status + sources + check results)
         data/etfs.csv         flat table for spreadsheets
         docs/data-overeni.md  verification report (what was checked, what failed, how it was resolved)
         site/assets/data.js   compact data the pages/ads read

Run:  .venv/Scripts/python -I tools/build_data.py     (exit code 1 if any check FAILS)
"""
import csv
import json
import pathlib
import re
import sys
from datetime import date

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
TODAY = date(2026, 10, 29)
RETURNS_AS_OF = "2026-09-30"

sys.path.insert(0, str(ROOT / "tools"))
from curation import (LIST, REF, ASSET, US_SHARE, TWIN_LABELS, PRESETS,  # noqa: E402
                      DIST_CZ, DOMICILE_CZ, build_cz, display_name, EXPLAINED, INDEX_SHORT, issuer_short)


# ---------------------------------------------------------------- helpers
def load(name):
    p = RAW / name
    if not p.exists():
        return None
    return json.loads(p.read_text(encoding="utf-8"))


def v(etf, field):
    f = etf["fields"].get(field) or {}
    return f.get("value")


def num(x):
    if isinstance(x, (int, float)):
        return float(x)
    if isinstance(x, str):
        m = re.search(r"-?\d+(?:[.,]\d+)?", x.replace("−", "-"))
        return float(m.group(0).replace(",", ".")) if m else None
    return None


def isin_ok(isin):
    """ISO 6166 check digit: letters → numbers (A=10…Z=35), then Luhn over the digit string."""
    if not isin or not re.fullmatch(r"[A-Z]{2}[A-Z0-9]{9}\d", isin):
        return False
    digits = "".join(str(int(c, 36)) for c in isin[:-1])
    total, dbl = 0, True
    for d in reversed(digits):
        n = int(d) * (2 if dbl else 1)
        total += n // 10 + n % 10
        dbl = not dbl
    return (10 - total % 10) % 10 == int(isin[-1])


class Checks:
    def __init__(self):
        self.rows = []

    def add(self, check, subject, ok, detail, level="fail"):
        result = "pass" if ok else level
        if not ok and level == "warn":
            why = next((w for (c, s), w in EXPLAINED.items() if c == check and subject.startswith(s)), None)
            if why:
                result, detail = "explained", f"{detail} — {why}"
        self.rows.append({"check": check, "subject": subject, "result": result, "detail": detail})

    def count(self, r):
        return sum(1 for x in self.rows if x["result"] == r)


# ---------------------------------------------------------------- load
parts = [load("us-etfs-part1.json"), load("us-etfs-part2.json")]
us_raw = {}
for part in parts:
    for e in (part or {}).get("etfs", []):
        us_raw[e["ticker"]] = e
twins_raw = load("ucits-twins.json") or {"twin_sets": []}
cz_raw = load("cz-context.json") or {}

missing_inputs = [n for n, d in [("us-etfs-part1.json", parts[0]), ("us-etfs-part2.json", parts[1]),
                                 ("ucits-twins.json", load("ucits-twins.json")), ("cz-context.json", load("cz-context.json"))] if d is None]

C = Checks()

# ticker -> twin set
set_of = {}
for s in twins_raw["twin_sets"]:
    for t in s.get("us_tickers", []):
        set_of[t] = s["id"]

# ---------------------------------------------------------------- US ETF checks
TOL = {"ret_1y_pct": 0.25, "ret_5y_pct": 0.15, "ret_10y_pct": 0.15}
RANGES = {"expense_ratio_pct": (0.0, 1.0), "aum_usd_bn": (0.5, 2000), "holdings_count": (1, 15000),
          "dividend_yield_pct": (0, 12), "ret_1y_pct": (-60, 80), "ret_5y_pct": (-25, 40), "ret_10y_pct": (-15, 30)}
REQUIRED = ["exchange", "index", "expense_ratio_pct", "aum_usd_bn", "inception_date"]

for t in LIST + REF:
    e = us_raw.get(t)
    if not e:
        C.add("coverage", t, False, "ticker missing from research files")
        continue
    for f in REQUIRED:
        C.add("required field", f"{t}.{f}", v(e, f) not in (None, ""), "value present" if v(e, f) not in (None, "") else "null")
    ex = (v(e, "exchange") or "")
    if t in LIST:
        C.add("listing venue", t, ex in ("NYSE Arca", "NYSE"), f"primary listing: {ex}")
    else:
        C.add("listing venue", t, True, f"reference fund, primary listing: {ex} (shown with label)", "info")
    for f, (lo, hi) in RANGES.items():
        x = num(v(e, f))
        if x is None:
            continue
        C.add("plausible range", f"{t}.{f}", lo <= x <= hi, f"{x} within [{lo}, {hi}]" if lo <= x <= hi else f"{x} OUTSIDE [{lo}, {hi}]")
    for f in ("ret_1y_pct", "ret_5y_pct", "ret_10y_pct"):
        fo = e["fields"].get(f) or {}
        if fo.get("value") is None:
            continue
        C.add("returns date", f"{t}.{f}", fo.get("as_of") == RETURNS_AS_OF, f"as_of {fo.get('as_of')}")
    # independent sources agree?
    for f, fo in e["fields"].items():
        st = (fo or {}).get("status")
        if st == "conflict":
            C.add("source agreement", f"{t}.{f}", False, f"conflict resolved by researcher: {fo.get('note','')[:160]}", "warn")
        elif st == "single-source" and f in ("expense_ratio_pct", "aum_usd_bn", "exchange"):
            C.add("source agreement", f"{t}.{f}", False, "only one source for a headline number", "warn")
    # expense ratio: every source that reports it must say the same (fees are exact)
    fo = e["fields"].get("expense_ratio_pct") or {}
    vals = sorted({round(num(s.get("value")), 4) for s in fo.get("sources", []) if num(s.get("value")) is not None})
    if len(vals) > 1:
        C.add("fee consensus", t, False, f"sources disagree {vals}; chosen {fo.get('value')} — {fo.get('note','')[:140]}", "warn")
    elif vals:
        C.add("fee consensus", t, True, f"all sources {vals[0]} %")

# Same index ⇒ same gross return. Differences beyond the fee gap + tolerance mean a data error.
PEERS = [
    ("S&P 500", ["VOO", "IVV", "SPY", "SPYM"], 0.0),
    ("US total market", ["VTI", "ITOT", "SCHB"], 0.6),
    ("developed ex-US", ["VEA", "IEFA"], 1.2),
    ("emerging markets", ["VWO", "IEMG"], 2.0),
    ("gold", ["GLD", "IAU"], 0.05),
    ("US large growth", ["VUG", "SCHG"], 3.5),
    ("US tech", ["VGT", "XLK"], 4.0),
]
for name, group, extra in PEERS:
    present = [t for t in group if t in us_raw]
    for f, tol in TOL.items():
        pts = [(t, num(v(us_raw[t], f)), num(v(us_raw[t], "expense_ratio_pct"))) for t in present]
        pts = [p for p in pts if p[1] is not None and p[2] is not None]
        for i in range(len(pts)):
            for j in range(i + 1, len(pts)):
                a, b = pts[i], pts[j]
                gap = abs(a[1] - b[1])
                allowed = abs(a[2] - b[2]) + tol + extra
                C.add("peer consistency", f"{name}: {a[0]} vs {b[0]} {f}", gap <= allowed,
                      f"Δ {gap:.2f} pp ≤ allowed {allowed:.2f} pp" if gap <= allowed else f"Δ {gap:.2f} pp > allowed {allowed:.2f} pp — investigate",
                      "fail" if extra == 0.0 or name == "gold" else "warn")

# ---------------------------------------------------------------- twin checks
for s in twins_raw["twin_sets"]:
    pick = (s.get("pick") or {}).get("default_isin")
    cands = {c["isin"]: c for c in s.get("candidates", []) if c.get("isin")}
    C.add("twin pick exists", s["id"], pick in cands, f"default {pick}")
    for isin, c in cands.items():
        C.add("ISIN check digit", isin, isin_ok(isin), c.get("name", ""))
        dom = (c.get("domicile") or "")[:2]
        C.add("ISIN ↔ domicile", isin, isin[:2] == dom or dom == "", f"prefix {isin[:2]} vs domicile {dom}", "warn")
        ter = num((c.get("ter_pct") or {}).get("value"))
        C.add("plausible range", f"{isin}.ter", ter is not None and 0 < ter < 1.0, f"TER {ter}")
        tst = (c.get("ter_pct") or {}).get("status")
        if tst != "verified":
            C.add("source agreement", f"{isin}.ter", False, f"TER status {tst}: {(c.get('ter_pct') or {}).get('note','')[:140]}", "warn")
        dist = (c.get("distribution") or {}).get("value")
        C.add("distribution policy", isin, dist in ("acc", "dist"), f"{dist}")
        C.add("listing present", isin, bool(c.get("listings")), ", ".join(f"{l.get('exchange')}:{l.get('ticker')}" for l in c.get("listings", [])))

for t in LIST + REF:
    C.add("twin mapped", t, t in set_of, set_of.get(t, "no twin set"))

# ---------------------------------------------------------------- dividend yield on one basis
# Part 1 researched trailing-12-month (TTM) yields, part 2 headlined the 30-day SEC yield. Mixing the two in
# one column would be apples and oranges, so every fund is normalised to TTM (issuer first, then databases).
TTM_PAT = re.compile(r"TTM|12m Trailing|12-month|trailing 12|Distribution Yield|rolling", re.I)


def ttm_yield(e):
    fo = e["fields"].get("dividend_yield_pct") or {}
    if fo.get("value") is None:
        return None, None
    if (fo.get("note") or "").lower().startswith("type: trailing"):
        return num(fo["value"]), "TTM (headline)"
    cands = [s for s in fo.get("sources", []) if TTM_PAT.search(s.get("name") or "") and "SEC" not in (s.get("name") or "")]
    cands.sort(key=lambda s: 0 if "issuer" in (s.get("name") or "").lower() else 1)
    if cands:
        return num(cands[0].get("value")), f"TTM from {cands[0].get('name')} ({cands[0].get('as_of')})"
    return None, None


for t in LIST + REF:
    e = us_raw.get(t)
    if not e or (e["fields"].get("dividend_yield_pct") or {}).get("value") is None:
        continue
    val, basis = ttm_yield(e)
    C.add("dividend basis", t, val is not None, f"{val} % — {basis}" if val is not None else "no TTM figure, only SEC yield")

# ---------------------------------------------------------------- assemble outputs
def listing(c, prefer=("Xetra", "LSE", "Borsa Italiana", "Euronext Amsterdam")):
    ls = c.get("listings", [])
    for ex in prefer:
        for l in ls:
            if (l.get("exchange") or "").lower().startswith(ex.lower()) and l.get("ticker"):
                return l
    return ls[0] if ls else {}


def twin_compact(c):
    l = listing(c)
    size = num((c.get("fund_size_eur_m") or {}).get("value"))
    dom = (c.get("domicile") or "").upper()[:2]
    return {
        "name": display_name(c.get("name")), "isin": c.get("isin"), "issuer": c.get("issuer"),
        "wrapper": "ETC" if "ETC" in (c.get("name") or "") else "UCITS",
        "ticker": l.get("ticker"), "ex": l.get("exchange"), "cur": l.get("currency"),
        "ter": num((c.get("ter_pct") or {}).get("value")),
        "dist": (c.get("distribution") or {}).get("value"),
        "size_eur_bn": round(size / 1000, 1) if size else None,
        "domicile_cz": DOMICILE_CZ.get(dom, dom),
        "listings": [{"ex": x.get("exchange"), "t": x.get("ticker"), "cur": x.get("currency")} for x in c.get("listings", [])],
    }


twins_out = {}
for s in twins_raw["twin_sets"]:
    cands = [c for c in s.get("candidates", []) if c.get("isin")]
    pick_isin = (s.get("pick") or {}).get("default_isin")
    pick = next((c for c in cands if c["isin"] == pick_isin), cands[0] if cands else None)
    if not pick:
        continue
    alts = sorted([c for c in cands if c is not pick], key=lambda c: num((c.get("ter_pct") or {}).get("value")) or 9)
    lab = TWIN_LABELS.get(s["id"], {})
    twins_out[s["id"]] = {
        "label": lab.get("label", s.get("us_index")), "match": "exact" if s.get("match") == "exact-index" else ("close" if s.get("match") == "close" else "none"),
        "short_note": lab.get("short"), "note_cz": lab.get("note"),
        "pick": twin_compact(pick), "alt": [twin_compact(c) for c in alts[:3]],
        "why": (s.get("pick") or {}).get("why"), "note_en": s.get("note"),
    }

us_out = []
for t in LIST + REF:
    e = us_raw.get(t)
    if not e:
        continue
    top3 = v(e, "top3_holdings")
    us_out.append({
        "t": t, "former": e.get("former_ticker"), "name": display_name(e.get("name")), "issuer": issuer_short(e.get("issuer")), "issuer_full": e.get("issuer"),
        "ex": v(e, "exchange"), "index": INDEX_SHORT.get(t) or v(e, "index"), "index_official": v(e, "index"),
        "ter": num(v(e, "expense_ratio_pct")), "aum": num(v(e, "aum_usd_bn")),
        "inception": v(e, "inception_date"), "n": int(num(v(e, "holdings_count"))) if num(v(e, "holdings_count")) else None,
        "dist": DIST_CZ.get(str(v(e, "distribution_freq") or "").lower(), v(e, "distribution_freq")),
        "yld": ttm_yield(e)[0], "yld_basis": ttm_yield(e)[1],
        "r1": num(v(e, "ret_1y_pct")), "r5": num(v(e, "ret_5y_pct")), "r10": num(v(e, "ret_10y_pct")),
        "top3": top3 if isinstance(top3, list) else None,
        "twin": set_of.get(t), "asset": ASSET.get(t, "equity"), "us_share": US_SHARE.get(t, {}).get("value"),
        "ref": t in REF, "in_list": t in LIST,
    })

cz = build_cz(cz_raw, C)

ground = {
    "compiled": TODAY.isoformat(), "returns_as_of": RETURNS_AS_OF, "missing_inputs": missing_inputs,
    "us_etfs": {t: us_raw[t] for t in LIST + REF if t in us_raw},
    "us_share_sources": US_SHARE, "twin_sets": twins_raw["twin_sets"], "cz": cz_raw,
    "checks": C.rows,
}
(ROOT / "data" / "etfs.json").write_text(json.dumps(ground, ensure_ascii=False, indent=1), encoding="utf-8", newline="\n")

with open(ROOT / "data" / "etfs.csv", "w", encoding="utf-8", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["ticker", "name", "issuer", "exchange", "index", "ter_pct", "aum_usd_bn", "inception", "holdings", "distribution",
                "yield_pct", "ret_1y", "ret_5y", "ret_10y", "twin_isin", "twin_ticker", "twin_exchange", "twin_ter_pct", "twin_dist", "twin_match"])
    for f in us_out:
        tw = twins_out.get(f["twin"] or "", {})
        p = tw.get("pick", {})
        w.writerow([f["t"], f["name"], f["issuer"], f["ex"], f["index"], f["ter"], f["aum"], f["inception"], f["n"], f["dist"],
                    f["yld"], f["r1"], f["r5"], f["r10"], p.get("isin"), p.get("ticker"), p.get("ex"), p.get("ter"), p.get("dist"), tw.get("match")])

front = {
    "meta": {"compiled": TODAY.isoformat(), "returns_as_of": RETURNS_AS_OF, "provisional": bool(missing_inputs)},
    "fx": cz.get("fx"), "us": us_out, "twins": twins_out, "brokers": cz.get("brokers", []),
    "bank": cz.get("bank"), "tax": cz.get("tax"), "calc": cz.get("calc"), "presets": PRESETS,
}
# The pages only need display fields; provenance (sources, notes, official names, all listings) stays in data/etfs.json.
SLIM_DROP = {"why", "note_en", "note_cz", "listings", "index_official", "issuer_full", "yld_basis", "source", "as_of", "uncertain"}


def slim(x):
    if isinstance(x, dict):
        return {k: slim(val) for k, val in x.items() if k not in SLIM_DROP}
    if isinstance(x, list):
        return [slim(val) for val in x]
    return x


# Never replace the pages' data with an incomplete build (use --partial to preview anyway).
if not missing_inputs or "--partial" in sys.argv:
    (ROOT / "site" / "assets" / "data.js").write_text(
        "/* Generated by tools/build_data.py from data/etfs.json — do not edit by hand. */\nwindow.ETF_DATA = "
        + json.dumps(slim(front), ensure_ascii=False, separators=(",", ":")) + ";\n", encoding="utf-8", newline="\n")

# ---------------------------------------------------------------- report
from report import write_report  # noqa: E402
write_report(ROOT / "docs" / "data-overeni.md", C, us_raw, us_out, twins_out, twins_raw, cz, missing_inputs, LIST, REF, RETURNS_AS_OF)

print(f"checks: {C.count('pass')} pass, {C.count('explained')} explained, {C.count('warn')} warn, {C.count('fail')} fail, {C.count('info')} info;"
      f" funds {len(us_out)}, twin sets {len(twins_out)}; missing inputs: {missing_inputs or 'none'}")
for r in C.rows:
    if r["result"] == "fail":
        print("FAIL", r["check"], r["subject"], "-", r["detail"])
sys.exit(1 if C.count("fail") else 0)
