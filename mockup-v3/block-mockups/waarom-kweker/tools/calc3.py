# The hedge calculator «Смета», restyled (the owner kept its structure and asked for new controls and surfaces only).
# The questions on the page, the answer on a sheet that stays beside them; on the phone a small bar with the total.
# calc_html(t) returns the block with control treatment t; apply(html, t) inserts it and adds tools/calc3.css and tools/calc3.js.
#   1 "Пилюли": outlined pills and round buttons, as the page's "Alle maten en prijzen" pill and the header's round buttons
#   2 "Строки": choices as rows on hairlines with a round mark, as the page's hairline lists; no slider, no drawing, no dots
#   3 "Плитки": soft tiles without borders; the selected one turns sage; no slider
# The structure and the logic come from tools/calc.py and tools/calc.js (design 1). Norms and prices are provisional
# (docs/normen-haag.md; prices of the live site) until the owner confirms them.
import json, pathlib, html as _html

SOORTEN = [  # the order of the assortment cards; prices for 40–60 / 60–80 / 80–100 / 100–120 cm; the colour of the flower
    # (the dot and the drawing). Hues from our own photos, spread apart so the three purples and the two pinks differ:
    # Ponticum blue-lavender, Grandiflorum lilac, Boursault orchid, Roseum Elegans mauve-pink, Ponticum Roseum rose.
    ('Nova Zembla', [29, 45, 65, 89], '#b3243a'), ('Catawbiense Grandiflorum', [29, 45, 65, 89], '#b18bd3'),
    ("Cunningham’s White", [25, 39, 55, 75], '#fbfaf6'), ('Catawbiense Boursault', [27, 42, 60, 82], '#a24da6'),
    ('Roseum Elegans', [27, 42, 60, 82], '#cf76ad'), ('Ponticum', [22, 35, 50, 70], '#7c64c1'),
    ('Ponticum Roseum', [22, 35, 50, 70], '#e48da5'),
]
# the glow of a chosen variety chip: the same hue, light and soft, at one lightness (OKLCH), so no colour shouts
GLOW = {'Nova Zembla': '#f2adb4', 'Catawbiense Grandiflorum': '#e1cff2', "Cunningham’s White": '#f8f3e8', 'Catawbiense Boursault': '#dfb9df',
        'Roseum Elegans': '#efc1dc', 'Ponticum': '#cec8ed', 'Ponticum Roseum': '#f8ccd6'}
SIZES = ['40–60 cm', '60–80 cm', '80–100 cm', '100–120 cm']
WA = 'href="https://wa.me/31620297849" target="_blank" rel="noopener noreferrer"'
# for the drawing: the photo of the assortment card (img/<slug>-2-sm.webp, 672 × 900) and where the shrub stands in it,
# as fractions of the photo: left, top, right, bottom
PHOTO = {'Nova Zembla': ('nova-zembla', [.05, .21, .95, .82]), 'Catawbiense Grandiflorum': ('catawbiense-grandiflorum', [.0, .05, 1, 1]),
         "Cunningham’s White": ('cunninghams-white', [.02, .18, .98, .92]), 'Catawbiense Boursault': ('catawbiense-boursault', [.02, .06, .98, .88]),
         'Roseum Elegans': ('roseum-elegans', [.0, .15, 1, .85]), 'Ponticum': ('ponticum', [.03, .08, .97, .88]), 'Ponticum Roseum': ('ponticum-roseum', [.0, .03, 1, 1])}
DATA = _html.escape(json.dumps([{'n': n, 'p': p, 'c': c, 'g': GLOW[n], 'f': PHOTO[n][0], 'b': PHOTO[n][1]} for n, p, c in SOORTEN], ensure_ascii=False), quote=True)


def _step(u, key='len', value='12', what='meter', cls=''):
    # one quiet control: minus, the value with its unit, plus
    return (f'<div class="sx-step {cls}"><button type="button" data-step="-1" data-for="{key}" aria-label="Eén {what} minder"><svg viewBox="0 0 16 16" aria-hidden="true"><path d="M3.5 8h9"/></svg></button>'
            f'<span class="sx-val"><input id="{u}-{key}" data-c="{key}" type="text" inputmode="decimal" autocomplete="off" value="{value}" size="3" aria-describedby="{u}-{key}h"><i aria-hidden="true">m</i></span>'
            f'<button type="button" data-step="1" data-for="{key}" aria-label="Eén {what} meer"><svg viewBox="0 0 16 16" aria-hidden="true"><path d="M3.5 8h9M8 3.5v9"/></svg></button></div>')


