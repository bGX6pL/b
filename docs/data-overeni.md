# Ověření dat (ground truth)

> Generováno skriptem `tools/build_data.py` — needitovat ručně. Každé číslo na stránkách, v PDF i v reklamách pochází z `data/etfs.json`.

**⚠ Chybějící vstupy:** us-etfs-part1.json — data jsou zatím neúplná.

**Výsledek:** 616 kontrol prošlo · 5 upozornění · 10 chyb · 0 informativních.  
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
| coverage | 0 | 0 | 10 | 0 |
| required field | 65 | 0 | 0 | 0 |
| listing venue | 13 | 0 | 0 | 0 |
| plausible range | 151 | 0 | 0 | 0 |
| returns date | 29 | 0 | 0 | 0 |
| fee consensus | 12 | 1 | 0 | 0 |
| source agreement | 0 | 1 | 0 | 0 |
| peer consistency | 8 | 1 | 0 | 0 |
| twin pick exists | 20 | 0 | 0 | 0 |
| ISIN check digit | 74 | 0 | 0 | 0 |
| ISIN ↔ domicile | 72 | 2 | 0 | 0 |
| distribution policy | 74 | 0 | 0 | 0 |
| listing present | 74 | 0 | 0 | 0 |
| twin mapped | 23 | 0 | 0 | 0 |
| bank benchmark sample | 1 | 0 | 0 | 0 |

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

## Upozornění (ověřeno ručně, ponecháno s poznámkou)

