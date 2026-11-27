# Landingspagina v2: verkoopweekend en brochure (20 november 2026)

Gebouwd volgens `../prompt-landingspagina-strand-residence.md`. De bestaande `index.html` en `ghl/` in de map erboven zijn niet aangeraakt.

## Bestanden

| Bestand | Wat |
|---|---|
| `voorbeeld-nl.html`, `voorbeeld-de.html` | Volledige voorbeeldpagina's. De formulieren zijn gestippelde placeholders. |
| `ghl/NL-blok-1-boven-formulieren.html` | GHL Custom Code: hero tot en met de formulierkop, plus de vaste balk |
| `ghl/NL-blok-2-onder-formulieren.html` | GHL Custom Code: "wat gebeurt er na verzenden" en de voettekst |
| `ghl/DE-blok-1-...`, `ghl/DE-blok-2-...` | Hetzelfde voor /de |
| `src/` | Bron: `nl.html`, `de.html`, `srp.css`. Hier wijzigen, daarna `python3 build.py` |

## Bedankpagina's (24 november 2026)

`ghl/NL-bedankt-nl.html` en `ghl/DE-danke-de.html`: elk één Custom Code-element voor de stap /bedankt-nl en /danke-de. Bron: `src/bedankt-nl.html` en `src/danke-de.html`; voorbeeld: `voorbeeld-bedankt-nl.html` en `voorbeeld-danke-de.html`. Inhoud: bevestiging, wat er nu gebeurt (mail, Willem belt binnen één werkdag, geen verplichting), de mededeling dat Willem het rendement met de bezoeker doorrekent, telefonisch (hij belt daarvoor) of op het verkoopweekend (eigen gebruik, eigen geld of financiering, privé of holding); bewust geen link naar de rekentool (25 november 2026) en dezelfde voettekst als de landingspagina. Na het plakken in de formulieren SR - VD en SR - BROCHURE (en de Duitse) instellen: bij verzenden doorsturen naar /bedankt-nl of /danke-de.

## Inbouwen in GHL

1. Pagina: Custom Code-element met blok 1, daaronder een rij met twee kolommen voor de native formulieren "SR - BROCHURE" (links) en "SR - VD" (rechts; omgedraaid op 27 november 2026), daaronder Custom Code met blok 2.
2. Geef het formulier "SR - BROCHURE" (of de kolom eromheen) de element-ID `sr-brochure`. De knoppen "Ontvang de brochure" en "Brochure" springen daarheen. "Verkoopweekend" springt naar de formulierkop (`sr-formulieren`) in blok 1, dat werkt altijd.
3. De beelden staan als absolute URL op GitHub Pages. Twee nieuwe beelden (`images/hero-mobiel.webp`, 73 kB, en `images/hero-desktop.webp`, 133 kB) staan nog niet online: eerst committen en pushen, anders is de hero leeg.
4. Head/Tracking Code van de NL-pagina: het bestaande `../ghl/5-NL-head-trackingcode.html` (doorsturen naar /de op tijdzone, `?taal=nl` blijft NL). Zet in de footer-code van beide pagina's ook het anti-scrollscript tegen de Meta in-app browser (snippet 1 van de skill landingspagina).
5. **Microsoft Clarity**: `ghl/clarity-head-trackingcode.html` staat in GHL bij funnel Strand Residence > Settings > Head tracking code (alle stappen), (Clarity-project "Strand Residence landingspagina", ID zj3g0eyaha). Klikken op de knoppen komen binnen als events `cta_verkoopweekend` en `cta_brochure`.
6. **Koppen boven de formulieren** (25 november 2026): bovenaan elke formulierkolom staat een Custom Code-element met label, titel en één regel: `ghl/NL-kop-verkoopweekend.html`, `ghl/NL-kop-brochure.html`, `ghl/DE-kop-verkaufswochenende.html`, `ghl/DE-kop-broschuere.html`. De head-code van de funnel zet de blokken met onze code over de volle breedte, zonder witregel bovenaan (GHL-padding en de maximale breedte van 1170 px op /de).
7. Plakken met UTF-8: `LC_ALL=en_US.UTF-8 pbcopy < ghl/NL-blok-1-boven-formulieren.html`.

### Vaste balk onderaan
De balk staat in blok 1 en gebruikt `position: sticky` in plaats van JavaScript. Hij blijft onderaan het scherm tot het einde van blok 1 en blijft dan staan boven de formulieren, dus hij komt er nooit overheen. Op desktop is hij verborgen. **Testen in GHL:** als een GHL-wrapper `overflow: hidden` heeft, plakt de balk niet. Dan voor die sectie in GHL de overflow op zichtbaar zetten.

