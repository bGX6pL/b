# ETF tahák — lead-magnet landing page (NYSE ETF comparison for Czech retail investors)

**Final version: sample B (fee receipt calculator), light theme, in `public/`.** It deploys to Vercel straight from GitHub; the four original samples stay in `site/` as an archive and are not deployed. Also here: two Meta ad creatives, the lead magnet itself (2-page PDF), the post-submit flow, and the research behind it, all driven by one verified dataset.

**Run the final site locally:** `.venv/Scripts/python -m http.server 8000 --bind 127.0.0.1 --directory public` → <http://localhost:8000/> (pages use absolute paths, so serve `public/` as the root; fonts and data need `http://`, not `file://`).

## Deploy (Vercel + GitHub)
1. Push this repo to GitHub, then in Vercel: **Add New → Project →** pick the repo **→ Deploy**. No settings to change: `vercel.json` sets framework "Other", no build step, output directory `public/`, security headers, long cache for fonts, `noindex` for the PDF and the thank-you page, and trailing-slash URLs.
2. Add the domain in **Settings → Domains**.
3. Keys go in **one file**, `public/assets/config.js`: Meta Pixel ID, GA4 Measurement ID, form endpoint URL. Commit + push and Vercel redeploys. These IDs are public by design; secrets (Conversions API token, e-mail service key) belong to the endpoint, never in that file.
4. Before ads run: see `docs/spusteni.md` (Czech launch checklist: what the client supplies, how tracking is wired, post-deploy checks).

Check the ad tracking any time: `.venv/Scripts/python -X utf8 tools/check_tracking.py` swaps in test IDs, stubs the Meta/Google scripts and mocks the endpoint, then walks three visitors through landing page → form → thank-you page (accepts cookies / refuses / accepts late). It asserts PageView, ViewContent and exactly one Lead whose eventID matches the `event_id` sent to the endpoint, the GA4 events, UTM/fbclid and calculator state in the payload, and zero Meta/Google requests after a refusal.

## What's where
| Path | What |
|---|---|
| `public/` | **The live site** (deployed): `index.html` = landing page, `dekujeme/` thank-you, `ochrana-udaju/` privacy notice, `tahak/` PDF, `assets/config.js` keys, `404.html`, `favicon.svg` |
| `vercel.json` | Vercel config: serve `public/` as-is, headers |
| `index.html` | Review overview of the 4 original samples, screenshots, ads, PDF, docs (serve the repo root to open it) |
| `gallery.html` | Landing page gallery: our 4 samples next to 20 competitor pages on one screen (mobile / after cookies / desktop), click for full page + notes. Pages whose cookie popup covers ≥ 45 % of the mobile screen or dims it are left out. Stills: `screenshots/_sheet-gallery-{mobile,desktop}.jpg` |
| `site/` | Archive: the 4 original samples (not deployed); `site/tahak/tahak.html` is still the PDF source |
| `site/a-dvojce/` · `b-poplatky/` · `c-srovnani/` · `d-portfolio/` | Samples A–D (B became the final, restyled light in `public/`) |
| `site/dekujeme/` | Thank-you page (instant PDF, personal result, unlocked twins, 1-tap profiling) |
| `site/tahak/` | Lead magnet: `etf-tahak-2026.pdf` + its HTML source and previews |
| `site/ochrana-udaju/` | Privacy notice template (GDPR Art. 13) |
| `site/assets/` | The samples' copies of `lead.js`, `consent.js`, `data.js` and fonts (the live versions are in `public/assets/`) |
| `ads/` | Two ad creatives × feed 4:5 and Stories 9:16 (PNG) + their HTML source; both lead to the final page and use its light look |
| `screenshots/` | `final-*.jpg`: the live site, mobile + desktop (`tools/capture_final.py`). The rest: captures of the 4 samples |
| `docs/strategie.md` | **Strategy:** target group, offer, when we ask, form, post-submit, variants, measurement |
| `docs/reklamy.md` | Ad copy, headlines, URLs with message-match parameters, campaign setup |
| `docs/data-overeni.md` | Ground-truth verification report (generated) |
| `docs/emaily.md` | E-mail sequence copy |
| `docs/spusteni.md` | Launch checklist ("could we run ads tomorrow?") |
| `research/competitors/` | Competitor research with mobile screenshots |
| `research/cz-context.md` | Czech brokers, taxes, regulation, ad platform rules, audience data |
| `data/raw/` | Research inputs, each value with sources · `data/etfs.json` / `.csv` ground truth |
| `tools/` | `build_data.py` (merge + checks), `make_pdf.py`, `render_ads.py`, `capture_final.py`, `check_tracking.py`, `capture.py` (samples), `shot.py` |

## Rebuild everything from data
```bash
.venv/Scripts/python -X utf8 -I tools/build_data.py   # fails on any outlier / bad ISIN / wrong listing venue
.venv/Scripts/python tools/make_pdf.py
.venv/Scripts/python tools/render_ads.py
.venv/Scripts/python tools/capture_final.py
.venv/Scripts/python -X utf8 tools/check_tracking.py
.venv/Scripts/python -X utf8 -I tools/build_gallery.py   # gallery data + thumbnails from competitors.json
.venv/Scripts/python tools/gallery_sheet.py
```
Setup once: `python -m venv .venv && .venv/Scripts/python -m pip install playwright pillow` (uses the installed Microsoft Edge, no browser download).

## Data verification (as of 2026-10-29)
23 US ETFs (20 NYSE-listed in the cheat sheet + 3 Nasdaq references) and 20 UCITS twin sets (74 candidates) — **842 checks pass, 8 anomalies investigated and explained, 0 failures** (`docs/data-overeni.md`). Checks include listing venue, same-index return consistency, ISIN check digits, one returns date, one dividend-yield basis (TTM), plausible ranges and source agreement.

Documents for the client are in Czech; this README is in English for the repo.
