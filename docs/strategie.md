# ETF tahák — strategie lead magnetu

> Landing page se srovnáním ETF z burzy NYSE pro českého drobného investora, který přichází z reklamy na mobilu a stránce dá pár vteřin. Cíl: získat e-mail výměnou za hodnotu, kterou návštěvník vidí ještě před vyplněním formuláře.

## Ve zkratce

1. **Klíčový insight:** Čech, který „chce koupit VOO“, ho u svého brokera nenajde. Většina brokerů v EU americká ETF drobným investorům neprodá, protože nemají dokument KID (nařízení PRIIPs). Ke skoro každému ale existuje evropský fond (UCITS) na stejný index — **„evropské dvojče“**. Kdo srovnává ETF z NYSE, ve skutečnosti hledá, *co si z toho může koupit on*. To je hodnota, kterou mu dáme.
2. **Výměnou za e-mail:** *ETF tahák 2026* — PDF na 2 strany: 20 ETF z NYSE, jejich evropská dvojčata (ISIN, ticker, poplatek), poplatky 6 brokerů dostupných v ČR a daně na jedné stránce. K tomu osobní výstup z interaktivního prvku (dvojče, výpočet, nákupní lístek) a čtvrtletní aktualizace.
3. **Kdy o kontakt žádáme:** až po první „malé výhře“ — výsledek interaktivního prvku je předvyplněný už v první obrazovce, formulář je hned pod ním. Žádný pop-up při vstupu.
4. **Formulář:** jedno pole (e-mail). Žádné jméno, **nikdy telefon** — v Česku je to i signál „nejsme podvodný call centrum“.
5. **Po odeslání:** okamžité stažení PDF na děkovací stránce (bez čekání na e-mail), odemčená tabulka všech dvojčat, jedna otázka na 1 klik („kde investujete?“) pro segmentaci a 4 krátké e-maily během 10 dnů.
6. **Čtyři varianty stránky** (A–D) testují čtyři různé interaktivní háčky; **dvě reklamy** (Dvojče, Účtenka) mají každá svou dvojici stránek se shodným slibem.

---

## 1. Cílová skupina

### Primární: „Samouk z Instagramu“
| | |
|---|---|
| Věk | 22–40 let (jádro 25–34) |
| Situace | Zaměstnaný, příjem kolem a nad mediánem, větší město. Na spořicím účtu 50 000–500 000 Kč, chce investovat 2 000–10 000 Kč měsíčně. |
| Znalosti | O ETF, S&P 500 a „VOO“ slyšel z YouTube, TikToku, Redditu nebo od kamaráda. Neví, co je KID, UCITS, akumulační třída, ani jak se ETF daní. |
| Stav | Buď už má účet (XTB, Trading 212, Revolut…) a VOO tam nenašel, nebo se teprve rozhoduje, kde začít. |
| Postoj | Nechce „poradce“ ani bankovní fond. Nedůvěřuje reklamám na investice (v Česku plných podvodů s deepfaky celebrit). Chce čísla, ne sliby. |
| Kontext návštěvy | Mobil, in-app prohlížeč Instagramu/Facebooku, jedna ruka, MHD nebo večer na gauči. Na stránce rozhoduje během 3–8 vteřin. |

**Job to be done:** *„Chci koupit to, co doporučují všichni na internetu, ale v Česku, správně, levně a bez problémů s daněmi.“*

**Bolesti, které stránka řeší:**
1. VOO/SPY/QQQ v aplikaci nejde koupit (chybí KID) → zmatek, „dělám něco špatně?“
2. Stovky fondů s podobnými názvy, ISINy, burzy, měny.
3. Nejasné poplatky (TER, směna měny, poplatky brokera).
4. Daně (časový test, dividendy, W-8BEN) působí děsivě.
5. Strach z podvodu — nechce, aby mu někdo volal.

### Sekundární: „Bankovní střadatel“ (35–55)
Má peníze v podílovém fondu od banky nebo v „investičním životku“, platí vstupní poplatek a kolem 2 % ročně a netuší, kolik ho to stojí. Na něj míří reklama **Účtenka** a varianta **B**. Je méně digitální, ale má víc peněz — pro klienta (broker, vzdělávací projekt) cennější lead.

