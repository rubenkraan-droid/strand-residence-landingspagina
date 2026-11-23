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
1. Hoe en hoe ver vooruit eigenaren hun verblijf vastleggen, en of er regels gelden voor het hoogseizoen (sectie 3 en vraag 1)
2. Wie schoonmaak en klein onderhoud regelt, en hoe vaak de eigenaar een afrekening ontvangt (sectie 3)
3. Waar de koper de hoogte van de commissie en de voorwaarden van de verhuurovereenkomst kan inzien (vraag 2)

**Sinds 1908**
4. Rol van Tom Stroomer bij Strand Residence Exploitatie B.V.
5. Citaat van Tom Stroomer (en Duitse vertaling)

**Rendement en kosten**
6. ~~Koopsom 1.0.4 v.o.n. zonder btw~~: bevestigd op 20 november 2026.
7. Is de netto opbrengst jaar 1 (€ 35.414) vóór of na aftrek van de jaarlijkse kosten (€ 8.600)? Dit moet helder zijn voordat de tabel live gaat.
8. Uit welke posten de jaarlijkse kosten bestaan (VvE, verzekering, belastingen)

**Kopen**
9. Financieringsmogelijkheden (DE: ook voor buitenlandse kopers)
10. Kopen via een BV mogelijk, en waar op te letten (DE: via een Duitse vennootschap)

**Verkoopweekend**
11. Tijden en adres van Strandpaviljoen De Jongens op 12 december
12. Wat de bezoeker op het verkoopweekend ziet en met wie hij spreekt

**Voettekst**
13. Link naar privacyverklaring en contactgegevens (DE: ook Datenschutzerklärung en Impressum)

**Woningtypen** (sectie 6, toegevoegd 20 november 2026)
16. Overzicht per woningtype uit de prijslijst van 1 november 2026: naam of code, personen, slaapkamers, m², sauna of spa, vanafprijs, aantal beschikbaar
17. Welk interieurbeeld bij Beach Luxury hoort en welk bij Residence Chique
18. "Nog 23 van de 70 beschikbaar" komt uit de prijslijst van 1 november: controleren op de dag van livegang
19. Is de berging standaard bij de prijs inbegrepen (zoals de prijslijst zegt) of een mogelijkheid tegen meerprijs? Op de pagina staat nu "mogelijkheid tot een eigen berging".

**Alleen DE**
14. Fiscale aandachtspunten voor kopers uit Duitsland, Oostenrijk of Zwitserland
15. Of de makelaar Duits spreekt

## Keuzes om te weten

- **Sfeer eerder (20 november 2026)**: direct na de feitenband staat een beeldmozaïek (dorp en zee, strand, woonkamer, binnentuin, gebouw). Twee beeldbanden over de volle breedte: begane grond met voorzieningen (na sectie 5) en de duinovergang (voor het rendement). Webformaten staan als `images/sfeer-*.webp`.
- **Hotel Prins Maurits**: de foto van het oude hotel (`images/hotel-prins-maurits.webp`) staat als "toen" naast de impressie bij Sinds 1908. Gebruik goedgekeurd op 20 november 2026.
- **Willem van de Griend** staat met foto bij de formulierkop en in stap 2 van "wat er gebeurt na verzenden" (`images/willem-van-de-griend.webp`).

- **"exclusief btw"** bevat het verboden woord "exclusief". Op de pagina staat daarom "zonder btw" (DE: "zzgl. MwSt.").
- **Bankgarantie**: om percentages buiten de rendementssectie te houden staat er "een tiende van de aanneemsom" in plaats van 10%.
- **Knoptekst Terracotta**: wit op #9E6B60 haalt 4,4:1. Dat is AA voor grote tekst, daarom staan de knoppen op 19 px vet (de balkknoppen 18,7 px vet). Kleiner of dunner maken betekent een donkerdere Terracotta nodig hebben, bijvoorbeeld #8E5E54 (5,4:1).
- **AFM-zin op /de** staat alleen in het Duits, zonder de Nederlandse zin erbij (besloten 20 november 2026).
- **Vrijblijvend-regel** in het Duits: "Unverbindlich. Sie gehen keinerlei Verpflichtung ein."
- **"op ons kantoor in Alkmaar"** is bewust "in Alkmaar" gebleven: het feitenblad noemt geen kantoor.