def _mode(u):
    # what is being planted: a hedge (plants per metre) or a group or border (plants per square metre)
    return (f'<fieldset class="sx-set sx-mode"><legend>Wat wilt u planten?</legend><div>'
            f'<label><input type="radio" name="{u}-mode" data-c="mode" value="haag" checked><span><b>Haag</b></span></label>'
            f'<label><input type="radio" name="{u}-mode" data-c="mode" value="border"><span><b>Groep of border</b></span></label></div></fieldset>')


def _area(u):
    # a group or border: its shape first. A group (an island bed) is planted round, by its diameter, or oval; a border along
    # a fence or path is straight, length times width. The square metres are shown beside the measures.
    shape = ''.join(f'<label><input type="radio" name="{u}-shape" data-c="shape" value="{v}"{" checked" if v == "rond" else ""}><span><b>{t}</b></span></label>'
                    for v, t in (('rond', 'Rond'), ('ovaal', 'Ovaal'), ('recht', 'Recht')))
    m2 = '<p class="sx-m2">= <b data-o="area"></b>&nbsp;m²</p>'
    return (f'<div class="sx-f sx-area" data-mode="border" hidden><fieldset class="sx-set sx-shape"><legend>Vorm</legend><div>{shape}</div></fieldset>'
            f'<div class="sx-arow" data-shape="rond"><label><span>Doorsnede</span>' + _step(u, 'bd', '3', 'meter doorsnede', 'is-s') + '</label>' + m2 + '</div>'
            f'<div class="sx-arow" data-shape="ovaal recht" role="group" aria-label="Lengte en breedte" hidden><label><span>Lengte</span>' + _step(u, 'bl', '4', 'meter lengte', 'is-s') + '</label>'
            '<b aria-hidden="true">×</b><label><span>Breedte</span>' + _step(u, 'bw', '3', 'meter breedte', 'is-s') + '</label>' + m2 + '</div>'
            f'<p class="sx-hint" id="{u}-blh">Elke maat van 1 tot 50 meter, ook halve meters.</p><span id="{u}-bwh" hidden></span><span id="{u}-bdh" hidden></span></div>')


def _range(u, top=40):
    return (f'<div class="sx-range" data-mode="haag"><input type="range" data-c="range" min="1" max="{top}" step="1" value="12" aria-label="Lengte van de haag in meters, grof instellen"></div>')


def _length(u):
    return (f'<div class="sx-f sx-length" data-mode="haag"><label class="sx-lab" for="{u}-len">Lengte van de haag</label><div class="sx-lenrow">' + _step(u) + _range(u) + '</div>'
            f'<p class="sx-hint" id="{u}-lenh">Van 1 tot 200 meter, ook halve meters.</p></div>' + _area(u))


def _vars(u):
    # --c: the flower's colour, for the dot · --g: its soft glow in the chosen chip
    items = ''.join(f'<label style="--c:{c};--g:{GLOW[n]}"><input type="radio" name="{u}-var" data-c="var" value="{i}"{" checked" if i == 0 else ""}><span><i></i><b>{n}</b></span></label>'
                    for i, (n, p, c) in enumerate(SOORTEN))
    return f'<fieldset class="sx-set sx-vars"><legend>Soort</legend><div>{items}</div></fieldset>'


def _sizes(u):
    items = ''.join(f'<label><input type="radio" name="{u}-size" data-c="size" value="{i}"{" checked" if i == 1 else ""}><span><b>{s}</b><em data-p="{i}"></em></span></label>'
                    for i, s in enumerate(SIZES))
    # what a size class means (owner, 23 Nov: the height is measured from the root ball; the ball does not count)
    note = ('<p class="sx-sizenote" data-o="sizenote">U krijgt planten tussen 60 en 80&nbsp;cm hoog, gemeten vanaf de kluit; '
            'de kluit telt niet mee.</p>')
    return f'<fieldset class="sx-set sx-sizes"><legend>Hoogte bij levering, prijs per plant</legend><div>{items}</div>{note}</fieldset>'