### Koho necílíme
Aktivní tradery, profesionální klienty (ti VOO koupit mohou), lidi bez úspor. Nepomůže jim to a zkreslí to metriky.

### Proč tahle skupina
Slib „srovnání ETF z NYSE“ si sám vybírá lidi, kteří už znají americké tickery — mají **vysoký úmysl začít investovat** a konkrétní, neřešený problém. Jsou to nejcennější leady pro brokera, robo-advisora i vzdělávací projekt.

---

## 2. Co návštěvník dostane

### ETF tahák 2026 (PDF, 2 strany)
| Strana | Obsah |
|---|---|
| 1 | **20 ETF z NYSE** v jedné tabulce: index, poplatek (TER), velikost, dividenda, výnos za 1/5/10 let. **U každého evropské dvojče:** název, ISIN, ticker na Xetře a v Londýně, poplatek, akumulační/distribuční. |
| 2 | **Kde koupit v ČR:** 6 brokerů — poplatek za nákup, směna korun, vedení účtu, pravidelné investování. **Daně v 5 bodech:** časový test 3 roky, limit 100 000 Kč, dividendy a W-8BEN, akumulační fondy, americká dědická daň u US fondů. **Kontrolní seznam** před prvním nákupem. |

**Plus osobní výstup** z interaktivního prvku dané varianty (dvojče k vybranému fondu / výpočet poplatků / nákupní lístek portfolia), **plus aktualizace každé čtvrtletí** (důvod zůstat přihlášený).

### Proč právě tohle
- **Řeší přesně to, co slíbila reklama** (srovnání ETF z NYSE) a přidává „aha“, které jinde v češtině na jednom místě není (dvojčata + daně + brokeři).
- **Je okamžitě použitelné:** ISIN zkopíruje do aplikace brokera a nakoupí. Žádný 40stránkový e-book, který nikdo nepřečte.
- **Levné na výrobu a údržbu:** generuje se z jednoho datového souboru (`data/etfs.json`), aktualizace jednou za čtvrtletí.
- **Segmentuje:** podle toho, na co klikal, víme, co ho zajímá (S&P 500 vs. dividendy vs. poplatky).

### Hodnota je vidět ještě před formulářem
Každá varianta ukazuje skutečná data už v první obrazovce, bez kliknutí: dvojče k VOO (A), účtenku poplatků (B), žebříček fondů (C), přeložené portfolio (D). Formulář slibuje „zbytek“ — dalších 19 dvojčat, brokery, daně — nikoli to, co už návštěvník vidí. Tím se e-mail mění z ceny za vstup na cenu za *víc toho, co už mi pomohlo*.

---

## 3. Kdy o kontakt žádáme

**Princip: nejdřív malá výhra, pak otázka.** Návštěvník z reklamy přijde s jednou otázkou v hlavě („kde je to dvojče?“, „kolik mě stojí poplatky?“). Stránka mu na ni odpoví v první obrazovce a formulář umístí *přímo pod odpověď* — v okamžiku nejvyšší zvědavosti.

| Místo | Kdy | Proč |
|---|---|---|
| **1. Pod výsledkem v první obrazovce** | Hned — výsledek je předvyplněný (VOO, 3 000 Kč × 20 let…) | 3vteřinový návštěvník vidí hodnotu i formulář bez scrollu. |
| **2. Po interakci** | Když klikne na jiný fond / částku / portfolio | Text pod formulářem se přepíše na jeho volbu („Pošleme dvojče k SPY a dalších 19“). Personalizovaný slib zvyšuje konverzi. |
| **3. Zamčený obsah** | Když klepne na rozmazané dvojče nebo „Odemknout všech 20“ | Otevře se spodní panel s jedním polem — přirozený moment „chci víc“. |
| **4. Plovoucí lišta (mobil)** | Jakmile hlavní formulář zmizí z obrazovky | Kdo scrolluje, má CTA stále na palec. Schová se, když je na obrazovce jiný formulář. |
| **5. Konec stránky** | Po FAQ | Pro ty, kdo potřebovali odpovědi na námitky. |

**Co vědomě neděláme:** pop-up při vstupu (na mobilu zakryje slib reklamy a Google ho penalizuje), exit-intent na mobilu, vícekrokový formulář, odpočet času, falešné „zbývá 12 kusů“.

---

## 4. Formulář: jedno pole

