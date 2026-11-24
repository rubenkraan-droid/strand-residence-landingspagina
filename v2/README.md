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

## Inbouwen in GHL

1. Pagina: Custom Code-element met blok 1, daaronder een rij met twee kolommen voor de native formulieren "SR - VD" (links) en "SR - BROCHURE" (rechts), daaronder Custom Code met blok 2.
2. Geef het formulier "SR - BROCHURE" (of de kolom eromheen) de element-ID `sr-brochure`. De knoppen "Ontvang de brochure" en "Brochure" springen daarheen. "Verkoopweekend" springt naar de formulierkop (`sr-formulieren`) in blok 1, dat werkt altijd.
3. De beelden staan als absolute URL op GitHub Pages. Twee nieuwe beelden (`images/hero-mobiel.webp`, 73 kB, en `images/hero-desktop.webp`, 133 kB) staan nog niet online: eerst committen en pushen, anders is de hero leeg.
4. Head/Tracking Code van de NL-pagina: het bestaande `../ghl/5-NL-head-trackingcode.html` (doorsturen naar /de op tijdzone, `?taal=nl` blijft NL). Zet in de footer-code van beide pagina's ook het anti-scrollscript tegen de Meta in-app browser (snippet 1 van de skill landingspagina).
5. Plakken met UTF-8: `LC_ALL=en_US.UTF-8 pbcopy < ghl/NL-blok-1-boven-formulieren.html`.

### Vaste balk onderaan
De balk staat in blok 1 en gebruikt `position: sticky` in plaats van JavaScript. Hij blijft onderaan het scherm tot het einde van blok 1 en blijft dan staan boven de formulieren, dus hij komt er nooit overheen. Op desktop is hij verborgen. **Testen in GHL:** als een GHL-wrapper `overflow: hidden` heeft, plakt de balk niet. Dan voor die sectie in GHL de overflow op zichtbaar zetten.

### Lettertypes
Titillium Web en Source Serif 4 via Google Fonts, met "axia" en "odile" vooraan in de stack. Zodra de Adobe Fonts-kit er is, de kit-link in de head van de pagina zetten. De rest gaat vanzelf.

## Placeholders die nog bevestigd moeten worden

Geel gemarkeerd op de pagina (`class="ph"`). NL en DE hebben dezelfde, plus een paar Duitse extra's.

**Eigen gebruik en verhuur**
1. Hoe en hoe ver vooruit eigenaren hun verblijf vastleggen (sectie 3 en vraag 1). Regels voor het hoogseizoen: die gelden niet, bevestigd op 24 november 2026.
2. Wie schoonmaak en klein onderhoud regelt, en hoe vaak de eigenaar een afrekening ontvangt (sectie 3)
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
10. Kopen via een BV mogelijk, en waar op te letten (DE: via een Duitse vennootschap)

**Verkoopweekend**
11. Tijden en adres van Strandpaviljoen De Jongens op 12 december, en of de latere weekenden op dezelfde plek zijn
12. Wat de bezoeker op het verkoopweekend ziet en met wie hij spreekt

**Voettekst**
13. Link naar privacyverklaring en contactgegevens (DE: ook Datenschutzerklärung en Impressum)

**Woningtypen** (sectie 6, toegevoegd 20 november 2026)
16. Overzicht per woningtype uit de prijslijst van 1 november 2026: naam of code, personen, slaapkamers, m², sauna of spa, vanafprijs, aantal beschikbaar
17. ~~Welk interieurbeeld bij Beach Luxury hoort en welk bij Residence Chique~~: bevestigd op 23 november 2026.
18. "Nog 23 van de 70 beschikbaar" komt uit de prijslijst van 1 november: controleren op de dag van livegang
19. ~~Berging standaard of optie~~: inbegrepen bij de prijs, bevestigd op 24 november 2026.

**Holding** (toegevoegd 24 november 2026)
20. ~~Mag "kopen vanuit uw holding" op de pagina en in de advertenties?~~: ja, bevestigd op 24 november 2026.

**Alleen DE**
14. Fiscale aandachtspunten voor kopers uit Duitsland, Oostenrijk of Zwitserland
15. Of de makelaar Duits spreekt

## Keuzes om te weten

- **Opgeschaalde beelden (24 november 2026)**: de luchtfoto (`images/luchtfoto-dorp-strand-hd.webp`) en de duinovergang (`images/duinovergang-strand-hd.webp`) zijn met AI opgeschaald via OpenArt (Nano Banana Pro, 4K). De 4K-bestanden staan in `Beeldmateriaal/Locatie/`. Bij de luchtfoto heeft de AI de details van de gebouwen opnieuw getekend; het blijft een impressie.

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