### Lettertypes
Titillium Web en Source Serif 4 via Google Fonts, met "axia" en "odile" vooraan in de stack. Zodra de Adobe Fonts-kit er is, de kit-link in de head van de pagina zetten. De rest gaat vanzelf.

## Placeholders die nog bevestigd moeten worden

Geel gemarkeerd op de pagina (`class="ph"`). NL en DE hebben dezelfde, plus een paar Duitse extra's.

**Eigen gebruik en verhuur**
1. ~~Hoe eigenaren hun verblijf vastleggen~~: geschrapt van de pagina op 24 november 2026. Geen aparte regels voor het hoogseizoen.
2. ~~Schoonmaak, klein onderhoud en afrekening~~: geschrapt van de pagina op 24 november 2026.
3. ~~Waar de koper de commissie en verhuurvoorwaarden inziet~~: geschrapt van de pagina op 24 november 2026.

**Sinds 1908**
4. ~~Rol van Tom Stroomer~~: initiatiefnemer en ontwikkelaar, bevestigd op 24 november 2026.
5. ~~Citaat van Tom Stroomer~~: uit videocast 04_02 (00:00 tot 00:15), licht ingekort, met Duitse vertaling (24 november 2026). Laat Tom de ingekorte versie even goedkeuren.

**Rendement en kosten**
6. ~~Koopsom 1.0.4 v.o.n. zonder btw~~: bevestigd op 20 november 2026.
7. ~~Netto opbrengst jaar 1 vóór of na kosten~~: na commissie en kosten, bevestigd op 23 november 2026 met de rendementsberekening van 1.0.4 (direct rendement 5,4%). Die berekening noemt € 35.413, de prijslijst € 35.414: op de pagina staat € 35.414.
8. ~~Uit welke posten de jaarlijkse kosten bestaan~~: geschrapt van de pagina op 24 november 2026.

**Kopen**
9. ~~Financieringsmogelijkheden~~: tot 70% voor inwoners van Nederland, tot € 150.000 voor inwoners van Duitsland (24 november 2026). Open: Oostenrijk en Zwitserland (alleen DE).
10. Kopen via een BV: ja (NL, 24 november 2026). DE: via een Duitse GmbH in principe mogelijk volgens Belastingdienst en RSM; overdrachtsbelasting is verschuldigd, het tarief voor een rechtspersoon (8% of 10,4%) is niet zeker. Laat Torero bevestigen dat zij aan een buitenlandse vennootschap verkopen.

**Verkoopweekend**
11. ~~Tijden en adres~~: niet op de pagina; Recraparcs stuurt ze na aanmelding (24 november 2026). Het ritme van elke drie weken staat ook niet meer op de pagina.
12. ~~Wat de bezoeker op het verkoopweekend ziet~~: ingevuld op 24 november 2026 (rendementen, het hele plaatje, de omgeving).

**Voettekst**
13. Privacyverklaring: gelinkt naar strandresidence.nl/privacyverklaring (24 november 2026). Contactgegevens: die van Strand Residence (Parelweg 6, 1812 RS Alkmaar, info@strandresidence.nl, +31 30 808 0445), op verzoek van Ruben (25 november 2026). DE: Impressum met Torero Invest B.V., KvK 76259889 (bron: privacyverklaring strandresidence.nl). Open voor DE: USt-IdNr. en vertegenwoordiger in het Impressum, en of er een Duitse privacyverklaring is.

**Woningtypen** (sectie 6, toegevoegd 20 november 2026)
16. ~~Overzicht per woningtype~~: geschrapt van de pagina op 24 november 2026. De prijslijst en de makelaar geven het overzicht.
17. ~~Welk interieurbeeld bij Beach Luxury hoort en welk bij Residence Chique~~: bevestigd op 23 november 2026.
18. "Nog 23 van de 70 beschikbaar" komt uit de prijslijst van 1 november: controleren op de dag van livegang
19. ~~Berging standaard of optie~~: inbegrepen bij de prijs, bevestigd op 24 november 2026.

**Holding** (toegevoegd 24 november 2026)
20. ~~Mag "kopen vanuit uw holding" op de pagina en in de advertenties?~~: ja, bevestigd op 24 november 2026.