- **source agreement** · SCHD.top3_holdings — conflict resolved by researcher: Issuer documents (2026-09-30, 2026-10-13, 2026-10-27) consistently show TXN, QCOM, PG as top 3; stockanalysis shows TXN, COP, CVX - rejected (issuer preferred).
- **fee consensus** · QQQ — sources disagree [0.18, 0.2]; chosen 0.18 — Cut from 0.20% to 0.18% with the conversion from a unit investment trust to an open-end ETF (shareholder vote 2025-12-19, effective ~2025-12
- **peer consistency** · US tech: VGT vs XLK ret_1y_pct — Δ 4.28 pp > allowed 4.26 pp — investigate
- **ISIN ↔ domicile** · DE000A2T0VU5 — prefix DE vs domicile IE
- **ISIN ↔ domicile** · FR0013416716 — prefix FR vs domicile IE


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
| **VUG** | NYSE Arca ✔ | Morningstar US Large Cap Growth Index | 0.03 ✔ | 232.87 ✔ | 135 ✔ | 0.35 ◐ | 13.09 ✔ | 13.87 ✔ | 17.94 ✔ |
| **SCHG** | NYSE Arca ✔ | Dow Jones U.S. Large-Cap Growth Total Stock Market Index | 0.04 ✔ | 63.78 ✔ | 189 ✔ | 0.35 ◐ | 13.01 ✔ | 14.71 ✔ | 18.68 ✔ |
| **VGT** | NYSE Arca ✔ | MSCI US Investable Market Information Technology 25/50 Index | 0.09 ✔ | 154.54 ✔ | 318 ✔ | 0.33 ◐ | 35.19 ✔ | 20.92 ✔ | 24.72 ✔ |
| **XLK** | NYSE Arca ✔ | Technology Select Sector Index | 0.08 ✔ | 125.02 ✔ | 75 ✔ | 0.42 ✔ | 39.47 ✔ | 22.14 ✔ | 24.66 ✔ |
| **SCHD** | NYSE Arca ✔ | Dow Jones U.S. Dividend 100 Index | 0.06 ✔ | 118.47 ✔ | 102 ✔ | 3.13 ◐ | 23.36 ✔ | 9.48 ✔ | 12.44 ✔ |
| **VYM** | NYSE Arca ✔ | FTSE High Dividend Yield Index | 0.04 ✔ | 78.95 ✔ | 593 ✔ | 2.35 ◐ | 12.72 ✔ | 11.63 ✔ | 11.28 ✔ |
| **VIG** | NYSE Arca ✔ | S&P U.S. Dividend Growers Index | 0.04 ✔ | 109.12 ✔ | 333 ✔ | 1.51 ◐ | 9.77 ✔ | 10.72 ✔ | 12.86 ✔ |
| **JEPI** | NYSE Arca ✔ | None - actively managed (performance benchmark: S&P 500 Index) | 0.35 ✔ | 46.09 ✔ | 135 ✔ | 7.45 ✔ | 6.62 ✔ | 7.78 ✔ | — |
| **AGG** | NYSE Arca ✔ | Bloomberg US Aggregate Bond Index | 0.03 ✔ | 139.14 ✔ | 13467 ✔ | 5.04 ✔ | -1.87 ✔ | -0.64 ✔ | 1.11 ✔ |
| **GLD** | NYSE Arca ✔ | LBMA Gold Price PM | 0.4 ✔ | 135.84 ✔ | — | — | 8.74 ✔ | 18.62 ✔ | 11.74 ✔ |
| **QQQ** (ref.) | Nasdaq ✔ | Nasdaq-100 Index | 0.18 ✔ | 482.97 ✔ | — | — | — | — | — |
| **VXUS** (ref.) | Nasdaq ✔ | FTSE Global All Cap ex US Index | 0.05 ✔ | 163.23 ✔ | — | — | — | — | — |
| **BND** (ref.) | Nasdaq ✔ | Bloomberg U.S. Aggregate Float Adjusted Index | 0.03 ✔ | 161.44 ✔ | — | — | — | — | — |

Velikost fondu: viz poznámka u každého fondu v `data/etfs.json`, zda jde o ETF třídu, nebo celý fond (u Vanguardu se liší).

## Test dvojčat — fondy na stejný / podobný index

| Skupina a pole | Výsledek | Detail |
|---|---|---|
| gold: GLD vs IAU ret_1y_pct | ✔ | Δ 0.16 pp ≤ allowed 0.45 pp |
| gold: GLD vs IAU ret_5y_pct | ✔ | Δ 0.18 pp ≤ allowed 0.35 pp |
| gold: GLD vs IAU ret_10y_pct | ✔ | Δ 0.17 pp ≤ allowed 0.35 pp |
| US large growth: VUG vs SCHG ret_1y_pct | ✔ | Δ 0.08 pp ≤ allowed 3.76 pp |
| US large growth: VUG vs SCHG ret_5y_pct | ✔ | Δ 0.84 pp ≤ allowed 3.66 pp |
| US large growth: VUG vs SCHG ret_10y_pct | ✔ | Δ 0.74 pp ≤ allowed 3.66 pp |
| US tech: VGT vs XLK ret_1y_pct | ! | Δ 4.28 pp > allowed 4.26 pp — investigate |
| US tech: VGT vs XLK ret_5y_pct | ✔ | Δ 1.22 pp ≤ allowed 4.16 pp |
| US tech: VGT vs XLK ret_10y_pct | ✔ | Δ 0.06 pp ≤ allowed 4.16 pp |

## Evropská dvojčata

| Sada | Shoda | Výchozí dvojče | ISIN | Ticker (burza) | TER % | Typ | Velikost mld. EUR |
|---|---|---|---|---|---:|---|---:|
| sp500 | exact | SPDR S&P 500 UCITS ETF (Acc) | `IE000XZSV718` | SPYL (Xetra) | 0.03 | acc | 17.8 |
| us_total_market | close | Xtrackers MSCI USA UCITS ETF 1C | `IE00BJ0KDR00` | XD9U (Xetra) | 0.03 | acc | 12.4 |
| global_all_cap | exact | Vanguard FTSE Global All-Cap UCITS ETF (USD) Accumulating | `IE000VAHT5T0` | VGLA (Xetra) | 0.07 | acc | 2.2 |
| world_ex_us | close | Vanguard FTSE All-World ex-U.S. UCITS ETF (USD) Accumulating | `IE0009A5ADV9` | VXUS (Xetra) | 0.12 | acc | 0.1 |
| developed_ex_us | close | Xtrackers MSCI World ex USA UCITS ETF 1C | `IE0006WW1TQ4` | EXUS (Xetra) | 0.15 | acc | 7.1 |
| em_msci_imi | exact | iShares Core MSCI EM IMI UCITS ETF USD (Acc) | `IE00BKM4GZ66` | IS3N (Xetra) | 0.18 | acc | 37.8 |
| em_ftse | close | Vanguard FTSE Emerging Markets UCITS ETF (USD) Accumulating | `IE00BK5BR733` | VFEA (Xetra) | 0.17 | acc | 2.1 |
| djia | exact | iShares Dow Jones Industrial Average UCITS ETF USD (Acc) | `IE00B53L4350` | SXRU (Xetra) | 0.33 | acc | 1.7 |
| russell2000 | exact | SPDR Russell 2000 U.S. Small Cap UCITS ETF (Acc) | `IE00BJ38QD84` | ZPRR (Xetra) | 0.3 | acc | 4.2 |
| us_small_cap | close | SPDR Russell 2000 U.S. Small Cap UCITS ETF (Acc) | `IE00BJ38QD84` | ZPRR (Xetra) | 0.3 | acc | 4.2 |
| sp500_equal_weight | exact | Xtrackers S&P 500 Equal Weight UCITS ETF 1C | `IE00BLNMYC90` | XDEW (Xetra) | 0.15 | acc | 11.6 |
| us_large_growth | close | Amundi Russell 1000 Growth UCITS ETF Acc | `IE0005E8B9S4` | MWOV (Xetra) | 0.19 | acc | 0.6 |
| us_tech | close | iShares S&P 500 Information Technology Sector UCITS ETF USD (Acc) | `IE00B3WJKG14` | QDVE (Xetra) | 0.15 | acc | 18.0 |
| us_dividend_income | close | Fidelity US Quality Income UCITS ETF Acc (ACC-USD) | `IE00BYXVGY31` | FUSA (Xetra) | 0.25 | acc | 0.4 |
| us_dividend_growth | close | WisdomTree US Quality Dividend Growth UCITS ETF - USD Acc | `IE00BZ56RG20` | WTDM (Xetra) | 0.33 | acc | 0.6 |
| us_equity_premium_income | close | JPM US Equity Premium Income Active UCITS ETF - USD (dist) | `IE000U5MJOZ6` | JEIP (Xetra) | 0.35 | dist | 0.5 |
| us_reit | close | iShares US Property Yield UCITS ETF USD (Dist) | `IE00B1FZSF77` | IQQ7 (Xetra) | 0.4 | dist | 0.5 |
| us_aggregate_bond | exact | iShares US Aggregate Bond UCITS ETF USD (Acc) | `IE00BYXYYM63` | IUAA (LSE) | 0.25 | acc | 4.0 |
| gold | close | Xtrackers IE Physical Gold ETC Securities | `DE000A2T0VU5` | XGDU (Xetra) | 0.11 | acc | 5.7 |
| nasdaq100 | exact | Xtrackers NASDAQ 100 UCITS ETF 1C | `IE00BMFKG444` | XNAS (Xetra) | 0.2 | acc | 2.7 |

## Poznámky výzkumu ke každému fondu

- **VUG** — Vanguard Morningstar Growth ETF
  - Name changed in 2026 from 'Vanguard Growth ETF' together with the index switch from CRSP to Morningstar; ticker unchanged. 6:1 share split effective 2026-04-21 (Yahoo split record; issuer 52-week high $504 vs NAV ~$88) - per-share prices before that date are not comparable.
  - *exchange*: Primary listing NYSE Arca (Yahoo 'PCX' and Nasdaq.com 'PSE' are legacy codes for NYSE Arca).
  - *index*: Vanguard renamed the fund 'Vanguard Morningstar Growth ETF'; it now tracks the Morningstar US Large Cap Growth Index (previously CRSP US Large Cap Growth Index). The switch happened in 2026 (one secondary report says effective 2026-07-29; exact date NOT confirmed from an issuer document). Caution: Vanguard's spliced-benchmark footnote reads 'MSCI US Prime Market Growth Index through April 16, 2013; Morningstar US Large Cap Growth Index thereafter', omitting the CRSP period - appears to be an issuer footnote error; the Q3-2026 fact sheet also still shows the old Bloomberg index ticker CRSPLCGT.
  - *expense_ratio_pct*: Net = gross (no fee waivers). Prospectus figure dated 2026-04-28 per Vanguard. Nasdaq.com shows 0.04% (stale, pre-fee-cut) - ignored.
  - *aum_usd_bn*: SHARE-CLASS value (ETF shares only). Fund-level total net assets incl. Vanguard mutual-fund share classes = 392.18 bn USD at 2026-09-30. Vanguard only publishes month-end TNA; stockanalysis (2026-10-28) differs by -3.2% because of the later date - within 5% tolerance.
  - *inception_date*: ETF share-class inception date. First trading day in Yahoo price history: 2004-01-30 (exchange listing/trading start can lag inception by a few days).
  - *holdings_count*: Issuer counts stocks only (month-end 2026-09-30, page and fact sheet agree). stockanalysis shows 139 because it counts every line of the holdings file (incl. cash / short-term reserves / futures) - different basis, not a conflict.
  - *dividend_yield_pct*: TYPE: 30-day SEC yield at 2026-09-30 (Vanguard footnote: based on holdings' yield for last 30 days of prior month). Only the issuer page publishes it (the fact sheet has no yield). Trailing-12-month yield per stockanalysis = 0.39% (TTM at price of 2026-10-28) - reference only, different type.
  - *ret_1y_pct*: Annualized total return at NAV, quarter-end 2026-09-30; issuer web data and issuer Q3-2026 fact sheet (separate document) match exactly. Independent cross-check on market-price basis: issuer market-price return 13.21% vs return computed from Yahoo Finance adjusted closes 2025/2021/2016-09-30 -> 2026-09-30 = 13.21% (diff 0.0 pp).
  - *ret_5y_pct*: Annualized total return at NAV, quarter-end 2026-09-30; issuer web data and issuer Q3-2026 fact sheet (separate document) match exactly. Independent cross-check on market-price basis: issuer market-price return 13.88% vs return computed from Yahoo Finance adjusted closes 2025/2021/2016-09-30 -> 2026-09-30 = 13.87% (diff -0.01 pp).
  - *ret_10y_pct*: Annualized total return at NAV, quarter-end 2026-09-30; issuer web data and issuer Q3-2026 fact sheet (separate document) match exactly. Independent cross-check on market-price basis: issuer market-price return 17.95% vs return computed from Yahoo Finance adjusted closes 2025/2021/2016-09-30 -> 2026-09-30 = 17.95% (diff 0.0 pp).
  - *top3_holdings*: Weights = % of fund market value per security, issuer month-end holdings file (2026-09-30); stockanalysis (same 2026-09-30 file) matches; fact sheet (rounded) lists the same top-3 names. (Fact sheet aggregates Alphabet A+C = 9.2% as one issuer; top 3 unchanged.)
- **SCHG** — Schwab U.S. Large-Cap Growth ETF
  - 4:1 share split 2024-10-10/11. Schwab site blocks scripted downloads; data read in a normal browser session (product page + PDF fact sheet).
  - *exchange*: Primary listing NYSE Arca (Yahoo 'PCX' and Nasdaq.com 'PSE' are legacy codes for NYSE Arca).
  - *index*: Bloomberg ticker DWLGT.
  - *aum_usd_bn*: Fund-level total net assets (single share class, so fund = share class). stockanalysis differs by -2.0%, Nasdaq.com by -0.0% (dates within 1 day) - within 5%.
  - *inception_date*: Yahoo price history for SCHG starts 2010-01-04 (data-coverage limit, not a listing date).
  - *holdings_count*: Fact sheet 187 is month-end 2026-09-30.
  - *dividend_yield_pct*: TYPE: 30-day SEC yield as of 2026-10-26 (Schwab page shows only the latest; no 2026-09-30 SEC value found, fact sheet has no yield). Trailing-12-month distribution yield 0.39% (issuer 2026-09-30) = 0.39% (stockanalysis) - verified for TTM type.
  - *ret_1y_pct*: Annualized total return at NAV, quarter-end 2026-09-30; issuer web data and issuer Q3-2026 fact sheet (separate document) match exactly. Independent cross-check on market-price basis: issuer market-price return 13.08% vs return computed from Yahoo Finance adjusted closes 2025/2021/2016-09-30 -> 2026-09-30 = 13.08% (diff 0.0 pp).
  - *ret_5y_pct*: Annualized total return at NAV, quarter-end 2026-09-30; issuer web data and issuer Q3-2026 fact sheet (separate document) match exactly. Independent cross-check on market-price basis: issuer market-price return 14.72% vs return computed from Yahoo Finance adjusted closes 2025/2021/2016-09-30 -> 2026-09-30 = 14.72% (diff 0.0 pp).
  - *ret_10y_pct*: Annualized total return at NAV, quarter-end 2026-09-30; issuer web data and issuer Q3-2026 fact sheet (separate document) match exactly. Independent cross-check on market-price basis: issuer market-price return 18.69% vs return computed from Yahoo Finance adjusted closes 2025/2021/2016-09-30 -> 2026-09-30 = 18.69% (diff 0.0 pp).
  - *top3_holdings*: Same names/order in all sources; stockanalysis weights differ by up to 0.11 pp (likely a slightly different file date).
- **VGT** — Vanguard Information Technology ETF
  - 8:1 share split effective 2026-04-21 (Yahoo split record).
  - *exchange*: Primary listing NYSE Arca (Yahoo 'PCX' and Nasdaq.com 'PSE' are legacy codes for NYSE Arca).
  - *expense_ratio_pct*: Net = gross (no fee waivers). Prospectus figure dated 2025-12-19 per Vanguard. Nasdaq.com shows 0.10% (stale, pre-fee-cut) - ignored.
  - *aum_usd_bn*: SHARE-CLASS value (ETF shares only). Fund-level total net assets incl. Vanguard mutual-fund share classes = 178.05 bn USD at 2026-09-30. Vanguard only publishes month-end TNA; stockanalysis (2026-10-28) differs by -4.5% because of the later date - within 5% tolerance.
  - *inception_date*: ETF share-class inception date. First trading day in Yahoo price history: 2004-01-30 (exchange listing/trading start can lag inception by a few days).
  - *holdings_count*: Issuer counts stocks only (month-end 2026-09-30, page and fact sheet agree). stockanalysis shows 323 because it counts every line of the holdings file (incl. cash / short-term reserves / futures) - different basis, not a conflict.
  - *dividend_yield_pct*: TYPE: 30-day SEC yield at 2026-09-30 (Vanguard footnote: based on holdings' yield for last 30 days of prior month). Only the issuer page publishes it (the fact sheet has no yield). Trailing-12-month yield per stockanalysis = 0.38% (TTM at price of 2026-10-28) - reference only, different type.
  - *ret_1y_pct*: Annualized total return at NAV, quarter-end 2026-09-30; issuer web data and issuer Q3-2026 fact sheet (separate document) match exactly. Independent cross-check on market-price basis: issuer market-price return 35.25% vs return computed from Yahoo Finance adjusted closes 2025/2021/2016-09-30 -> 2026-09-30 = 35.25% (diff 0.0 pp).
  - *ret_5y_pct*: Annualized total return at NAV, quarter-end 2026-09-30; issuer web data and issuer Q3-2026 fact sheet (separate document) match exactly. Independent cross-check on market-price basis: issuer market-price return 20.93% vs return computed from Yahoo Finance adjusted closes 2025/2021/2016-09-30 -> 2026-09-30 = 20.94% (diff 0.01 pp).
  - *ret_10y_pct*: Annualized total return at NAV, quarter-end 2026-09-30; issuer web data and issuer Q3-2026 fact sheet (separate document) match exactly. Independent cross-check on market-price basis: issuer market-price return 24.72% vs return computed from Yahoo Finance adjusted closes 2025/2021/2016-09-30 -> 2026-09-30 = 24.73% (diff 0.01 pp).
  - *top3_holdings*: Weights = % of fund market value per security, issuer month-end holdings file (2026-09-30); stockanalysis (same 2026-09-30 file) matches; fact sheet (rounded) lists the same top-3 names.
- **XLK** — State Street Technology Select Sector SPDR ETF
  - Renamed from 'Technology Select Sector SPDR Fund' (SSGA rebranded to State Street Investment Management). 2:1 share split 2025-12-05 per Yahoo split record.
  - *exchange*: Primary listing NYSE Arca (Yahoo 'PCX' and Nasdaq.com 'PSE' are legacy codes for NYSE Arca).
  - *index*: S&P Dow Jones index (ticker IXTTR); a capped subset of the S&P 500 technology sector.
  - *expense_ratio_pct*: Gross = net. Nasdaq.com shows 0.1% (stale) - ignored.
  - *aum_usd_bn*: Fund-level total net assets (single share class, so fund = share class). stockanalysis differs by -3.3%, Nasdaq.com by +0.0% (dates within 1 day) - within 5%.
  - *inception_date*: Inception 1998-12-16; exchange listing date 1998-12-22 (issuer 'Listing Date'; Yahoo first trade 1998-12-22).
  - *holdings_count*: Stocks only. Holdings XLSX = 75 stocks + money-market fund + USD cash + index future = 78 lines (what stockanalysis counts). Fact sheet 74 at 2026-09-30.
  - *dividend_yield_pct*: TYPE: 30-day SEC yield (0.42% both at 2026-09-30 fact sheet and 2026-10-27 page). Trailing-12-month distribution yield 0.44% (issuer) = 0.44% (stockanalysis).
  - *ret_1y_pct*: Annualized total return at NAV, quarter-end 2026-09-30; issuer web data and issuer Q3-2026 fact sheet (separate document) match exactly. Independent cross-check on market-price basis: issuer market-price return 39.53% vs return computed from Yahoo Finance adjusted closes 2025/2021/2016-09-30 -> 2026-09-30 = 39.61% (diff 0.08 pp). SSGA 'market value' return uses bid/ask midpoint at NAV time, Yahoo uses official close -> explains the 0.08 pp gap. VGT vs XLK 1y gap (35.19 vs 39.47) checked: both confirmed by fact sheets and Yahoo; XLK is S&P 500-only and capped, VGT includes mid/small caps.
  - *ret_5y_pct*: Annualized total return at NAV, quarter-end 2026-09-30; issuer web data and issuer Q3-2026 fact sheet (separate document) match exactly. Independent cross-check on market-price basis: issuer market-price return 22.16% vs return computed from Yahoo Finance adjusted closes 2025/2021/2016-09-30 -> 2026-09-30 = 22.16% (diff 0.0 pp).
  - *ret_10y_pct*: Annualized total return at NAV, quarter-end 2026-09-30; issuer web data and issuer Q3-2026 fact sheet (separate document) match exactly. Independent cross-check on market-price basis: issuer market-price return 24.67% vs return computed from Yahoo Finance adjusted closes 2025/2021/2016-09-30 -> 2026-09-30 = 24.68% (diff 0.01 pp).
- **SCHD** — Schwab U.S. Dividend Equity ETF
  - 3:1 share split 2024-10 (Yahoo split record 2024-10-11). Schwab site blocks scripted downloads; data read in a normal browser session.
  - *exchange*: Primary listing NYSE Arca (Yahoo 'PCX' and Nasdaq.com 'PSE' are legacy codes for NYSE Arca).
  - *index*: Bloomberg ticker DJUSDIVT.
  - *aum_usd_bn*: Fund-level total net assets (single share class, so fund = share class). stockanalysis differs by +0.3%, Nasdaq.com by -0.2% (dates within 1 day) - within 5%. Large jump vs fact sheet (107.89 bn at 2026-09-30) is real: price rose ~8% in October 2026 plus inflows (NAV 32.5 -> 35.11).
  - *inception_date*: First trading day in Yahoo history: 2011-10-20.
  - *holdings_count*: Fact sheet 100 is month-end 2026-09-30.
  - *dividend_yield_pct*: TYPE: 30-day SEC yield as of 2026-10-26 (only latest value published; fact sheet has no yield). Trailing-12-month distribution yield 3.24% (issuer, 2026-09-30 price) vs 3.00% (stockanalysis, 2026-10-28 price - lower because price rose ~8% in October).
  - *ret_1y_pct*: Annualized total return at NAV, quarter-end 2026-09-30; issuer web data and issuer Q3-2026 fact sheet (separate document) match exactly. Independent cross-check on market-price basis: issuer market-price return 23.32% vs return computed from Yahoo Finance adjusted closes 2025/2021/2016-09-30 -> 2026-09-30 = 23.34% (diff 0.02 pp). Large gap vs VYM (12.72%) checked: confirmed by fact sheet and by raw Yahoo prices (close 27.30 -> 32.53 plus 1.055 USD dividends = ~23.0% simple). Genuine divergence (different index rules), not a data error.
  - *ret_5y_pct*: Annualized total return at NAV, quarter-end 2026-09-30; issuer web data and issuer Q3-2026 fact sheet (separate document) match exactly. Independent cross-check on market-price basis: issuer market-price return 9.47% vs return computed from Yahoo Finance adjusted closes 2025/2021/2016-09-30 -> 2026-09-30 = 9.46% (diff -0.01 pp).
  - *ret_10y_pct*: Annualized total return at NAV, quarter-end 2026-09-30; issuer web data and issuer Q3-2026 fact sheet (separate document) match exactly. Independent cross-check on market-price basis: issuer market-price return 12.44% vs return computed from Yahoo Finance adjusted closes 2025/2021/2016-09-30 -> 2026-09-30 = 12.44% (diff 0.0 pp).
  - *top3_holdings*: Issuer documents (2026-09-30, 2026-10-13, 2026-10-27) consistently show TXN, QCOM, PG as top 3; stockanalysis shows TXN, COP, CVX - rejected (issuer preferred). Caveat: on 2026-10-27 #3 is a near-tie - PG, CVX and COP are all 4.27%, so #3 can flip day to day. SCHD is ~equal-weight-ish (top 10 = ~42%).
- **VYM** — Vanguard High Dividend Yield ETF
  - *exchange*: Primary listing NYSE Arca (Yahoo 'PCX' and Nasdaq.com 'PSE' are legacy codes for NYSE Arca).
  - *index*: stockanalysis labels it 'FTSE Custom High Dividend Yield'; issuer name used.
  - *expense_ratio_pct*: Net = gross (no fee waivers). Prospectus figure dated 2026-02-27 per Vanguard. Nasdaq.com shows 0.06% (stale, pre-fee-cut) - ignored.
  - *aum_usd_bn*: SHARE-CLASS value (ETF shares only). Fund-level total net assets incl. Vanguard mutual-fund share classes = 95.77 bn USD at 2026-09-30. Vanguard only publishes month-end TNA; stockanalysis (2026-10-28) differs by +4.0% because of the later date - within 5% tolerance.
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
- **JEPI** — JPMorgan Equity Premium Income ETF
  - Actively managed covered-call style income ETF.
  - *exchange*: Primary listing NYSE Arca (Yahoo 'PCX' and Nasdaq.com 'PSE' are legacy codes for NYSE Arca).
  - *index*: ACTIVE fund - does not track an index. S&P 500 is only the comparison benchmark. Strategy: low-volatility US large-cap stock portfolio plus S&P 500 index call options sold via equity-linked notes (ELNs).
  - *expense_ratio_pct*: Gross = net 0.35%.
  - *aum_usd_bn*: Fund-level total net assets (single share class, so fund = share class). stockanalysis differs by -1.0%, Nasdaq.com by -0.4% (dates within 1 day) - within 5%.
  - *inception_date*: First trading day in Yahoo history: 2020-05-21.
  - *holdings_count*: Issuer 135 vs stockanalysis 137 (1.5%, within 2%; issuer daily file has 137 lines incl. ELNs/cash). Fact sheet 140 at 2026-09-30.
  - *dividend_yield_pct*: TYPE: 30-day SEC yield at 2026-09-30 (7.29% on 2026-10-27). 12-month rolling distribution yield 8.04% (issuer) / 7.94% TTM (stockanalysis). IMPORTANT: the payout is LARGELY OPTION PREMIUM (income from S&P 500 call options sold via ELNs) plus stock dividends - not a classic dividend yield; it varies with market volatility.
  - *ret_1y_pct*: Annualized total return at NAV, quarter-end 2026-09-30; issuer web data and issuer Q3-2026 fact sheet (separate document) match exactly. Independent cross-check on market-price basis: issuer market-price return 6.68% vs return computed from Yahoo Finance adjusted closes 2025/2021/2016-09-30 -> 2026-09-30 = 6.66% (diff -0.02 pp).
  - *ret_5y_pct*: Annualized total return at NAV, quarter-end 2026-09-30; issuer web data and issuer Q3-2026 fact sheet (separate document) match exactly. Independent cross-check on market-price basis: issuer market-price return 7.76% vs return computed from Yahoo Finance adjusted closes 2025/2021/2016-09-30 -> 2026-09-30 = 7.76% (diff 0.0 pp).
  - *ret_10y_pct*: Fund younger than 10 years at 2026-09-30 (inception 2020-05-20); no 10-year return exists.
  - *top3_holdings*: Very flat portfolio (~1.8-2.0% each), so ranks change often (2026-09-30: Microsoft, NVIDIA, Apple).
- **AGG** — iShares Core U.S. Aggregate Bond ETF
  - *exchange*: Primary listing NYSE Arca (Yahoo 'PCX' and Nasdaq.com 'PSE' are legacy codes for NYSE Arca).
  - *index*: Bloomberg index ticker LBUSTRUU.
  - *expense_ratio_pct*: Net = gross (management fee 0.03%, no waiver).
  - *aum_usd_bn*: Fund-level total net assets (single share class, so fund = share class). stockanalysis differs by +0.0%, Nasdaq.com by +0.2% (dates within 1 day) - within 5%.
  - *inception_date*: First trading day in Yahoo history: 2003-09-29.
  - *holdings_count*: Issuer vs stockanalysis differ by 0.09%. Fact sheet 13,375 is month-end 2026-09-30 (different date).
  - *dividend_yield_pct*: TYPE: 30-day SEC yield. Fact sheet (2026-09-30) and page (2026-10-27) both show 5.04%. Trailing-12-month yield 4.13% (issuer, 2026-10-27) / 4.14% (stockanalysis).
  - *ret_1y_pct*: Annualized total return at NAV, quarter-end 2026-09-30; issuer web data and issuer Q3-2026 fact sheet (separate document) match exactly. Independent cross-check on market-price basis: issuer market-price return -1.86% vs return computed from Yahoo Finance adjusted closes 2025/2021/2016-09-30 -> 2026-09-30 = -1.86% (diff 0.0 pp).
  - *ret_5y_pct*: Annualized total return at NAV, quarter-end 2026-09-30; issuer web data and issuer Q3-2026 fact sheet (separate document) match exactly. Independent cross-check on market-price basis: issuer market-price return -0.62% vs return computed from Yahoo Finance adjusted closes 2025/2021/2016-09-30 -> 2026-09-30 = -0.62% (diff 0.0 pp).
  - *ret_10y_pct*: Annualized total return at NAV, quarter-end 2026-09-30; issuer web data and issuer Q3-2026 fact sheet (separate document) match exactly. Independent cross-check on market-price basis: issuer market-price return 1.1% vs return computed from Yahoo Finance adjusted closes 2025/2021/2016-09-30 -> 2026-09-30 = 1.12% (diff 0.02 pp).
  - *top3_holdings*: Only the issuer publishes bond-level holdings (stockanalysis has none for AGG); fact sheet (2026-09-30) shows the same pattern. #1 is a cash/money-market vehicle; the largest actual bonds are individual Treasury notes at ~0.40% each (#2/#3 are a tie at 0.40% - ordered by market value). Not very meaningful for a 13,000-bond index fund.
- **GLD** — SPDR Gold Shares
  - Legal name SPDR Gold Trust; grantor trust (not a 1940-Act fund).
  - *exchange*: Primary listing NYSE Arca (Yahoo 'PCX' and Nasdaq.com 'PSE' are legacy codes for NYSE Arca).
  - *index*: Not an index fund: grantor trust holding physical gold, NAV valued at LBMA Gold Price PM (since 2015-03-20; London PM Fix before).
  - *expense_ratio_pct*: Sponsor fee; gross = net.
  - *aum_usd_bn*: Fund-level total net assets (single share class, so fund = share class). stockanalysis differs by -1.2%, Nasdaq.com by +0.1% (dates within 1 day) - within 5%.
  - *inception_date*: Inception = listing date (first trade 2004-11-18).
  - *holdings_count*: n/a - physically backed gold trust.
  - *distribution_freq*: Grantor gold trust - pays no distributions (issuer pages list no distribution schedule; stockanalysis 'n/a').
  - *dividend_yield_pct*: n/a - no income, no distributions.
  - *ret_1y_pct*: Annualized total return at NAV, quarter-end 2026-09-30; issuer web data and issuer Q3-2026 fact sheet (separate document) match exactly. Independent cross-check on market-price basis: issuer market-price return 7.14% vs return computed from Yahoo Finance adjusted closes 2025/2021/2016-09-30 -> 2026-09-30 = 7.14% (diff 0.0 pp). Sanity check vs IAU (NAV 8.9%): gap 0.16 pp ~= fee gap 0.15 pp x (1+return) - consistent. NAV (LBMA PM) vs market (bid/ask mid at NAV time per SSGA) can differ noticeably for gold trusts.
  - *ret_5y_pct*: Annualized total return at NAV, quarter-end 2026-09-30; issuer web data and issuer Q3-2026 fact sheet (separate document) match exactly. Independent cross-check on market-price basis: issuer market-price return 18.31% vs return computed from Yahoo Finance adjusted closes 2025/2021/2016-09-30 -> 2026-09-30 = 18.32% (diff 0.01 pp). Sanity check vs IAU (NAV 18.8%): gap 0.18 pp ~= fee gap 0.15 pp x (1+return) - consistent. NAV (LBMA PM) vs market (bid/ask mid at NAV time per SSGA) can differ noticeably for gold trusts.
  - *ret_10y_pct*: Annualized total return at NAV, quarter-end 2026-09-30; issuer web data and issuer Q3-2026 fact sheet (separate document) match exactly. Independent cross-check on market-price basis: issuer market-price return 11.72% vs return computed from Yahoo Finance adjusted closes 2025/2021/2016-09-30 -> 2026-09-30 = 11.73% (diff 0.01 pp). Sanity check vs IAU (NAV 11.91%): gap 0.17 pp ~= fee gap 0.15 pp x (1+return) - consistent. NAV (LBMA PM) vs market (bid/ask mid at NAV time per SSGA) can differ noticeably for gold trusts.
  - *top3_holdings*: n/a - gold bullion only.
- **QQQ** — Invesco QQQ ETF
  - Reference ticker only: listed on Nasdaq, not NYSE. Issuer now brands it 'Invesco QQQ ETF'; legal/registrant name 'Invesco QQQ Trust, Series 1' still shown by Nasdaq.com and stockanalysis. Converted from UIT to open-end ETF in Dec 2025.
  - *exchange*: Primary listing Nasdaq (Nasdaq Global Market per Nasdaq.com/Yahoo) - NOT listed on NYSE/NYSE Arca. Issuer page text not explicit on venue; three independent market-data sources agree.
  - *expense_ratio_pct*: Cut from 0.20% to 0.18% with the conversion from a unit investment trust to an open-end ETF (shareholder vote 2025-12-19, effective ~2025-12-22 per press reports). Nasdaq.com still shows 0.20% (stale).
  - *aum_usd_bn*: Fund-level total net assets (single share class, so fund = share class). stockanalysis differs by -2.4%, Nasdaq.com by +0.9% (dates within 1 day) - within 5%.
- **VXUS** — Vanguard Total International Stock ETF
  - Reference ticker only: listed on Nasdaq, not NYSE/NYSE Arca. Only exchange, name, index, expense ratio, AUM and inception collected.
  - *exchange*: Primary listing Nasdaq (Nasdaq Global Market per Nasdaq.com/Yahoo) - NOT listed on NYSE/NYSE Arca.
  - *expense_ratio_pct*: Net = gross (no fee waivers). Prospectus figure dated 2026-02-27 per Vanguard. Nasdaq.com shows 0.07% (stale, pre-fee-cut) - ignored.
  - *aum_usd_bn*: SHARE-CLASS value (ETF shares only). Fund-level total net assets incl. Vanguard mutual-fund share classes = 649.29 bn USD at 2026-09-30. Vanguard only publishes month-end TNA; stockanalysis (2026-10-28) differs by -1.5% because of the later date - within 5% tolerance.
  - *inception_date*: ETF share-class inception date. First trading day in Yahoo price history: 2011-01-28 (exchange listing/trading start can lag inception by a few days).
- **BND** — Vanguard Total Bond Market ETF
  - Reference ticker only: listed on Nasdaq, not NYSE/NYSE Arca. Only exchange, name, index, expense ratio, AUM and inception collected.
  - *exchange*: Primary listing Nasdaq (Nasdaq Global Market per Nasdaq.com/Yahoo) - NOT listed on NYSE/NYSE Arca.
  - *expense_ratio_pct*: Net = gross (no fee waivers). Prospectus figure dated 2026-04-28 per Vanguard.
  - *aum_usd_bn*: SHARE-CLASS value (ETF shares only). Fund-level total net assets incl. Vanguard mutual-fund share classes = 389.34 bn USD at 2026-09-30. Vanguard only publishes month-end TNA; stockanalysis (2026-10-28) differs by +2.9% because of the later date - within 5% tolerance.
  - *inception_date*: ETF share-class inception date. First trading day in Yahoo price history: 2007-04-10 (exchange listing/trading start can lag inception by a few days).

## Zdroje

- **VUG:** <https://api.nasdaq.com/api/quote/VUG/info?assetclass=etf> · <https://api.nasdaq.com/api/quote/VUG/summary?assetclass=etf> · <https://fund-docs.vanguard.com/F0967.pdf> · <https://investor.vanguard.com/investment-products/etfs/profile/vug> · <https://investor.vanguard.com/irr/funds/profile/VUG-AdditionalFundData> · <https://query1.finance.yahoo.com/v8/finance/chart/VUG> · <https://stockanalysis.com/etf/vug/> · <https://stockanalysis.com/etf/vug/holdings/>
- **SCHG:** <https://api.nasdaq.com/api/quote/SCHG/info?assetclass=etf> · <https://api.nasdaq.com/api/quote/SCHG/summary?assetclass=etf> · <https://query1.finance.yahoo.com/v8/finance/chart/SCHG> · <https://stockanalysis.com/etf/schg/> · <https://stockanalysis.com/etf/schg/holdings/> · <https://www.schwabassetmanagement.com/products/schg> · <https://www.schwabassetmanagement.com/resource/schg-fact-sheet>
- **VGT:** <https://api.nasdaq.com/api/quote/VGT/info?assetclass=etf> · <https://api.nasdaq.com/api/quote/VGT/summary?assetclass=etf> · <https://fund-docs.vanguard.com/F0958.pdf> · <https://investor.vanguard.com/investment-products/etfs/profile/vgt> · <https://investor.vanguard.com/irr/funds/profile/VGT-AdditionalFundData> · <https://query1.finance.yahoo.com/v8/finance/chart/VGT> · <https://stockanalysis.com/etf/vgt/> · <https://stockanalysis.com/etf/vgt/holdings/>
- **XLK:** <https://api.nasdaq.com/api/quote/XLK/info?assetclass=etf> · <https://api.nasdaq.com/api/quote/XLK/summary?assetclass=etf> · <https://query1.finance.yahoo.com/v8/finance/chart/XLK> · <https://stockanalysis.com/etf/xlk/> · <https://stockanalysis.com/etf/xlk/holdings/> · <https://www.ssga.com/library-content/products/factsheets/etfs/us/factsheet-us-en-xlk.pdf> · <https://www.ssga.com/library-content/products/fund-data/etfs/us/holdings-daily-us-en-xlk.xlsx> · <https://www.ssga.com/us/en/intermediary/etfs/state-street-technology-select-sector-spdr-etf-xlk>
- **SCHD:** <https://api.nasdaq.com/api/quote/SCHD/info?assetclass=etf> · <https://api.nasdaq.com/api/quote/SCHD/summary?assetclass=etf> · <https://query1.finance.yahoo.com/v8/finance/chart/SCHD> · <https://stockanalysis.com/etf/schd/> · <https://stockanalysis.com/etf/schd/holdings/> · <https://www.schwabassetmanagement.com/allholdings/SCHD> · <https://www.schwabassetmanagement.com/products/schd> · <https://www.schwabassetmanagement.com/resource/schd-fact-sheet>
- **VYM:** <https://api.nasdaq.com/api/quote/VYM/info?assetclass=etf> · <https://api.nasdaq.com/api/quote/VYM/summary?assetclass=etf> · <https://fund-docs.vanguard.com/F0923.pdf> · <https://investor.vanguard.com/investment-products/etfs/profile/vym> · <https://investor.vanguard.com/irr/funds/profile/VYM-AdditionalFundData> · <https://query1.finance.yahoo.com/v8/finance/chart/VYM> · <https://stockanalysis.com/etf/vym/> · <https://stockanalysis.com/etf/vym/holdings/>
- **VIG:** <https://api.nasdaq.com/api/quote/VIG/info?assetclass=etf> · <https://api.nasdaq.com/api/quote/VIG/summary?assetclass=etf> · <https://fund-docs.vanguard.com/F0920.pdf> · <https://investor.vanguard.com/investment-products/etfs/profile/vig> · <https://investor.vanguard.com/irr/funds/profile/VIG-AdditionalFundData> · <https://query1.finance.yahoo.com/v8/finance/chart/VIG> · <https://stockanalysis.com/etf/vig/> · <https://stockanalysis.com/etf/vig/holdings/>
- **JEPI:** <https://am.jpmorgan.com/FundsMarketingHandler/product-data?cusip=46641Q332&country=us&role=adv&language=en&userLoggedIn=false> · <https://am.jpmorgan.com/content/dam/jpm-am-aem/americas/us/en/literature/fact-sheet/etfs/FS-JEPI.PDF> · <https://api.nasdaq.com/api/quote/JEPI/info?assetclass=etf> · <https://api.nasdaq.com/api/quote/JEPI/summary?assetclass=etf> · <https://query1.finance.yahoo.com/v8/finance/chart/JEPI> · <https://stockanalysis.com/etf/jepi/> · <https://stockanalysis.com/etf/jepi/holdings/>
- **AGG:** <https://api.nasdaq.com/api/quote/AGG/info?assetclass=etf> · <https://api.nasdaq.com/api/quote/AGG/summary?assetclass=etf> · <https://query1.finance.yahoo.com/v8/finance/chart/AGG> · <https://stockanalysis.com/etf/agg/> · <https://www.ishares.com/us/literature/fact-sheet/agg-ishares-core-u-s-aggregate-bond-etf-fund-fact-sheet-en-us.pdf> · <https://www.ishares.com/us/products/239458/ishares-core-total-us-bond-market-etf/latest-holdings.csv> · <https://www.ishares.com/us/products/239458/ishares-core-us-aggregate-bond-etf>
- **GLD:** <https://api.nasdaq.com/api/quote/GLD/info?assetclass=etf> · <https://api.nasdaq.com/api/quote/GLD/summary?assetclass=etf> · <https://query1.finance.yahoo.com/v8/finance/chart/GLD> · <https://stockanalysis.com/etf/gld/> · <https://www.spdrgoldshares.com/usa/gld/> · <https://www.ssga.com/library-content/products/factsheets/etfs/us/factsheet-us-en-gld.pdf> · <https://www.ssga.com/us/en/intermediary/etfs/spdr-gold-shares-gld>
- **QQQ:** <https://api.nasdaq.com/api/quote/QQQ/info?assetclass=etf> · <https://api.nasdaq.com/api/quote/QQQ/summary?assetclass=etf> · <https://dng-api.invesco.com/cache/v1/accounts/en_US/shareclasses/46090E103?expand=nav&idType=cusip&variationType=fundDetails&productType=ETF> · <https://dng-api.invesco.com/cache/v1/accounts/en_US/shareclasses/QQQ/performance/standard?idType=ticker&performanceSubType=annualized&productType=ETF> · <https://query1.finance.yahoo.com/v8/finance/chart/QQQ> · <https://stockanalysis.com/etf/qqq/> · <https://www.invesco.com/qqq-etf/en/home.html>
- **VXUS:** <https://api.nasdaq.com/api/quote/VXUS/info?assetclass=etf> · <https://api.nasdaq.com/api/quote/VXUS/summary?assetclass=etf> · <https://fund-docs.vanguard.com/F3369.pdf> · <https://investor.vanguard.com/investment-products/etfs/profile/vxus> · <https://query1.finance.yahoo.com/v8/finance/chart/VXUS> · <https://stockanalysis.com/etf/vxus/>
- **BND:** <https://api.nasdaq.com/api/quote/BND/info?assetclass=etf> · <https://api.nasdaq.com/api/quote/BND/summary?assetclass=etf> · <https://fund-docs.vanguard.com/F0928.pdf> · <https://investor.vanguard.com/investment-products/etfs/profile/bnd> · <https://query1.finance.yahoo.com/v8/finance/chart/BND> · <https://stockanalysis.com/etf/bnd/>
