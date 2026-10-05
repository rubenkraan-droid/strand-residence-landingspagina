# Strand Residence Bergen aan Zee, landingspagina

Landingspagina voor koud verkeer uit Meta-advertenties. Eén bestand, `index.html`,
met alle CSS en JavaScript inline. Geen build.

## Live

https://rubenkraan-droid.github.io/strand-residence-landingspagina/

## Bestanden

| Bestand | Inhoud |
|---|---|
| `index.html` | de landingspagina |
| `bedankt.html` | bedankpagina na verzenden van een formulier |
| `images/` | projectbeeld, afkomstig uit het officiële archief van strandresidence.nl |
| `ghl/formulieren.md` | velden, labels en tags voor de twee GoHighLevel-formulieren |
| `voorstel/` | webversie van het voorstel aan Torero Invest (aanpak verkoop en marketing), met eigen beelden in `voorstel/img/` |
| `plan-van-aanpak/` | plan van aanpak voor Torero Invest: vergoeding, planning vanaf 12 oktober, verwachting en voorwaarden |

## Wijzigen

1. Pas `index.html` aan.
2. Committen en pushen:
   ```
   git add -A
   git commit -m "Beschrijving van de wijziging"
   git push
   ```
3. Na ongeveer een minuut staat het live.

## Let op voor livegang

De pagina staat op `noindex`, want hij is bedoeld voor advertentieverkeer.
In de HTML staan nog markeringen `TE BEVESTIGEN` en `BEWIJS NODIG`. Die moeten eruit
voordat er advertentiebudget op gaat. De beschikbaarheid `[AANTAL] van 70` staat op twee
plekken en moet overal hetzelfde getal worden.

De twee formulieren zijn nu placeholders. Daar komen de embeds uit GoHighLevel.