- **E-mail, nic víc.** Jméno nepotřebujeme (tykat/vykat oslovením nebudeme), telefon nikdy.
- **Tlačítko říká, co dostanu:** „Poslat tahák“, „Odemknout“, „Poslat lístek“ — ne „Odeslat“.
- **Pod polem jedna věta:** co přijde, že bez telefonu a že odhlášení je jedním klikem. Odkaz na ochranu údajů.
- **Oprava překlepů v doméně** (`seznam.cs` → `seznam.cz`, `gmial.com` → `gmail.com`) — v Česku je velký podíl schránek na Seznamu, překlep = ztracený lead.
- **Klávesnice pro e-mail** (`inputmode="email"`, `autocomplete="email"`) → na mobilu jeden ťuk na návrh adresy.
- **Honeypot** místo CAPTCHA (CAPTCHA na mobilu zabíjí konverzi).
- **Žádné zaškrtávátko:** souhlas s navazujícími e-maily je jasně napsaný u tlačítka a odhlášení je v každém e-mailu. *(Právní posouzení: viz `research/cz-context.md`; pokud právník trvá na samostatném souhlasu, přidá se jedno nepovinné zaškrtávátko — tahák se pošle i bez něj.)*

---

## 5. Po odeslání

### Děkovací stránka (`/dekujeme/`) — navazuje vzhledem na variantu, ze které přišel
1. **„Hotovo. Tahák je váš.“ + tlačítko Stáhnout PDF.** Okamžitá odměna; nemusí čekat na e-mail (ten může skončit v Promoakcích).
2. **Jeho osobní výstup** — dvojče k fondu, který vybral / jeho výpočet / jeho nákupní lístek s ISIN.
3. **Odemčená tabulka všech dvojčat** — splněný slib „odemknout“.
4. **Jedna otázka, 1 klik:** „Kde investujete, nebo chcete začít?“ (XTB, Trading 212, DEGIRO, IBKR, Fio, Revolut, Portu/Fondee, jinde, zatím nikde). Progresivní profilace bez dalšího pole ve formuláři. Odpověď řídí obsah e-mailu č. 3 a je nejcennější segmentací pro klienta.
5. **Co přijde dál:** časová osa e-mailů — žádné překvapení, méně odhlášení.

### E-mailová sekvence (detail v `docs/emaily.md`)
| Kdy | E-mail | Cíl |
|---|---|---|
| hned | Tahák v PDF + osobní výstup | Doručit slib, ověřit adresu |
| D+1 | 3 chyby při prvním nákupu ETF | Užitečnost → otevírání dalších e-mailů |
| D+3 | Dvojče u vašeho brokera (podle odpovědi z děkovací stránky) | Personalizace, první konverzní krok klienta |
| D+6 | Daně bez stresu | Odstranit poslední bariéru |
| D+10 | Kontrolní seznam před prvním nákupem + nabídka klienta | Konverze na produkt klienta |
| čtvrtletně | Aktualizovaný tahák | Udržet seznam živý a legitimní |

---

## 6. Čtyři varianty stránky

| | A — Dvojče | B — Účtenka | C — Žebříček | D — Přeložit portfolio |
|---|---|---|---|---|
| **URL** | `/a-dvojce/` | `/b-poplatky/` | `/c-srovnani/` | `/d-portfolio/` |
| **Háček** | „Chcete VOO? Tady je jeho evropské dvojče.“ | „Kolik vám za 20 let sebere poplatek?“ | „Srovnali jsme 20 ETF z NYSE. Tady je výsledek.“ | „Složte si portfolio z amerických ETF. Přeložíme ho do evropských.“ |
| **Interakce** | Výběr fondu (VOO, SPY, QQQ…) → lístek US fondu s razítkem „V EU nekoupíte“ a pod ním dvojče s ISIN | Částka × doba → účtenka: bankovní fond vs. VOO vs. jeho dvojče | Řazení podle velikosti, poplatku, výnosu, dividendy; sloupec dvojčat zamčený | Vzorová portfolia z YouTube/Redditu, úprava poměrů → nákupní lístek evropských ETF, vážený poplatek, podíl USA |
| **Co je zamčené** | Dalších 19 dvojčat | Dvojčata nejlevnějších fondů, brokeři | Dvojčata 19 z 20 fondů | ISIN dalších fondů v lístku |
| **Vizuální jazyk** | Papír a inkoust, lístky s perforací, razítko | Tmavá, termopapírová účtenka, limetková | Noviny / datová žurnalistika, serif, zvýrazňovač | Teplá, „recept“, barevné podíly |
| **Pro reklamu** | 1 Dvojče | 2 Účtenka | 2 Účtenka (`?sort=ter`) nebo obecná | 1 Dvojče (`?p=…`) |
| **Hypotéza** | Nejsilnější „aha“, nejrychlejší pochopení | Peníze jsou nejsilnější motivace, osloví i sekundární skupinu | Nejvěrnější zadání, působí nejdůvěryhodněji | Nejvyšší osobní hodnota → nejkvalitnější leady |
| **Riziko** | Kdo VOO nezná, nepochopí háček | Výpočet stojí na předpokladech (7 % p.a., poplatky banky) | Méně „wow“, formulář až pod tabulkou | Složitější, delší čas do výsledku |

