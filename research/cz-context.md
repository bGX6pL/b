# CZ context for the ETF lead-magnet landing page

Research compiled 2026-10-29 (Europe/Prague). Every claim carries a source link and the date it was read ("read 2026-10-29" unless stated otherwise). Raw downloads are under `D:\etf-landing\data\raw\downloads\<source>\` (untrusted data, never executed). Hard numbers for the page are in `D:\etf-landing\data\raw\cz-context.json`.

Legend: **[UNCERTAIN]** = could not be verified from a primary source, or sources conflict. **[MY READING]** = legal interpretation, not a regulator's statement; get it checked by a lawyer before relying on it.

---

## 0. Launch blockers and contradictions with the brief (short)

(Filled in at the end; see bottom of the file.)

---

## 1. Přístup k US ETF pro české retailové klienty (PRIIPs/KID)

_(in progress)_

## 2. Náklady nákupu UCITS ETF u brokerů

_(in progress)_

## 3. Zdanění fyzických osob v ČR

_(in progress)_

## 4. Typické náklady bankovních podílových fondů

All figures read on 2026-10-29.

**Terminology.** KID ("sdělení klíčových informací") figures use PRIIPs terms. "Náklady na vstup" is a maximum; the distributor may charge less. "Poplatky za vedení a jiné správní nebo provozní náklady" corresponds to ongoing charges / TER. Transaction costs and performance fees are reported separately.

### 4.1 Flagship equity funds sold by Czech banks and large distributors

| Fund (ISIN) | Distributor | Entry fee (max) | Ongoing | Transaction | Performance fee | RIY at RHP | KID date |
|---|---|---|---|---|---|---|---|
| TOP STOCKS CZK C (CZ0008472404), Erste AM | Česká spořitelna | 3.00 % | 1.88 % | 0.06 % | none | 2.6 % p.a. (5 y) | 01.07.2026 |
| Amundi Funds Global Equity A CZK Hgd (LU1894680591) | KB | 3.00 % per KB price list; KID max 4.50 % | 1.93 % | 0.54 % | 20 % of outperformance vs MSCI World CZK hedged (5-y avg ≈ 0.41 % p.a.) | 4.3 % p.a. (5 y, with 4.5 % entry) | published 19.08.2026 |
| ČSOB Akciový (770000001170) | ČSOB | 3.00 % | 2.59 % (KID says "odhad") | 0.39 % | none | 3.4 % p.a. (8 y) | 01.06.2026 |
| Raiffeisen fond amerických akcií (CZ0008475175) | Raiffeisenbank | **0 %** | 2.24 % | 0 % | yes, 5-y avg 0.46 % p.a. | 3.06 % p.a. (7 y) | 17.02.2026 |
| Generali Fond globálních značek R CZK (CZ0008471778) | Generali Investments CEE | 4.0 % (0–99 999 Kč; 3.5/3/2.5 % above) | 2.3 % (TER 2.32 %) | 0.1 % | none | 3.5 % p.a. (5 y) | 01.06.2026 |
| Conseq Invest Akcie Nové Evropy A (CZ0008477049) | Conseq (Classic Invest) | 5.00 % (<350 000 Kč) | 1.34 % (mgmt fee 1.15 %) | n/a | n/a | n/a | KID not read |

Sources per fund (all read 2026-10-29):

- **TOP STOCKS** – KID: https://data.erste-am.com/gem/erste-am/getDocumentContent/20020871-c83a-4843-adbc-fedff51e9282 ; Erste AM key-facts API: https://data.erste-am.com/gem/erste-am/GEM_FACTSHEET;ddsSources=FUND_KEYFACTS,FUND_DOCUMENTS_PUBLIC?ISIN=CZ0008472404 (OGC 1.88 %, management fee 1.70 %, sales charge 3.00 %, assets CZK 33 986 mil. at 30.09.2026). Česká spořitelna price list effective 23.10.2026: https://www.csas.cz/static_internet/cs/Obchodni_informace-Produkty/Sazebnik/Produktove_sazebniky/Prilohy/vybrane_polozky_investovani.pdf – equity funds 3.00 %; regular investing: no discount for contributions 1–12, 25 % off for 13–36, 50 % off from the 37th. Other Erste funds sold by ČS (same API): Sporotrend 3 % / 1.90 %; Global Stocks FF 3 % / 2.53 %; Erste Responsible Stock Global CZK KID max 5 % / 1.78 %.
- **Amundi Funds Global Equity A CZK Hgd** – KID: https://www.amundi.cz/produkty/dl/doc/kid-priips/LU1894680591/CES/CZE ; KB "Ceník Amundi Invest" effective 1.10.2026: https://www.kb.cz/getmedia/938b9cfc-cf67-4be9-9a44-b3b78bfc6b74/CZ-014-20261001_Cenik-Amundi-Invest_KB.pdf ("AMUNDI FUNDS GLOBAL EQUITY (CZK Hedged) 3,00 %"; KB Portfolio – Akciových indexů 3 % below 1 mil. / 2 % above).
- **ČSOB Akciový** – KID: https://multimediafiles.kbcgroup.eu/ng/feed/am/funds/KID/KID_770000001170_CS.PDF ; fund page: https://www.csobam.cz/podilove-fondy/detail/isin/770000001170/1 (entry 3.00 %, management fee 1.90 % falling to 1.80 % from 1.1.2027; equity capital CZK 18 586 mil.). ČSOB "Parametry trhů CP" effective 15.6.2026: https://cdn.patria.cz/CSOB-parametry-fondu.pdf (domestic equity funds 3.00 %).
- **Raiffeisen fond amerických akcií** – KID: https://www.rb.cz/attachments/ris/KID-RFAA-CZ.pdf ; RB "Parametry fondů" effective 1.10.2026: https://www.rb.cz/attachments/ris/parametry_fondu.pdf (0 % entry on all RIS equity and strategy funds; 1 % on most third-party funds); factsheet 09/2026: https://www.rb.cz/attachments/ris/report_RFAA.pdf (fee to the investment company 1.7 %, NAV CZK 4 187 mil.).
- **Generali Fond globálních značek** – KID: https://www.generali-investments.cz/media/generali/docs/KID_CZ_CZ0008471778_FGZ_20260601.PDF ; fund page with entry-fee bands and TER 2.32 % (management fee 2.2 %): https://www.generali-investments.cz/produkty/investice-v-czk/fondy/generali-fond-globalnich-znacek.html
- **Conseq Invest Akcie Nové Evropy** – fund page (ongoing charges): https://www.conseq.cz/investice/prehled-fondu/conseq-invest-akcie-nove-evropy-a-cs ; Classic Invest price list Saz-CCI-2510 effective 1.10.2025 (newest found): https://www.conseq.cz/getmedia/38db4ef5-0f76-482f-8502-f8d7cf84866a/CCI-Sazebnik-2510.pdf.aspx ("Dynamické" category 5.00 % / 4.10 % / 3.10 % by ticket size; prepaid entry fee on target amount 3.10–4.60 %, non-refundable).

Caveats: Conseq fund is Central European equity, not global; RFAA KID classifies the fund as "dynamický smíšený" feeder (≥85 % in Raiffeisen's US equity master fund); the ČSOB 2.59 % ongoing figure is labelled an estimate in the KID. **[UNCERTAIN]** Conseq ongoing figure is from the web page, not the KID; Conseq price list dated 1.10.2025.

**Prepaid / regular-investment fee structures**
- KB "EXPRES": entry fee for an Investiční plán can be prepaid on the whole target amount (up to 10 years, up to 5.4 mil. Kč) with a 15 % discount on the rate (KB price list above).
- Conseq: prepaid fee, non-refundable (price list above).
- **ČNB warning, 25.6.2024**: prepaid fees can take up to 100 % of the first contributions, and the discount "nemusí … kompenzovat snížení celkového výnosu". https://www.cnb.cz/cs/dohled-financni-trh/vykon-dohledu/upozorneni-pro-verejnost/Varovani-Ceske-narodni-banky-pro-retailove-investory-ohledne-nakladu-anbsppoplatku-vnbspsouvislosti-snbspinvestovanim (read 2026-10-29)

**Inducements** (part of the ongoing fee goes to the distributor): KB receives 0.093–1.17 % p.a. from the management fee plus a one-off 1.0–3.0 % acquisition fee (KB price list 1.10.2026). RB receives up to 64 % of the RIS management fee plus up to 60 % of entry fees (undated): https://www.rb.cz/attachments/investice/dip/informace-o-pobidkach.pdf

**Entry-fee computation differs (matters for the calculator):** ČS/Erste and KB charge a mark-up ("přirážka") inside the amount paid: fee = amount × rate/(1+rate) (KB formula; ČS KID: 3 % on 250 000 Kč = 7 282 Kč ≈ 2.91 % of the payment). ČSOB KID: 7 500 Kč on 250 000 Kč, i.e. a flat 3 %.

### 4.2 Studies and averages

- **ESMA, Market Report on Costs and Performance of EU Retail Investment Products 2025** (published 3.3.2026, data to end-2024): https://www.esma.europa.eu/sites/default/files/2026-03/ESMA50-1949966494-4065_Market_Report_-_Costs_and_Performance_of_EU_Retail_Investment_Products.pdf (read 2026-10-29). EU27 retail equity UCITS (non-ETF), 1-year horizon, 2024: ongoing costs 1.32 %; maximum subscription + redemption fees 2.48 % (ESMA notes actual fees can be much lower). 5-year horizon 2020–2024: equity funds total costs 1.9 % p.a. (ongoing 1.38 %, subscription 0.51 % p.a. annualised); equity ETFs total 0.5 %, ongoing 0.22 %. **No Czech-specific figures** – CZ is pooled in "Other EU27".
- **ESMA, Report on total costs of investing in UCITS and AIFs** (6.11.2025): https://www.esma.europa.eu/sites/default/files/2025-11/ESMA50-1949966494-3918_Report_on_total_costs_of_investing_in_UCITS_and_AIFs.pdf – total cost of active equity UCITS incl. distribution ≈ 2 % p.a. (EUR 200 per EUR 10 000 per year); distribution = 48 % of UCITS total costs; inducements average 45 % of product ongoing costs. No national breakdowns.
- **Czech academic figure (secondary):** Sobková, Český finanční a účetní časopis 2025/1, DOI 10.18267/j.cfuc.608: https://cfuc.actavia.vse.cz/pdfs/cfu/2025/01/02.pdf – cites an average cost of Czech funds of 2.1 % (Čermák 2019) and an average management fee of 1.98 % across 57 equity funds (Conseq 2022).
- **ČNB:** no ČNB study of average fund fees found. Closest: press release of 15.4.2026 – investment intermediaries passed orders worth more than CZK 65 bn in 2024 and received more than CZK 3.6 bn in commissions: https://www.cnb.cz/cs/cnb-news/tiskove-zpravy/Reakce-CNB-na-tiskovou-zpravu-CASF-zedne-15.dubna2026
- **AKAT:** asset statistics only, no cost statistics found.

### 4.3 Proposed benchmark: "typický akciový fond prodávaný bankou"

- **Entry fee 3.0 %** per contribution – median of the maximum small-ticket entry fee across the 6 funds (0 / 3 / 3 / 3 / 4 / 5 %); also the standard equity-fund rate at ČS, KB and ČSOB.
- **Ongoing 2.0 % p.a.** – median of the 6 funds 2.09 %, mean 2.05 %, range 1.34–2.59 %; consistent with 1.98 % (Conseq 2022) and 2.1 % (Čermák 2019); above the ESMA EU average of 1.32 %.
- Optional transaction costs +0.1–0.2 % p.a. (median 0.10 %, mean 0.22 %).
- Cross-check: median KID annual cost impact (RIY) at the recommended holding period 3.4 % p.a. (range 2.6–4.3 %).
- Sensitivity cases: "cheap bank fund" 0 % entry / 1.9 % ongoing; "expensive" 5 % entry / 2.6 % ongoing.
- **[UNCERTAIN]** KID entry fees are maxima; actual fees may be lower/discounted; KIDs are updated yearly; ČSOB cuts its management fee from 1.1.2027.

**Implications for the landing page (4)**
- Claim "vstupní poplatek obvykle až 3 % a průběžné náklady kolem 2 % ročně". **Do not say "3–5 %" as typical** (RB charges 0 %, ČS discounts regular investing). Footnote with the KID list and dates.
- Prefer an anonymised "typický bankovní akciový fond (medián 6 fondů, KID k datu …)" over naming banks. If funds are named, quote exact KID figures/dates and refresh them when KIDs change.
- Use PRIIPs wording ("Náklady na vstup", "Poplatky za vedení…") so readers can check their own fund's KID.
- Cite the ČNB prepaid-fee warning (25.6.2024) as a neutral authority.
- Calculator: model entry fee as a mark-up inside the contribution (rate/(1+rate)) and ongoing fee as an annual drag; show the sensitivity cases.
- Banks also sell cheap options (ČS 0.35 % commission on US/German ETFs, George Strategies 0 % entry, Erste's own UCITS ETFs) – avoid absolute claims like "banky prodávají jen drahé fondy".

## 5. Kurzy ČNB (FX)

- **Latest available ČNB fixing: 27.10.2026, #207** – **USD/CZK 21,834**, **EUR/CZK 24,340** (also GBP 29,097). Source: ČNB text feed https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt and EN feed https://www.cnb.cz/en/financial-markets/foreign-exchange-market/central-bank-exchange-rate-fixing/central-bank-exchange-rate-fixing/daily.txt (read 2026-10-29 00:54 CET). Raw: `data/raw/downloads/cnb-fx/`.
- 28.10. is a Czech public holiday (no fixing); the 29.10.2026 fixing is published after 14:30 the same day – re-run the fetch before launch if the page shows a date-stamped rate.

**Implications for the landing page (5)**
- Show the rate with its date: "Kurz ČNB k 27. 10. 2026: 1 USD = 21,834 Kč; 1 EUR = 24,340 Kč."
- For tax illustrations, note that the tax return may use the ČNB daily rate or the single annual rate ("jednotný kurz") – see section 3.

## 6. Marketing / právní náležitosti

Note: EUR-Lex returned an AWS-WAF JavaScript challenge on 2026-10-29 and was not bypassed; MAR / CDR 2016/958 / CDR 2017/565 wording below comes from ESMA/ČNB documents and the legislation.gov.uk copy of 2017/565 as adopted by the EU. Raw copies of Czech statutes: `data/raw/downloads/zakonyprolidi/`.

### 6a. Investment recommendation (MAR) vs investment advice (ZPKT)

- **MAR applies to anyone, not only licensed firms.** An investment recommendation (MAR art. 3(1)(34)–(35)) is information recommending or suggesting an investment strategy, explicitly or implicitly, concerning a financial instrument, incl. opinions on its present or future value or price. ESMA: "any video or any other type of public communications… in which a person gives advice or ideas, directly or indirectly, about buying or selling a financial instrument or on how to compose a portfolio… may constitute an investment recommendation"; using "educational" or non-technical language does not change this. Source: ESMA74-1103241886-912, 6 Feb 2024, https://www.esma.europa.eu/sites/default/files/2024-02/ESMA74-1103241886-912_Warnings_on_Social_Media_and_Investment_Recommendations.pdf (read 2026-10-29; raw `esma/ESMA74-1103241886-912_social_media_IR.pdf`). MAR: https://eur-lex.europa.eu/legal-content/CS/TXT/?uri=CELEX:32014R0596 ; CDR 2016/958: https://eur-lex.europa.eu/legal-content/CS/TXT/?uri=CELEX:32016R0958 (not fetchable live).
- **Duties if content is a recommendation (CDR 2016/958 arts 2, 3, 5), for everyone:** name and job title of the author; date and time of production/release; facts clearly separated from interpretations/opinions; reliable sources; conflicts of interest disclosed in the recommendation itself.
- **Extra duties for "experts" (arts 4, 6):** people who repeatedly propose investment decisions and present themselves as having expertise must add methodology, investment horizon, risk warning, planned update frequency. ESMA cites fines up to EUR 500k (natural persons) / EUR 1m (legal persons). Source: ESMA as above.
- **ČNB finfluencer notice (23 Jan 2025):** a direct recommendation explicitly calls to buy/sell/hold; finfluencers often meet the MAR "odborník" definition; investment advice = "individualizované doporučení ohledně obchodu s konkrétním investičním nástrojem" and differs by the degree of individualisation (replies to comments given as an example); sanctions up to 15 / 30 mil. Kč for breaching recommendation duties; unlicensed advice up to 150 mil. Kč, twice the unlawful gain or 10 % of turnover. https://www.cnb.cz/cs/dohled-financni-trh/ochrana-spotrebitele/upozorneni/Upozorneni-Ceske-narodni-banky-pro-influencery-v-oblasti-financi (read 2026-10-29)
- **ČNB RS2018-08 (25 May 2018):** a recommendation "vydané výlučně pro veřejnost" is not a personal recommendation, but mass/online communication can become advice if the client may perceive it as suited to them, e.g. "tento produkt je pro Vás nejlepším řešením" or "lidé Vám podobní si pořizují tento produkt". https://www.cnb.cz/cs/dohled-financni-trh/legislativni-zakladna/stanoviska-k-regulaci-financniho-trhu/RS2018-08/ (read 2026-10-29)
- **ZPKT (zákon 256/2004 Sb., version effective 1 Sep–31 Dec 2026):** §2(1)(f) investiční poradenství = individualised recommendation to a client on a trade in a specific instrument; §4(2)(e) + §4a: investment advice is a main investment service requiring a ČNB licence; §4(3)(d) "investiční výzkum a finanční analýza nebo jiné formy obecných doporučení" is only an ancillary service. §4(4) + §2(1)(y): "zprostředkování obchodů" (treated as reception and transmission of orders, licensed) includes, on a business basis, "nabízení možnosti… poskytnout investiční službu jménem poskytovatele" and "přípravné práce… včetně poskytování doporučení vedoucího ke sjednání" → **risk for paid broker affiliate links [UNCERTAIN – legal review]**. https://www.zakonyprolidi.cz/cs/2004-256 (read 2026-10-29; raw `zakonyprolidi/2004-256_ZPKT.html`)
- **ZISIF (zákon 240/2013 Sb.):** §294 defines "nabízení investic"; §295: no offering where the investor acts on own initiative; §295a(1): investments in a foreign fund "lze v ČR veřejně nabízet jen… je-li tento fond zapsán v příslušném seznamu vedeném ČNB". US-domiciled NYSE ETFs are not on that list → a comparison page with a buy CTA could be read as public offering **[MY READING – lawyer]**. https://www.zakonyprolidi.cz/cs/2013-240 (read 2026-10-29)
- **MAR scope caveat [UNCERTAIN]:** MAR covers instruments traded on EU venues; Irish UCITS ETFs clearly fall in, NYSE-only ETFs may not. Apply the MAR standards anyway.
- **Identification duty:** OZ §435(1) – name, registered seat, register entry and IČO on the website. https://www.zakonyprolidi.cz/cs/2012-89 (read 2026-10-29)

### 6b. Past performance and marketing communications

- **CDR 2017/565 art. 44 binds investment firms, not a non-licensed publisher** – use as best practice. 44(2): name of the firm; accurate; fair and prominent indication of risks whenever benefits are mentioned. 44(4) past performance: not the most prominent feature; preceding 5 years (or whole period since launch if shorter), complete 12-month periods; reference period and source; prominent warning that figures refer to the past and past performance is not a reliable indicator of future results; if in a foreign currency, state the currency and warn that return may increase or decrease as a result of currency fluctuations; if gross, disclose the effect of fees. 44(6) future performance: reasonable assumptions, scenarios, warning. 44(7) tax: state that treatment depends on individual circumstances and may change. 44(8): no use of a competent authority's name implying endorsement. https://www.legislation.gov.uk/eur/2017/565/article/44/adopted (read 2026-10-29)
- **ESMA34-45-1272 (2 Aug 2021) binds fund managers (UCITS ManCos, AIFMs, EuVECA/EuSEF), and third-party communications only where the manager uses them**; explicitly covers social media and webpages. Past performance: 10 years for funds with a KIID, 5 years for others (or since launch), complete 12-month periods; cumulative performance only together with annual figures; statement "Past performance does not predict future returns"; currency warning; risk info in a font at least the size of the predominant font. https://www.esma.europa.eu/sites/default/files/library/esma34-45-1272_guidelines_on_marketing_communications.pdf (read 2026-10-29; raw `esma/`)

### 6c. E-mail lead capture

- **Two legal bases:** sending the requested PDF – GDPR art. 6(1)(b) (necessary for a service the person asked for); newsletter/follow-ups – consent (GDPR 6(1)(a) + zákon 480/2004 Sb. §7(2) "předchozí souhlas").
- **Conditioning the PDF on newsletter consent = high risk.** EDPB Guidelines 05/2020 §3.1.2 paras 25–41: tying is presumed not freely given (art. 7(4)); only "highly exceptional" cases survive; burden of proof on the controller. https://www.edpb.europa.eu/system/files/documents/files/file1/edpb_guidelines_202005_consent_en.pdf (read 2026-10-29; raw `edpb/`). Czech commentary split (epravo.cz, podnikatel.cz: not allowed; mediaguru.cz 2018: allowed). ÚOOÚ FAQ Q12 (related context): "Poskytnutí tohoto souhlasu nemůže být podmiňováno". **[UNCERTAIN]** no ÚOOÚ statement specifically on e-books found.
- **ÚOOÚ FAQ on 480/2004:** Q8 – a customer is someone who entered a contract (paid or free); a prospect or competition participant is not. Q14 – consent must be prior, no form prescribed, burden of proof on the sender. Q15 – ÚOOÚ recommends a confirmation request to the address (double opt-in). https://uoou.gov.cz/cinnost/obchodni-sdeleni/casto-kladene-otazky-k-zakonu-c-4802004-sb (read 2026-10-29)
- **Zákon 480/2004 Sb.:** §2(f) "obchodní sdělení" includes "vybízení k návštěvě internetových stránek"; §7(3) customer exception only for the sender's own similar products, with opt-out at collection and in every message; §7(4) every message must be identifiable as commercial, identify the sender, contain a valid unsubscribe address; supervisor ÚOOÚ (§10). https://www.zakonyprolidi.cz/cs/2004-480 (read 2026-10-29)

### 6d. Cookies, Meta Pixel and GA4

- **Zákon 127/2005 Sb. §89(3)** (opt-in since amendment effective 1.1.2022): storing/accessing information in the user's device only with "předem prokazatelný souhlas"; exceptions only for transmission or a service explicitly requested by the user. https://www.zakonyprolidi.cz/cs/2005-127 (read 2026-10-29)
- **ÚOOÚ presentation 12 Jun 2024:** fines since 2023 (≈2 mil. Kč final at the time); accept and reject in the same layer (ideally the first), comparable size/colour; footer link to reopen settings; Czech language; browser settings are not a substitute; a site with technical cookies only needs no banner but still needs privacy information. https://uoou.gov.cz/media/seminare-uoou/prezentace/2024-06-12-p04-praxe-uoou-v-oblasti-cookies.pdf (read 2026-10-29; raw `uoou/`)
- **Case law (via secondary summaries):** CJEU C-673/17 Planet49 (1.10.2019) – pre-ticked boxes are not valid consent; CJEU C-40/17 Fashion ID (29.7.2019) – a site embedding Facebook tools is joint controller with Meta for collection/transmission.
- **Google Consent Mode v2:** EEA personalisation/measurement need `ad_user_data` and `ad_personalization` signals. https://support.google.com/analytics/answer/14275483 (via search result 2026-10-29)

### 6e. Fonts

- LG München I, 20.1.2022, 3 O 17493/20: EUR 100 damages + injunction for passing a visitor's IP to Google via the Google Fonts CDN without consent; legitimate interest rejected because fonts can be self-hosted. https://www.gesetze-bayern.de/Content/Document/Y-300-Z-GRURRS-B-2022-N-612 (via search 2026-10-29). No ÚOOÚ position on Google Fonts found.

### 6f. Czech wording examples (draft – have a lawyer check)

- **Hlavní disclaimer (u srovnání + patička):** „Informace na této stránce mají pouze vzdělávací a informativní charakter. Nejde o investiční doporučení, investiční poradenství ve smyslu zákona č. 256/2004 Sb. ani o nabídku či výzvu ke koupi nebo prodeji investičního nástroje. [Provozovatel], IČO […], se sídlem […], není obchodníkem s cennými papíry, investičním zprostředkovatelem ani jinou osobou s povolením České národní banky. Nezohledňujeme vaše cíle, finanční situaci, znalosti ani zkušenosti. Investování je spojeno s rizikem: hodnota investice může klesat i stoupat a nemusí se vám vrátit celá vložená částka. Před investicí si přečtěte sdělení klíčových informací (KID) a prospekt fondu. Údaje k [datum], zdroje: […].“
- **Autor / střet zájmů:** „Autor: [jméno, role]. Aktualizováno [datum, čas]. Za odkazy na brokery nedostáváme žádnou odměnu. Autor ani provozovatel nedrží pozice v uvedených ETF.“ (adjust if not true)
- **Minulá výkonnost (před grafem):** „Minulá výkonnost nepředpovídá budoucí výnosy. Údaje se týkají minulosti; minulá výkonnost není spolehlivým ukazatelem budoucích výsledků. Výkonnost za ucelená 12měsíční období za posledních 10 let (nebo od založení), po odečtení průběžných nákladů fondu, bez poplatků brokera a daní. Zdroj: […], období […].“ (first sentence is a translation of ESMA's mandatory text; official Czech version not verified)
- **Měnové riziko:** „Výnosy jsou uvedeny v USD (EUR). Vaší měnou je koruna, proto se může váš výnos v důsledku pohybu kurzů zvýšit i snížit.“
- **Daně:** „Daňové informace jsou zjednodušené, vycházejí z předpisů platných k [datum], závisí na individuálních poměrech každého investora a mohou se v budoucnu změnit.“
- **Kalkulačka:** „Ilustrativní výpočet. Předpokládaný výnos [X] % ročně je modelový předpoklad, ne předpověď. Skutečný výsledek se bude lišit podle vývoje trhů a doby držení.“
- **Formulář:** field „Váš e-mail“, button „Pošlete mi tahák zdarma“. Under the button: „E-mail použijeme k zaslání taháku (PDF). Telefon ani jiné údaje nechceme. Více v [Zásadách ochrany osobních údajů].“ Optional **unticked** checkbox: „☐ Chci také dostávat newsletter [Název] o ETF a investování, včetně obchodních sdělení (zhruba 2× měsíčně). Souhlas můžete kdykoli odvolat odkazem v každém e-mailu.“ Double opt-in e-mail: „Potvrďte prosím odběr newsletteru – [Ano, chci odebírat]. Tahák vám posíláme v samostatném e-mailu bez ohledu na odběr.“
- **Krátké informace o zpracování:** „Správce: [firma, IČO, sídlo, e-mail]. Tahák: zasíláme na vaši žádost (čl. 6 odst. 1 písm. b) GDPR), e-mail poté uchováváme [30 dní]. Newsletter: jen s vaším souhlasem (čl. 6 odst. 1 písm. a) GDPR; § 7 zák. č. 480/2004 Sb.), do odvolání. Zpracovatel: [poskytovatel e-mailingu]. Máte právo na přístup, opravu, výmaz, omezení, námitku, přenositelnost, odvolání souhlasu a stížnost u ÚOOÚ (uoou.gov.cz).“
- **Cookie lišta (1. vrstva, tlačítka stejně výrazná):** „Používáme nezbytné cookies, aby web fungoval. S vaším souhlasem použijeme také analytické (Google Analytics) a marketingové cookies (Meta Pixel, Google Ads) k měření návštěvnosti a účinnosti reklam; údaje mohou být předány společnostem Google a Meta, i mimo EU (USA). Volbu můžete kdykoli změnit v odkazu „Nastavení cookies“ v patičce.“ Buttons: [Odmítnout vše] [Nastavení] [Přijmout vše].

**Implications for the landing page (6)**
- Present the comparison as factual and educational (data, sources, date). No „kupte“ / „nejlepší ETF pro vás“; no quiz or calculator that outputs a personalised pick; use "ilustrace", not "vhodné pro vás".
- If any ranking or "our pick" appears: author name and role, date and time, conflicts statement inside the content.
- Show NYSE ETFs as reference/benchmark only (Czech retail cannot buy them anyway – see §1); point readers to UCITS equivalents. No buy CTA for US-domiciled funds.
- No paid broker affiliate links (or unpaid, labelled ones) until legal review.
- Full operator identification (name, seat, IČO, register) in the footer.
- Past performance: annual bars for 10 calendar years (or since inception) next to any cumulative figure; currency stated + CZK FX warning; warning before the chart, at least body font size; tax caveat next to tax facts; never "regulováno ČNB"-style badges.
- E-mail: deliver the PDF to anyone who enters an e-mail; separate, unticked, optional newsletter checkbox + double opt-in; PDF e-mail free of promotion; don't rely on the §7(3) customer exception; ask for e-mail only.
- Cookies: load nothing from Meta/Google before consent (no Pixel, GA4, Google Ads tag, no CAPI with hashed e-mail for non-consenting users); Consent Mode v2 default "denied"; budget for lost conversion signal.
- Fonts: self-host woff2; no calls to fonts.googleapis.com / fonts.gstatic.com.

## 7. Reklamní platformy

### Google Ads – BLOCKER unless already verified

- **Czechia is in scope of Financial Services Verification.** Change log: "Rolling enforcement begins on July 23, 2026" for 24 EEA markets incl. Czechia; regulators table gives Czechia enforcement from **"September 15, 2026"**. Recognised regulators for CZ: ČNB, KAČR, KDP, Ministry of Justice, MPO, EBA, EIOPA, ESMA.
- **Who must verify:** advertisers "need to be verified" to show financial-services ads "including showing ads to… users who appear to be seeking financial services". The G2RS step also covers non-financial advertisers "that have a compelling reason to target users who appear to be seeking financial services" (they warrant they will not promote financial services) and regulation-exempt advertisers. Approved third parties (affiliates/lead-gen for a licensed firm) need the licensed firm to vouch for them. Applies to all ad formats; separate verification per country.
- **Scope:** "products and services related to the management or investment of money… including personalized advice".
- **Landing-page disclosures** visible without clicking: "physical address for the business", "All associated fees", links to accreditation when affiliation is implied.
- **Grace period:** Google blog (23 Jun 2026): businesses get "30 days to complete the process" – that window has passed for CZ.
- Sources (read 2026-10-29; raw `google-adspolicy/`): https://support.google.com/adspolicy/answer/12390454?hl=en ; https://support.google.com/adspolicy/answer/12492484?hl=en (Czechia dropdown rendered client-side, not extracted; German template identical in structure); https://support.google.com/adspolicy/answer/17127726?hl=en ; https://support.google.com/adspolicy/answer/2464998?hl=en ; https://blog.google/products/ads-commerce/eu-financial-advertiser-verification/
- **Mitigation:** apply via G2RS today as a non-financial / exempt advertiser (educational publisher, no licence) – turnaround unknown **[UNCERTAIN]**; until approved, no Google Search on finance keywords; add address, fees and IČO to the page now.

### Meta (Facebook/Instagram) – not blocked

- **Ad Standard – Financial and insurance products and services** (change-log entry 26 Oct 2026): "Advertisers promoting financial products and services are required to verify… and demonstrate that they are authorised by the relevant regulatory authorities where this is a requirement"; "Ads that only mention a financial service or product without the ability to obtain or connect with that product/service" can run without authorisation; CFDs, binary options, ICOs, payday loans prohibited. https://transparency.meta.com/en-gb/policies/ad-standards/restricted-goods-services/financial-services/ (read 2026-10-29)
- **Financial-services advertiser verification required only in:** Australia, Hong Kong, India, Ireland, Israel, Spain, Taiwan, Thailand, UK, US. "If the country… is not listed… there is no verification requirement… at this time." Education/news ads generally exempt. https://www.facebook.com/business/help/719892839342050 (read 2026-10-29) → **Czechia not on the list.**
- **EU advertiser + payer fields mandatory** (DSA, since 5 Jun 2023): "Without this information, your ad cannot be published." https://www.facebook.com/business/help/605021638170961
- **Identity verification** may be demanded immediately for new accounts and ad types "more susceptible to abuse from scammers"; ads may be paused until done. https://www.facebook.com/business/help/983527276402621 ; https://www.facebook.com/business/help/810450577622394
- **Special Ad Category "Financial products and services"** mandatory only for the US (since 21 Jan 2025); Meta mentions restrictions for "certain countries in Europe" (developer docs mention credit) **[UNCERTAIN]**. If applied: no age/gender/postcode targeting, no lookalikes. https://www.facebook.com/business/help/298000447747885 ; https://developers.facebook.com/docs/marketing-api/audiences/special-ad-category
- **Claims:** prohibited commercial practices include "guaranteed investment returns" and unauthorised endorsements. https://transparency.meta.com/policies/ad-standards/deceptive-content/prohibited-commercial-practices/
- **Reach:** since Jan 2026 EU users can choose less-personalised ads under a DMA commitment. https://digital-markets-act.ec.europa.eu/meta-commits-give-eu-users-choice-personalised-ads-under-digital-markets-act-2025-12-08_en . Meta may auto-apply "Core Setup" data restrictions to finance advertisers (no URL parameters/custom data) **[UNCERTAIN – third-party sources only]**.
- **Mitigation:** verify the business portfolio today; fill advertiser/payer; target 18+; creative without return promises, celebrities, fake-news look or „zbohatněte“; point the ad at the education piece and the PDF, not at a broker.

### TikTok – treat as blocked for day 1

- General: advertisers must "Be licensed by local and regional authorities"; ads restricted to 18+; no get-rich-quick / too-good-to-be-true offers.
- Czech Republic section: "Investment services" may be allowed if licensed; "Advisory services", high-risk products (forex, binary options), get-rich-quick schemes not allowed. No financial-education exemption found.
- Source: https://ads.tiktok.com/help/article/tiktok-ads-policy-financial-services read via Wayback snapshot of 12 Jun 2026 ("Last updated: May 2026"): https://web.archive.org/web/20260612142026/https://ads.tiktok.com/help/article/tiktok-ads-policy-financial-services (read 2026-10-29; live site blocked by local DNS – `ads.tiktok.com` resolves to 0.0.0.0 on this network; raw `tiktok-ads-help/`). **[UNCERTAIN]** check the live page / ask a TikTok rep.

**Implications for launch (7)**
- Day 1: **Meta only**, 18+, educational creative, landing page with full operator identification.
- Google: only after G2RS/Google financial-services verification (or skip finance keywords entirely).
- TikTok: only after a TikTok rep confirms an unlicensed educational publisher may run; note TikTok Ads Manager needs a network without the DNS block.

## 8. Cílová skupina

All sources read 2026-10-29.

### 8.1 Market size and growth (no official head-count of investors exists)

- **Households hold almost 1.7 trillion Kč in investment funds** (end-2025, +278.2 bn Kč in 2025) = 22.2 % of 7.6 trillion Kč household financial-market assets; deposit share fell to 57.3 % over five years; directly held listed shares +29.4 % to almost 340 bn Kč. Ministry of Finance (15 Jul 2026): https://mf.gov.cz/assets/attachments/2026-07-15_Strucne-shrnuti-Zprava-o-vyvoji-financniho-trhu-v-roce-2025.pdf
- **Mutual funds sold in CZ (AKAT via ČTK/e15, 27 May 2026):** 1.423 trillion Kč at end-Q1 2026 (+13 bn Kč in the quarter; +218 bn Kč over 2025); natural persons hold 90 %; end-2025 holdings: bond 475.2 bn, mixed 416.1 bn, equity 341.4 bn, real estate 145.8 bn Kč. https://www.e15.cz/investice/nemovitostni-fondy/cesi-vice-sazi-na-podilove-fondy-prumerny-cesky-investor-letos-ale-zatim-vydelal-mene-nez-loni-1433132 . Q2/Q3 2026 not found (AKAT data portal https://www.akatcr.cz/Zverejnena-data requires a form – not submitted).
- **Growth since 2020 [UNCERTAIN]:** search snippets citing AKAT give ≈708 bn Kč at end-2021 (+117.9 bn in 2021) → roughly doubled since 2021.
- **DIP (dlouhodobý investiční produkt), AKAT, 30 Sep 2026:** 288,726 contracts, 14.2 bn Kč, 91 % in investment funds. https://www.akatcr.cz/Dokumenty/Aktuality/tiskov225-zpr225va-popularita-dlouhodob201ho-investicn205ho-produktu-i-nad193le-roste-uzavreno-jich-bylo-jiz-288-726
- **No national investor count:** CDCP publishes trade volumes and issue counts, not owner-account counts. https://www.cdcp.cz/dokumenty/statistiky/

### 8.2 Provider figures

- **Česká spořitelna:** more than 750,000 investors (Feb 2026, +12 % y/y), mostly in mutual funds; share/ETF purchases in George growing, interest >2.5× in a year; digital investors average age 35, branch investors 59. https://www.businessinfo.cz/clanky/index-prosperity-pres-8-z-10-cechu-zhodnocuje-sve-uspory-a-vice-nez-polovina-populace-aktivne-investuje/ ; https://www.seznamzpravy.cz/clanek/ekonomika-b2b-investuji-uz-ctyri-z-peti-cechu-inflacni-sok-pusobil-jako-budicek-301142 . Sep 2024: 644,000 investors, **average regular investment ≈2,000 Kč/month**: https://www.businessinfo.cz/clanky/index-prosperity-aktivne-investuji-4-z-10-cechu-jako-ziskove-hodnoti-sve-investice-76-procent-z-nich/
- **Portu (annual report 2025):** >280,000 clients, >55 bn Kč AUM at end-2025 (clients +34 %, AUM +39 %); ≈80 % invest regularly; 2.5 m deposits in 2025; women 38 %; 18–26 group +32 % to >16,000; ≈42,000 DIP contracts. https://cdn.portu.cz/portu/documents/obligatory-published-information/cs/Annual-report-2025.pdf (raw `portu/`)
- **Fondee:** no verified current numbers (older undated 10,000–17,000+ clients). **[UNCERTAIN]**
- **XTB (group only, no CZ/SK split published):** 2025 – 864,286 new clients (+73.4 %), 2,164,867 total, ≈1.19 m active; outdoor/TV campaigns in CZ/SK in 2025. https://ir.xtb.com/wp-content/uploads/2026/01/RB-2-2026-Wstepne-wyniki-finansowe-i-operacyjne-2025-ENG-all.pdf (raw `xtb-ir/`). Polish press: 1.49 m active / 2.83 m total at 30 Jun 2026 (group).
- **XTB Gen Z (18–26) analysis CZ+SK, Jan–Jul 2026 (published 16 Oct 2026; XTB client data, not representative):** 61.1 % of young Czech XTB investors used ETFs (65.9 % single stocks); ETFs 33 % of their transactions; 72 % of women vs 56 % of men used ETFs; 53 % bought the same ETF in ≥3 different months; **most popular ETF SXR8 (iShares Core S&P 500 UCITS Acc)**; most active in March, least in November; new Gen Z investors in CZ +20 % y/y. https://www.newstream.cz/trhy/burzovni-derby-gen-z-cesi-chteji-microsoft-slovaci-nvidii
- **Revolut CZ (24 Mar 2026):** 1.3 m users (+34 % in 2025); number of investors +41 %. https://cc.cz/revolut-v-cesku-dal-roste-ma-13-milionu-uzivatelu-kteri-s-nim-uz-zdaleka-neplati-jen-v-zahranici/
- **Raiffeisenbank (20 Feb 2026):** investment app >100,000 clients, >12 bn Kč invested via it in 2025; survey: 39 % invest (2024: 32 %); two thirds invest regularly (35 % fixed monthly amount, 35 % variable); half prefer a bank; 64 % use an online platform at least monthly; sample not stated. https://www.e15.cz/finexpert/banky-a-ucty/pribyva-mladych-a-pravidelnych-investoru-vetsina-sazi-na-dlouhodoby-pristup-1430974
- Trading 212, Patria, Fio, Lynx: no published CZ client numbers found.

### 8.3 Who invests (surveys)

- **Index prosperity a finančního zdraví** (Ipsos for ČS + Evropa v datech; n = 1,003, age 18–65; published 11 Mar 2026): 82 % put savings to work (2024: 66 %); 55 % consider themselves investors (41 % two years earlier); typical investor = man under 40, university degree, above-average income; 59 % of investors use funds or ETFs (incl. pension funds), more among under-30s; 23 % buy shares directly; three quarters invest at least monthly; two thirds hold < 500,000 Kč; 89 % value tracking in an app; **46 % of non-investors would start if sure they wouldn't lose money**. https://www.businessinfo.cz/clanky/index-prosperity-pres-8-z-10-cechu-zhodnocuje-sve-uspory-a-vice-nez-polovina-populace-aktivne-investuje/
- **AKAT / Perfect Crowd (n > 1,000, 20 Feb 2024):** 39 % invest; **fear of fraud the top barrier (43 %, +10 pp y/y)**, ahead of fear of risk (42 %). https://ct24.ceskatelevize.cz/clanek/ekonomika/investuje-39-procent-cechu-nejvic-si-ceni-nakupu-bydleni-346260
- **Monthly amounts:** verified ≈2,000 Kč/month (ČS 2024); ≈2,500 Kč appears undated; no verified 2026 average. **[UNCERTAIN]** share of Czechs who invest: 39–55 % depending on definitions.

### 8.4 Devices and social media

- **StatCounter CZ** (all-web page views, not social-ad traffic): Sep 2026 mobile 49.2 %, desktop 49.2 %, tablet 1.6 %; Oct 2026 MTD mobile 46.8 %; 12-month average (Nov 2025–Oct 2026) ≈44 % mobile (40–41 % in Feb–Apr, 55–59 % in summer 2025). https://gs.statcounter.com/platform-market-share/desktop-mobile-tablet/czech-republic (raw CSV `statcounter/platform_cz_monthly.csv`). Traffic from Meta ads is expected to be mostly mobile in-app browser – **no sourced figure**.
- **DataReportal Digital 2026 Czechia** (platform ad-tool data, late 2025; ad reach, not active users): Facebook 5.00 m (58.0 % of adults 18+, F 52 / M 46); Instagram 3.95 m (46.4 %, F 52.5 / M 43.8); TikTok 18+ 2.13 m (24.7 %, F 61.8 / M 38.2); YouTube 8.08 m; internet users 9.96 m. https://datareportal.com/reports/digital-2026-czechia
- **NapoleonCat (Sep 2026, Meta ad-audience estimates – use shares rather than totals):**

| Age | Facebook | Instagram |
|---|---|---|
| 18–24 | 14.7 % | 20.1 % |
| **25–34** | **24.2 %** | **30.7 %** |
| 35–44 | 20.9 % | 20.8 % |
| 45–54 | 19.6 % | 16.5 % |
| 55–64 | 11.2 % | 7.2 % |
| 65+ | 9.4 % | 4.7 % |
| Total | 6.87 m (64.3 % of pop.) | 4.10 m (38.3 %) |
| Women | 53.3 % | 55.5 % |

Sources: https://napoleoncat.com/stats/facebook-users-in-czechia/ ; https://napoleoncat.com/stats/instagram-users-in-czechia/

**Implications for the landing page (8)**
- Core audience: 25–44 on Instagram/Facebook, digital-first, often already in a bank fund or George, investing small regular amounts.
- Don't build male-only creative: Instagram skews female (55 %); Portu 38 % women; young women at XTB use ETFs more than young men.
- Calculator defaults: 2,000 Kč/month (slider ≈1,000–3,000+); 500,000 Kč as upper "typical portfolio" anchor.
- Anchor the comparison on bank funds (≈1.7 trn Kč in funds; ČS alone 750,000+ fund investors) → "váš bankovní fond vs. UCITS ETF".
- Cheat-sheet: lead with UCITS equivalents of US-listed S&P 500 and MSCI World / All-World ETFs (SXR8/CSPX, IWDA/SWDA, VWCE); SXR8 is the top ETF among young Czech XTB investors.
- Mobile-first for the Meta in-app browser, but solid desktop layout; PDF must read well on a phone.
- Timing: November is the weakest month (XTB data) → expect higher CPL in Nov–Dec; plan the main push for January/March.
- Lead with safety, not returns: fear of fraud (43 %) and of losing money (46 % of non-investors) are the main barriers.

## 9. Kontext podvodů

All sources read 2026-10-29.

### 9.1 Scale

- **Bank-client fraud Jan–Jul 2026 (ČBA data relayed by ČNB press release 9 Oct 2026):** 1.9 bn Kč lost (+79 % y/y); average loss 30,335 Kč (+47 %); more than half of fraud cases never reported; ČNB working group discussed platforms blocking scam ads, payee-name display before payment, a national anti-fraud centre; report scam SMS/calls to 7726, online fraud to strazciinternetu.cz (CSIRT.CZ). https://www.cnb.cz/cs/cnb-news/tiskove-zpravy/Pracovni-skupina-pro-prevenci-podvodu-resila-edukaci-verejnosti-i-zkusenosti-zezahranici/
- **2025 full year (ČBA via Newstream, 10 Feb 2026):** almost 91,000 attacks; 2.1 bn Kč lost (+>700 m Kč vs 2024); average loss 23,462 Kč; banks blocked a record 12.2 bn Kč; deepfake investment ads with politicians/celebrities named as a channel. https://www.newstream.cz/money/kybersmejdi-loni-utocili-ve-velkem-banky-cechum-zachranily-pres-12-miliard
- **2024 (ČT24, 29 Jan 2025):** 87,407 clients attacked, 1.39 bn Kč lost; police recorded 18,495 cybercrime cases. https://ct24.ceskatelevize.cz/clanek/domaci/kyberutoky-na-klienty-bank-loni-vzrostly-o-ctvrtinu-357557
- **Police, national report for 2025 (10 Jul 2026):** internet crime +14.2 %; cyber 12.4 % of all recorded crime; cyber fraud 62.1 % of frauds against individuals; no national investment-fraud figure on the summary page (full 28 MB PDF did not download). https://archiv.policie.gov.cz/clanek/vyrocni-zprava-skpv-2025.aspx
- **Police, Moravian-Silesian region 2025:** >700 internet investment-fraud cases (≈+45 % vs ≈480 in 2024); regional cyber damage >435 m Kč; fake investment platforms, reverse classified-ad fraud, "fake banker". https://policie.gov.cz/moravskoslezsky-kraj/vyhodnoceni-kriminality-a-dopravni-nehodovosti-v-moravskoslezskem-kraji-v-roce-2025
- **Police, Hradec Králové region (20 Nov 2025):** online fraud +55 %, marked rise of "recovery" scams (phone calls, fake licences, small entry fees e.g. 2,000 Kč, remote-access apps, couriers). https://archiv.policie.gov.cz/clanek/narust-investicnich-podvodu.aspx

### 9.2 How the scams work (ČNB warnings, police case reports)

1. **Deepfake ads and fake news articles.** 12 Feb 2026: fake CNN Prima NEWS report with AI images of Governor Michl and the Prime Minister promoting "Záře Finthor"; masking page redirecting to the scam; urgency ("Zbývá 7 míst v Praze"). https://www.cnb.cz/cs/dohled-financni-trh/ochrana-spotrebitele/upozorneni/Falesna-reportaz-zneuziva-identitu-guvernera-k-propagaci-podvodnych-investic . 20 Mar 2026: AI videos/articles misusing politicians (SEGURO MALEDOXY, Ziskotria) via Facebook, YouTube, TikTok, Telegram, spam. https://www.cnb.cz/cs/dohled-financni-trh/ochrana-spotrebitele/upozorneni/Upozorneni-na-podvodna-videa-a-fotografie-vytvorene-AI-SEGURO-MALEDOXY-platforma-Ziskotria-aj. . 20 Jun 2025: deepfake video of the governor – "ČNB žádné investiční produkty nenabízí". https://www.cnb.cz/cs/cnb-news/aktuality/Upozorneni-Podvodne-video-zneuziva-podvrzene-zabery-guvernera.-Pokud-naletite-muzete-prijit-o-vsechno
2. **Contact form → phone call (the pattern most relevant to our form).** 27 Feb 2026, South Bohemia: a woman filled in her contact details under a social ad with politicians' photos; a fake "adviser" called from ≥13 numbers, took a 3,000 Kč "entry" payment and an SMS code; loss ≈200,000 Kč. Police: "Když žena vyplnila své kontaktní údaje pod reklamou, ozval se jí telefonicky muž". https://archiv.policie.gov.cz/clanek/zena-prisla-o-bezmala-200-tisic-korun.aspx . 18 May 2023, Liberec: ČEZ-shares ad with the president's photo; she "zadala svůj e-mail a telefon", got a call, paid 5,000 Kč, installed remote access, lost 185,000 Kč. https://archiv.policie.gov.cz/clanek/chtela-investovat-a-stala-se-obeti-podvodu.aspx
3. **Fake licences, clone firms, ČNB impersonation.** 4 Jun 2026: fake ČNB decisions and fake "deposit insurance", small entry fees to real transparent accounts, then larger sums/crypto, AnyDesk/TeamViewer, repeated "fees" before withdrawal. https://www.cnb.cz/cs/dohled-financni-trh/ochrana-spotrebitele/upozorneni/Varovani-pred-podvodnymi-nabidkami-zneuzivajicimi-jmeno-CNB . 12 Mar 2025 clone firms: "ověřujte nejen licenci, ale i to, kdo za nabídkou skutečně stojí!" https://www.cnb.cz/cs/dohled-financni-trh/ochrana-spotrebitele/upozorneni/Pozor-na-podvodne-investicni-nabidky-Overujte-si-nejen-licenci-ale-i-identitu-poskytovatele/ . "Investiční vouchery" e-mails targeting seniors from cnb@podatelna.net (≈19–20 Oct 2026 per Expats.cz, date not confirmed on cnb.cz **[UNCERTAIN]**): https://www.cnb.cz/cs/dohled-financni-trh/ochrana-spotrebitele/upozorneni/Upozorneni-na-podvodnou-investicni-nabidku-zneuzivajici-jmeno-Ceske-narodni-banky/
4. **Police red flags:** guaranteed/high returns, fake on-screen gains, pressure to deposit more, blocked withdrawals, discrediting bank warnings, later "recovery" offers. https://policie.gov.cz/kyberkriminalita/podvody-s-legendou-vyhodne-investice
5. **Where to check a provider:** ČNB register JERRS https://jerrs.cnb.cz/apljerrsdad/JERRS.WEB07.INTRO_PAGE?p_lang=cz ; ČNB warnings list https://www.cnb.cz/cs/dohled-financni-trh/ochrana-spotrebitele/upozorneni/ ; ČNB campaign "Chraňte své peníze!" https://www.cnb.cz/cs/dohled-financni-trh/ochrana-spotrebitele/chrante-sve-penize/index.html

### 9.3 Meta and scam ads

- 26 Aug 2026: Poland's digital minister asked the European Commission to fine Meta €250 m over scam ads; in CERT Polska tests Meta left 106 of 122 reported scam ads running (Reuters via The Star, 27 Aug 2026): https://www.thestar.com.my/tech/tech-news/2026/08/27/poland-asks-eu-to-fine-meta-250-million-urges-action-against-scams-and-false-ads
- Press reports: Meta extended facial-recognition "celeb-bait" checks to the EU/UK in 2025 (Meta's own announcement not read) **[UNCERTAIN]**. Expect strict automated review of finance ads, especially with faces.

**Implications for the landing page (9) – trust design**
- **Ask for e-mail only, never a phone number** – "contact details under an ad → call from an adviser" is exactly the 2026 police pattern. No WhatsApp/Telegram, no callback widget, no "ozve se vám konzultant".
- Near the form and in every e-mail footer: „Nikdy vám nebudeme volat, psát přes WhatsApp/Telegram ani chtít přístup k vašemu účtu, kódy z SMS nebo instalaci aplikací jako AnyDesk. Nepřijímáme žádné peníze.“
- No faces of celebrities/politicians, no news-article/advertorial look, no scarcity/urgency ("zbývá X míst", countdowns), no profit screenshots, no "garantovaný" / "pasivní příjem".
- One domain matching the ad, no redirects/masking pages (ČNB names masking pages as a scam marker). HTTPS; SPF/DKIM/DMARC on the sending domain (own recommendation).
- Show who runs the page: legal name, IČO, seat, contact e-mail, link to ARES/obchodní rejstřík; „Nejsme investiční firma ani poradce; nenabízíme investice ani nespravujeme peníze.“
- Short "jak poznat podvod" box with JERRS + ČNB warnings links: „Než někomu pošlete peníze, ověřte si ho v seznamu ČNB (JERRS). Zaručené výnosy, nátlak a telefonáty od ‚makléřů‘ jsou typické znaky podvodu.“
- In the PDF: buy only via an EU-authorised broker (check in JERRS), never install remote-access apps, ignore "recovery" offers.
