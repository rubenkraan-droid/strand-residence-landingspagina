# Opdracht: GoHighLevel inrichten voor Strand Residence Bergen aan Zee

Je richt in GoHighLevel (GHL) alles in voor de leadgeneratie van Strand Residence Bergen aan Zee. Werk stap voor stap, controleer na elke stap of het werkt, en rapporteer aan het eind wat staat en wat nog openstaat. Vraag om bevestiging voordat je iets live zet, een workflow activeert of iets naar echte contacten verstuurt.

## Context

- Recraparcs verkoopt voor ontwikkelaar Torero Invest het project Strand Residence: 70 nieuwbouw vakantieappartementen in Bergen aan Zee, circa 100 meter van het strand, op de plek van het voormalige Hotel Prins Maurits (sinds 1908 van de familie Stroomer). Oplevering 2028. Eigen gebruik tot 89 dagen per jaar, de rest van het jaar professionele verhuur.
- Doelgroep: vermogende Nederlanders, waaronder DGA's die zakelijk beleggen, en stellen van 55 tot 72 jaar. Eerst Nederland; Duitse leads worden wel opgepakt.
- Leads komen uit Meta-advertenties naar een eigen landingspagina in GHL. GHL vangt de aanvraag op, verstuurt mail en geeft de lead via een webhook door aan n8n, dat de deal in Pipedrive aanmaakt. De makelaars bellen vanuit Pipedrive en CloudTalk. Pipedrive is leidend voor de stand van zaken per koper; GHL is leidend voor pagina's, formulieren en mail.
- Verkoopweekenden: één per drie weken, op vrijdag en zaterdag. De datum staat alleen op de landingspagina, niet in de advertenties.

## Huisregels voor alle teksten

- Nederlands, u-vorm, iets formeel en direct.
- Geen gedachtestreepjes (em-dashes). Gebruik komma's, punten of dubbele punten.
- Verboden: een rendementspercentage in kop of onderwerpregel, "gegarandeerd", "uniek", "exclusief", "toplocatie", "een van de laatste kansen", "zorgeloos rendement", "waardevaste investering". Geen commissiepercentages.
- Gebruik alleen feiten uit het feitenblad. Bij twijfel: [INVULLEN] laten staan en melden.
- Alle teksten gaan vóór livegang ter goedkeuring naar Torero; zonder bezwaar binnen 48 uur gelden ze als goedgekeurd. Zet niets live vóór die termijn.
- Beelden van het gebouw zijn impressies; vermeld dat bij elk beeld.
- AFM-zin op de landingspagina en in de voettekst van elke mail: "Let op! U belegt buiten AFM-toezicht. Geen vergunningplicht voor deze activiteit."

## 1. Subaccount en basis

1. Controleer of er al een subaccount "Strand Residence" bestaat. Zo niet, maak hem aan.
2. Tijdzone Europe/Amsterdam, taal Nederlands, valuta EUR.
3. Bedrijfsnaam in mails: Strand Residence. Telefoonnummer op pagina en in mails: [INVULLEN].

## 2. Domeinen

1. Landingspagina op `info.strandresidence.nl`. Het CNAME-record verwijst naar `sites.ludicrous.cloud`. Koppel het domein aan de funnel en controleer of het SSL-certificaat actief is.
2. Verzenddomein `mail.strandresidence.nl` (Mailgun via GHL). Controleer of SPF, DKIM, MX en het tracking-CNAME geverifieerd zijn. Zo niet: meld welke records ontbreken, verander niets aan het hoofddomein.
3. Afzender: "Strand Residence" <[INVULLEN]@strandresidence.nl>. Antwoordadres: [INVULLEN], een mailbox die dagelijks gelezen wordt.

## 3. Eigen velden (contact)

| Veld | Type |
|---|---|
| Aanvraagtype | keuze: Verkoopweekend, Brochure |
| utm_source, utm_medium, utm_campaign | tekst |
| AD naam (utm_content) | tekst |
| AD ID (utm_term) | tekst |
| fbclid | tekst |
| Bron | keuze: Eigen marketing, Opdrachtgever, Afgeschreven Croon en Teer |
| Datum afspraak | datum |
| Tijd afspraak | tekst |
| Locatie afspraak | tekst |
| Betrokken makelaar | tekst |
| Pipedrive deal ID | tekst |

## 4. Tags

`sr-verkoopweekend`, `sr-brochure`, `sr-mailflow`, `sr-geklikt`, `sr-afspraak-gepland`, `sr-afgemeld`, `sr-afgeschreven-croon-teer`

## 5. Formulieren

Twee formulieren. Vraag niet naar eigen gebruik, belegging of privé/BV; dat bespreekt de makelaar aan de telefoon.

**Aanmelding verkoopweekend**: voornaam, achternaam, e-mailadres, telefoonnummer (alle vier verplicht). Knop: "Meld u aan voor het verkoopweekend". Zet Aanvraagtype op Verkoopweekend en tag `sr-verkoopweekend`.

**Brochure**: voornaam, achternaam, e-mailadres, telefoonnummer (alle vier verplicht). Knop: "Ontvang de brochure". Zet Aanvraagtype op Brochure en tag `sr-brochure`.

Beide formulieren:
- Verborgen velden die utm_source, utm_medium, utm_campaign, utm_content, utm_term en fbclid uit de URL overnemen.
- Toestemmingsvinkje met link naar de privacyverklaring: [INVULLEN URL].
- Na verzenden doorsturen naar de bedankpagina.

