# ETF tahák — lead-magnet landing pages (NYSE ETF comparison for Czech retail investors)

Four launch-ready landing page samples, two Meta ad concepts, the lead magnet itself (2-page PDF), the post-submit flow, and the research behind it — all driven by one verified dataset.

**Open the overview:** run `.venv/Scripts/python -m http.server 8000` in this folder and go to <http://localhost:8000/> (fonts and data need `http://`, not `file://`).

## What's where
| Path | What |
|---|---|
| `index.html` | Review gallery: all samples, screenshots, ads, PDF, docs |
| `site/` | The deployable website (static, no build step) |
| `site/a-dvojce/` · `b-poplatky/` · `c-srovnani/` · `d-portfolio/` | Samples A–D |
| `site/dekujeme/` | Thank-you page (instant PDF, personal result, unlocked twins, 1-tap profiling) |
| `site/tahak/` | Lead magnet: `etf-tahak-2026.pdf` + its HTML source and previews |
| `site/ochrana-udaju/` | Privacy notice template (GDPR Art. 13) |
| `site/assets/` | Shared: `lead.js` (form), `consent.js` (cookie opt-in + tracking), `data.js` (generated), self-hosted fonts |
| `ads/` | Two ad creatives × feed 4:5 and Stories 9:16 (PNG) + their HTML source |
| `screenshots/` | Mobile and desktop captures of every sample, interaction states, thank-you page |
| `docs/strategie.md` | **Strategy:** target group, offer, when we ask, form, post-submit, variants, measurement |
| `docs/reklamy.md` | Ad copy, headlines, URLs with message-match parameters, campaign setup |
| `docs/data-overeni.md` | Ground-truth verification report (generated) |
| `docs/emaily.md` | E-mail sequence copy |
| `docs/spusteni.md` | Launch checklist ("could we run ads tomorrow?") |
| `research/competitors/` | Competitor research with mobile screenshots |
| `research/cz-context.md` | Czech brokers, taxes, regulation, ad platform rules, audience data |
| `data/raw/` | Research inputs, each value with sources · `data/etfs.json` / `.csv` ground truth |
| `tools/` | `build_data.py` (merge + checks), `make_pdf.py`, `render_ads.py`, `capture.py`, `shot.py` |

## Rebuild everything from data
```bash
.venv/Scripts/python -I tools/build_data.py   # fails on any outlier / bad ISIN / wrong listing venue
.venv/Scripts/python tools/make_pdf.py
.venv/Scripts/python tools/render_ads.py
.venv/Scripts/python tools/capture.py
```
Setup once: `python -m venv .venv && .venv/Scripts/python -m pip install playwright` (uses the installed Microsoft Edge, no browser download).

## Data verification (as of 2026-10-29)
23 US ETFs (20 NYSE-listed in the cheat sheet + 3 Nasdaq references) and 20 UCITS twin sets (74 candidates) — **842 checks pass, 8 anomalies investigated and explained, 0 failures** (`docs/data-overeni.md`). Checks include listing venue, same-index return consistency, ISIN check digits, one returns date, one dividend-yield basis (TTM), plausible ranges and source agreement.

Documents for the client are in Czech; this README is in English for the repo.
