# The hedge calculator ("Haagcalculator"), a homepage block after the assortment. calc_html(n) returns design n;
# apply(html, n) puts it between the assortment and the guarantee block and adds tools/calc.css and tools/calc.js.
#   1 "Смета": the questions on the page, the answer on a paper slip beside them, like a quote
#   2 "Фраза": one sentence in the heading's serif with the three choices set in it; the sum as a second sentence
#   3 "Ряд": the hedge itself drawn to scale (the plants along a metre rule), the choices above it, the sum under it
# Norms and prices are provisional (docs/normen-haag.md; prices of the live site) until the owner confirms them.
import json, pathlib, html as _html

SOORTEN = [  # the order of the assortment cards; prices for 40–60 / 60–80 / 80–100 / 100–120 cm; the colour of the flower
    ('Nova Zembla', [29, 45, 65, 89], '#b3243a'), ('Catawbiense Grandiflorum', [29, 45, 65, 89], '#a58ad6'),
    ("Cunningham’s White", [25, 39, 55, 75], '#fbfaf6'), ('Catawbiense Boursault', [27, 42, 60, 82], '#8a62c4'),
    ('Roseum Elegans', [27, 42, 60, 82], '#c98bd2'), ('Ponticum', [22, 35, 50, 70], '#7d55b8'), ('Ponticum Roseum', [22, 35, 50, 70], '#d98fbd'),
]
SIZES = ['40–60 cm', '60–80 cm', '80–100 cm', '100–120 cm']
WA = 'href="https://wa.me/31620297849" target="_blank" rel="noopener noreferrer"'
DATA = _html.escape(json.dumps([{'n': n, 'p': p, 'c': c} for n, p, c in SOORTEN], ensure_ascii=False), quote=True)


def _len(u, tag='div'):
    return (f'<{tag} class="hc-len">' '<button type="button" data-step="-1" aria-label="Eén meter korter">−</button>'
            f'<input id="{u}-len" data-c="len" type="text" inputmode="decimal" autocomplete="off" value="12" aria-describedby="{u}-lenh">'
            f'<span aria-hidden="true">m</span><button type="button" data-step="1" aria-label="Eén meter langer">+</button></{tag}>')


def _chips(u, kind):
    if kind == 'var':
        items = ''.join(f'<label><input type="radio" name="{u}-var" data-c="var" value="{i}"{" checked" if i == 0 else ""}><span><i style="background:{c}"></i>{n}</span></label>'
                        for i, (n, p, c) in enumerate(SOORTEN))
        return f'<fieldset class="hc-set hc-vars"><legend>Soort</legend><div>{items}</div></fieldset>'
    items = ''.join(f'<label><input type="radio" name="{u}-size" data-c="size" value="{i}"{" checked" if i == 1 else ""}><span><b>{s}</b><em data-p="{i}"></em></span></label>'
                    for i, s in enumerate(SIZES))
    return f'<fieldset class="hc-set hc-sizes"><legend>Hoogte bij levering</legend><div>{items}</div></fieldset>'


def _select(u, kind):
    if kind == 'var':
        return (f'<select id="{u}-var" data-c="var" aria-label="Soort">' + ''.join(f'<option value="{i}">{n}</option>' for i, (n, p, c) in enumerate(SOORTEN)) + '</select>')
    return (f'<select id="{u}-size" data-c="size" aria-label="Hoogte bij levering">' + ''.join(f'<option value="{i}"{" selected" if i == 1 else ""}>{s}</option>' for i, s in enumerate(SIZES)) + '</select>')


def _sub(u):
    return (f'<label class="hc-sub"><input type="checkbox" data-c="sub" checked><span><b>Tuinturf-substraat erbij</b>'
            '<em>1 zak van 40&nbsp;L per plant, € 14,95 per zak. Bij zandgrond of een grote kluit meer.</em></span></label>')


