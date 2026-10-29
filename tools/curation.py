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

# Czech labels per twin set id (ids from data/raw/ucits-twins.json). "short" = one-line honest difference for
# close (non-identical) matches, shown next to the twin; exact-index sets need none.
TWIN_LABELS = {
    "sp500": {"label": "S&P 500"},
    "global_all_cap": {"label": "celý svět (FTSE Global All Cap)"},
    "em_msci_imi": {"label": "rozvíjející se trhy (MSCI EM IMI)"},
    "djia": {"label": "Dow Jones, 30 firem"},
    "russell2000": {"label": "malé firmy USA (Russell 2000)"},
    "sp500_equal_weight": {"label": "S&P 500 se stejnými vahami"},
    "us_aggregate_bond": {"label": "dluhopisy USA (Bloomberg US Aggregate)"},
    "nasdaq100": {"label": "Nasdaq-100"},
    "us_total_market": {"label": "celý trh USA", "short": "index MSCI USA, bez malých firem"},
    "world_ex_us": {"label": "svět bez USA", "short": "bez malých firem, fond je zatím malý"},
    "developed_ex_us": {"label": "vyspělé trhy bez USA", "short": "index MSCI místo FTSE, bez malých firem"},
    "em_ftse": {"label": "rozvíjející se trhy (FTSE)", "short": "stejný poskytovatel FTSE, bez malých firem"},
    "us_small_cap": {"label": "malé firmy USA", "short": "Russell 2000 místo CRSP Small Cap"},
    "us_large_growth": {"label": "růstové akcie USA", "short": "jiný index: Russell 1000 Growth"},
    "us_tech": {"label": "technologie USA", "short": "stejné firmy, jiné limity vah"},
    "us_dividend_income": {"label": "dividendové akcie USA", "short": "jiná strategie: kvalita + dividenda"},
    "us_dividend_growth": {"label": "rostoucí dividendy USA", "short": "podobná strategie, jiný index"},
    "us_equity_premium_income": {"label": "příjem z opcí na S&P 500", "short": "stejný správce i strategie, evropská struktura"},
    "us_reit": {"label": "nemovitostní firmy USA", "short": "jiný index, jen distribuční třída"},
    "gold": {"label": "zlato", "short": "ETC krytá fyzickým zlatem, ne fond UCITS"},
}


def display_name(name):
    """Readable fund name for the pages: drop the registered/trademark signs and the long 'State Street'
    brand prefix of SPDR funds. The official name stays in data/etfs.json."""
    import re
    n = re.sub("[®™�]", "", name or "")
    n = re.sub(r"^State Street\s+(?=SPDR)", "", n)
    return re.sub(r"\s{2,}", " ", n).strip()


