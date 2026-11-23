# The hedge calculator ("Haagcalculator"), a homepage block after the assortment. calc_html(n) returns design n;
# apply(html, n) puts it between the assortment and the guarantee block and adds tools/calc.css and tools/calc.js.
#   1 "Смета": the questions on the page, the answer on a paper slip that stays beside them (owner chose it; refined)
#   2 "Линейка": the hedge drawn to scale on a metre rule, the length set by a slider under it; the sum in one row
#   3 "Фото и итог": the variety chosen from its photo; the answer in a moss panel with one large figure
# Norms and prices are provisional (docs/normen-haag.md; prices of the live site) until the owner confirms them.
import json, pathlib, html as _html

SOORTEN = [  # the order of the assortment cards; prices for 40–60 / 60–80 / 80–100 / 100–120 cm; the colour of the flower; the photo
    ('Nova Zembla', [29, 45, 65, 89], '#b3243a', 'nova-zembla'), ('Catawbiense Grandiflorum', [29, 45, 65, 89], '#a58ad6', 'catawbiense-grandiflorum'),
    ("Cunningham’s White", [25, 39, 55, 75], '#fbfaf6', 'cunninghams-white'), ('Catawbiense Boursault', [27, 42, 60, 82], '#8a62c4', 'catawbiense-boursault'),
    ('Roseum Elegans', [27, 42, 60, 82], '#c98bd2', 'roseum-elegans'), ('Ponticum', [22, 35, 50, 70], '#7d55b8', 'ponticum'),
    ('Ponticum Roseum', [22, 35, 50, 70], '#d98fbd', 'ponticum-roseum'),
]
SIZES = ['40–60 cm', '60–80 cm', '80–100 cm', '100–120 cm']
WA = 'href="https://wa.me/31620297849" target="_blank" rel="noopener noreferrer"'
DATA = _html.escape(json.dumps([{'n': n, 'p': p, 'c': c} for n, p, c, f in SOORTEN], ensure_ascii=False), quote=True)


def _step(u):
    # one quiet control: minus, the value with its unit, plus
    return ('<div class="hc-step"><button type="button" data-step="-1" aria-label="Eén meter korter"><svg viewBox="0 0 16 16" aria-hidden="true"><path d="M3.5 8h9"/></svg></button>'
            f'<span class="hc-val"><input id="{u}-len" data-c="len" type="text" inputmode="decimal" autocomplete="off" value="12" size="3" aria-describedby="{u}-lenh"><i aria-hidden="true">m</i></span>'
            '<button type="button" data-step="1" aria-label="Eén meter langer"><svg viewBox="0 0 16 16" aria-hidden="true"><path d="M3.5 8h9M8 3.5v9"/></svg></button></div>')


def _range(u, top=40):
    return (f'<div class="hc-range"><input type="range" data-c="range" min="1" max="{top}" step="1" value="12" aria-label="Lengte van de haag in meters, grof instellen">'
            f'<p aria-hidden="true"><span>1 m</span><span>{top} m</span></p></div>')


def _length(u, slider=True):
    return (f'<div class="hc-f hc-length"><label class="hc-lab" for="{u}-len">Lengte van de haag</label><div class="hc-lenrow">' + _step(u) + (_range(u) if slider else '') + '</div>'
            f'<p class="hc-hint" id="{u}-lenh">Van 1 tot 200 meter, ook halve meters.</p></div>')


def _vars(u, photos=False):
    if photos:
        items = ''.join(f'<label><input type="radio" name="{u}-var" data-c="var" value="{i}"{" checked" if i == 0 else ""}>'
                        f'<span><img src="img/{f}-2-sm.webp" alt="" loading="lazy"><b><i style="background:{c}"></i>{n}</b></span></label>' for i, (n, p, c, f) in enumerate(SOORTEN))
        return f'<fieldset class="hc-set hc-photos"><legend>Soort</legend><div>{items}</div></fieldset>'
    items = ''.join(f'<label><input type="radio" name="{u}-var" data-c="var" value="{i}"{" checked" if i == 0 else ""}><span><i style="background:{c}"></i>{n}</span></label>'
                    for i, (n, p, c, f) in enumerate(SOORTEN))
    return f'<fieldset class="hc-set hc-vars"><legend>Soort</legend><div>{items}</div></fieldset>'


def _sizes(u):
    items = ''.join(f'<label><input type="radio" name="{u}-size" data-c="size" value="{i}"{" checked" if i == 1 else ""}><span><b>{s}</b><em data-p="{i}"></em></span></label>'
                    for i, s in enumerate(SIZES))
    # what a size class means (owner, 23 Nov: the height is measured from the root ball; the ball does not count)
    note = ('<p class="hc-sizenote" data-o="sizenote">U krijgt planten tussen 60 en 80&nbsp;cm hoog, gemeten vanaf de kluit; '
            'de kluit telt niet mee.</p>')
    return f'<fieldset class="hc-set hc-sizes"><legend>Hoogte bij levering <small>prijs per plant</small></legend><div>{items}</div>{note}</fieldset>'


