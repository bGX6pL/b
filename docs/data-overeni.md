# Ověření dat (ground truth)

> Generováno skriptem `tools/build_data.py` — needitovat ručně. Každé číslo na stránkách, v PDF i v reklamách pochází z `data/etfs.json`.

**⚠ Chybějící vstupy:** us-etfs-part1.json, ucits-twins.json, cz-context.json — data jsou zatím neúplná.

**Výsledek:** 86 kontrol prošlo · 0 upozornění · 40 chyb · 0 informativních.  
Výnosy ke dni **2026-09-30** (celkový výnos v USD na NAV, p.a.). Sestaveno 2026-10-29.

## Metodika

1. **Primární zdroj = správce fondu** (web, fact sheet, prospekt). Pro evropská dvojčata web/KID správce + justETF.
2. **Nezávislá kontrola** proti dalším databázím (stockanalysis.com, etf.com, Morningstar, Yahoo Finance, justETF). Stav pole: ✔ ověřeno ≥ 2 zdroji v toleranci · ◐ jediný zdroj · ⚠ zdroje se lišily, rozhodl správce.
3. **Tolerance:** poplatek musí sedět přesně; velikost fondu ±5 % (různá data); počet akcií ±2 %; výnosy ±0,15 p. b. při stejném datu a bázi (NAV).
4. **Test dvojčat (outliery):** fondy na stejný index musí mít výnos lišící se nejvýš o rozdíl poplatků + toleranci. Pro podobné (ne stejné) indexy je tolerance širší a odchylka je jen upozornění.
5. **Formální kontroly:** primární burza NYSE/NYSE Arca u všech 20 fondů v taháku, rozumné rozsahy hodnot, jednotné datum výnosů, kontrolní číslice ISIN (ISO 6166), shoda ISIN s domicilem, akumulační/distribuční třída, existence kotace.

## Souhrn kontrol

| Kontrola | ✔ prošlo | ! upozornění | ✖ chyba | i |
|---|---:|---:|---:|---:|
| coverage | 0 | 0 | 17 | 0 |
| required field | 30 | 0 | 0 | 0 |
| listing venue | 6 | 0 | 0 | 0 |
| plausible range | 32 | 0 | 0 | 0 |
| returns date | 12 | 0 | 0 | 0 |
| fee consensus | 6 | 0 | 0 | 0 |
| twin mapped | 0 | 0 | 23 | 0 |

## Chyby

- **coverage** · VOO — ticker missing from research files
- **coverage** · SPY — ticker missing from research files
- **coverage** · IVV — ticker missing from research files
- **coverage** · SPYM — ticker missing from research files
- **coverage** · VTI — ticker missing from research files
- **coverage** · VT — ticker missing from research files
- **coverage** · VEA — ticker missing from research files
- **coverage** · IEFA — ticker missing from research files
- **coverage** · VWO — ticker missing from research files
- **coverage** · IEMG — ticker missing from research files
- **coverage** · SCHG — ticker missing from research files
- **coverage** · XLK — ticker missing from research files
- **coverage** · SCHD — ticker missing from research files
- **coverage** · JEPI — ticker missing from research files
- **coverage** · AGG — ticker missing from research files
- **coverage** · GLD — ticker missing from research files
- **coverage** · QQQ — ticker missing from research files
- **twin mapped** · VOO — no twin set
- **twin mapped** · SPY — no twin set
- **twin mapped** · IVV — no twin set
- **twin mapped** · SPYM — no twin set
- **twin mapped** · VTI — no twin set
- **twin mapped** · VT — no twin set
- **twin mapped** · VEA — no twin set
- **twin mapped** · IEFA — no twin set
- **twin mapped** · VWO — no twin set
- **twin mapped** · IEMG — no twin set
- **twin mapped** · VUG — no twin set
- **twin mapped** · SCHG — no twin set
- **twin mapped** · VGT — no twin set
- **twin mapped** · XLK — no twin set
- **twin mapped** · SCHD — no twin set
- **twin mapped** · VYM — no twin set
- **twin mapped** · VIG — no twin set
- **twin mapped** · JEPI — no twin set
- **twin mapped** · AGG — no twin set
- **twin mapped** · GLD — no twin set
- **twin mapped** · QQQ — no twin set
- **twin mapped** · VXUS — no twin set
- **twin mapped** · BND — no twin set

