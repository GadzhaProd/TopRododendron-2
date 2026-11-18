# Mockup tool (not site code): fase2b.html = the main mockup with "Hoe het werkt" variant D (owner chose it, 18 Nov),
# refined, in place of the placeholder between the guarantee and the footer. CSS: tools/hoe-werkt-d.css.
# Review bar: the photo set. ps-0 our photos (img/hw-veld.webp, img/hw-tuin.webp) · ps-1 / ps-2 example photos from
# Wikimedia Commons (img/voorbeeld/, see CREDITS.md there): another nursery's field and other gardens, only to see the
# block with other pictures; the live site uses the nursery's own photos. All Dutch copy is a draft.
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
     '<p class="hw-m">Afhalen: Esserbroekweg&nbsp;2, Otterlo. <span class="nb">Ma–vr 08:00–17:00,</span> <span class="nb">za 09:00–13:00.</span></p>'),
]
SETS = [('p0', 'img/hw-veld.webp', 'img/hw-tuin.webp', 'Ons rhododendronveld in Otterlo', 'Een Cunningham&#x27;s White in een tuin'),
        ('p1', 'img/voorbeeld/hw-v1-veld.webp', 'img/voorbeeld/hw-v1-tuin.webp', 'Voorbeeldfoto: een rhododendronveld', 'Voorbeeldfoto: een rhododendron in een tuin'),
        ('p2', 'img/voorbeeld/hw-v2-veld.webp', 'img/voorbeeld/hw-v2-tuin.webp', 'Voorbeeldfoto: een rhododendronveld', 'Voorbeeldfoto: rhododendrons langs een tuinpad')]
PAN = ''.join(f'<img class="hwd-veld {k}" src="{v}" alt="{av}" loading="lazy"><img class="hwd-tuin {k}" src="{t}" alt="{at}" loading="lazy">'
              for k, v, t, av, at in SETS)
ROUTE = '<ol class="hw-route">' + ''.join(f'<li><h3>{v}</h3><p>{p}</p>{x}</li>' for v, p, x in STEPS) + '</ol>'
BLOCK = ('<section class="hw" id="hoe" aria-labelledby="h-hoe"><div class="in">'
         '<h2 id="h-hoe" class="hw-h"><span>Van ons veld naar uw tuin,</span> <span>in vier stappen.</span></h2>'
         '<div class="hwd"><div class="hwd-pan">' + PAN + '</div>' + ROUTE + '</div>'
         '<p class="rv-cr">Фото для примера, не наши: Wikimedia Commons. Набор 1 — JoachimKohler-HB (CC BY-SA 4.0), Daderot (CC0); '
         'набор 2 — JoachimKohler-HB, 8enzone (CC BY-SA 4.0). Подробно: img/voorbeeld/CREDITS.md</p>'
         '</div></section>')

PH = '<div class="between"><div class="in"><span>… hier volgt Hoe het werkt: bij de stap «afhalen» staan het adres en de openingstijden …</span></div></div>'
rep(PH, BLOCK)
rep('</head>', '<style id="hoe-werkt-css">' + (D / 'tools' / 'hoe-werkt-d.css').read_text() + '</style>'
    '<style id="fase2b-rv">body{padding-top:48px}header.fixed{top:48px}#hero{min-height:calc(100svh - 48px)}'
    '.rv-cr{display:none;margin-top:14px!important;font-size:13px!important;color:#6b6a64!important}html:not(.ps-0) .rv-cr{display:block}</style></head>')
Bt = lambda g, v, t, on: f'<button type="button" data-g="{g}" data-v="{v}" aria-pressed="{"true" if on else "false"}">{t}</button>'
rep('<div id="root">', '<div class="rv" role="group" aria-label="Варианты"><div class="rv-g"><i>Фото</i>'
    + Bt('ps', '0', 'Наши', 0) + Bt('ps', '1', 'Пример 1 · торф и розовый', 1) + Bt('ps', '2', 'Пример 2 · ряды и дорожка', 0) + '</div></div><div id="root">')
s = re.sub(r'<html lang="nl" class="([^"]*)">', lambda m: f'<html lang="nl" class="{m.group(1)} ps-1">', s, count=1)
s = re.sub(r'<title>[^<]*</title>', '<title>Этап 2 · Hoe het werkt, вариант D</title>', s, count=1)
(D / 'fase2b.html').write_text(s)
print('ok', len(s))
