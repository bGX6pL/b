# Dvě verze reklamy

Obě reklamy jsou připravené pro Meta (Instagram + Facebook: Feed, Stories, Reels). Kreativy se generují z `ads/creative.html` stejnými daty a stejným vzorcem jako landing pages (`tools/render_ads.py`), takže číslo v reklamě vždy sedí s číslem na stránce.

| | Reklama 1 — Dvojče | Reklama 2 — Účtenka |
|---|---|---|
| Úhel | Problém + zvědavost („proč VOO nejde koupit?“) | Peníze + překvapení („kolik mě stojí poplatky?“) |
| Pro koho | Samouk z Instagramu, zná VOO/SPY/QQQ | I bankovní střadatel, ETF zná jen z doslechu |
| Landing page | **A — Dvojče** (`/a-dvojce/?t=VOO`), alt. **D** (`/d-portfolio/?p=sp`) | **B — Účtenka** (`/b-poplatky/?m=3000&y=20`), alt. **C** (`/c-srovnani/?sort=ter`) |
| Feed 4:5 | `ads/ad-1-dvojce-feed.png` | `ads/ad-2-uctenka-feed.png` |
| Stories/Reels 9:16 | `ads/ad-1-dvojce-story.png` | `ads/ad-2-uctenka-story.png` |

Slib reklamy a první obrazovka stránky jsou **stejná věta a stejný obrázek** — návštěvník během první vteřiny pozná, že je na správném místě.

---

## Reklama 1 — „Dvojče“

![Reklama 1 feed](../ads/ad-1-dvojce-feed.png)

**Primární text** (prvních ~125 znaků je vidět bez „Zobrazit víc“):
> VOO, SPY ani QQQ vám většina brokerů v Česku neprodá. Ke každému ale existuje evropské „dvojče“ se stejným indexem.
>
> Srovnali jsme 20 známých ETF z burzy NYSE: poplatky, výnosy a jejich dvojčata, která si koupíte normálně. Plus poplatky 6 brokerů a daně na jedné stránce.
>
> Tahák v PDF zdarma. Stačí e-mail, žádný telefon.

**Nadpis:** Chcete VOO? Tady je jeho dvojče
**Popis:** 20 ETF z NYSE + dvojčata · PDF zdarma
**Tlačítko:** Stáhnout
**URL:** `https://[doména]/a-dvojce/?t=VOO&utm_source=meta&utm_medium=paid_social&utm_campaign=etf_tahak_2026&utm_content=ad1_dvojce`

**Varianty textu na test (stejný vizuál):**
- „Hledáte VOO u XTB nebo Trading 212 a nejde to? Není to chyba aplikace…“
- Vizuál s SPY nebo QQQ místo VOO → odkaz s `?t=SPY` / `?t=QQQ` (stránka otevře přesně ten fond).

---

## Reklama 2 — „Účtenka“

![Reklama 2 feed](../ads/ad-2-uctenka-feed.png)

**Primární text:**
> Stejné akcie, jiný poplatek. Typický akciový fond od banky si bere kolem 2 % ročně a k tomu vstupní poplatek. ETF z americké burzy NYSE a jejich evropská dvojčata začínají na 0,03 %.
>
> Při 3 000 Kč měsíčně je to za 20 let rozdíl ve stovkách tisíc korun. Spočítejte si to sami za 5 vteřin.
>
> Výpočet a tahák nejlevnějších ETF pošleme zdarma do e-mailu.

**Nadpis:** Účtenka za 20 let investování
**Popis:** Kalkulačka poplatků + tahák zdarma
**Tlačítko:** Zjistit více
**URL:** `https://[doména]/b-poplatky/?m=3000&y=20&utm_source=meta&utm_medium=paid_social&utm_campaign=etf_tahak_2026&utm_content=ad2_uctenka`

V kreativě je drobným písmem předpoklad výpočtu (7 % ročně před poplatky, modelový výpočet) — tvrzení „rozdíl ve stovkách tisíc“ je tak podložené a dohledatelné na stránce („Jak počítáme“).

---

## Nastavení kampaně (návrh)

- **Cíl:** Potenciální zákazníci (Leads) s konverzí na webu, událost `Lead` z Meta Pixelu (vyvolá se na úspěšné odeslání formuláře) + doporučeně Conversions API ze serveru.
- **Publikum:** ČR, 22–45 let, Advantage+ audience se signály: investování, ETF, akcie, XTB, Trading 212, Portu, finanční gramotnost. Vyloučit stávající kontakty (nahraný seznam).
- **Umístění:** Advantage+ placements; kreativa 4:5 pro feed, 9:16 pro Stories/Reels.
- **Rozpočet testu:** 2 reklamy × 2 landing pages, rovnoměrně, cca 7 dní nebo 300 návštěv na kombinaci.
- **Pozor na zakázané praktiky:** žádné garantované výnosy, žádné celebrity, žádné „zbohatněte“. Kategorie finanční služby — viz `research/cz-context.md` (ověření inzerenta).
