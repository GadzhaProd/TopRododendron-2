# The plant calculator of the homepage, between the assortment and the guarantee block: the questions on the page,
# the answer on a sheet that stays beside them; on the phone a small bar with the total while the questions are in view.
# The state the owner chose (23 Nov): soft tiles, compact, the chosen tile with the cards' glow, no dots, no drawing,
# the cart button with the same glow. calc_html() returns the block; apply(html) inserts it with tools/calc3.css and
# tools/calc3.js. Norms and prices are provisional (docs/normen-haag.md; prices of the live site) until the owner confirms them.
import json, pathlib, html as _html

SOORTEN = [  # the order of the assortment cards: name · prices per plant for the four size classes · the range of sizes (cm)
    # The range comes from the assortment cards ("50 tot 180 cm"); the owner confirms it. The first class starts where the
    # card starts (50–60 or 40–60 cm) and keeps the first price, which is the card's "vanaf" price; the classes after it
    # are 60–80, 80–100 and 100–120 cm for every variety. Above 120 cm, up to the card's maximum, the price is on request.
    ('Nova Zembla', [29, 45, 65, 89], (50, 180)), ('Catawbiense Grandiflorum', [29, 45, 65, 89], (50, 225)),
    ("Cunningham’s White", [25, 39, 55, 75], (50, 225)), ('Catawbiense Boursault', [27, 42, 60, 82], (40, 180)),
    ('Roseum Elegans', [27, 42, 60, 82], (50, 225)), ('Ponticum', [22, 35, 50, 70], (50, 120)),
    ('Ponticum Roseum', [22, 35, 50, 70], (40, 160)),
]
# the glow of a chosen variety tile: the flower's hue from our own photos, light and soft, all at one lightness (OKLCH), so
# no colour shouts; the three purples and the two pinks are spread apart
GLOW = {'Nova Zembla': '#f2adb4', 'Catawbiense Grandiflorum': '#e1cff2', "Cunningham’s White": '#f8f3e8', 'Catawbiense Boursault': '#dfb9df',
        'Roseum Elegans': '#efc1dc', 'Ponticum': '#cec8ed', 'Ponticum Roseum': '#f8ccd6'}
TOPS = [60, 80, 100, 120]   # the upper ends of the four size classes; the first class starts at the variety's own minimum
WA = 'href="https://wa.me/31620297849" target="_blank" rel="noopener noreferrer"'
DATA = _html.escape(json.dumps([{'n': n, 'p': p, 'a': r[0], 'm': r[1]} for n, p, r in SOORTEN], ensure_ascii=False), quote=True)
U = 'sx'   # the prefix of the ids and of the radio groups' names


def _tiles(group, items, on, cls, legend, after=''):
    # one choice as a row of tiles: real radio buttons, the label is the control. items: (value, text or markup)
    tiles = ''.join(f'<label{extra}><input type="radio" name="{U}-{group}" data-c="{group}" value="{v}"{" checked" if v == on else ""}><span>{t}</span></label>'
                    for v, t, extra in items)
    return f'<fieldset class="sx-set {cls}"><legend>{legend}</legend><div>{tiles}</div>{after}</fieldset>'


def _step(key, value, name, hint):
    # a measure: minus, the figure with its unit, plus. The field's own label stands outside it (a label round the whole
    # control would make the minus button its target)
    return (f'<div class="sx-step"><button type="button" data-step="-1" data-for="{key}" aria-label="{name}: één meter minder"><svg viewBox="0 0 16 16" aria-hidden="true"><path d="M3.5 8h9"/></svg></button>'
            f'<span class="sx-val"><input id="{U}-{key}" data-c="{key}" type="text" inputmode="decimal" autocomplete="off" value="{value}" aria-describedby="{U}-{hint}"><i aria-hidden="true">m</i></span>'
            f'<button type="button" data-step="1" data-for="{key}" aria-label="{name}: één meter meer"><svg viewBox="0 0 16 16" aria-hidden="true"><path d="M3.5 8h9M8 3.5v9"/></svg></button></div>')


def _field(key, value, name, hint):
    return f'<div class="sx-fld"><label for="{U}-{key}">{name}</label>' + _step(key, value, name, hint) + '</div>'


def _measures():
    # a hedge by its length. A group or border by its shape first: a group (an island bed) is planted round, by its
    # diameter, or oval; a border along a fence or path is a rectangle, length times width. The square metres on a line of their own.
    shape = _tiles('shape', [('rond', '<b>Rond</b>', ''), ('ovaal', '<b>Ovaal</b>', ''), ('recht', '<b>Rechthoekig</b>', '')], 'rond', 'sx-shape', 'Vorm')
    return (f'<div class="sx-f" data-mode="haag"><label class="sx-lab" for="{U}-len">Lengte van de haag</label>' + _step('len', '12', 'Lengte van de haag', 'lenh')
            + f'<p class="sx-hint" id="{U}-lenh">Van 1 tot 200 meter, ook halve meters.</p></div>'
            '<div class="sx-f" data-mode="border" hidden>' + shape
            + '<div class="sx-meas" data-shape="rond">' + _field('bd', '3', 'Doorsnede', 'bedh') + '</div>'
            '<div class="sx-meas" data-shape="ovaal recht" role="group" aria-label="Lengte en breedte" hidden>' + _field('bl', '4', 'Lengte', 'bedh')
            + '<span class="sx-x" aria-hidden="true">×</span>' + _field('bw', '3', 'Breedte', 'bedh') + '</div>'
            f'<p class="sx-m2">= <b data-o="area"></b>&nbsp;m²</p><p class="sx-hint" id="{U}-bedh">Van 1 tot 50 meter, ook halve meters.</p></div>')