## 6. Funnel en pagina's

1. Funnel "Strand Residence" met twee pagina's: landingspagina en bedankpagina, op `info.strandresidence.nl`.
2. Neem inhoud en opbouw over van de bestaande pagina: https://rubenkraan-droid.github.io/strand-residence-landingspagina/ (twee gelijkwaardige knoppen: verkoopweekend en brochure). Pas de datum aan naar het eerstvolgende verkoopweekend: [INVULLEN].
3. Meta-pixel op beide pagina's; de gebeurtenis Lead alleen op de bedankpagina. Zet de Conversies-API aan met dataset-ID [INVULLEN] en toegangstoken [INVULLEN].
4. Cookiebanner: de pixel laadt pas na toestemming.
5. Pagina's op noindex.

## 7. Workflows

**W1. Nieuwe aanvraag** (trigger: een van beide formulieren verzonden)
1. Tags en Aanvraagtype zetten.
2. Webhook naar n8n: [INVULLEN URL]. Stuur alle contactvelden mee, inclusief UTM-velden, fbclid, Aanvraagtype en tijdstip van aanvraag.
3. Bij Brochure: direct de brochuremail met de pdf zonder prijslijst ([INVULLEN link]). Gebruik niet de brochure uit 2021 (verouderd rendement en verboden woorden); gebruik de goedgekeurde leaflet of eigen pdf. Bij Verkoopweekend: direct een bevestiging dat de aanmelding binnen is en dat een makelaar binnen één werkdag belt om een vast tijdvak in te plannen.
4. Tag `sr-mailflow` en door naar W2.

**W2. Mailflow projectinformatie** (elke lead)
- Ongeveer tien mails, verspreid over zes weken, bijvoorbeeld dag 1, 3, 5, 8, 12, 16, 21, 28, 35 en 42. Verstuur tussen 9.00 en 20.00 uur, nooit twee mails op één dag.
- Onderwerpen, in deze volgorde: de plek en de geschiedenis van Hotel Prins Maurits; de appartementen en de twee interieurstijlen; verhuur en eigen gebruik; fiscale informatie (btw bij verhuur, met verwijzing naar de onafhankelijke fiscaal adviseur); Bergen aan Zee en de omgeving; bouw en oplevering; hoe het verkoopproces werkt; uitnodiging voor het eerstvolgende verkoopweekend; een korte vraag of we nog iets kunnen toelichten; afsluiting.
- Elke mail bevat een link naar de landingspagina of een document. Een klik op een link: tag `sr-geklikt` en een webhook naar n8n ([INVULLEN URL]), zodat de makelaar een belactiviteit krijgt.
- Stoppen zodra de tag `sr-afspraak-gepland` of `sr-afgemeld` wordt gezet.

**W3. Afspraak gepland** (trigger: inkomende webhook vanuit n8n bij stage "Afspraak gepland" in Pipedrive, met Datum afspraak, Tijd afspraak, Locatie afspraak en Betrokken makelaar)
1. Velden bijwerken, tag `sr-afspraak-gepland`, W2 stoppen.
2. Direct een bevestigingsmail met datum, tijd, adres, naam van de makelaar en een agenda-uitnodiging.
3. Omgevingsmails: een korte reeks van twee of drie mails over Bergen aan Zee en de omgeving, samengeperst zodat alle mails vóór de afspraak vallen. Reken terug vanaf Datum afspraak. Ligt de afspraak binnen twee dagen, stuur dan alleen de bevestiging en één omgevingsmail.
4. Herinnering 24 uur vooraf.
5. Komt er een nieuwe datum binnen via de webhook: de reeks opnieuw berekenen. Bij annulering: de reeks stoppen.

**W4. Afgeschreven leads van Croon en Teer** (trigger: tag `sr-afgeschreven-croon-teer`)
- Bron op "Afgeschreven Croon en Teer", webhook naar n8n met die bron, door naar W2. Deze leads tellen niet mee in de conversie van de eigen marketing; houd ze daarom altijd herkenbaar gescheiden.

**Bronregel (contract artikel 3.9 en 4.5)**
- Komt een aanvraag binnen met utm_source=callinghe, of meldt het contact zich als eerste via een kanaal van Torero: Bron op "Opdrachtgever". Een contact dat zich als eerste via onze advertenties meldde, houdt Bron "Eigen marketing", ook als het zich later via een ander kanaal meldt.
- Leg bij elk contact het tijdstip van de eerste aanmelding vast; dat is het bewijs bij een discussie over de herkomst.

## 8. Testen

1. Twee testaanvragen (een per formulier) met een URL met UTM-parameters en een fbclid. Controleer: tags, eigen velden, de juiste eerste mail, de webhook-inhoud richting n8n.
2. Controleer in Meta Events Manager of de Lead-gebeurtenis binnenkomt, via de pixel en de Conversies-API, zonder dubbele telling.
3. Test W3 met een testwebhook met een afspraak over vijf dagen en een met een afspraak over één dag.
4. Controleer de bezorging van een testmail (inbox, niet spam).
5. Verwijder of markeer alle testcontacten na afloop.

## 9. Oplevering

Rapporteer als lijst:
- Wat ingericht en getest is.
- Wat openstaat, met de [INVULLEN]-punten die nog ontbreken.
- De webhook-URL's van GHL die n8n nodig heeft (voor W3), en de inhoud van de uitgaande webhook (veldnamen), zodat de n8n-flow erop kan worden afgestemd.
