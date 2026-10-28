# Spuštění zítra — kontrolní seznam

Stránky jsou statické (HTML + 3 malé skripty, bez frameworku), takže se dají nasadit na jakýkoli hosting (Netlify, Cloudflare Pages, Vercel, Wedos…) za pár minut. Co musí dodat klient nebo technik, je označeno **[K]**.

## 1. Povinné před první korunou do reklamy
| # | Úkol | Kdo | Kde v kódu |
|---|---|---|---|
| 1 | Identifikace provozovatele (firma, IČO, sídlo, kontakt) do patičky, PDF a `/ochrana-udaju/` | [K] | žluté `[…]` v `site/**/index.html`, `site/tahak/tahak.html` |
| 2 | Doména + HTTPS, nasazení složky `site/` | [K] | — |
| 3 | E-mailová služba (doporučení: Ecomail nebo SmartEmailing — české, servery v EU, české šablony) + seznam „ETF tahák“ + automatizace 5 e-mailů z `docs/emaily.md` | [K] | — |
| 4 | Endpoint formuláře (`LEAD_CONFIG.endpoint`) — malá serverless funkce, která přijme JSON z formuláře a založí kontakt v e-mailové službě se štítky `variant`, `placement`, `ticker`/`portfolio`/`calc`, `utm_*`; vrátí `{"id": "<náhodné ID>"}` (nikdy ne e-mail) | technik | `site/assets/lead.js` (kontrakt v hlavičce souboru) |
| 5 | Endpoint `…/profile` pro odpověď „kde investujete“ (přiřadí podle `id` štítek brokera) | technik | `site/dekujeme/index.html` |
| 6 | Meta Pixel ID a GA4 ID do `LEAD_CONFIG` (načtou se až po souhlasu) | [K] | `site/assets/consent.js` |
| 7 | Ověření domény v Meta Business, událost `Lead` jako konverze kampaně | [K] | — |
| 8 | Právní kontrola textů: patička, souhlas u formuláře, `/ochrana-udaju/`, upozornění v PDF a reklamách | právník [K] | viz `research/cz-context.md` |
| 9 | Ověření inzerenta / kategorie finančních služeb v Meta a Google, pokud se na ČR vztahuje | [K] | viz `research/cz-context.md` |
| 10 | Finální PDF: `tools/make_pdf.py` po doplnění provozovatele | technik | `site/tahak/` |

Konfigurace se vkládá na každou stránku **před** skripty, např.:
```html
<script>window.LEAD_CONFIG = { endpoint: "https://api.[doména]/lead", ga4: "G-XXXXXXX", metaPixel: "0000000000" };</script>
```
Bez `endpoint` běží formulář v ukázkovém režimu (nic neodesílá, rovnou přesměruje na děkovací stránku) — vhodné pro kontrolu, **ne pro spuštění**.

## 2. Technická kontrola před spuštěním (15 minut)
- [ ] Odeslat formulář z každé varianty na skutečný e-mail (Seznam i Gmail) → přišel e-mail 0, odkaz na PDF funguje, kontakt má správné štítky.
- [ ] Překlep `jan@seznam.cs` nabídne opravu.
- [ ] „Odmítnout“ cookies → v síťových požadavcích žádný `facebook.net` ani `googletagmanager.com`. „Povolit“ → po odeslání formuláře se v Meta Events Manageru objeví `Lead`.
- [ ] Otevřít odkaz z reklamy v in-app prohlížeči Instagramu (iOS i Android): první obrazovka, klávesnice nepřekrývá tlačítko, spodní panel jde zavřít.
- [ ] Parametry z reklamy fungují: `/a-dvojce/?t=SPY`, `/b-poplatky/?m=5000&y=30`, `/c-srovnani/?sort=ter`, `/d-portfolio/?p=div`.
- [ ] PageSpeed Insights (mobil) — cíl LCP < 2 s. Stránka je bez frameworku: HTML + CSS + 3 skripty + 2 písma.

## 3. Údržba dat (jednou za čtvrtletí, ~1 hodina)
1. Aktualizovat `data/raw/*.json` (stejná struktura, stejné zdroje — viz `docs/data-overeni.md`).
2. `.venv/Scripts/python -I tools/build_data.py` — skript skončí chybou, pokud něco nesedí (outlier, špatný ISIN, jiné datum výnosů, fond mimo NYSE).
3. `.venv/Scripts/python tools/make_pdf.py` a `tools/render_ads.py` — PDF, náhled i reklamy se přegenerují ze stejných dat.
4. Odeslat čtvrtletní e-mail s novou verzí.

## 4. Co je záměrně mimo rozsah ukázky
- Serverless funkce pro endpoint (závisí na zvolené e-mailové službě a hostingu).
- Skutečné ID pixelů, doména, identifikace provozovatele.
- Grafika e-mailů (texty jsou hotové v `docs/emaily.md`).
