# Spuštění — kontrolní seznam

**Finální verze:** varianta B (Účtenka) ve světlém provedení. Celý web je ve složce `public/` (hlavní stránka `/`, děkovací stránka `/dekujeme/`, `/ochrana-udaju/`, PDF v `/tahak/`), formulář obsluhuje funkce `api/lead.mjs`. Vzorky A–D v `site/` jsou archiv a nenasazují se.

Stránky jsou statické (HTML + 4 malé skripty, bez frameworku a bez build kroku) plus jedna serverová funkce bez závislostí. Hosting: **Vercel napojený na GitHub** — každý push do `main` se sám nasadí. Co musí dodat klient nebo technik, je označeno **[K]**.

## 1. Nasazení na Vercel (jednou, ~10 minut)
1. Repozitář nahrát na GitHub (`git remote add origin …` a `git push -u origin main`).
2. Vercel → **Add New → Project** → vybrat repozitář → **Deploy**. Nic nenastavovat: `vercel.json` v kořeni repozitáře určuje, že se servíruje jen složka `public/` (bez build kroku), funkce formuláře běží ve Frankfurtu (`fra1`, data zůstávají v EU), a přidá bezpečnostní hlavičky, dlouhé cache pro písma a `noindex` pro PDF a děkovací stránku.
3. **Settings → Domains** → přidat doménu **[K]** a nastavit DNS podle Vercelu. HTTPS zařídí Vercel sám.
4. Ověřit: `https://[doména]/`, `/dekujeme/`, `/ochrana-udaju/`, `/tahak/etf-tahak-2026.pdf` a neexistující adresa (vlastní stránka 404).

## 2. Klíče — dvě místa, nic dalšího
**a) Veřejná ID → `public/assets/config.js`** (commit + push, Vercel nasadí do minuty):
```js
window.LEAD_CONFIG = {
  metaPixel: "",   // ID Meta Pixelu (Events Manager → Zdroje dat), jen číslice
  ga4: "",         // ID měření GA4, „G-…“
  endpoint: …      // už nastaveno: /api/lead (na localhostu ukázkový režim) — neměnit
};
```
Tato ID jsou veřejná (vidí je každý prohlížeč), proto mohou být v repozitáři.

**b) Tajné klíče → Vercel → Settings → Environment Variables** (Production; po uložení **Redeploy**). Nikdy ne do repozitáře.

| Proměnná | Povinná | Co to je |
|---|---|---|
| `ECOMAIL_API_KEY` | ano | Ecomail → Správa účtu → Pro vývojáře → Zkopírovat API klíč |
| `ECOMAIL_LIST_PDF` | ano | ID seznamu „ETF tahák — PDF“ (číslo v URL seznamu) |
| `ECOMAIL_LIST_TIPS` | ano | ID seznamu „ETF tipy“ (newsletter) |
| `META_PIXEL_ID` | pro CAPI | stejné ID jako v `config.js` |
| `META_CAPI_TOKEN` | pro CAPI | Events Manager → pixel → Nastavení → Conversions API → Vygenerovat přístupový token |
| `META_TEST_EVENT_CODE` | jen při testu | kód z Events Manager → Test Events; po kontrole smazat |
| `LEAD_SECRET` | ne | vlastní klíč pro token děkovací stránky (jinak se odvodí z API klíče Ecomailu) |
| `ALLOWED_ORIGINS` | ne | další domény, ze kterých smí formulář posílat (vlastní doména je povolená vždy) |

Bez Ecomail klíčů funkce odpoví 503 a formulář ukáže „Nepodařilo se odeslat“ — **před spuštěním reklam musí být vyplněné**. Bez `META_CAPI_TOKEN` vše funguje, jen bez serverové kopie konverze.

## 3. Nastavení Ecomailu (jednou, ~30 minut) [K]
1. **Seznam „ETF tahák — PDF“** — double opt-in **vypnutý** (člověk o PDF sám požádal; e-mail 0 je doručení, ne marketing). Na tento seznam **nikdy neposílat kampaně**.
2. **Automatizace** se spouštěčem „Přihlášení do seznamu ETF tahák — PDF“ → hned e-mail 0 z `docs/emaily.md` s odkazem `https://[doména]/tahak/etf-tahak-2026.pdf`. Povolit **opakované spuštění** (kdo si o tahák řekne znovu, dostane ho znovu).
3. **Seznam „ETF tipy“** — double opt-in **zapnutý**, potvrzovací e-mail česky („Potvrďte prosím odběr tipů o ETF“).
4. **Automatizace** se spouštěčem „Potvrzení odběru seznamu ETF tipy“ → e-maily 1–4 z `docs/emaily.md` (zítra, za 3, 6 a 10 dní). E-mail 3 větvit podle vlastního pole `broker` (`xtb`, `t212`, `degiro`, `ibkr`, `fio`, `revolut`, `robo`, `other`, `none`).
5. Vlastní pole se založí sama při prvním leadu: `lp_variant`, `lp_placement`, `lp_page`, `calc_amount`, `calc_years`, `calc_case`, `calc_save_czk`, `utm_*`, `lead_at`; na seznamu tipů navíc `consent_text`, `consent_at`, `consent_page` (důkaz souhlasu — přesné znění a čas) a `broker`.
6. Odesílací doména: v Ecomailu ověřit doménu (SPF, DKIM, DMARC) — jinak e-mail 0 skončí ve spamu. DNS záznamy se přidávají u Vercelu (Domains → DNS).