**Doporučení pro první test:** A a B (každá se svou reklamou). C a D jako druhé kolo proti vítězi. Všechny čtyři jsou připravené ke spuštění.

### Dynamická shoda s reklamou (message match)
Stránky čtou parametry z URL reklamy, takže první obrazovka může zopakovat přesně to, co bylo v reklamě:
- A: `?t=SPY` → stránka otevře rovnou SPY a nadpis „Chcete SPY?…“
- C: `?sort=ter` → žebříček seřazený podle poplatku
- D: `?p=div` → otevře dividendové portfolio

---

## 7. Dvě reklamy
Kreativy jsou v `ads/` (PNG 1080×1350 pro feed a 1080×1920 pro Stories/Reels), texty a nastavení v `docs/reklamy.md`.

**Reklama 1 — „Dvojče“** (problém, zvědavost) → stránka A (alt. D)
**Reklama 2 — „Účtenka“** (peníze, překvapení) → stránka B (alt. C)

---

## 8. Měření

**Události** (v `dataLayer`, do Meta/GA4 jen se souhlasem): `lp_view`, `finder_select`, `calc_change`, `table_sort`, `builder_preset`, `lead_sheet_open`, `lead_form_start`, `generate_lead` (Meta: `Lead`), `lead_thankyou_view`, `lead_profile`.

**Trychtýř a cílové hodnoty pro první týden** (orientační; benchmarky ověříme na vlastních datech):
| Krok | Metrika | Cíl |
|---|---|---|
| Reklama | CTR odkazu | ≥ 1,2 % |
| Stránka | podíl návštěv s interakcí | ≥ 35 % |
| Stránka | konverze návštěva → e-mail | ≥ 20 % |
| Děkovačka | odpověď na otázku „kde investujete“ | ≥ 50 % |
| E-maily | open rate e-mailu č. 1 / proklik | ≥ 55 % / ≥ 20 % |
| Kvalita | odhlášení do 10 dnů | ≤ 6 % |

**Test:** 2 reklamy × 2 stránky, rovnoměrný rozpočet, min. 300 návštěv na variantu, rozhoduje cena za lead *a* podíl odpovědí „mám brokera / chci začít“ (kvalita).

---

## 9. Právní a regulatorní minimum
Podrobně v `research/cz-context.md` a `docs/spusteni.md`.
- **Není to investiční doporučení:** stránky srovnávají veřejná data, nic nedoporučují, vzorová portfolia jsou označená jako příklady. Na každé stránce je standardní upozornění na riziko, minulé výnosy a měnové riziko.
- **Minulé výnosy** jen jako doplňkový údaj, vždy s datem, měnou (USD) a zdrojem, za 1/5/10 let.
- **E-maily:** souhlas jasně u tlačítka, odhlášení v každém e-mailu, správce a účely v `/ochrana-udaju/`.
- **Cookies:** měřicí kódy Meta a Google se načtou až po souhlasu; „Odmítnout“ je stejně velké jako „Povolit“.
- **Fonty hostujeme sami** — žádný přenos IP adresy na Google při načtení stránky.

## 10. Co chybí ke spuštění zítra
Viz `docs/spusteni.md` — identifikace provozovatele, napojení formuláře na e-mailovou službu, ID Meta Pixelu / GA4, doména, kontrola právníkem, schválení reklam.