def build_cz(cz_raw, C):
    """Map the Czech-context research (brokers, taxes, bank funds, FX) to what the pages need.
    Every number keeps a pointer to its source in data/raw/cz-context.json."""
    out = {"fx": None, "brokers": [], "bank": None, "tax": None, "calc": {"fx_fee_pct": 0.5, "fx_fee_basis": "provisional"}}

    fx = cz_raw.get("fx") or {}
    u, e = fx.get("usd_czk") or {}, fx.get("eur_czk") or {}
    if u.get("rate") and e.get("rate"):
        out["fx"] = {"usd_czk": u["rate"], "eur_czk": e["rate"], "date": u.get("date"), "source": u.get("source")}
        C.add("plausible range", "fx.usd_czk", 15 < u["rate"] < 30, f"{u['rate']} CZK on {u.get('date')}")
        C.add("plausible range", "fx.eur_czk", 20 < e["rate"] < 30, f"{e['rate']} CZK on {e.get('date')}")

    b = cz_raw.get("bank_fund_benchmark") or {}
    if b.get("entry_fee_pct") is not None and b.get("ongoing_charges_pct") is not None:
        sens = b.get("sensitivity") or {}
        cases = []
        if sens.get("cheap"):
            cases.append({"id": "cheap", "label": "levnější", "entry_pct": sens["cheap"]["entry_fee_pct"], "ter_pct": sens["cheap"]["ongoing_charges_pct"]})
        cases.append({"id": "typical", "label": "typický", "entry_pct": b["entry_fee_pct"], "ter_pct": b["ongoing_charges_pct"]})
        if sens.get("expensive"):
            cases.append({"id": "exp", "label": "dražší", "entry_pct": sens["expensive"]["entry_fee_pct"], "ter_pct": sens["expensive"]["ongoing_charges_pct"]})
        funds = cz_raw.get("bank_funds") or []
        out["bank"] = {
            "entry_pct": b["entry_fee_pct"], "ter_pct": b["ongoing_charges_pct"], "cases": cases,
            "source_note": ("Bankovní fond v kalkulačce = medián 6 akciových fondů prodávaných v ČR podle jejich sdělení klíčových informací "
                            f"({len(funds)} fondů: Česká spořitelna, KB, ČSOB, Raiffeisenbank, Generali, Conseq; stav k 29. 10. 2026). "
                            "Vstupní poplatek je maximum podle ceníku, banka může účtovat méně. Levnější a dražší varianta = rozpětí těchto fondů."),
        }
        C.add("plausible range", "bank.ongoing", 1.0 <= b["ongoing_charges_pct"] <= 3.0, f"{b['ongoing_charges_pct']} % p.a.")
        C.add("plausible range", "bank.entry", 0 <= b["entry_fee_pct"] <= 5, f"{b['entry_fee_pct']} %")
        C.add("bank benchmark sample", "bank_funds", len(funds) >= 5, f"{len(funds)} KID-sourced funds")

    out["brokers"] = map_brokers(cz_raw, C)
    out["tax"] = map_tax(cz_raw, C)
    fxb = next((x for x in out["brokers"] if x.get("calc_fx")), None)
    if fxb:
        out["calc"] = {"fx_fee_pct": fxb["fx_fee_pct"], "fx_fee_basis": fxb["name"]}
    return out


def _n(x, dec=0):
    """Czech number: 100000 -> '100 000', 0.15 -> '0,15'."""
    s = f"{x:,.{dec}f}".replace(",", " ").replace(".", ",")
    return s.replace(" ", " ")


def _p(x):
    return (f"{x:g}".replace(".", ",")) + " %"


def map_brokers(cz_raw, C):
    """Six brokers a Czech beginner meets most often. Wording is editorial; every number comes from cz-context.json."""
    by = {b["name"]: b for b in cz_raw.get("brokers", [])}
    rows = []

    def add(key, short, buy, fx, custody, plan, us_text, calc_fx=False):
        b = by.get(key)
        if not b:
            C.add("broker data", key, False, "missing in cz-context.json", "warn")
            return
        rows.append({"name": short, "buy": buy, "fx": fx, "custody": custody, "plan": plan,
                     "us_etfs": b.get("us_etfs_for_retail") is True, "us_text": us_text,
                     "fx_fee_pct": b.get("fx_fee_pct"), "calc_fx": calc_fx,
                     "source": b.get("source") or b.get("us_etfs_source"), "as_of": b.get("as_of"),
                     "uncertain": bool(b.get("uncertain") or b.get("uncertain_source"))})

    x = by.get("XTB", {})
    add("XTB", "XTB", f"0 % do {_n(x.get('commission_free_monthly_limit_eur', 100000))} € obratu měsíčně",
        _p(x.get("fx_fee_pct", 0.5)), "zdarma (poplatek jen po roce nečinnosti)", "investiční plány, zlomky akcií", "ne", calc_fx=True)
    t = by.get("Trading 212", {})
    add("Trading 212", "Trading 212", "0 Kč", _p(t.get("fx_fee_pct", 0.15)), "zdarma", "Pies (automatické investování), zlomky", "ne")
    d = by.get("DEGIRO", {})
    add("DEGIRO", "DEGIRO", f"Core Selection {_n(d.get('commission_core_selection_eur', 1))} €, ostatní ETF {_n(d.get('commission_other_etf_eur', 3))} €",
        f"AutoFX {_p(d.get('fx_fee_pct', 0.25))}", "zdarma (připojení k burze max. 2,50 €/rok)", "–", "ne")
    i = by.get("Interactive Brokers (IBKR Ireland)", {})
    add("Interactive Brokers (IBKR Ireland)", "Interactive Brokers",
        f"{_p(i.get('commission_tiered_pct', 0.05))} (min. {_n(i.get('commission_tiered_min_eur', 1.25), 2)} €) + poplatky burzy",
        f"{_p(i.get('fx_fee_pct', 0.002))} (min. 2 USD)", "zdarma", "zlomky akcií", "ne (jen profesionální klienti)")
    f = by.get("Fio e-Broker", {})
    fx_ = (f.get("commission_xetra_eur") or {})
    add("Fio e-Broker", "Fio e-Broker", f"Xetra {_n(fx_.get('to_1400', 3.95), 2)} € (obchod do 1 400 €)",
        "kurz Fio (rozpětí)", "zdarma", "–", "ano (execution-only)")
    r = by.get("Revolut", {})
    add("Revolut", "Revolut", f"{_n(r.get('commission_outside_allowance_eur', 1), 0)} € nad měsíční limit, investiční plány 0 €",
        "podle tarifu", "zdarma", "investiční plány, zlomky", "ne")
    for row in rows:
        C.add("broker data", row["name"], bool(row["source"]), f"source {row['source']} ({row['as_of']}){' [uncertain]' if row['uncertain'] else ''}")
    return rows


