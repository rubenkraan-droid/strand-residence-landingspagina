#!/usr/bin/env python3
"""Bouwt uit src/ de voorbeeldpagina's (NL en DE) en de GHL-blokken.
Gebruik: python3 build.py   (vanuit de map v2)"""
import re, pathlib

HIER = pathlib.Path(__file__).resolve().parent
SRC = HIER / "src"
GHL = HIER / "ghl"
GHL.mkdir(exist_ok=True)
ABS_IMG = "https://rubenkraan-droid.github.io/strand-residence-landingspagina/images"
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Source+Serif+4:opsz,wght@8..60,400;8..60,600'
         '&family=Titillium+Web:wght@400;600;700&display=swap" rel="stylesheet">')

css = (SRC / "srp.css").read_text()
css_min = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
css_min = re.sub(r"\s*\n\s*", "", css_min)

logo = (HIER.parent.parent / "Huisstijl/web/logo-currentcolor.svg").read_text().strip()
logo = logo.replace(' xmlns:c2pa="http://c2pa.org/manifest"', "")
logo = re.sub(r"<metadata.*?</metadata>", "", logo, flags=re.S)
logo = re.sub(r">\s+<", "><", logo)


def deel(src, naam):
    m = re.search(rf"<!--{naam}-->(.*?)<!--/{naam}-->", src, re.S)
    return m.group(1).strip()


def vul(html, img):
    return html.replace("{{IMG}}", img).replace("{{LOGO}}", logo)


TITELS = {"nl": "Strand Residence Bergen aan Zee", "de": "Strand Residence Bergen aan Zee"}
for taal in ("nl", "de"):
    src = (SRC / f"{taal}.html").read_text()
    b1, forms, b2 = deel(src, "BLOK1"), deel(src, "FORMS"), deel(src, "BLOK2")
    # voorbeeldpagina met relatieve beelden
    pagina = (f'<!doctype html><html lang="{taal}"><head><meta charset="utf-8">'
              '<meta name="viewport" content="width=device-width,initial-scale=1">'
              '<meta name="robots" content="noindex,nofollow">'
              f"<title>{TITELS[taal]}</title>{FONTS}"
              '<link rel="preload" as="image" href="../images/hero-mobiel.webp" media="(max-width:759px)">'
              f"<style>html,body{{margin:0;background:#FAF9F7}}{css}</style></head><body>\n"
              f"{vul(b1, '../images')}\n<!-- HIER KOMEN DE TWEE NATIVE GHL-FORMULIEREN -->\n{forms}\n"
              f"{vul(b2, '../images')}\n</body></html>\n")
    (HIER / f"voorbeeld-{taal}.html").write_text(pagina)
    # GHL-blokken met absolute beelden en eigen CSS per blok
    for nr, blok, wat in ((1, b1, "boven"), (2, b2, "onder")):
        kop = (f"<!-- Strand Residence | {taal.upper()} | blok {nr}: alles {wat} de formulieren. "
               "Plakken in een GHL Custom Code-element. Alle CSS is gescoped onder .srp -->\n")
        uit = kop + FONTS + f"<style>{css_min}</style>\n" + vul(blok, ABS_IMG) + "\n"
        (GHL / f"{taal.upper()}-blok-{nr}-{wat}-formulieren.html").write_text(uit)

# Bedankpagina's: één Custom Code-blok per pagina
for taal, naam, titel in (("nl", "bedankt-nl", "Bedankt | Strand Residence Bergen aan Zee"), ("de", "danke-de", "Vielen Dank | Strand Residence Bergen aan Zee")):
    blok = deel((SRC / f"{naam}.html").read_text(), "BEDANKT")
    pagina = (f'<!doctype html><html lang="{taal}"><head><meta charset="utf-8">'
              '<meta name="viewport" content="width=device-width,initial-scale=1">'
              '<meta name="robots" content="noindex,nofollow">'
              f"<title>{titel}</title>{FONTS}"
              f"<style>html,body{{margin:0;background:#FAF9F7}}{css}</style></head><body>\n"
              f"{vul(blok, '../images')}\n</body></html>\n")
    (HIER / f"voorbeeld-{naam}.html").write_text(pagina)
    kop = (f"<!-- Strand Residence | {taal.upper()} | {naam}: volledige bedankpagina. "
           "Plakken in één GHL Custom Code-element. Alle CSS is gescoped onder .srp -->\n")
    (GHL / f"{taal.upper()}-{naam}.html").write_text(kop + FONTS + f"<style>{css_min}</style>\n" + vul(blok, ABS_IMG) + "\n")

print("Klaar:", *sorted(p.name for p in HIER.glob("voorbeeld-*.html")), *sorted(p.name for p in GHL.iterdir()))
