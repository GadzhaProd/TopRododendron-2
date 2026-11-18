# Mockup tool (not site code): fase2c.html = the main mockup with "Hoe het werkt" variant D in three forms, so it no longer
# repeats the guarantee card right above it (owner, 18 Nov). Review bar on <html>:
#   hv-0 the card (fase2b.html) · hv-1 open: the field edge to edge, the heading above it, the steps on the page.
# CSS: tools/hoe-werkt-d.css (shared route and the card) + tools/hoe-werkt-open.css (the open forms).
# The field photo is an example (img/voorbeeld/hw-v3-veld.webp, Wikimedia Commons, see CREDITS.md); the live site needs the
# nursery's own field photo. All Dutch copy is a draft.
# Usage: python3 tools/build_fase2c.py [dir]
import re, pathlib, sys
D = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
s = (D / 'index.html').read_text()
def rep(a, b):
    global s
    assert s.count(a) == 1, (s.count(a), a[:70]); s = s.replace(a, b)

STEPS = [
    ('Kiezen', 'Soort, maat en aantal. Bij elke soort staan alle maten met hun prijs.', ''),
    ('Bestellen', 'Online of per telefoon. U&nbsp;betaalt met iDEAL, per overschrijving of bij ontvangst; zakelijk op factuur.', ''),
    ('Afspreken', 'Samen kiezen we de dag van bezorgen of afhalen, wanneer het u&nbsp;uitkomt.', ''),
    ('Ontvangen', 'Bezorgd of afgehaald. De bezorgkosten hangen af van afstand en aantal; u&nbsp;ziet ze vóór u&nbsp;betaalt.',
     '<p class="hw-m">Afhalen: Esserbroekweg&nbsp;2, Otterlo.</p>'),
]
IMG = '<img src="img/voorbeeld/hw-v3-veld.webp" alt="Voorbeeldfoto: bloeiende rhododendrons op een veld" loading="lazy">'
ROUTE = '<ol class="hw-route">' + ''.join(f'<li><h3>{v}</h3><p>{p}</p>{x}</li>' for v, p, x in STEPS) + '</ol>'
H2 = lambda i: f'<h2 id="{i}" class="hw-h"><span>Van ons veld naar uw tuin,</span> <span>in vier stappen.</span></h2>'
CR = ('<p class="rv-cr">Фото для примера, не наше: «Rhododendronfeld einer Baumschule in Edewecht», JoachimKohler-HB, Wikimedia Commons, '
      'CC BY-SA 4.0 (img/voorbeeld/CREDITS.md). Для сайта нужно своё фото поля.</p>')
CARD = ('<section class="hw hw-card" aria-labelledby="h-hoe-c"><div class="in">' + H2('h-hoe-c')
        + '<div class="hwd"><div class="hwd-pan">' + IMG + '</div>' + ROUTE + '</div>' + CR + '</div></section>')
OPEN = ('<section class="hw hw-open" id="hoe" aria-labelledby="h-hoe"><div class="in hwo-hd">' + H2('h-hoe') + '</div>'
        '<div class="hwo-band">' + IMG + '</div><div class="in hwo-ft">' + ROUTE + CR + '</div></section>')
PH = '<div class="between"><div class="in"><span>… hier volgt Hoe het werkt: bij de stap «afhalen» staan het adres en de openingstijden …</span></div></div>'
rep(PH, CARD + OPEN)
rep('</head>', '<style id="hoe-werkt-css">' + (D / 'tools' / 'hoe-werkt-d.css').read_text() + (D / 'tools' / 'hoe-werkt-open.css').read_text() + '</style>'
    '<style id="fase2c-rv">body{padding-top:48px}header.fixed{top:48px}#hero{min-height:calc(100svh - 48px)}'
    '.rv-cr{margin-top:14px!important;font-size:13px!important;color:#6b6a64!important}</style></head>')
Bt = lambda g, v, t, on: f'<button type="button" data-g="{g}" data-v="{v}" aria-pressed="{"true" if on else "false"}">{t}</button>'
rep('<div id="root">', '<div class="rv" role="group" aria-label="Варианты"><div class="rv-g"><i>Hoe het werkt</i>'
    + Bt('hv', '0', 'Карточка (как было)', 0) + Bt('hv', '1', 'Во всю ширину', 1) + '</div></div><div id="root">')
s = re.sub(r'<html lang="nl" class="([^"]*)">', lambda m: f'<html lang="nl" class="{m.group(1)} hv-1">', s, count=1)
s = re.sub(r'<title>[^<]*</title>', '<title>Этап 2 · Hoe het werkt, D без карточки</title>', s, count=1)
(D / 'fase2c.html').write_text(s)
print('ok', len(s))