def map_tax(cz_raw, C):
    t = cz_raw.get("tax") or {}
    if not t:
        return None
    tt, small = t.get("time_test", {}), t.get("small_sales_exemption", {})
    cap, note = t.get("exempt_cap_40m", {}), t.get("notification_exempt_income", {})
    rates, est = t.get("rates", {}), t.get("us_estate_tax_nra", {})
    wht = t.get("us_wht_without_w8ben_pct", 30)
    wht = wht.get("value", wht.get("pct", 30)) if isinstance(wht, dict) else wht
    est_usd = (est.get("threshold_usd") or est.get("filing_threshold_usd") or 60000) if isinstance(est, dict) else 60000
    thr = rates.get("higher_threshold_2026_czk")
    cap_txt = " Limit 40 mil. Kč z roku 2025 se od 1. 1. 2026 na cenné papíry nevztahuje." if cap.get("applies_to_securities_from_2026") is False else ""
    C.add("tax facts", "40m cap", cap.get("applies_to_securities_from_2026") is False, "cap removed for securities from 2026 (zákon 360/2025 Sb.)", "warn")
    points = [
        f"<b>Držíte déle než {tt.get('years', 3)} roky?</b> Zisk z prodeje je osvobozený (časový test, {tt.get('section', '§ 4 odst. 1 písm. u)')} ZDP), počítá se u každého nákupu zvlášť.{cap_txt}",
        f"<b>Prodáte za rok cenné papíry celkem do {_n(small.get('czk_per_year', 100000))} Kč?</b> Příjem je osvobozený ({small.get('section', '§ 4 odst. 1 písm. t)')}). Počítá se celá prodejní cena, ne zisk.",
        f"<b>Jinak</b> se zisk daní {rates.get('general_pct', 15)} %, nad 36násobek průměrné mzdy ({'pro rok 2026 asi ' + _n(thr / 1e6, 2) + ' mil. Kč' if thr else '§ 16'}) {rates.get('higher_pct', 23)} %. "
        f"Osvobozený příjem nad {_n(note.get('czk_threshold', 5000000) / 1e6)} mil. Kč je nutné oznámit finančnímu úřadu ({note.get('section', '§ 38v')}).",
        "<b>Akumulační fond (Acc)</b> dividendy nevyplácí, takže do prodeje nic nepřiznáváte. <b>Distribuční fond</b> nebo americké ETF: dividendy patří do přiznání (příloha č. 3, 15 %, se zápočtem daně sražené v zahraničí).",
        f"<b>Americká ETF (VOO, SPY…):</b> bez formuláře W-8BEN strhnou USA z dividend {wht} % místo 15 %. Nad {_n(est_usd)} USD v amerických aktivech hrozí při úmrtí americká dědická daň (smlouva ČR–USA o dědictví neexistuje). Irské fondy se podle pravidel IRS za americký majetek nepovažují.",
    ]
    return {"points": points,
            "src": "Zdroje: zákon č. 586/1992 Sb. ve znění k 29. 10. 2026; zákon č. 360/2025 Sb.; smlouva ČR–USA č. 32/1994 Sb.; IRS (Form 706-NA). "
                   "Daňové informace jsou zjednodušené, závisí na individuálních poměrech a mohou se změnit. Nejde o daňové poradenství."}
