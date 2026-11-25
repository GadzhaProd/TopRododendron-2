# Mockup tool (not site code): phase 2, item 2.1 "Hoe het werkt" as approved by the owner (19 Nov), applied by
# tools/finalize_main.py in place of the placeholder between the guarantee and the footer. CSS: tools/hoe-werkt-main.css.
# History: fase2a.html (rounds 1-3, Fable's staircase and more), fase2b.html (D, one photo), fase2c.html / fase2c-fable.html
# (D without a card, Fable's fixes).
# Photo (owner, 19 Nov): img/gen/veld-L2.webp, the example field photo (Wikimedia Commons, "Rhododendronfeld einer Baumschule
# in Edewecht", JoachimKohler-HB, CC BY-SA 4.0) edited with one more shrub at the back left (img/gen/README.md, round 6).
# Pickup: the owner's map pin (screenshot, 19 Nov): 52.0914891, 5.7283254, Apeldoornseweg, 6733 SC Wekerom (OpenStreetMap;
# about 1.9 km from Esserbroekweg 2, Otterlo, the office address on the old site and in the footer). All Dutch copy is a draft.
import pathlib
T = pathlib.Path(__file__).parent

# (owner, 23 Nov: the search link opened the office; a route to the exact pin of the field instead)
MAP = 'https://www.google.com/maps/dir/?api=1&amp;destination=52.0914891%2C5.7283254'
STEPS = [  # (verb, text, meta)
    ('Kiezen', 'Soort, maat en aantal. Bij elke soort staan alle maten met hun prijs.', ''),
    ('Bestellen', 'Online of per telefoon. U&nbsp;betaalt met iDEAL, per overschrijving of bij ontvangst; zakelijk op factuur.', ''),
    ('Afspreken', 'Samen kiezen we de dag van bezorgen of afhalen, wanneer het u&nbsp;uitkomt.', ''),
    ('Ontvangen', 'Bezorgd of afgehaald. Bezorgen kost €&nbsp;75 per bestelling; afhalen is gratis.',
     f'<p class="hw-m">Afhalen: <a href="{MAP}" target="_blank" rel="noopener noreferrer">Apeldoornseweg, Wekerom</a></p>'),
]
ROUTE = '<ol class="hw-route">' + ''.join(f'<li><h3>{v}</h3><p>{p}</p>{x}</li>' for v, p, x in STEPS) + '</ol>'
BLOCK = ('<section class="hw" id="hoe" aria-labelledby="h-hoe"><div class="in hwo-hd">'
         '<h2 id="h-hoe" class="hw-h"><span>Van ons veld naar uw tuin,</span> <span>in vier stappen.</span></h2></div>'
         '<div class="hwo-band"><img src="img/gen/veld-L2.webp" alt="Bloeiende rhododendrons op het veld" loading="lazy"></div>'
         '<div class="in hwo-ft">' + ROUTE + '</div></section>')
# (owner, 19 Nov: no credit line under the block; the photo's source is in img/voorbeeld/CREDITS.md)
PH = '<div class="between"><div class="in"><span>… hier volgt Hoe het werkt: bij de stap «afhalen» staan het adres en de openingstijden …</span></div></div>'


def apply(s):
    assert s.count(PH) == 1, s.count(PH)
    s = s.replace(PH, BLOCK)
    return s.replace('</head>', '<style id="hoe-werkt-css">' + (T / 'hoe-werkt-main.css').read_text() + '</style></head>', 1)
