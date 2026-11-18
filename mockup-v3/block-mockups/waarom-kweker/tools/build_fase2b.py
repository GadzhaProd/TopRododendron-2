# Mockup tool (not site code): fase2b.html = the main mockup with "Hoe het werkt" variant D (owner chose it, 18 Nov),
# refined, in place of the placeholder between the guarantee and the footer. CSS: tools/hoe-werkt-d.css.
# Owner (18 Nov): one photo only, the Edewecht field on peat (img/voorbeeld/hw-v3-veld.webp, an example photo from Wikimedia
# Commons, see CREDITS.md; the live site needs the nursery's own field photo); no opening hours in "Ontvangen"; the steps at
# the bottom of the card, balanced. All Dutch copy is a draft.
# Usage: python3 tools/build_fase2b.py [dir]
import re, pathlib, sys
D = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
s = (D / 'index.html').read_text()
def rep(a, b):
    global s
    assert s.count(a) == 1, (s.count(a), a[:70]); s = s.replace(a, b)

STEPS = [  # (verb, text, meta)
    ('Kiezen', 'Soort, maat en aantal. Bij elke soort staan alle maten met hun prijs.', ''),
    ('Bestellen', 'Online of per telefoon. U&nbsp;betaalt met iDEAL, per overschrijving of bij ontvangst; zakelijk op factuur.', ''),
    ('Afspreken', 'Samen kiezen we de dag van bezorgen of afhalen, wanneer het u&nbsp;uitkomt.', ''),
    ('Ontvangen', 'Bezorgd of afgehaald. De bezorgkosten hangen af van afstand en aantal; u&nbsp;ziet ze vóór u&nbsp;betaalt.',
     '<p class="hw-m">Afhalen: Esserbroekweg&nbsp;2, Otterlo.</p>'),
]
PAN = '<img src="img/voorbeeld/hw-v3-veld.webp" alt="Voorbeeldfoto: bloeiende rhododendrons op een veld" loading="lazy">'
ROUTE = '<ol class="hw-route">' + ''.join(f'<li><h3>{v}</h3><p>{p}</p>{x}</li>' for v, p, x in STEPS) + '</ol>'
BLOCK = ('<section class="hw" id="hoe" aria-labelledby="h-hoe"><div class="in">'
         '<h2 id="h-hoe" class="hw-h"><span>Van ons veld naar uw tuin,</span> <span>in vier stappen.</span></h2>'
         '<div class="hwd"><div class="hwd-pan">' + PAN + '</div>' + ROUTE + '</div>'
         '<p class="rv-cr">Фото для примера, не наше: «Rhododendronfeld einer Baumschule in Edewecht», JoachimKohler-HB, Wikimedia Commons, CC BY-SA 4.0 '
         '(img/voorbeeld/CREDITS.md). Для сайта нужно своё фото поля.</p>'
         '</div></section>')

PH = '<div class="between"><div class="in"><span>… hier volgt Hoe het werkt: bij de stap «afhalen» staan het adres en de openingstijden …</span></div></div>'
rep(PH, BLOCK)
rep('</head>', '<style id="hoe-werkt-css">' + (D / 'tools' / 'hoe-werkt-d.css').read_text() + '</style>'
    '<style id="fase2b-rv">'
    '.rv-cr{margin-top:14px!important;font-size:13px!important;color:#6b6a64!important}</style></head>')
s = re.sub(r'<title>[^<]*</title>', '<title>Этап 2 · Hoe het werkt, вариант D</title>', s, count=1)
(D / 'fase2b.html').write_text(s)
print('ok', len(s))
