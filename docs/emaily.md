# E-mailová sekvence po odeslání formuláře

Pravidla pro všechny e-maily: krátké (čtou se na mobilu), jedna myšlenka a jeden odkaz, odesílatel je člověk se jménem + značka (např. „Petra z ETF taháku“), patička s identifikací provozovatele, důvodem, proč e-mail chodí, a odhlášením jedním klikem. Žádné přílohy (horší doručitelnost) — PDF je odkaz.

Proměnné: `{{dvojce}}` (blok s dvojčetem, výpočtem nebo lístkem podle varianty), `{{broker}}` (odpověď z děkovací stránky), `{{pdf_url}}`.

---

**Kdo dostává co:** E-mail 0 (tahák) dostane každý, kdo zadá e-mail — je transakční a nesmí obsahovat propagaci. Potvrzovací e-mail a sekvenci 1–4 + čtvrtletní aktualizace dostanou jen ti, kdo na děkovací stránce klikli „Ano, posílejte“ a odběr potvrdili (double opt-in).

## E-mail 0 — hned po odeslání (všem, transakční)
**Předmět:** Váš ETF tahák (PDF)
**Preheader:** 20 ETF z NYSE, jejich evropská dvojčata, brokeři a daně na 2 stranách.

> Dobrý den,
>
> tady je slíbený tahák: **[Stáhnout ETF tahák 2026 (PDF)]({{pdf_url}})**
>
> {{dvojce}}
>
> Na první straně najdete 20 ETF z burzy NYSE a ke každému evropské dvojče — ISIN stačí zkopírovat do vyhledávání v aplikaci brokera. Na druhé straně je, kolik berou brokeři v ČR, a daně v pěti bodech.
>
> Petra, ETF tahák
>
> *P. S. Nikdy vám nebudeme volat. Pokud vám kvůli investicím volá někdo neznámý sám od sebe, buďte opatrní.*

---

## Potvrzení odběru — hned, jen po „Ano, posílejte“
**Předmět:** Potvrďte prosím odběr tipů o ETF
> Klikli jste, že chcete 4 krátké tipy o ETF a čtvrtletní aktualizace taháku. Potvrďte to prosím jedním klikem: **[Ano, chci odebírat]**
>
> Pokud jste to nebyli vy, e-mail ignorujte — nic vám posílat nebudeme. Tahák už máte v samostatném e-mailu.

---

## E-mail 1 — D+1 (jen potvrzení odběratelé)
**Předmět:** 3 chyby při prvním nákupu ETF
**Preheader:** Dvě z nich stojí peníze, třetí nervy u daňového přiznání.

> 1. **Kupujete na špatné burze nebo v jiné měně.** Stejný fond se obchoduje třeba v eurech na Xetře i v dolarech v Londýně. Každá směna korun stojí procento navíc — vyberte si jednu kotaci a držte se jí.
> 2. **Distribuční místo akumulační.** Distribuční třída vám vyplácí dividendy, které musíte uvést v daňovém přiznání. Akumulační je reinvestuje uvnitř fondu.
> 3. **Hledáte podle názvu, ne podle ISIN.** Názvy se podobají („S&P 500 UCITS ETF“ jich existuje desítky). ISIN je jednoznačný.
>
> **[Tahák s ISIN všech 20 dvojčat]({{pdf_url}})**

---

## E-mail 2 — D+3 (personalizovaný podle `{{broker}}`)
**Předmět:** Jak najít dvojče VOO u {{broker}}
**Preheader:** Krok za krokem, s poplatky, které tam zaplatíte.

> Vybrali jste **{{broker}}**. Takhle tam najdete a koupíte evropské dvojče:
>
> 1. V aplikaci otevřete vyhledávání a vložte ISIN (např. `{{isin}}`).
> 2. Vyberte kotaci v {{mena_doporucena}} — u {{broker}} vás směna stojí {{fx_fee}}.
> 3. Pokud chcete investovat pravidelně, {{broker}} nabízí {{plan_info}}.
>
> Kolik zaplatíte za nákup, směnu a vedení účtu, máte v taháku na str. 2.
>
> *(Varianta „Zatím nikde“: srovnání 6 brokerů ve třech větách + odkaz na nabídku klienta.)*

---

## E-mail 3 — D+6
**Předmět:** Daně z ETF: kdy nemusíte řešit nic
**Preheader:** Časový test, limit 100 000 Kč a co s dividendami.

> - **Držíte déle než 3 roky?** Zisk z prodeje je osvobozený (časový test). Limit 40 mil. Kč platil jen pro rok 2025, od 1. 1. 2026 se na cenné papíry nevztahuje.
> - **Prodáte za méně než 100 000 Kč za rok?** I pak je příjem osvobozený.
> - **Akumulační fond** nevyplácí dividendy, takže do prodeje nic nepřiznáváte.
> - **Distribuční fond** = dividendy patří do daňového přiznání.
>
> *Daňové informace jsou zjednodušené, vycházejí z předpisů platných k [datum], závisí na vašich individuálních poměrech a mohou se změnit. Nejde o daňové poradenství.* Podrobnosti a zdroje: str. 2 taháku.

*(Formulace v tomto e-mailu se finalizují podle `research/cz-context.md`, kapitola Daně.)*

---

## E-mail 4 — D+10
**Předmět:** Než pošlete první peníze: 5 otázek
**Preheader:** Kontrolní seznam na jednu obrazovku.

> 1. Mám rezervu na 3–6 měsíců mimo investice?
> 2. Vydržím, když hodnota na rok klesne o třetinu?
> 3. Investuji na 10 a více let?
> 4. Vím, kolik mě stojí nákup a směna u mého brokera?
> 5. Mám ISIN fondu, ne jen název?
>
> **[Nabídka klienta — např. webinář, srovnání brokerů, otevření účtu u partnera, konzultace]**
>
> Další e-mail od nás přijde až s aktualizovaným tahákem za čtvrtletí.

---

## Čtvrtletně — aktualizace
**Předmět:** ETF tahák — aktualizace k {{datum}}
> Co se změnilo: nové poplatky ({{zmeny}}), výnosy k {{datum}}. **[Stáhnout aktuální verzi]({{pdf_url}})**

---

## Patička (všechny e-maily)
> Tento e-mail dostáváte, protože jste se po stažení ETF taháku na [doména] přihlásili k odběru tipů. **[Odhlásit se jedním klikem]** · Provozovatel: [společnost s.r.o., IČO, sídlo] · Obsah má informační charakter a není investičním doporučením. Investování je spojeno s rizikem.
