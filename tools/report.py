"""Writes docs/data-overeni.md — the human-readable verification report for data/etfs.json."""
from collections import Counter, defaultdict

MARK = {"verified": "✔", "single-source": "◐", "conflict": "⚠"}


def _f(e, k):
    return (e["fields"].get(k) or {})


def _cell(e, k, fmt="{}"):
    fo = _f(e, k)
    val = fo.get("value")
    if val is None:
        return "—"
    if isinstance(val, float):
        val = f"{val:g}"
    return f"{fmt.format(val)} {MARK.get(fo.get('status'), '?')}"


def write_report(path, C, us_raw, us_out, twins_out, twins_raw, cz, missing, LIST, REF, returns_as_of):
    res = Counter(r["result"] for r in C.rows)
    by_check = defaultdict(Counter)
    for r in C.rows:
        by_check[r["check"]][r["result"]] += 1
    L = []
    w = L.append
    w("# Ověření dat (ground truth)\n")
    w("> Generováno skriptem `tools/build_data.py` — needitovat ručně. Každé číslo na stránkách, v PDF i v reklamách pochází z `data/etfs.json`.\n")
    if missing:
        w(f"**⚠ Chybějící vstupy:** {', '.join(missing)} — data jsou zatím neúplná.\n")
    w(f"**Výsledek:** {res['pass']} kontrol prošlo · {res['warn']} upozornění · {res['fail']} chyb · {res['info']} informativních.  ")
    w(f"Výnosy ke dni **{returns_as_of}** (celkový výnos v USD na NAV, p.a.). Sestaveno 2026-10-29.\n")

    w("## Metodika\n")
    w("1. **Primární zdroj = správce fondu** (web, fact sheet, prospekt). Pro evropská dvojčata web/KID správce + justETF.")
    w("2. **Nezávislá kontrola** proti dalším databázím (stockanalysis.com, etf.com, Morningstar, Yahoo Finance, justETF). Stav pole: "
      "✔ ověřeno ≥ 2 zdroji v toleranci · ◐ jediný zdroj · ⚠ zdroje se lišily, rozhodl správce.")
    w("3. **Tolerance:** poplatek musí sedět přesně; velikost fondu ±5 % (různá data); počet akcií ±2 %; výnosy ±0,15 p. b. při stejném datu a bázi (NAV).")
    w("4. **Test dvojčat (outliery):** fondy na stejný index musí mít výnos lišící se nejvýš o rozdíl poplatků + toleranci. Pro podobné (ne stejné) indexy je tolerance širší a odchylka je jen upozornění.")
    w("5. **Formální kontroly:** primární burza NYSE/NYSE Arca u všech 20 fondů v taháku, rozumné rozsahy hodnot, jednotné datum výnosů, kontrolní číslice ISIN (ISO 6166), shoda ISIN s domicilem, akumulační/distribuční třída, existence kotace.\n")

    w("## Souhrn kontrol\n")
    w("| Kontrola | ✔ prošlo | ! upozornění | ✖ chyba | i |")
    w("|---|---:|---:|---:|---:|")
    for k, c in by_check.items():
        w(f"| {k} | {c['pass']} | {c['warn']} | {c['fail']} | {c['info']} |")
    w("")

    fails = [r for r in C.rows if r["result"] == "fail"]
    warns = [r for r in C.rows if r["result"] == "warn"]
    w("## Chyby\n")
    w("Žádné." if not fails else "\n".join(f"- **{r['check']}** · {r['subject']} — {r['detail']}" for r in fails))
    w("\n## Upozornění (ověřeno ručně, ponecháno s poznámkou)\n")
    w("Žádná." if not warns else "\n".join(f"- **{r['check']}** · {r['subject']} — {r['detail']}" for r in warns))
    w("")

    w("\n## Americká ETF v taháku\n")
    w("| Ticker | Burza | Index | Poplatek % | Velikost mld. USD | Akcií | Dividenda % | 1 rok % | 5 let % p.a. | 10 let % p.a. |")
    w("|---|---|---|---:|---:|---:|---:|---:|---:|---:|")
    for t in LIST + REF:
        e = us_raw.get(t)
        if not e:
            w(f"| {t} | — chybí — | | | | | | | | |")
            continue
        w(f"| **{t}**{' (ref.)' if t in REF else ''} | {_cell(e,'exchange')} | {(_f(e,'index').get('value') or '—')} | {_cell(e,'expense_ratio_pct')} | {_cell(e,'aum_usd_bn')} | "
          f"{_cell(e,'holdings_count')} | {_cell(e,'dividend_yield_pct')} | {_cell(e,'ret_1y_pct')} | {_cell(e,'ret_5y_pct')} | {_cell(e,'ret_10y_pct')} |")
    w("\nVelikost fondu: viz poznámka u každého fondu v `data/etfs.json`, zda jde o ETF třídu, nebo celý fond (u Vanguardu se liší).\n")

    w("## Test dvojčat — fondy na stejný / podobný index\n")
    w("| Skupina a pole | Výsledek | Detail |")
    w("|---|---|---|")
    for r in C.rows:
        if r["check"] == "peer consistency":
            w(f"| {r['subject']} | {'✔' if r['result']=='pass' else ('!' if r['result']=='warn' else '✖')} | {r['detail']} |")
    w("")

    w("## Evropská dvojčata\n")
    w("| Sada | Shoda | Výchozí dvojče | ISIN | Ticker (burza) | TER % | Typ | Velikost mld. EUR |")
    w("|---|---|---|---|---|---:|---|---:|")
    for sid, s in twins_out.items():
        p = s["pick"]
        w(f"| {sid} | {s['match']} | {p['name']} | `{p['isin']}` | {p['ticker']} ({p['ex']}) | {p['ter']} | {p['dist']} | {p['size_eur_bn'] or '—'} |")
    w("")

    w("## Poznámky výzkumu ke každému fondu\n")
    for t in LIST + REF:
        e = us_raw.get(t)
        if not e:
            continue
        notes = [f"  - *{k}*: {fo.get('note')}" for k, fo in e["fields"].items() if fo and fo.get("note")]
        if e.get("notes"):
            notes.insert(0, f"  - {e['notes']}")
        if notes:
            w(f"- **{t}** — {e.get('name')}")
            L.extend(notes)
    w("\n## Zdroje\n")
    for t in LIST + REF:
        e = us_raw.get(t)
        if not e:
            continue
        urls = sorted({s.get("url") for fo in e["fields"].values() if fo for s in fo.get("sources", []) if s.get("url")})
        w(f"- **{t}:** " + " · ".join(f"<{u}>" for u in urls[:8]))
    path.write_text("\n".join(L) + "\n", encoding="utf-8", newline="\n")
