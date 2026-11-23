# The plant calculator, second take ("Rekenhulp"), a homepage block between the assortment and the guarantee.
# calc_html(d) returns one direction; apply(html, d) inserts it and adds tools/calc2.css and tools/calc2.js.
#   'a' "Фраза": the calculator is one sentence in the heading type; the underlined words are the controls,
#       the answer stands inside the sentence, the sum sits beside it on hairlines. No boxes, no surface.
#   'b' "Сорт и строки": the photo of the chosen variety, four quiet rows on hairlines, the answer as one large figure.
# Both use the page's own means only: the serif heading type, hairlines, one moss button, underlined words, a photo.
# Norms and prices are provisional (docs/normen-haag.md; prices of the live site) until the owner confirms them.
import json, pathlib, html as _html

SOORTEN = [  # the order of the assortment cards: name, prices for the four sizes, the flower colour, the photo, its crop
    ('Nova Zembla', [29, 45, 65, 89], '#b3243a', 'nova-zembla', '50% 70%'),
    ('Catawbiense Grandiflorum', [29, 45, 65, 89], '#a58ad6', 'catawbiense-grandiflorum', '50% 50%'),
    ('Cunningham’s White', [25, 39, 55, 75], '#fbfaf6', 'cunninghams-white', '50% 50%'),
    ('Catawbiense Boursault', [27, 42, 60, 82], '#8a62c4', 'catawbiense-boursault', '50% 50%'),
    ('Roseum Elegans', [27, 42, 60, 82], '#c98bd2', 'roseum-elegans', '50% 50%'),
    ('Ponticum', [22, 35, 50, 70], '#7d55b8', 'ponticum', '50% 50%'),
    ('Ponticum Roseum', [22, 35, 50, 70], '#d98fbd', 'ponticum-roseum', '50% 50%'),
]
SIZES = ['40–60 cm', '60–80 cm', '80–100 cm', '100–120 cm']
WA = 'href="https://wa.me/31620297849" target="_blank" rel="noopener noreferrer"'
DATA = _html.escape(json.dumps([{'n': n, 'p': p, 'c': c, 'f': f, 'o': o} for n, p, c, f, o in SOORTEN], ensure_ascii=False), quote=True)
NOTE = 'U krijgt planten tussen 60 en 80&nbsp;cm hoog, gemeten vanaf de kluit; de kluit telt niet mee.'
BIG = ('<p class="pc-note">Grotere maten tot 225&nbsp;cm? Vraag een prijs aan via <a ' + WA + '>WhatsApp</a> of bel '
       '<a href="tel:+31620104312">06&nbsp;20&nbsp;10&nbsp;43&nbsp;12</a>.</p>')
ADD = '<button type="button" class="pc-add" data-add>In winkelwagen</button><p class="pc-status" data-o="status" role="status"></p>'
SAID = '<p class="pc-said" data-o="said" aria-live="polite"></p>'
MINUS = '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M3.5 8h9"/></svg>'
PLUS = '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M3.5 8h9M8 3.5v9"/></svg>'


def _opt(u, group, value, text, on=False, extra='', dot=''):
    # one choice written as a word: a real radio button, the chosen one is underlined
    return (f'<label class="pc-o"><input type="radio" name="{u}-{group}" data-c="{group}" value="{value}"{" checked" if on else ""}>'
            f'<span>{dot}<b data-t="{text}">{text}</b>{extra}</span></label>')


def _modes(u):
    return _opt(u, 'mode', 'haag', 'Haag', True) + _opt(u, 'mode', 'border', 'Groep of border')


def _sizes(u):
    return ''.join(_opt(u, 'size', i, s, i == 1, f'<em data-p="{i}"></em>') for i, s in enumerate(SIZES))


def _num(u, key, value, label):
    return f'<input id="{u}-{key}" class="pc-n" data-c="{key}" type="text" inputmode="decimal" autocomplete="off" value="{value}" aria-label="{label}">'


def _a(u):
    word = lambda key, inner: (f'<button type="button" class="pc-w" data-open="{key}" aria-expanded="false" aria-controls="{u}-p-{key}">{inner}</button>')
    zin = ('<p class="pc-zin">Voor een ' + word('mode', '<span data-o="modeword">haag</span>') + ' van '
           '<span data-mode="haag">' + _num(u, 'len', '12', 'Lengte van de haag in meters') + '</span>'
           '<span data-mode="border" hidden>' + _num(u, 'bl', '4', 'Lengte van de border in meters') + ' bij ' + _num(u, 'bw', '3', 'Breedte van de border in meters') + '</span>'
           ' meter met ' + word('var', '<i class="pc-dot" data-dot aria-hidden="true"></i><span data-o="var">Nova Zembla</span>') + ' van '
           + word('size', '<span data-o="size">60–80 cm</span>') + ' heeft u <strong class="pc-ans"><span data-o="n">18</span> <span data-o="nword">planten</span></strong> nodig.</p>')
    vars_ = ''.join(_opt(u, 'var', i, n, i == 0, dot=f'<i class="pc-dot" style="background:{c}" aria-hidden="true"></i>') for i, (n, p, c, f, o) in enumerate(SOORTEN))
    panels = (f'<fieldset class="pc-p" id="{u}-p-mode" data-panel="mode" hidden><legend>Wat wilt u planten?</legend><div class="pc-os">' + _modes(u) + '</div></fieldset>'
              f'<fieldset class="pc-p" id="{u}-p-var" data-panel="var" hidden><legend>Welke soort?</legend><div class="pc-os pc-os-var">' + vars_ + '</div></fieldset>'
              f'<fieldset class="pc-p" id="{u}-p-size" data-panel="size" hidden><legend>Hoe hoog bij levering?</legend><div class="pc-os pc-os-size">' + _sizes(u) + '</div>'
              '<p class="pc-sizenote" data-o="sizenote">' + NOTE + '</p></fieldset>')
    tip = '<p class="pc-tip" data-o="tip">Kies een onderstreept woord om het aan te passen.</p>'
    lines = ('<dl class="pc-lines">'
             '<div><dt><span data-o="n"></span> <span data-o="nword"></span><small><span data-o="each"></span> per plant · <span data-o="perm"></span></small></dt><dd data-o="plants"></dd></div>'
             '<div><dt><label class="pc-chk"><input type="checkbox" data-c="sub" checked><span>Tuinturf-substraat erbij</span></label>'
             '<small>1 zak van 40&nbsp;L per plant, € 14,95 per zak</small></dt><dd data-o="bagsum"></dd></div>'
             '<div class="pc-tot"><dt>Totaal<small>exclusief bezorgkosten; die ziet u vóór u betaalt</small></dt><dd data-o="total"></dd></div></dl>')
    return ('<h2 id="h-rekenhulp" class="pc-h">Hoeveel planten heeft u nodig?</h2>'
            '<div class="pc-say">' + zin + tip + panels + '</div>'
            f'<div class="pc-sum" id="{u}-res" data-res>' + lines + ADD + BIG + '</div>')