## 4. Povinné před první korunou do reklamy
| # | Úkol | Kdo | Kde |
|---|---|---|---|
| 1 | Identifikace provozovatele (firma, IČO, sídlo, kontakt), autor a prohlášení o střetu zájmů do patičky, PDF a `/ochrana-udaju/` | [K] | žluté `[…]` v `public/**/index.html`, `site/tahak/tahak.html` |
| 2 | Doména + nasazení (bod 1) | [K] | — |
| 3 | Klíče (bod 2) a Ecomail (bod 3) | [K] | `public/assets/config.js`, Vercel → Environment Variables |
| 4 | Meta: business portfolio, **ověření domény přes DNS TXT záznam** (Business Settings → Brand safety → Domains; záznam se přidá u Vercelu v Domains → DNS), povinná pole DSA (inzerent/plátce), případné ověření identity | [K] | — |
| 5 | Meta Events Manager: událost `Lead` jako konverze kampaně; v **Aggregated Event Measurement** dát `Lead` nahoru. Volitelně vlastní konverze z `NewsletterOptin` (kvalitnější lead). | [K] | — |
| 6 | GA4: v Admin → Events označit `generate_lead` jako **klíčovou událost** | [K] | — |
| 7 | Právní kontrola: patička a prohlášení (MAR — autor, datum, střet zájmů), souhlas na děkovací stránce, `/ochrana-udaju/` (zpracovatelé: Vercel, Ecomail, Meta včetně serverového předání), upozornění v PDF a reklamách | právník [K] | `research/cz-context.md` §6 |
| 8 | Google Ads: zahájit Financial Services Verification (G2RS) — bez ní reklamy na finanční témata v ČR neběží (od 15. 9. 2026). TikTok: zatím ne. | [K] | `docs/reklamy.md` |
| 9 | Finální PDF: `tools/make_pdf.py` po doplnění provozovatele (zkopíruje PDF i do `public/tahak/`) | technik | `site/tahak/` |
| 10 | Doporučeně: Vercel → Firewall → pravidlo **rate limit** pro `/api/lead` (např. 10 požadavků za minutu z jedné IP). Funkce má vlastní limit 5 leadů / 10 min / IP, ale jen v rámci jedné instance. | technik | — |

## 5. Jak je formulář a měření zapojené (hotovo, ověřeno)
**Formulář → `api/lead.mjs`:**
- `POST /api/lead` — zkontroluje e-mail a původ požadavku, založí/aktualizuje kontakt v seznamu PDF (spustí automatizaci s e-mailem 0), uloží kalkulačku, UTM a umístění formuláře. Vrátí `{"id": token}` — e-mail zašifrovaný (AES-256-GCM) s časem, platí 24 h; děkovací stránka e-mail nikdy nedrží.
- `POST /api/lead/consent` — „Ano, posílejte“: podle tokenu přihlásí e-mail do seznamu tipů s double opt-in a uloží přesné znění souhlasu a čas. Kdo už je potvrzený, nedostane druhý potvrzovací e-mail.
- `POST /api/lead/profile` — volba brokera do pole `broker` v obou seznamech.
- Logy funkce nikdy neobsahují e-mailové adresy. Při chybě Ecomailu formulář ukáže „zkuste znovu“ a návštěvník zůstane na stránce.

