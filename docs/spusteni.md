# Spuštění — kontrolní seznam

**Finální verze:** varianta B (Účtenka) ve světlém provedení. Celý web je ve složce `public/` (hlavní stránka `/`, děkovací stránka `/dekujeme/`, `/ochrana-udaju/`, PDF v `/tahak/`). Vzorky A–D v `site/` jsou archiv a nenasazují se.

Stránky jsou statické (HTML + 4 malé skripty, bez frameworku a bez build kroku). Hosting: **Vercel napojený na GitHub** — každý push do `main` se sám nasadí. Co musí dodat klient nebo technik, je označeno **[K]**.

## 1. Nasazení na Vercel (jednou, ~10 minut)
1. Repozitář nahrát na GitHub (`git remote add origin …` a `git push -u origin main`).
2. Vercel → **Add New → Project** → vybrat repozitář → **Deploy**. Nic nenastavovat: `vercel.json` v kořeni repozitáře určuje, že se servíruje jen složka `public/` (bez build kroku), přidá bezpečnostní hlavičky, dlouhé cache pro písma a `noindex` pro PDF a děkovací stránku.
3. **Settings → Domains** → přidat doménu **[K]** a nastavit DNS podle Vercelu. HTTPS zařídí Vercel sám.
4. Ověřit: `https://[doména]/`, `/dekujeme/`, `/ochrana-udaju/`, `/tahak/etf-tahak-2026.pdf` a neexistující adresa (vlastní stránka 404).

## 2. Klíče — jediný soubor `public/assets/config.js`
```js
window.LEAD_CONFIG = {
  metaPixel: "",   // ID Meta Pixelu (Events Manager → Zdroje dat), jen číslice
  ga4: "",         // ID měření GA4, „G-…“
  endpoint: ""     // URL, kam formulář posílá e-mail (viz bod 3)
};
```
Doplnit, commitnout, pushnout — Vercel nasadí do minuty. Tato ID jsou veřejná (vidí je každý prohlížeč), proto mohou být v repozitáři. **Tajné klíče sem nikdy** (token Conversions API, API klíč e-mailové služby) — ty patří do nastavení serveru endpointu.

Bez `endpoint` běží formulář v ukázkovém režimu (nic neodesílá, rovnou přesměruje na děkovací stránku) — vhodné pro kontrolu, **ne pro spuštění**.

## 3. Povinné před první korunou do reklamy
| # | Úkol | Kdo | Kde |
|---|---|---|---|
| 1 | Identifikace provozovatele (firma, IČO, sídlo, kontakt), autor a prohlášení o střetu zájmů do patičky, PDF a `/ochrana-udaju/` | [K] | žluté `[…]` v `public/**/index.html`, `site/tahak/tahak.html` |
| 2 | Doména + nasazení (bod 1) | [K] | — |
| 3 | Meta Pixel ID a GA4 ID (bod 2) | [K] | `public/assets/config.js` |
| 4 | E-mailová služba (doporučení: Ecomail nebo SmartEmailing — české, servery v EU) + seznam „ETF tahák“ + automatizace 5 e-mailů z `docs/emaily.md` | [K] | — |
| 5 | **Endpoint formuláře** — malá serverless funkce (může běžet přímo na Vercelu jako `api/lead.js`), která přijme JSON z formuláře a založí kontakt v e-mailové službě se štítky `variant`, `placement`, `calc_*`, `utm_*`; vrátí `{"id": "<náhodné ID>"}` (nikdy ne e-mail). Plus `…/consent` (souhlas s tipy — uloží přesné znění a čas, odešle double opt-in) a `…/profile` (odpověď „kde investujete“), obojí podle `id`. E-mail 0 s PDF odchází všem bez ohledu na souhlas. | technik | kontrakt v hlavičce `public/assets/lead.js` |
| 6 | Meta: business portfolio, **ověření domény přes DNS TXT záznam** (Business Settings → Brand safety → Domains; záznam se přidá u Vercelu v Domains → DNS), povinná pole DSA (inzerent/plátce), případné ověření identity | [K] | — |
| 7 | Meta Events Manager: událost `Lead` jako konverze kampaně; v **Aggregated Event Measurement** dát `Lead` nahoru. Volitelně vlastní konverze z `NewsletterOptin` (kvalitnější lead). | [K] | — |
| 8 | GA4: v Admin → Events označit `generate_lead` jako **klíčovou událost** | [K] | — |
| 9 | Právní kontrola: patička a prohlášení (MAR — autor, datum, střet zájmů), souhlas na děkovací stránce, `/ochrana-udaju/`, upozornění v PDF a reklamách | právník [K] | `research/cz-context.md` §6 |
| 10 | Google Ads: zahájit Financial Services Verification (G2RS) — bez ní reklamy na finanční témata v ČR neběží (od 15. 9. 2026). TikTok: zatím ne. | [K] | `docs/reklamy.md` |
| 11 | Finální PDF: `tools/make_pdf.py` po doplnění provozovatele (zkopíruje PDF i do `public/tahak/`) | technik | `site/tahak/` |