SUB = ('<label class="sx-sub"><input type="checkbox" data-c="sub" checked><span><b>Tuinturf-substraat erbij</b>'
       '<em>1 zak van 40&nbsp;L per plant, € 14,95 per zak. Bij zandgrond of een grote kluit meer.</em></span></label>')
LINES = ('<dl class="sx-lines"><div><dt><span data-o="n"></span> <span data-o="nword"></span><small><span data-o="each"></span> per plant</small></dt><dd data-o="plants"></dd></div>'
         '<div data-row="sub"><dt><span data-o="bags"></span> <span data-o="bword"></span> substraat<small>€ 14,95 per zak van 40&nbsp;L</small></dt><dd data-o="bagsum"></dd></div>'
         '<div class="sx-tot"><dt>Totaal</dt><dd data-o="total"></dd></div></dl>'
         '<p class="sx-totnote">Exclusief bezorgkosten; die ziet u vóór u betaalt.</p>')
ADD = '<div class="sx-act"><button type="button" class="sx-add" data-add>In winkelwagen</button><p class="sx-status" data-o="status" role="status"></p></div>'
BIG = ('<p class="sx-note">Grotere maten, tot 225&nbsp;cm? Vraag een prijs aan via <a ' + WA + '>WhatsApp</a> of bel <a href="tel:+31620104312">06&nbsp;20&nbsp;10&nbsp;43&nbsp;12</a>.</p>')
SAID = '<p class="sx-said" data-o="said" aria-live="polite"></p>'
H2 = '<h2 id="h-haag" class="sx-h"><span>Hoeveel planten</span> <span>voor uw <span data-o="h2">haag</span>?</span></h2>'
# the guideline: under the drawing as its caption, and once more as a plain line for the treatment without a drawing
NORM = '<span data-o="permlead"></span>: <span data-o="perm"></span>. Dichter planten sluit sneller.'
STRIP = ('<figure class="sx-strip"><div data-draw=""></div><figcaption>' + NORM + ' <span data-o="shown"></span></figcaption></figure>'
         '<p class="sx-norm">' + NORM + '</p>')


def _mini(u):
    return (f'<a class="sx-mini" href="#{u}-res"><span><b data-o="total"></b><i><span data-o="n"></span> <span data-o="nword"></span></i></span><em>Bekijk de berekening</em></a>')


def calc_html(t=3, b=1, glow=True, k=3):
    # t: the controls (1 pills, 2 rows, 3 tiles) · b: the cart button (0 moss, 1 olive, 2 sage, 3 glow) · glow: the cards' soft spots or flat · k: the drawn plants (1 the chips' flow, 2 a planting plan in fine lines, 3 the variety's photo)
    u = 'sx'
    body = ('<div class="sx-ask">' + H2 + _mode(u) + _length(u) + _vars(u) + _sizes(u) + SUB + '</div>'
            f'<div class="sx-slip" id="{u}-res" data-res><p class="sx-sliph" data-o="title"></p>'
            '<p class="sx-slips"><span data-o="var"></span>, <span data-o="size"></span></p>' + STRIP + LINES + ADD + BIG + '</div>')
    return (f'<section class="sx sx-t{t} sx-b{b}{"" if glow else " sx-flat"} sx-k{k}" id="haag" aria-labelledby="h-haag" data-soorten="{DATA}"><div class="in">{body}{SAID}</div>{_mini(u)}</section>')


def css():
    return (pathlib.Path(__file__).parent / 'calc3.css').read_text()


def js():
    return (pathlib.Path(__file__).parent / 'calc3.js').read_text()


def place(html, block):
    mark = '<section class="fd fp fp-1" id="kweker"'
    assert html.count(mark) == 1
    return html.replace(mark, block + mark)


def apply(html, t=3, b=1, glow=True):
    html = place(html, calc_html(t, b, glow))
    assert html.count('</head>') == 1 and html.count('</body>') == 1
    return html.replace('</head>', '<style id="calc3-css">' + css() + '</style></head>').replace('</body>', '<script>' + js() + '</script></body>')