**Měření:**
| Událost | Kdy | Meta | GA4 |
|---|---|---|---|
| `lp_view` | načtení hlavní stránky | `ViewContent` (+ `PageView`) | `lp_view` |
| `calc_change`, `calc_case` | změna kalkulačky | — | ano |
| `lead_form_start` | první klik do pole e-mailu | vlastní `LeadFormStart` | ano |
| `lead_sheet_open` | otevření formuláře zespodu | — | ano |
| `generate_lead` | **konverze** — jednou po úspěšném odeslání, na děkovací stránce (reload ani přímá návštěva ji nezopakují) | `Lead` z Pixelu s `eventID` **+ `Lead` ze serveru (Conversions API) se stejným `event_id`** — Meta je spáruje | `generate_lead` |
| `newsletter_optin` / `_decline` | odpověď na tipy e-mailem | vlastní `NewsletterOptin` | ano |
| `lead_profile` | volba brokera | — | ano |

- Pixel ani GA4 se nenačtou, dokud návštěvník neklikne „Povolit“ (Consent Mode v2: vše `denied`). Po „Odmítnout“ nejde na Meta ani Google žádný požadavek — ani z prohlížeče, ani ze serveru (formulář posílá stav souhlasu a Conversions API se volá jen při „Povolit“).
- Kdo lištu na hlavní stránce přehlédne, uvidí ji znovu na děkovací stránce; když povolí tam, konverze `Lead` z Pixelu se započítá.
- Serverová událost posílá e-mail jen jako SHA-256 hash, k tomu IP, prohlížeč a `fbc`/`fbp` (z `fbclid` reklamy a cookies Pixelu).

**Kontroly kdykoli po změně** (testovací klíče, nic neodchází na Ecomail, Meta ani Google):
- `node tools/check_endpoint.mjs` — funkce samotná: chybějící klíče, cizí web, špatný e-mail, limit, uložení do Ecomailu, Conversions API jen se souhlasem, double opt-in, podvržený nebo prošlý token, broker, výpadek Ecomailu.
- `.venv/Scripts/python -X utf8 tools/check_tracking.py` — čtyři návštěvníci v prohlížeči: povolí, odmítne, povolí až na děkovací stránce, a celý řetězec přes skutečnou funkci (`tools/dev_server.mjs` s falešným Ecomailem a Meta).

## 6. Technická kontrola po nasazení (20 minut)
- [ ] Odeslat formulář na skutečný e-mail (Seznam i Gmail) → přišel e-mail 0 s PDF; v Ecomailu je kontakt v seznamu PDF s vyplněnými poli `calc_*` a `utm_*`.
- [ ] Na děkovací stránce „Ano, posílejte“ → přišel potvrzovací e-mail; po potvrzení je kontakt v seznamu tipů se stavem „přihlášen“ a polem `consent_text`; volba brokera je v poli `broker`.
- [ ] Překlep `jan@seznam.cs` nabídne opravu.
- [ ] Meta Events Manager → **Test Events** (dočasně nastavit `META_TEST_EVENT_CODE`): otevřít stránku, „Povolit“, odeslat formulář → vidět `PageView`, `ViewContent` a `Lead` jednou z prohlížeče a jednou ze serveru, označené jako spárované (deduplikované). Pak `META_TEST_EVENT_CODE` smazat.
- [ ] GA4 → **DebugView** / Realtime: `lp_view`, `generate_lead`.
- [ ] „Odmítnout“ cookies → v síťových požadavcích žádný `facebook.net` ani `googletagmanager.com`; v Test Events žádný serverový `Lead`.
- [ ] Vercel → projekt → **Logs**: žádné chyby funkce `/api/lead`.
- [ ] Otevřít odkaz z reklamy v in-app prohlížeči Instagramu (iOS i Android): první obrazovka, klávesnice nepřekrývá tlačítko, spodní panel jde zavřít.
- [ ] Parametry z reklamy: `/?m=5000&y=30` otevře účtenku 5 000 Kč × 30 let.
- [ ] PageSpeed Insights (mobil) — cíl LCP < 2 s.

## 7. Údržba dat (jednou za čtvrtletí, ~1 hodina)
1. Aktualizovat `data/raw/*.json` (stejná struktura, stejné zdroje — viz `docs/data-overeni.md`).
2. `.venv/Scripts/python -I tools/build_data.py` — skript skončí chybou, pokud něco nesedí (outlier, špatný ISIN, jiné datum výnosů, fond mimo NYSE). Zapíše `public/assets/data.js`.
3. `.venv/Scripts/python tools/make_pdf.py` a `tools/render_ads.py` — PDF, náhled i reklamy se přegenerují ze stejných dat.
4. Commit + push → Vercel nasadí. Odeslat čtvrtletní e-mail s novou verzí (jen seznamu tipů).

## 8. Co je záměrně mimo rozsah
- Skutečné klíče a ID, doména, identifikace provozovatele.
- Grafika e-mailů a jejich nastavení v Ecomailu (texty jsou hotové v `docs/emaily.md`, postup v bodě 3).
