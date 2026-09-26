# Formulieren in GoHighLevel

Twee formulieren. Beide met telefoonnummer verplicht, want elke aanvraag wordt nagebeld.
De embeds komen in `index.html` op de plek van de blokken met id `kennismaking` en `brochure`.

## 1. Kennismaking (krijgt visuele voorrang)

| Label | Type | Verplicht |
|---|---|---|
| Voornaam | tekst | ja |
| Achternaam | tekst | ja |
| E-mailadres | e-mail | ja |
| Telefoonnummer | telefoon | ja |
| Waar denkt u vooral aan? | keuze: vooral eigen gebruik / vooral belegging / beide | ja |
| Voorkeur | keuze: op locatie in Bergen aan Zee / via videobellen | ja |
| Wanneer bent u het best bereikbaar? | keuze: ochtend / middag / avond | ja |
| Koopt u privé of via een BV? | keuze: privé / via een BV / weet ik nog niet | nee |

Knoptekst: **Plan een kennismaking**
Na verzenden: doorsturen naar `bedankt.html`.
Tag: `srbaz kennismaking` plus de waarde van "Waar denkt u vooral aan".

## 2. Brochure en prijslijst

| Label | Type | Verplicht |
|---|---|---|
| Voornaam | tekst | ja |
| Achternaam | tekst | ja |
| E-mailadres | e-mail | ja |
| Telefoonnummer | telefoon | ja |
| Waar denkt u vooral aan? | keuze: vooral eigen gebruik / vooral belegging / beide | ja |

Knoptekst: **Ontvang de brochure en prijslijst**
Na verzenden: doorsturen naar `bedankt.html`, brochure direct per e-mail.
Tag: `srbaz brochure` plus de waarde van "Waar denkt u vooral aan".

## Belofte op de pagina, dus zo inrichten

1. Brochure en prijslijst direct per e-mail.
2. Binnen één werkdag belt een adviseur. TE BEVESTIGEN of deze termijn haalbaar is.
3. Bezoek of videogesprek plannen, alleen als de aanvrager dat wil.
