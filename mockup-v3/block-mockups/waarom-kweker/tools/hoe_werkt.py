# Mockup tool (not site code): phase 2, item 2.1 "Hoe het werkt" as approved by the owner (19 Nov), applied by
# tools/finalize_main.py in place of the placeholder between the guarantee and the footer. CSS: tools/hoe-werkt-main.css.
# History: fase2a.html (rounds 1-3, Fable's staircase and more), fase2b.html (D, one photo), fase2c.html / fase2c-fable.html
# (D without a card, Fable's fixes).
# Pickup: the owner's map pin (screenshot, 19 Nov): 52.0914891, 5.7283254, Apeldoornseweg, 6733 SC Wekerom (OpenStreetMap;
# about 1.9 km from Esserbroekweg 2, Otterlo, the office address on the old site and in the footer). All Dutch copy is a draft.
import pathlib
T = pathlib.Path(__file__).parent

MAP = 'https://www.google.com/maps/search/?api=1&amp;query=52.0914891%2C5.7283254'
STEPS = [  # (verb, text, meta)
    ('Kiezen', 'Soort, maat en aantal. Bij elke soort staan alle maten met hun prijs.', ''),
    ('Bestellen', 'Online of per telefoon. U&nbsp;betaalt met iDEAL, per overschrijving of bij ontvangst; zakelijk op factuur.', ''),
    ('Afspreken', 'Samen kiezen we de dag van bezorgen of afhalen, wanneer het u&nbsp;uitkomt.', ''),
    ('Ontvangen', 'Bezorgd of afgehaald. De bezorgkosten hangen af van afstand en aantal; u&nbsp;ziet ze vóór u&nbsp;betaalt.',
     f'<p class="hw-m">Afhalen: <a href="{MAP}" target="_blank" rel="noopener noreferrer">Apeldoornseweg, Wekerom</a></p>'),
]
ROUTE = '<ol class="hw-route">' + ''.join(f'<li><h3>{v}</h3><p>{p}</p>{x}</li>' for v, p, x in STEPS) + '</ol>'
BLOCK = ('<section class="hw" id="hoe" aria-labelledby="h-hoe"><div class="in hwo-hd">'
         '<h2 id="h-hoe" class="hw-h"><span>Van ons veld naar uw tuin,</span> <span>in vier stappen.</span></h2></div>'
         '<div class="hwo-band"><img src="img/voorbeeld/hw-v3-veld.webp" alt="Voorbeeldfoto: bloeiende rhododendrons op een veld" loading="lazy"></div>'
         '<div class="in hwo-ft">' + ROUTE +
         '<p class="hw-cr">Voorbeeldfoto, niet van onze kwekerij: ‘Rhododendronfeld einer Baumschule in Edewecht’, '
         'JoachimKohler-HB, Wikimedia Commons, CC BY-SA 4.0.</p></div></section>')
PH = '<div class="between"><div class="in"><span>… hier volgt Hoe het werkt: bij de stap «afhalen» staan het adres en de openingstijden …</span></div></div>'


def apply(s):
    assert s.count(PH) == 1, s.count(PH)
    s = s.replace(PH, BLOCK)
    return s.replace('</head>', '<style id="hoe-werkt-css">' + (T / 'hoe-werkt-main.css').read_text() + '</style></head>', 1)