**Alleen DE**
14. Fiscale aandachtspunten voor kopers uit Duitsland, Oostenrijk of Zwitserland
15. ~~Of de makelaar Duits spreekt~~: ja, bevestigd op 24 november 2026.

## Keuzes om te weten

- **Split-test headline NL (25 november 2026)**: op stap Landingspagina NL draait een variatie (GHL split-test, 50/50). Alleen de H1 verschilt. A: "Vermogen in uw holding, en een eigen plek aan zee". B: "Tot 89 dagen per jaar zelf aan zee, de rest van het jaar verhuurd" (`ghl/NL-blok-1-variant-b-headline.html`, zet in Clarity `variant=B-89-dagen`). Beoordelen op aanmeldingen verkoopweekend en doorstroom naar afspraak, niet alleen op conversie. Wijzig je blok 1, plak het dan in beide pagina's.

- **Opgeschaalde beelden (24 november 2026)**: de luchtfoto (`images/luchtfoto-dorp-strand-hd.webp`) en de duinovergang (`images/duinovergang-strand-hd.webp`) zijn met AI opgeschaald via OpenArt (Nano Banana Pro, 4K). De 4K-bestanden staan in `Beeldmateriaal/Locatie/`. Bij de luchtfoto heeft de AI de details van de gebouwen opnieuw getekend; het blijft een impressie.
- **Gevel zonder logo (24 november 2026)**: in de beeldband na sectie 5 staat `images/sfeer-gebouw-avond-zonder-logo.webp`: de originele render met het onleesbare opschrift weggewerkt. Het logo wordt in Canva op de gevel gezet; bron zonder logo: `Beeldmateriaal/Locatie/gebouw-hoek-avond-zonder-logo.png`. Daarna dat bestand als webp in `images/` zetten en in `src/` verwijzen.
- **Nieuwe renders (25 november 2026)**: uit `Beeldmateriaal/Renders 2026-11` zijn de vier interieurbeelden bij de inventarispakketten vervangen (Beach Luxury `2-5A Woonkamer`, Residence Chique `1-4C Woonkamer`, slaapkamers `2-6C` bijgesneden naar 3:2 en `2-4C`), staat `2-6A Terras` onderaan sectie 3 (eigen gebruik) en `Gevels - Overzicht` naast de luchtfoto in sectie 5. Webp-bestanden in `images/` (`interieur-*`, `terras-spa-binnentuin`, `overzicht-duinen-zee`). Omdat de GitHub Pages-deploy die dag mislukte (serverfout 500), staan deze zes beelden in GHL Media Storage en verwijzen de geplakte blokken 1 (NL, variant B, DE) naar `files.leadconnectorhq.com`. `build.py` schrijft weer GitHub-URL's; dat is pas goed als Pages de beelden serveert. Op 27 november 2026 is het terrasbeeld (`terras-spa-binnentuin`) op verzoek van Ruben weer van alle drie de pagina's gehaald; het bestand staat nog in `images/` en in GHL Media Storage.

- **DGA-hoek (24 november 2026)**: de NL-pagina sluit aan op de Meta-advertenties voor DGA's met geld in de holding. De hero noemt holding, € 35.414, eigen grond, 89 dagen en circa 100 m. De feitenband toont dezelfde vier feiten als het cijferblok in de advertenties. Sectie 2C "Zakelijk kopen" staat direct na het sfeermozaïek, met btw en de fiscale gevolgen van eigen gebruik. De bedenktijd staat er op verzoek niet in (24 november 2026). De DE-pagina is niet aangepast.

- **Data verkoopweekenden (23 november 2026)**: 12 december, daarna 8 en 9 januari en vanaf dan elke drie weken op vrijdag en zaterdag. Alleen het eerstvolgende weekend is zichtbaar (enkelvoud, 24 november 2026). De lijst staat in sectie 9 van `src/nl.html` en `src/de.html` (`<ol class="data">`, per datum `data-eind`). Een klein script in blok 1 haalt verstreken data weg, daarna schuift het volgende weekend vanzelf door. De lijst loopt tot 4 en 5 juni 2027: vóór die tijd aanvullen, anders staat er "Nieuwe data volgen".

- **Sfeer eerder (20 november 2026)**: direct na de feitenband staat een beeldmozaïek (dorp en zee, strand, woonkamer, binnentuin, gebouw). Twee beeldbanden over de volle breedte: begane grond met voorzieningen (na sectie 5) en de duinovergang (voor het rendement). Webformaten staan als `images/sfeer-*.webp`.
- **Hotel Prins Maurits**: de foto van het oude hotel (`images/hotel-prins-maurits.webp`) staat als "toen" naast de impressie bij Sinds 1908. Gebruik goedgekeurd op 20 november 2026.
- **Willem van de Griend** staat met foto bij de formulierkop en in stap 2 van "wat er gebeurt na verzenden" (`images/willem-van-de-griend.webp`).