## Upozornění (ověřeno ručně, ponecháno s poznámkou)

Žádná.


## Americká ETF v taháku

| Ticker | Burza | Index | Poplatek % | Velikost mld. USD | Akcií | Dividenda % | 1 rok % | 5 let % p.a. | 10 let % p.a. |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| VOO | — chybí — | | | | | | | | |
| SPY | — chybí — | | | | | | | | |
| IVV | — chybí — | | | | | | | | |
| SPYM | — chybí — | | | | | | | | |
| VTI | — chybí — | | | | | | | | |
| VT | — chybí — | | | | | | | | |
| VEA | — chybí — | | | | | | | | |
| IEFA | — chybí — | | | | | | | | |
| VWO | — chybí — | | | | | | | | |
| IEMG | — chybí — | | | | | | | | |
| **VUG** | NYSE Arca ✔ | Morningstar US Large Cap Growth Index | 0.03 ✔ | 232.9 ✔ | 135 ✔ | 0.35 ◐ | 13.09 ✔ | 13.87 ✔ | 17.94 ✔ |
| SCHG | — chybí — | | | | | | | | |
| **VGT** | NYSE Arca ✔ | MSCI US Investable Market Information Technology 25/50 Index | 0.09 ✔ | 154.5 ✔ | 318 ✔ | 0.33 ◐ | 35.19 ✔ | 20.92 ✔ | 24.72 ✔ |
| XLK | — chybí — | | | | | | | | |
| SCHD | — chybí — | | | | | | | | |
| **VYM** | NYSE Arca ✔ | FTSE High Dividend Yield Index | 0.04 ✔ | 78.9 ✔ | 593 ✔ | 2.35 ◐ | 12.72 ✔ | 11.63 ✔ | 11.28 ✔ |
| **VIG** | NYSE Arca ✔ | S&P U.S. Dividend Growers Index | 0.04 ✔ | 109.1 ✔ | 333 ✔ | 1.51 ◐ | 9.77 ✔ | 10.72 ✔ | 12.86 ✔ |
| JEPI | — chybí — | | | | | | | | |
| AGG | — chybí — | | | | | | | | |
| GLD | — chybí — | | | | | | | | |
| QQQ | — chybí — | | | | | | | | |
| **VXUS** (ref.) | Nasdaq ✔ | FTSE Global All Cap ex US Index | 0.05 ✔ | 163.2 ✔ | — | — | — | — | — |
| **BND** (ref.) | Nasdaq ✔ | Bloomberg U.S. Aggregate Float Adjusted Index | 0.03 ✔ | 161.4 ✔ | — | — | — | — | — |

Velikost fondu: viz poznámka u každého fondu v `data/etfs.json`, zda jde o ETF třídu, nebo celý fond (u Vanguardu se liší).

## Test dvojčat — fondy na stejný / podobný index

| Skupina a pole | Výsledek | Detail |
|---|---|---|

## Evropská dvojčata

| Sada | Shoda | Výchozí dvojče | ISIN | Ticker (burza) | TER % | Typ | Velikost mld. EUR |
|---|---|---|---|---|---:|---|---:|

## Poznámky výzkumu ke každému fondu