**Doporučeně:** Conversions API (serverová kopie události `Lead`). Formulář posílá endpointu `event_id` a Pixel na děkovací stránce posílá stejné `eventID`, takže Meta obě události spáruje a nezapočítá dvakrát. Token CAPI patří do proměnných prostředí endpointu (Vercel → Settings → Environment Variables), ne do `config.js`.

## 4. Jak je měření zapojené (hotovo, ověřeno `tools/check_tracking.py`)
| Událost | Kdy | Meta Pixel | GA4 |
|---|---|---|---|
| `lp_view` | načtení hlavní stránky | `ViewContent` (+ `PageView`) | `lp_view` |
| `calc_change`, `calc_case` | změna kalkulačky | — | ano |
| `lead_form_start` | první klik do pole e-mailu | vlastní `LeadFormStart` | ano |
| `lead_sheet_open` | otevření formuláře zespodu | — | ano |
| `generate_lead` | **konverze** — jednou po úspěšném odeslání, na děkovací stránce (reload ani přímá návštěva ji nezopakují) | `Lead` s `eventID` | `generate_lead` |
| `newsletter_optin` / `_decline` | odpověď na tipy e-mailem | vlastní `NewsletterOptin` | ano |
| `lead_profile` | volba brokera | — | ano |

- Pixel ani GA4 se nenačtou, dokud návštěvník neklikne „Povolit“ (Consent Mode v2: vše `denied`). Po „Odmítnout“ nejde na Meta ani Google žádný požadavek.
- Kdo lištu na hlavní stránce přehlédne, uvidí ji znovu na děkovací stránce; když povolí tam, konverze `Lead` se započítá.
- Endpoint dostane UTM parametry, `fbclid`, `gclid`, stav kalkulačky, umístění formuláře a `event_id`.
- Kontrola kdykoli po změně: `.venv/Scripts/python -X utf8 tools/check_tracking.py` (testovací ID, žádné skutečné požadavky na Meta ani Google; projde tři návštěvníky: povolí, odmítne, povolí až na děkovací stránce).

## 5. Technická kontrola po nasazení (15 minut)
- [ ] Odeslat formulář na skutečný e-mail (Seznam i Gmail) → přišel e-mail 0, odkaz na PDF funguje, kontakt má správné štítky.
- [ ] Překlep `jan@seznam.cs` nabídne opravu.
- [ ] Meta Events Manager → **Test Events**: otevřít stránku, „Povolit“, odeslat formulář → vidět `PageView`, `ViewContent`, `Lead`. Rozšíření Meta Pixel Helper ukáže totéž.
- [ ] GA4 → **DebugView** / Realtime: `lp_view`, `generate_lead`.
- [ ] „Odmítnout“ cookies → v síťových požadavcích žádný `facebook.net` ani `googletagmanager.com`.
- [ ] Otevřít odkaz z reklamy v in-app prohlížeči Instagramu (iOS i Android): první obrazovka, klávesnice nepřekrývá tlačítko, spodní panel jde zavřít.
- [ ] Parametry z reklamy: `/?m=5000&y=30` otevře účtenku 5 000 Kč × 30 let.
- [ ] PageSpeed Insights (mobil) — cíl LCP < 2 s.

## 6. Údržba dat (jednou za čtvrtletí, ~1 hodina)
1. Aktualizovat `data/raw/*.json` (stejná struktura, stejné zdroje — viz `docs/data-overeni.md`).
2. `.venv/Scripts/python -I tools/build_data.py` — skript skončí chybou, pokud něco nesedí (outlier, špatný ISIN, jiné datum výnosů, fond mimo NYSE). Zapíše `public/assets/data.js`.
3. `.venv/Scripts/python tools/make_pdf.py` a `tools/render_ads.py` — PDF, náhled i reklamy se přegenerují ze stejných dat.
4. Commit + push → Vercel nasadí. Odeslat čtvrtletní e-mail s novou verzí.

## 7. Co je záměrně mimo rozsah
- Serverless funkce pro endpoint (závisí na zvolené e-mailové službě).
- Skutečné ID pixelů, doména, identifikace provozovatele.
- Grafika e-mailů (texty jsou hotové v `docs/emaily.md`).