- **"exclusief btw"** bevat het verboden woord "exclusief". Op de pagina staat daarom "zonder btw" (DE: "zzgl. MwSt.").
- **Bankgarantie**: om percentages buiten de rendementssectie te houden staat er "een tiende van de aanneemsom" in plaats van 10%.
- **Knoptekst Terracotta**: wit op #9E6B60 haalt 4,4:1. Dat is AA voor grote tekst, daarom staan de knoppen op 19 px vet (de balkknoppen 18,7 px vet). Kleiner of dunner maken betekent een donkerdere Terracotta nodig hebben, bijvoorbeeld #8E5E54 (5,4:1).
- **AFM-zin op /de** staat alleen in het Duits, zonder de Nederlandse zin erbij (besloten 20 november 2026).
- **Vrijblijvend-regel** in het Duits: "Unverbindlich. Sie gehen keinerlei Verpflichtung ein."
- **"op ons kantoor in Alkmaar"** is bewust "in Alkmaar" gebleven: het feitenblad noemt geen kantoor.

## Beelden in 4K en nieuwe hero (27 november 2026)

- In OpenArt (Nano Banana Pro, image2image 4K) opgeschaald, trouw aan het origineel. De 4K-PNG's staan in
  `Beeldmateriaal/Renders 2026-11/Upscaled 4K/`.
- Voor het web omgezet naar webp met `-hd` in de naam (`Landingspagina/images/`) en in GHL Media Storage gezet; de blokken 1
  (NL, variant B, DE) verwijzen naar `files.leadconnectorhq.com`: de vier interieurs, het overzicht en `sfeer-gebouw-zonsondergang`
  (2000 px breed).
- **Nieuwe hero**: op verzoek van Ruben vervangen door de daglichtrender `Gevels - Strandresidence aan Zee`
  (`hero-desktop-gevel-hd.webp` 2560 x 1717, `hero-mobiel-gevel-hd.webp` 1200 x 1609, uitsnede rond het hoofdgebouw met de naam).
  De golden-hourhero met de cabrio is eraf. Alt-tekst aangepast: "overdag" in plaats van "bij zonsondergang".
- `src/nl.html` en `src/de.html` gebruiken dezelfde `-hd`-bestandsnamen; die staan pas op GitHub Pages na een push.
- Plakken in GHL: kopieer pas vlak voor het plakken naar het klembord en controleer de editor voor Save. Tijdens deze sessie werd het
  klembord tussendoor overschreven; zo'n plak is telkens geannuleerd.
- **Overlay hero** (27 november 2026): op desktop alleen donker links achter de tekst (horizontaal verloop), zodat de daglichtrender
  zichtbaar is; op mobiel bovenaan lichter, achter de tekst donker. Uitsnede desktop `object-position:60% 55%`. Selectors zijn bewust
  `.srp .hero.hero::before` en `.hero-img.hero-img`, omdat blok 2 dezelfde CSS met de oude overlay bevat en later op de pagina staat.
  Voorbeeld: `hero-overlay-lichter.jpg`.
- **Hero mobiel** (27 november 2026): beeld vrij bovenaan (50svh, logo erop), kop, tekst en knoppen eronder op nacht-blauw;
  geen tekst meer over het beeld. Tekst ongewijzigd. Voorbeeld: `hero-mobiel-voorstel.png`. Desktop ongewijzigd.

- **Formulieren omgedraaid** (27 november 2026): op NL-control, variant B en DE staat het brochureformulier nu links (op mobiel bovenaan) en het verkoopweekend-formulier rechts. Gedaan in GHL via Layers (2 Column Row, kolommen versleept); de class `sr-brochure` is meeverhuisd.
- **Verkoopweekendknoppen** (27 november 2026): het klikscript in de funnel-head (`ghl/clarity-head-trackingcode.html`) laat
  `#sr-formulieren` direct naar de kolom van "SR - VD" / "SR - VD - DE" scrollen (herkend aan de formulier-ID), zodat bezoekers niet
  eerst bij de brochure uitkomen. Getest op desktop (NL en DE) en mobiel (NL, heroknop en vaste balk).