def _step(u, key, value, what, label):
    return (f'<span class="pc-step"><button type="button" data-step="-1" data-for="{key}" aria-label="Eén {what} minder">{MINUS}</button>'
            f'<span class="pc-val">' + _num(u, key, value, label) + '<i aria-hidden="true">m</i></span>'
            f'<button type="button" data-step="1" data-for="{key}" aria-label="Eén {what} meer">{PLUS}</button></span>')


def _b(u):
    n0, p0, c0, f0, o0 = SOORTEN[0]
    photo = (f'<figure class="pc-ph"><img data-photo src="img/{f0}-2-sm.webp" alt="" loading="lazy" style="object-position:{o0}"></figure>')
    opts = ''.join(f'<option value="{i}"{" selected" if i == 0 else ""}>{n}</option>' for i, (n, p, c, f, o) in enumerate(SOORTEN))
    rows = ('<div class="pc-rows">'
            f'<fieldset class="pc-r"><legend>Wat plant u?</legend><div class="pc-os">' + _modes(u) + '</div></fieldset>'
            f'<div class="pc-r" data-mode="haag"><label class="pc-l" for="{u}-len">Lengte</label>' + _step(u, 'len', '12', 'meter', 'Lengte van de haag in meters') + '</div>'
            f'<div class="pc-r" data-mode="border" hidden role="group" aria-labelledby="{u}-arl"><p class="pc-l" id="{u}-arl">Lengte × breedte</p><div class="pc-two">'
            + _step(u, 'bl', '4', 'meter lengte', 'Lengte van de border in meters') + '<span class="pc-x" aria-hidden="true">×</span>' + _step(u, 'bw', '3', 'meter breedte', 'Breedte van de border in meters')
            + '</div></div>'
            f'<div class="pc-r"><label class="pc-l" for="{u}-var">Soort</label><span class="pc-sel"><select id="{u}-var" data-c="var">{opts}</select>'
            '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M4 6.5l4 4 4-4"/></svg></span></div>'
            '<fieldset class="pc-r"><legend>Hoogte bij levering</legend><div class="pc-os pc-os-size">' + _sizes(u) + '</div>'
            '<p class="pc-sizenote" data-o="sizenote">' + NOTE + '</p></fieldset></div>')
    out = (f'<div class="pc-out" id="{u}-res" data-res><p class="pc-big"><b data-o="n">18</b> <span data-o="nword">planten</span></p>'
           '<p class="pc-norm"><span data-o="var"></span>, <span data-o="size"></span>. Richtlijn: <span data-o="perm"></span>.</p>'
           '<dl class="pc-lines"><div><dt>Planten<small><span data-o="n"></span> × <span data-o="each"></span></small></dt><dd data-o="plants"></dd></div>'
           '<div><dt><label class="pc-chk"><input type="checkbox" data-c="sub" checked><span>Tuinturf-substraat erbij</span></label>'
           '<small>1 zak van 40&nbsp;L per plant, € 14,95 per zak</small></dt><dd data-o="bagsum"></dd></div>'
           '<div class="pc-tot"><dt>Totaal<small>exclusief bezorgkosten; die ziet u vóór u betaalt</small></dt><dd data-o="total"></dd></div></dl>'
           + ADD + BIG + '</div>')
    return '<h2 id="h-rekenhulp" class="pc-h">Hoeveel planten heeft u nodig?</h2><div class="pc-grid">' + photo + rows + out + '</div>'


def calc_html(d):
    u = f'pc{d}'
    body = _a(u) if d == 'a' else _b(u)
    return f'<section class="pc pc-{d}" id="rekenhulp" aria-labelledby="h-rekenhulp" data-soorten="{DATA}"><div class="in">{body}{SAID}</div></section>'


def css():
    return (pathlib.Path(__file__).parent / 'calc2.css').read_text()


def js():
    return (pathlib.Path(__file__).parent / 'calc2.js').read_text()


def place(html, block):
    mark = '<section class="fd fp fp-1" id="kweker"'
    assert html.count(mark) == 1
    return html.replace(mark, block + mark)


def apply(html, d='a'):
    html = place(html, calc_html(d))
    assert html.count('</head>') == 1 and html.count('</body>') == 1
    return html.replace('</head>', '<style id="calc2-css">' + css() + '</style></head>').replace('</body>', '<script>' + js() + '</script></body>')
