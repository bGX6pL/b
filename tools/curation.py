"""Editorial decisions that are not raw data: which funds are in the cheat sheet, Czech labels,
and the few hand-sourced values (each with its source). Imported by build_data.py."""

# The 20 NYSE-listed ETFs in the cheat sheet. Broad core first, then style/income, bonds, gold.
# Researched-but-not-listed funds (ITOT, SCHB, IAU, DIA, IWM, RSP, VNQ, VB, DGRO) still serve as
# cross-checks for their peers (same index ⇒ same return).
LIST = ["VOO", "SPY", "IVV", "SPYM", "VTI", "VT", "VEA", "IEFA", "VWO", "IEMG",
        "VUG", "SCHG", "VGT", "XLK", "SCHD", "VYM", "VIG", "JEPI", "AGG", "GLD"]

# Nasdaq-listed, but people ask for them all the time (QQQ) or they appear in the classic
# three-fund portfolio (VXUS, BND). Always shown with a "Nasdaq" label, never counted in the 20.
REF = ["QQQ", "VXUS", "BND"]

# Peers used only for verification.
CHECK_ONLY = ["ITOT", "SCHB", "IAU"]

ASSET = {"AGG": "bond", "BND": "bond", "GLD": "gold", "IAU": "gold", "VNQ": "reit"}

_US_ONLY = "Index contains US-listed US companies only (index methodology); 100 % US by construction."
_EX_US = "Index excludes the United States by construction (ex-US / emerging markets index)."
US_SHARE = {t: {"value": 1.0, "source": _US_ONLY} for t in
            ["VOO", "SPY", "IVV", "SPYM", "VTI", "ITOT", "SCHB", "VUG", "SCHG", "VGT", "XLK", "SCHD", "VYM", "VIG", "JEPI", "QQQ"]}
US_SHARE.update({t: {"value": 0.0, "source": _EX_US} for t in ["VEA", "IEFA", "VWO", "IEMG", "VXUS"]})
US_SHARE["VT"] = {"value": 0.6243, "as_of": "2026-09-30",
                  "source": "Vanguard VT product page, market allocation: United States 62.43 % (benchmark 62.35 %) as at 30 Sep 2026 — "
                            "https://www.vanguardsouthamerica.com/en/product/etf/equity/3141/vanguard-total-world-stock-etf ; "
                            "secondary: MarketXLS 59.9 % as of 31 Aug 2026 (different date/classification)"}
# QQQ: Nasdaq-100 admits non-US companies listed on Nasdaq (a few % of weight). Treat as ~US, flagged.
US_SHARE["QQQ"] = {"value": 0.97, "source": "Nasdaq-100 includes a few non-US Nasdaq listings (approx. 3 % weight); rounded estimate, shown as approx."}

# Example portfolios for variant D. These are combinations that circulate in investing content,
# labelled on the page as examples, not recommendations.
PRESETS = [
    {"id": "sp", "name": "Jen S&P 500", "w": {"VOO": 100}},
    {"id": "spq", "name": "S&P 500 + Nasdaq", "w": {"VOO": 70, "QQQ": 30}},
    {"id": "world", "name": "Celý svět jedním fondem", "w": {"VT": 100}},
    {"id": "three", "name": "3 fondy (Bogleheads)", "w": {"VTI": 60, "VXUS": 30, "BND": 10}},
    {"id": "div", "name": "Dividendové", "w": {"SCHD": 60, "VOO": 40}},
]

DIST_CZ = {"quarterly": "čtvrtletně", "monthly": "měsíčně", "annual": "ročně", "annually": "ročně",
           "semi-annual": "pololetně", "semi-annually": "pololetně", "none": "nevyplácí", "n/a": "nevyplácí"}
DOMICILE_CZ = {"IE": "Irsko", "LU": "Lucembursko", "DE": "Německo", "FR": "Francie", "JE": "Jersey", "GB": "Velká Británie", "NL": "Nizozemsko"}

# Czech labels per twin set id (ids come from data/raw/ucits-twins.json). Filled after research.
TWIN_LABELS = {}


def build_cz(cz_raw, C):
    """Map the Czech-context research (brokers, taxes, bank funds, FX) to what the pages need.
    Filled after research lands; returns safe defaults so the build never crashes."""
    return {"fx": None, "brokers": [], "bank": None, "tax": None, "calc": None}