LINES = ('<dl class="hc-lines"><div><dt><span data-o="n"></span> <span data-o="nword"></span> <span data-o="var"></span>, <span data-o="size"></span>'
         '<small><span data-o="each"></span> per plant</small></dt><dd data-o="plants"></dd></div>'
         '<div data-row="sub"><dt><span data-o="bags"></span> <span data-o="bword"></span> Tuinturf-substraat, 40&nbsp;L<small>€ 14,95 per zak</small></dt><dd data-o="bagsum"></dd></div>'
         '<div class="hc-tot"><dt>Totaal</dt><dd data-o="total"></dd></div></dl>')
ADD = ('<div class="hc-act"><button type="button" class="hc-add" data-add>In winkelwagen</button><p class="hc-status" data-o="status" role="status"></p></div>')
NOTES = ('<p class="hc-note">Richtlijn voor één rij: <span data-o="perm"></span>. Dichter planten sluit sneller. Exclusief bezorgkosten; die ziet u vóór u betaalt.</p>'
         '<p class="hc-note">Grotere maten tot 225&nbsp;cm? Vraag een prijs aan via <a ' + WA + '>WhatsApp</a> of bel <a href="tel:+31620104312">06&nbsp;20&nbsp;10&nbsp;43&nbsp;12</a>.</p>')
SAID = '<p class="hc-said" data-o="said" aria-live="polite"></p>'
H2 = '<h2 id="h-haag" class="hc-h"><span>Hoeveel planten</span> <span>voor uw haag?</span></h2>'


def calc_html(n):
    u = f'hc{n}'
    if n == 1:
        body = ('<div class="hc-ask">' + H2 + f'<div class="hc-f"><label class="hc-lab" for="{u}-len">Lengte van de haag</label>' + _len(u)
                + f'<p class="hc-hint" id="{u}-lenh">Van 1 tot 200 meter.</p></div>' + _chips(u, 'var') + _chips(u, 'size') + _sub(u) + '</div>'
                '<div class="hc-slip"><p class="hc-sliph">Uw haag van <span data-o="len"></span>&nbsp;meter</p>' + LINES + ADD + NOTES + '</div>')
    elif n == 2:
        body = (H2 + f'<p class="hc-zin">Voor een haag van <span class="hc-inl">' + _len(u, 'span') + f'<span class="hc-hint" id="{u}-lenh">meter, van 1 tot 200</span></span> meter '
                'van <span class="hc-inl">' + _select(u, 'var') + '</span> in de maat <span class="hc-inl">' + _select(u, 'size') + '</span> '
                'heeft u <b><span data-o="n"></span>&nbsp;<span data-o="nword"></span></b> nodig.</p>'
                '<div class="hc-ans"><p class="hc-sum">Dat is <span data-o="plants"></span> aan planten (<span data-o="each"></span> per plant)'
                '<span data-row="sub"> en <span data-o="bagsum"></span> voor <span data-o="bags"></span>&nbsp;<span data-o="bword"></span> substraat</span>. '
                'Samen <b data-o="total"></b>.</p>' + _sub(u) + ADD + '</div>' + NOTES)
    else:
        body = (H2 + f'<div class="hc-bar"><div class="hc-f"><label class="hc-lab" for="{u}-len">Lengte van de haag</label>' + _len(u)
                + f'<p class="hc-hint" id="{u}-lenh">Van 1 tot 200 meter.</p></div>' + _chips(u, 'var') + _chips(u, 'size') + '</div>'
                '<figure class="hc-row"><div data-draw></div><figcaption>Zo staan ze: <span data-o="perm"></span>. '
                '<span class="hc-rowmore">De tekening toont de eerste meters.</span></figcaption></figure>'
                '<div class="hc-out">' + _sub(u) + LINES + ADD + '</div>' + NOTES)
    return (f'<section class="hc hc{n}" id="haag" aria-labelledby="h-haag" data-soorten="{DATA}"><div class="in">{body}{SAID}</div></section>')


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