- **VUG** — Vanguard Morningstar Growth ETF
  - Name changed in 2026 from 'Vanguard Growth ETF' together with the index switch from CRSP to Morningstar; ticker unchanged. 6:1 share split effective 2026-04-21 (Yahoo split record; issuer 52-week high $504 vs NAV ~$88) - per-share prices before that date are not comparable.
  - *exchange*: Primary listing NYSE Arca (Yahoo 'PCX' and Nasdaq.com 'PSE' are legacy codes for NYSE Arca).
  - *index*: Vanguard renamed the fund 'Vanguard Morningstar Growth ETF'; it now tracks the Morningstar US Large Cap Growth Index (previously CRSP US Large Cap Growth Index). The switch happened in 2026 (one secondary report says effective 2026-07-29; exact date NOT confirmed from an issuer document). Caution: Vanguard's spliced-benchmark footnote reads 'MSCI US Prime Market Growth Index through April 16, 2013; Morningstar US Large Cap Growth Index thereafter', omitting the CRSP period - appears to be an issuer footnote error; the Q3-2026 fact sheet also still shows the old Bloomberg index ticker CRSPLCGT.
  - *expense_ratio_pct*: Net = gross (no fee waivers). Prospectus figure dated 2026-04-28 per Vanguard. Nasdaq.com shows 0.04% (stale, pre-fee-cut) - ignored.
  - *aum_usd_bn*: SHARE-CLASS value (ETF shares only). Fund-level total net assets incl. Vanguard mutual-fund share classes = 392.2 bn USD at 2026-09-30. Vanguard only publishes month-end TNA; stockanalysis (2026-10-28) differs by -3.2% because of the later date - within 5% tolerance.
  - *inception_date*: ETF share-class inception date. First trading day in Yahoo price history: 2004-01-30 (exchange listing/trading start can lag inception by a few days).
  - *holdings_count*: Issuer counts stocks only (month-end 2026-09-30, page and fact sheet agree). stockanalysis shows 139 because it counts every line of the holdings file (incl. cash / short-term reserves / futures) - different basis, not a conflict.
  - *dividend_yield_pct*: TYPE: 30-day SEC yield at 2026-09-30 (Vanguard footnote: based on holdings' yield for last 30 days of prior month). Only the issuer page publishes it (the fact sheet has no yield). Trailing-12-month yield per stockanalysis = 0.39% (TTM at price of 2026-10-28) - reference only, different type.
  - *ret_1y_pct*: Annualized total return at NAV, quarter-end 2026-09-30; issuer web data and issuer Q3-2026 fact sheet (separate document) match exactly. Independent cross-check on market-price basis: issuer market-price return 13.21% vs return computed from Yahoo Finance adjusted closes 2025/2021/2016-09-30 -> 2026-09-30 = 13.21% (diff 0.0 pp).
  - *ret_5y_pct*: Annualized total return at NAV, quarter-end 2026-09-30; issuer web data and issuer Q3-2026 fact sheet (separate document) match exactly. Independent cross-check on market-price basis: issuer market-price return 13.88% vs return computed from Yahoo Finance adjusted closes 2025/2021/2016-09-30 -> 2026-09-30 = 13.87% (diff -0.01 pp).
  - *ret_10y_pct*: Annualized total return at NAV, quarter-end 2026-09-30; issuer web data and issuer Q3-2026 fact sheet (separate document) match exactly. Independent cross-check on market-price basis: issuer market-price return 17.95% vs return computed from Yahoo Finance adjusted closes 2025/2021/2016-09-30 -> 2026-09-30 = 17.95% (diff 0.0 pp).
  - *top3_holdings*: Weights = % of fund market value per security, issuer month-end holdings file (2026-09-30); stockanalysis (same 2026-09-30 file) matches; fact sheet (rounded) lists the same top-3 names. (Fact sheet aggregates Alphabet A+C = 9.2% as one issuer; top 3 unchanged.)
- **VGT** — Vanguard Information Technology ETF
  - 8:1 share split effective 2026-04-21 (Yahoo split record).
  - *exchange*: Primary listing NYSE Arca (Yahoo 'PCX' and Nasdaq.com 'PSE' are legacy codes for NYSE Arca).
  - *expense_ratio_pct*: Net = gross (no fee waivers). Prospectus figure dated 2025-12-19 per Vanguard. Nasdaq.com shows 0.10% (stale, pre-fee-cut) - ignored.
  - *aum_usd_bn*: SHARE-CLASS value (ETF shares only). Fund-level total net assets incl. Vanguard mutual-fund share classes = 178.0 bn USD at 2026-09-30. Vanguard only publishes month-end TNA; stockanalysis (2026-10-28) differs by -4.4% because of the later date - within 5% tolerance.
  - *inception_date*: ETF share-class inception date. First trading day in Yahoo price history: 2004-01-30 (exchange listing/trading start can lag inception by a few days).
  - *holdings_count*: Issuer counts stocks only (month-end 2026-09-30, page and fact sheet agree). stockanalysis shows 323 because it counts every line of the holdings file (incl. cash / short-term reserves / futures) - different basis, not a conflict.
  - *dividend_yield_pct*: TYPE: 30-day SEC yield at 2026-09-30 (Vanguard footnote: based on holdings' yield for last 30 days of prior month). Only the issuer page publishes it (the fact sheet has no yield). Trailing-12-month yield per stockanalysis = 0.38% (TTM at price of 2026-10-28) - reference only, different type.
  - *ret_1y_pct*: Annualized total return at NAV, quarter-end 2026-09-30; issuer web data and issuer Q3-2026 fact sheet (separate document) match exactly. Independent cross-check on market-price basis: issuer market-price return 35.25% vs return computed from Yahoo Finance adjusted closes 2025/2021/2016-09-30 -> 2026-09-30 = 35.25% (diff 0.0 pp).
  - *ret_5y_pct*: Annualized total return at NAV, quarter-end 2026-09-30; issuer web data and issuer Q3-2026 fact sheet (separate document) match exactly. Independent cross-check on market-price basis: issuer market-price return 20.93% vs return computed from Yahoo Finance adjusted closes 2025/2021/2016-09-30 -> 2026-09-30 = 20.94% (diff 0.01 pp).
  - *ret_10y_pct*: Annualized total return at NAV, quarter-end 2026-09-30; issuer web data and issuer Q3-2026 fact sheet (separate document) match exactly. Independent cross-check on market-price basis: issuer market-price return 24.72% vs return computed from Yahoo Finance adjusted closes 2025/2021/2016-09-30 -> 2026-09-30 = 24.73% (diff 0.01 pp).
  - *top3_holdings*: Weights = % of fund market value per security, issuer month-end holdings file (2026-09-30); stockanalysis (same 2026-09-30 file) matches; fact sheet (rounded) lists the same top-3 names.
- **VYM** — Vanguard High Dividend Yield ETF
  - *exchange*: Primary listing NYSE Arca (Yahoo 'PCX' and Nasdaq.com 'PSE' are legacy codes for NYSE Arca).
  - *index*: stockanalysis labels it 'FTSE Custom High Dividend Yield'; issuer name used.
  - *expense_ratio_pct*: Net = gross (no fee waivers). Prospectus figure dated 2026-02-27 per Vanguard. Nasdaq.com shows 0.06% (stale, pre-fee-cut) - ignored.
  - *aum_usd_bn*: SHARE-CLASS value (ETF shares only). Fund-level total net assets incl. Vanguard mutual-fund share classes = 95.8 bn USD at 2026-09-30. Vanguard only publishes month-end TNA; stockanalysis (2026-10-28) differs by +4.1% because of the later date - within 5% tolerance.
  - *inception_date*: ETF share-class inception date. First trading day in Yahoo price history: 2006-11-16 (exchange listing/trading start can lag inception by a few days).
  - *holdings_count*: Issuer counts stocks only (month-end 2026-09-30, page and fact sheet agree). stockanalysis shows 603 because it counts every line of the holdings file (incl. cash / short-term reserves / futures) - different basis, not a conflict.
  - *dividend_yield_pct*: TYPE: 30-day SEC yield at 2026-09-30 (Vanguard footnote: based on holdings' yield for last 30 days of prior month). Only the issuer page publishes it (the fact sheet has no yield). Trailing-12-month yield per stockanalysis = 2.25% (TTM at price of 2026-10-28) - reference only, different type.
  - *ret_1y_pct*: Annualized total return at NAV, quarter-end 2026-09-30; issuer web data and issuer Q3-2026 fact sheet (separate document) match exactly. Independent cross-check on market-price basis: issuer market-price return 12.81% vs return computed from Yahoo Finance adjusted closes 2025/2021/2016-09-30 -> 2026-09-30 = 12.81% (diff 0.0 pp).
  - *ret_5y_pct*: Annualized total return at NAV, quarter-end 2026-09-30; issuer web data and issuer Q3-2026 fact sheet (separate document) match exactly. Independent cross-check on market-price basis: issuer market-price return 11.64% vs return computed from Yahoo Finance adjusted closes 2025/2021/2016-09-30 -> 2026-09-30 = 11.64% (diff 0.0 pp).
  - *ret_10y_pct*: Annualized total return at NAV, quarter-end 2026-09-30; issuer web data and issuer Q3-2026 fact sheet (separate document) match exactly. Independent cross-check on market-price basis: issuer market-price return 11.28% vs return computed from Yahoo Finance adjusted closes 2025/2021/2016-09-30 -> 2026-09-30 = 11.28% (diff 0.0 pp).
  - *top3_holdings*: Weights = % of fund market value per security, issuer month-end holdings file (2026-09-30); stockanalysis (same 2026-09-30 file) matches; fact sheet (rounded) lists the same top-3 names.
- **VIG** — Vanguard Dividend Appreciation ETF
  - *exchange*: Primary listing NYSE Arca (Yahoo 'PCX' and Nasdaq.com 'PSE' are legacy codes for NYSE Arca).
  - *index*: Tracked since 2021-09-19 (before: NASDAQ US Dividend Achievers Select Index), per Vanguard benchmark footnote.
  - *expense_ratio_pct*: Net = gross (no fee waivers). Prospectus figure dated 2026-05-28 per Vanguard. Nasdaq.com shows 0.06% (stale, pre-fee-cut) - ignored.
  - *aum_usd_bn*: SHARE-CLASS value (ETF shares only). Fund-level total net assets incl. Vanguard mutual-fund share classes = 127.7 bn USD at 2026-09-30. Vanguard only publishes month-end TNA; stockanalysis (2026-10-28) differs by +4.1% because of the later date - within 5% tolerance.
  - *inception_date*: ETF share-class inception date. First trading day in Yahoo price history: 2006-05-02 (exchange listing/trading start can lag inception by a few days).
  - *holdings_count*: Issuer counts stocks only (month-end 2026-09-30, page and fact sheet agree). stockanalysis shows 343 because it counts every line of the holdings file (incl. cash / short-term reserves / futures) - different basis, not a conflict.
  - *dividend_yield_pct*: TYPE: 30-day SEC yield at 2026-09-30 (Vanguard footnote: based on holdings' yield for last 30 days of prior month). Only the issuer page publishes it (the fact sheet has no yield). Trailing-12-month yield per stockanalysis = 1.48% (TTM at price of 2026-10-28) - reference only, different type.
  - *ret_1y_pct*: Annualized total return at NAV, quarter-end 2026-09-30; issuer web data and issuer Q3-2026 fact sheet (separate document) match exactly. Independent cross-check on market-price basis: issuer market-price return 9.88% vs return computed from Yahoo Finance adjusted closes 2025/2021/2016-09-30 -> 2026-09-30 = 9.87% (diff -0.01 pp).
  - *ret_5y_pct*: Annualized total return at NAV, quarter-end 2026-09-30; issuer web data and issuer Q3-2026 fact sheet (separate document) match exactly. Independent cross-check on market-price basis: issuer market-price return 10.73% vs return computed from Yahoo Finance adjusted closes 2025/2021/2016-09-30 -> 2026-09-30 = 10.74% (diff 0.01 pp).
  - *ret_10y_pct*: Annualized total return at NAV, quarter-end 2026-09-30; issuer web data and issuer Q3-2026 fact sheet (separate document) match exactly. Independent cross-check on market-price basis: issuer market-price return 12.87% vs return computed from Yahoo Finance adjusted closes 2025/2021/2016-09-30 -> 2026-09-30 = 12.87% (diff 0.0 pp).
  - *top3_holdings*: Weights = % of fund market value per security, issuer month-end holdings file (2026-09-30); stockanalysis (same 2026-09-30 file) matches; fact sheet (rounded) lists the same top-3 names.
- **VXUS** — Vanguard Total International Stock ETF
  - Reference ticker only: listed on Nasdaq, not NYSE/NYSE Arca. Only exchange, name, index, expense ratio, AUM and inception collected.
  - *exchange*: Primary listing Nasdaq (Nasdaq Global Market per Nasdaq.com/Yahoo) - NOT listed on NYSE/NYSE Arca.
  - *expense_ratio_pct*: Net = gross (no fee waivers). Prospectus figure dated 2026-02-27 per Vanguard. Nasdaq.com shows 0.07% (stale, pre-fee-cut) - ignored.
  - *aum_usd_bn*: SHARE-CLASS value (ETF shares only). Fund-level total net assets incl. Vanguard mutual-fund share classes = 649.3 bn USD at 2026-09-30. Vanguard only publishes month-end TNA; stockanalysis (2026-10-28) differs by -1.5% because of the later date - within 5% tolerance.
  - *inception_date*: ETF share-class inception date. First trading day in Yahoo price history: 2011-01-28 (exchange listing/trading start can lag inception by a few days).
- **BND** — Vanguard Total Bond Market ETF
  - Reference ticker only: listed on Nasdaq, not NYSE/NYSE Arca. Only exchange, name, index, expense ratio, AUM and inception collected.
  - *exchange*: Primary listing Nasdaq (Nasdaq Global Market per Nasdaq.com/Yahoo) - NOT listed on NYSE/NYSE Arca.
  - *expense_ratio_pct*: Net = gross (no fee waivers). Prospectus figure dated 2026-04-28 per Vanguard.
  - *aum_usd_bn*: SHARE-CLASS value (ETF shares only). Fund-level total net assets incl. Vanguard mutual-fund share classes = 389.3 bn USD at 2026-09-30. Vanguard only publishes month-end TNA; stockanalysis (2026-10-28) differs by +2.9% because of the later date - within 5% tolerance.
  - *inception_date*: ETF share-class inception date. First trading day in Yahoo price history: 2007-04-10 (exchange listing/trading start can lag inception by a few days).

## Zdroje

- **VUG:** <https://api.nasdaq.com/api/quote/VUG/info?assetclass=etf> · <https://api.nasdaq.com/api/quote/VUG/summary?assetclass=etf> · <https://fund-docs.vanguard.com/F0967.pdf> · <https://investor.vanguard.com/investment-products/etfs/profile/vug> · <https://investor.vanguard.com/irr/funds/profile/VUG-AdditionalFundData> · <https://query1.finance.yahoo.com/v8/finance/chart/VUG> · <https://stockanalysis.com/etf/vug/> · <https://stockanalysis.com/etf/vug/holdings/>
- **VGT:** <https://api.nasdaq.com/api/quote/VGT/info?assetclass=etf> · <https://api.nasdaq.com/api/quote/VGT/summary?assetclass=etf> · <https://fund-docs.vanguard.com/F0958.pdf> · <https://investor.vanguard.com/investment-products/etfs/profile/vgt> · <https://investor.vanguard.com/irr/funds/profile/VGT-AdditionalFundData> · <https://query1.finance.yahoo.com/v8/finance/chart/VGT> · <https://stockanalysis.com/etf/vgt/> · <https://stockanalysis.com/etf/vgt/holdings/>
- **VYM:** <https://api.nasdaq.com/api/quote/VYM/info?assetclass=etf> · <https://api.nasdaq.com/api/quote/VYM/summary?assetclass=etf> · <https://fund-docs.vanguard.com/F0923.pdf> · <https://investor.vanguard.com/investment-products/etfs/profile/vym> · <https://investor.vanguard.com/irr/funds/profile/VYM-AdditionalFundData> · <https://query1.finance.yahoo.com/v8/finance/chart/VYM> · <https://stockanalysis.com/etf/vym/> · <https://stockanalysis.com/etf/vym/holdings/>
- **VIG:** <https://api.nasdaq.com/api/quote/VIG/info?assetclass=etf> · <https://api.nasdaq.com/api/quote/VIG/summary?assetclass=etf> · <https://fund-docs.vanguard.com/F0920.pdf> · <https://investor.vanguard.com/investment-products/etfs/profile/vig> · <https://investor.vanguard.com/irr/funds/profile/VIG-AdditionalFundData> · <https://query1.finance.yahoo.com/v8/finance/chart/VIG> · <https://stockanalysis.com/etf/vig/> · <https://stockanalysis.com/etf/vig/holdings/>
- **VXUS:** <https://api.nasdaq.com/api/quote/VXUS/info?assetclass=etf> · <https://api.nasdaq.com/api/quote/VXUS/summary?assetclass=etf> · <https://fund-docs.vanguard.com/F3369.pdf> · <https://investor.vanguard.com/investment-products/etfs/profile/vxus> · <https://query1.finance.yahoo.com/v8/finance/chart/VXUS> · <https://stockanalysis.com/etf/vxus/>
- **BND:** <https://api.nasdaq.com/api/quote/BND/info?assetclass=etf> · <https://api.nasdaq.com/api/quote/BND/summary?assetclass=etf> · <https://fund-docs.vanguard.com/F0928.pdf> · <https://investor.vanguard.com/investment-products/etfs/profile/bnd> · <https://query1.finance.yahoo.com/v8/finance/chart/BND> · <https://stockanalysis.com/etf/bnd/>