def calc_html():
    mode = _tiles('mode', [('haag', '<b>Haag</b>', ''), ('border', '<b>Groep of border</b>', '')], 'haag', 'sx-mode', 'Wat wilt u planten?')
    # --g: the soft colour of the variety's flower, the glow of its tile when chosen
    soort = _tiles('var', [(str(i), f'<b>{n}</b>', f' style="--g:{GLOW[n]}"') for i, (n, p, r) in enumerate(SOORTEN)], '0', 'sx-vars', 'Soort')
    # the size classes: their labels follow the chosen variety (the first class), written here for the first variety.
    # What a class means (owner, 23 Nov): the height is measured from the top of the root ball; the ball does not count
    lo = [SOORTEN[0][2][0]] + TOPS[:-1]
    maat = _tiles('size', [(str(i), f'<b data-s="{i}">{lo[i]}–{t} cm</b><em data-p="{i}"></em>', '') for i, t in enumerate(TOPS)], '1', 'sx-sizes', 'Hoogte bij levering, prijs per plant',
                  '<p class="sx-hint" data-o="sizenote">U krijgt planten van 60 tot 80&nbsp;cm hoog, gemeten vanaf de bovenkant van de kluit.</p>')
    # the substrate as a choice in tiles like the others, so it reads as optional (owner, 23 Nov: a checkbox looked compulsory)
    sub = _tiles('sub', [('1', '<b>Ja, erbij</b>', ''), ('0', '<b>Nee, niet nodig</b>', '')], '1', 'sx-subst', 'Tuinturf-substraat',
                 '<p class="sx-hint">1 zak van 40&nbsp;L per plant, € 14,95 per zak. Bij zandgrond of een grote kluit meer.</p>')
    ask = ('<div class="sx-ask"><h2 id="h-haag" class="sx-h"><span>Hoeveel planten</span> <span>voor uw <span data-o="h2">haag</span>?</span></h2>'
           '<p class="sx-lead">Vul de maten in en kies soort en hoogte. U ziet meteen hoeveel planten u nodig heeft en wat het kost.</p>'
           + mode + _measures() + soort + maat + sub + '</div>')
    # the sheet: no drawing (owner, 23 Nov: what counts is the number); the guideline is one line. The line about larger
    # sizes names the variety's own maximum and is left out where the classes already reach it
    slip = (f'<div class="sx-slip" id="{U}-res" data-res><p class="sx-sliph" data-o="title"></p>'
            '<p class="sx-slips"><span data-o="var"></span>, <span data-o="size"></span></p>'
            '<p class="sx-norm"><span data-o="permlead"></span>: <span data-o="perm"></span>. <span data-o="dense"></span></p>'
            '<dl class="sx-lines"><div><dt><span data-o="n"></span> <span data-o="nword"></span><small><span data-o="each"></span> per plant</small></dt><dd data-o="plants"></dd></div>'
            '<div data-row="sub"><dt><span data-o="bags"></span> <span data-o="bword"></span> substraat<small>€ 14,95 per zak van 40&nbsp;L</small></dt><dd data-o="bagsum"></dd></div>'
            '<div class="sx-tot"><dt>Totaal</dt><dd data-o="total"></dd></div></dl>'
            '<p class="sx-totnote">Exclusief bezorgkosten; die ziet u vóór u betaalt.</p>'
            '<button type="button" class="sx-add" data-add>In winkelwagen</button><p class="sx-status" data-o="status" role="status"></p>'
            '<p class="sx-note" data-row="big">Grotere maten, tot <span data-o="max"></span>&nbsp;cm? Vraag een prijs aan via <a ' + WA + '>WhatsApp</a> of bel <a href="tel:+31620104312">06&nbsp;20&nbsp;10&nbsp;43&nbsp;12</a>.</p></div>')
    mini = (f'<a class="sx-mini" href="#{U}-res"><span><b data-o="total"></b><i><span data-o="n"></span> <span data-o="nword"></span></i></span><em>Bekijk de berekening</em></a>')
    return (f'<section class="sx" id="haag" aria-labelledby="h-haag" data-soorten="{DATA}"><div class="in">{ask}{slip}'
            f'<p class="sx-said" data-o="said" aria-live="polite"></p></div>{mini}</section>')


def css():
    return (pathlib.Path(__file__).parent / 'calc3.css').read_text()


def js():
    return (pathlib.Path(__file__).parent / 'calc3.js').read_text()


def place(html, block):
    mark = '<section class="fd fp fp-1" id="kweker"'
    assert html.count(mark) == 1
    return html.replace(mark, block + mark)


def apply(html):
    html = place(html, calc_html())
    assert html.count('</head>') == 1 and html.count('</body>') == 1
    return html.replace('</head>', '<style id="calc3-css">' + css() + '</style></head>').replace('</body>', '<script>' + js() + '</script></body>')