SUB = ('<label class="hc-sub"><input type="checkbox" data-c="sub" checked><span><b>Tuinturf-substraat erbij</b>'
       '<em>1 zak van 40&nbsp;L per plant, € 14,95 per zak. Bij zandgrond of een grote kluit meer.</em></span></label>')
LINES = ('<dl class="hc-lines"><div><dt><span data-o="n"></span> <span data-o="nword"></span><small><span data-o="each"></span> per plant</small></dt><dd data-o="plants"></dd></div>'
         '<div data-row="sub"><dt><span data-o="bags"></span> <span data-o="bword"></span> substraat<small>€ 14,95 per zak van 40&nbsp;L</small></dt><dd data-o="bagsum"></dd></div>'
         '<div class="hc-del"><dt>Bezorgen</dt><dd>ziet u vóór u betaalt</dd></div>'
         '<div class="hc-tot"><dt>Totaal<small>exclusief bezorgkosten</small></dt><dd data-o="total"></dd></div></dl>')
ADD = '<div class="hc-act"><button type="button" class="hc-add" data-add>In winkelwagen</button><p class="hc-status" data-o="status" role="status"></p></div>'
BIG = ('<p class="hc-note">Grotere maten, tot 225&nbsp;cm? Vraag een prijs aan via <a ' + WA + '>WhatsApp</a> of bel <a href="tel:+31620104312">06&nbsp;20&nbsp;10&nbsp;43&nbsp;12</a>.</p>')
SAID = '<p class="hc-said" data-o="said" aria-live="polite"></p>'
H2 = '<h2 id="h-haag" class="hc-h"><span>Hoeveel planten</span> <span>voor uw haag?</span></h2>'


def _strip(mode=''):
    return (f'<figure class="hc-strip"><div data-draw="{mode}"></div><figcaption>Richtlijn voor één rij: <span data-o="perm"></span>. Dichter planten sluit sneller. '
            '<span data-o="shown"></span></figcaption></figure>')


def _mini(u):
    return (f'<a class="hc-mini" href="#{u}-res"><span><b data-o="total"></b><i><span data-o="n"></span> <span data-o="nword"></span></i></span><em>Bekijk de berekening</em></a>')


def calc_html(n):
    u = f'hc{n}'
    if n == 1:
        body = ('<div class="hc-ask">' + H2 + _length(u) + _vars(u) + _sizes(u) + SUB + '</div>'
                f'<div class="hc-slip" id="{u}-res" data-res><p class="hc-sliph">Uw haag van <span data-o="len"></span>&nbsp;meter</p>'
                '<p class="hc-slips"><span data-o="var"></span>, <span data-o="size"></span></p>' + _strip() + LINES + ADD + BIG + '</div>')
    elif n == 2:
        body = (H2 + '<div class="hc-field">' + f'<div class="hc-fhead"><label class="hc-lab" for="{u}-len">Lengte van de haag</label>' + _step(u)
                + f'<p class="hc-hint" id="{u}-lenh">Van 1 tot 200 meter, ook halve meters.</p></div>' + _strip('fit').replace('<figcaption>', _range(u) + '<figcaption>') + '</div>'
                '<div class="hc-pick">' + _vars(u) + _sizes(u) + '</div>'
                f'<div class="hc-out" id="{u}-res" data-res>' + LINES + '<div class="hc-side">' + SUB + ADD + '</div></div>' + BIG)
    else:
        body = ('<div class="hc-ask">' + H2 + _vars(u, True) + '<div class="hc-two">' + _length(u, False) + _sizes(u) + '</div>' + SUB + '</div>'
                f'<div class="hc-panel" id="{u}-res" data-res><p class="hc-pk">U heeft nodig</p><p class="hc-big"><b data-o="n"></b> <span data-o="nword"></span></p>'
                '<p class="hc-pv"><span data-o="var"></span>, <span data-o="size"></span>, voor <span data-o="len"></span>&nbsp;meter. <span data-o="perm"></span>.</p>'
                + LINES + ADD + BIG + '</div>')
    return (f'<section class="hc hc{n}" id="haag" aria-labelledby="h-haag" data-soorten="{DATA}"><div class="in">{body}{SAID}</div>{_mini(u)}</section>')


def css():
    return (pathlib.Path(__file__).parent / 'calc.css').read_text()


def js():
    return (pathlib.Path(__file__).parent / 'calc.js').read_text()


def place(html, block):
    mark = '<section class="fd fp fp-1" id="kweker"'
    assert html.count(mark) == 1
    return html.replace(mark, block + mark)


def apply(html, n=1):
    html = place(html, calc_html(n))
    assert html.count('</head>') == 1 and html.count('</body>') == 1
    return html.replace('</head>', '<style id="calc-css">' + css() + '</style></head>').replace('</body>', '<script>' + js() + '</script></body>')
