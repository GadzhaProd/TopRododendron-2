# Mockup tool (not site code): the product page of a variety, the page behind a card of the assortment. Three directions
# for review (tools/build_soort_fable.py -> soort-fable.html):
#   a  "Тихая страница"   the two photos on the left, everything else in one calm column on the page, no card at all
#   b  "Диптих и лист"    the name and the two photos side by side first, then the order as on the calculator: the
#                         questions on the page, the answer on a sheet that stays beside them
#   c  "Карточка сорта"   one card in the soft colour of the variety's own flower: the photo and the order together
# The language is the calculator's (tools/calc3.css): soft tiles without borders, the chosen tile glows, the cart button
# with the same glow, hairline rows, the total in Newsreader. Prices, size classes and glow colours are read from calc3.py.
# The variety is chosen by the hash (soort-fable.html#ponticum); tools/soort.js fills the slots marked data-o.
# Copy: DRAFT. The texts and the "kenmerken" come from the live site (rhododendrons/lib/products.ts), rewritten without the
# claims we cannot verify; the owner confirms them.
import json, pathlib, html as _html
import calc3

WA = 'href="https://wa.me/31620297849" target="_blank" rel="noopener noreferrer"'
TEL = '<a href="tel:+31620104312">06&nbsp;20&nbsp;10&nbsp;43&nbsp;12</a>'
KEN = ['Kleur', 'Bloei', 'Standplaats', 'Hoogte, volgroeid', 'Breedte, volgroeid', 'Groei', 'Winterhard', 'Blad', 'Grond']
GROND = 'Zure, losse grond (pH 4,5–6)'
# slug: the facts line · the short description · "Over" · the kenmerken (in the order of KEN, without the last two, which are
# the same for all) · the focus of the bush photo on a card (as on the homepage)
TEXT = {
    'nova-zembla': (['Mei – juni', 'tot 3 m', 'Halfschaduw', 'Winterhard'],
        'Helderrode bloemtrossen in mei en juni, op een stevige, groenblijvende struik.',
        'Nova Zembla is een van de bekendste rode rhododendrons. De helderrode bloemtrossen verschijnen in mei en juni boven donkergroen blad. '
        'De struik is winterhard en geschikt als solitair, in een groep of als haag. Hij staat het liefst in halfschaduw en verdraagt ook zon, zolang de grond niet uitdroogt.',
        ['Helderrood', 'Mei – juni', 'Halfschaduw, verdraagt ook zon', 'tot 3 m', 'tot 2,5 m', 'Matig', 'Ja (zone 5)'], '50% 70%'),
    'catawbiense-grandiflorum': (['Mei – juni', 'tot 3 m', 'Halfschaduw of zon', 'Winterhard'],
        'Lila-roze bloemtrossen in mei en juni. De soort voor een hoge haag of een grote tuin.',
        'Catawbiense Grandiflorum is een van de grootste soorten die wij kweken: volgroeid tot ongeveer 3 meter hoog en breed. In mei en juni draagt hij lila-roze bloemtrossen. '
        'Door zijn formaat is hij geschikt voor een hoge haag, een groenblijvende afscherming of een grote groep. Winterhard, voor halfschaduw of zon.',
        ['Lila-roze', 'Mei – juni', 'Halfschaduw, verdraagt ook zon', 'tot 3 m', 'tot 3 m', 'Matig tot snel', 'Ja (zone 5)'], '50% 50%'),
    'cunninghams-white': (['April – mei', 'tot 2 m', 'Halfschaduw', 'Winterhard'],
        'Witte bloemen met een lichtroze tint, al in april en mei: de vroegste bloeier van ons assortiment.',
        'Cunningham’s White bloeit als eerste van onze zeven soorten, in april en mei. De bloemen zijn wit met een lichtroze tint. '
        'De struik groeit langzaam en blijft vol en compact, volgroeid tot ongeveer 2 meter. Geschikt als solitair, in een groep of als haag, in halfschaduw. Winterhard.',
        ['Wit met een lichtroze tint', 'April – mei', 'Halfschaduw', 'tot 2 m', 'tot 2 m', 'Langzaam', 'Ja (zone 4)'], '50% 40%'),
    'catawbiense-boursault': (['Mei – juni', 'tot 2,5 m', 'Halfschaduw of zon', 'Winterhard'],
        'Paars-lavendelkleurige bloemen in mei en juni, op een compacte, goed vertakte struik.',
        'Catawbiense Boursault bloeit in mei en juni met paars-lavendelkleurige bloemtrossen. De struik blijft compact en vertakt goed, volgroeid tot ongeveer 2,5 meter. '
        'Hij is winterhard en staat in halfschaduw of op een zonnigere plek. Geschikt als solitair, in een groep of als haag.',
        ['Paars-lavendel', 'Mei – juni', 'Halfschaduw, verdraagt ook zon', 'tot 2,5 m', 'tot 2,5 m', 'Matig', 'Ja (zone 5)'], '50% 50%'),
    'roseum-elegans': (['Mei – juni', 'tot 2,5 m', 'Halfschaduw of zon', 'Winterhard'],
        'Warmroze bloemtrossen in mei en juni, op een brede, krachtige struik.',
        'Roseum Elegans bloeit in mei en juni met warmroze tot lavendelroze bloemtrossen. De struik groeit krachtig en breed uit, volgroeid tot ongeveer 2,5 meter hoog en breed. '
        'Hij is winterhard en verdraagt naast halfschaduw ook zon. Geschikt als solitair of als haag in een ruimere tuin.',
        ['Warmroze tot lavendelroze', 'Mei – juni', 'Halfschaduw, verdraagt ook zon', 'tot 2,5 m', 'tot 2,5 m', 'Matig tot snel', 'Ja (zone 5)'], '50% 60%'),
    'ponticum': (['Mei – juni', 'tot 4 m', 'Halfschaduw of schaduw', 'Winterhard'],
        'Violetpaarse bloemen in mei en juni, op een snelgroeiende struik voor halfschaduw en schaduw.',
        'Ponticum bloeit in mei en juni met violetpaarse bloemen. Het is een snelgroeiende soort die op den duur tot 4 meter hoog en breed kan worden. '
        'Geschikt voor een grote tuin of een hoge, groenblijvende afscherming, in halfschaduw of schaduw. Winterhard.',
        ['Violetpaars', 'Mei – juni', 'Halfschaduw of schaduw', 'tot 4 m', 'tot 4 m', 'Snel', 'Ja (zone 5)'], '50% 50%'),
    'ponticum-roseum': (['Mei – juni', 'tot 4 m', 'Halfschaduw of schaduw', 'Winterhard'],
        'Roze tot lichtpaarse bloemen in mei en juni, op een snelgroeiende struik.',
        'Ponticum Roseum bloeit in mei en juni met roze tot lichtpaarse bloemen. De struik groeit snel en kan op den duur tot 4 meter hoog worden. '
        'Daardoor is hij geschikt voor een hoge haag of een groenblijvende afscherming. Hij staat in halfschaduw of schaduw en is winterhard.',
        ['Roze tot lichtpaars', 'Mei – juni', 'Halfschaduw of schaduw', 'tot 4 m', 'tot 3,5 m', 'Snel', 'Ja (zone 5)'], '50% 50%'),
}
# a2: "Over" in two sentences (what it looks like, what it is for); the months, the height and the position are in the facts line
OVER2 = {
    'nova-zembla': 'Een van de bekendste rode rhododendrons: helderrode bloemtrossen boven donkergroen, groenblijvend blad. Voor solitair, groep of haag.',
    'catawbiense-grandiflorum': 'Een van de grootste soorten die wij kweken, met lila-roze bloemtrossen en groenblijvend blad. Geschikt voor een hoge haag, een afscherming of een grote groep.',
    'cunninghams-white': 'De vroegste bloeier van ons assortiment: witte bloemen met een lichtroze tint, al in april. Een volle, compacte, groenblijvende struik voor solitair, groep of haag.',
    'catawbiense-boursault': 'Paars-lavendelkleurige bloemtrossen op een compacte, goed vertakte, groenblijvende struik. Voor solitair, groep of haag.',
    'roseum-elegans': 'Warmroze tot lavendelroze bloemtrossen op een brede, krachtige, groenblijvende struik. Geschikt als solitair of als haag in een ruimere tuin.',
    'ponticum': 'Violetpaarse bloemen op een snelgroeiende, groenblijvende struik. Geschikt voor een grote tuin of een hoge afscherming, ook in de schaduw.',
    'ponticum-roseum': 'Roze tot lichtpaarse bloemen op een snelgroeiende, groenblijvende struik. Geschikt voor een hoge haag of een afscherming.',
}
SLUGS = ['nova-zembla', 'catawbiense-grandiflorum', 'cunninghams-white', 'catawbiense-boursault', 'roseum-elegans', 'ponticum', 'ponticum-roseum']
# the widths of the photos: img/<slug>-sm.webp, img/<slug>-lg.webp (the flower) and the same with "-2" (the bush). The
# "-lg" files are copies of rhododendrons/public/images, at most 1344 px wide, made for this page (24 Nov)
W = {'nova-zembla': ((900, 1024), (672, 896)), 'roseum-elegans': ((900, 1024), (900, 1024)), 'ponticum': ((600, 1024), (672, 1344))}
SOORTEN = []
for slug, (name, prices, rng) in zip(SLUGS, calc3.SOORTEN):
    f, d, o, k, pos = TEXT[slug]
    SOORTEN.append({'slug': slug, 'n': name, 'p': prices, 'a': rng[0], 'm': rng[1], 'g': calc3.GLOW[name], 'f': f, 'd': d, 'o': o, 'o2': OVER2[slug],
                    'k': k + ['Groenblijvend', GROND],
                    'k2': [k[3] + ' hoog, ' + k[4].replace('tot ', '') + ' breed', k[5], k[6], 'Zuur en los, pH 4,5–6'], 'w': W.get(slug, ((672, 1344), (672, 1344))), 'pos': pos})
DATA = _html.escape(json.dumps(SOORTEN, ensure_ascii=False), quote=True)
MINUS = '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M3.5 8h9"/></svg>'
PLUS = '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M3.5 8h9M8 3.5v9"/></svg>'


def _tiles(u, group, items, on, cls, legend, after=''):
    tiles = ''.join(f'<label><input type="radio" name="{u}-{group}" data-c="{group}" value="{v}"{" checked" if v == on else ""}><span>{t}</span></label>' for v, t in items)
    return f'<fieldset class="so-set {cls}"><legend>{legend}</legend><div>{tiles}</div>{after}</fieldset>'


def _img(n, sizes, cls='', lazy=False):
    # n: 2 the bush, 1 the flower; the script sets src, srcset and alt
    return f'<img data-img="{n}" sizes="{sizes}" alt=""{" class=" + chr(34) + cls + chr(34) if cls else ""}{" loading=" + chr(34) + "lazy" + chr(34) if lazy else ""}>'


def crumb():
    return ('<nav class="so-crumb" aria-label="Kruimelpad"><a href="index.html">Home</a><span aria-hidden="true">›</span>'
            '<a href="index.html#assortiment">Assortiment</a><span aria-hidden="true">›</span><span data-o="name" aria-current="page"></span></nav>')


def sizes(u):
    return _tiles(u, 'size', [(str(i), f'<b data-s="{i}"></b><em data-p="{i}"></em>') for i in range(4)], '0', 'so-sizes', 'Hoogte bij levering, prijs per plant',
                  '<p class="so-hint" data-o="sizenote"></p>')


def qty(u):
    return (f'<div class="so-f so-qty"><label class="so-lab" for="{u}-qty">Aantal planten</label><div class="so-step">'
            f'<button type="button" data-step="-1" aria-label="Eén plant minder">{MINUS}</button>'
            f'<span class="so-val"><input id="{u}-qty" data-c="qty" type="text" inputmode="numeric" autocomplete="off" value="1"></span>'
            f'<button type="button" data-step="1" aria-label="Eén plant meer">{PLUS}</button></div></div>')


def subst(u):
    return _tiles(u, 'sub', [('1', '<b>Ja, erbij</b>'), ('0', '<b>Nee, niet nodig</b>')], '0', 'so-subst', 'Tuinturf-substraat',
                  '<p class="so-hint">1 zak van 40&nbsp;L per plant, € 14,95 per zak.</p>')


CALC = '<p class="so-hint so-calc">Voor een haag of een groep? <a href="index.html#haag">Reken uit hoeveel planten u nodig heeft</a>.</p>'
TOTNOTE = '<p class="so-totnote">Exclusief bezorgkosten; die ziet u vóór u betaalt.</p>'
ADD = '<button type="button" class="so-add" data-add>In winkelwagen</button><p class="so-status" data-o="status" role="status"></p>'
# one line with the two ways to reach the nursery: about larger sizes where the variety has them, a plain one otherwise
ASK = ('<p class="so-note" data-row="big">Grotere maten, tot <span data-o="max"></span>&nbsp;cm? Vraag een prijs aan via <a ' + WA + '>WhatsApp</a> of bel ' + TEL + '.</p>'
       '<p class="so-note" data-row="ask">Vragen over deze soort? Stuur een <a ' + WA + '>WhatsApp</a> of bel ' + TEL + '.</p>')


def total():
    # the total on the page: a dark hairline, what it is made of on the left, the sum in Newsreader on the right
    return ('<div class="so-tot"><p class="so-totl"><b>Totaal</b><small data-o="sumline"></small></p><p class="so-totv" data-o="total"></p></div>' + TOTNOTE + ADD + ASK)


def slip(u):
    # the calculator's sheet: the facts card's surface, the lines, the total
    return (f'<div class="so-slip" id="{u}-res" data-res><p class="so-sliph">Uw bestelling</p>'
            '<p class="so-slips"><span data-o="name"></span>, <span data-o="size"></span></p>'
            '<dl class="so-lines"><div><dt><span data-o="n"></span> <span data-o="nword"></span><small><span data-o="each"></span> per plant</small></dt><dd data-o="plants"></dd></div>'
            '<div data-row="sub"><dt><span data-o="bags"></span> <span data-o="bword"></span> substraat<small>€ 14,95 per zak van 40&nbsp;L</small></dt><dd data-o="bagsum"></dd></div>'
            '<div class="so-ltot"><dt>Totaal</dt><dd data-o="total"></dd></div></dl>' + TOTNOTE + ADD + ASK + '</div>')


def trust():
    return ('<ul class="so-trust"><li><b><a href="garantie.html">3 maanden aangroeigarantie</a></b><span>Slaat een plant niet aan, dan krijgt u een nieuwe.</span></li>'
            '<li><b>Eigen transport door heel Nederland</b><span>Of haal uw planten af op de kwekerij in Otterlo.</span></li>'
            '<li><b>Vers gerooid, met kluit</b><span>Wij rooien uw planten pas vlak voor de levering.</span></li></ul>')


def over(u):
    return f'<section class="so-over" aria-labelledby="{u}-ho"><h2 id="{u}-ho" class="so-h3">Over <span data-o="name"></span></h2><p data-o="over"></p></section>'


def ken(u):
    rows = ''.join(f'<div><dt>{l}</dt><dd data-k="{i}"></dd></div>' for i, l in enumerate(KEN))
    return f'<section class="so-kenb" aria-labelledby="{u}-hk"><h2 id="{u}-hk" class="so-h3">Kenmerken</h2><dl class="so-ken">{rows}</dl></section>'


def head(u, desc=True):
    return (f'<h1 id="{u}-h1" tabindex="-1" data-o="name"></h1><p class="so-facts" data-o="facts"></p>'
            + ('<p class="so-desc" data-o="desc"></p>' if desc else ''))


def bar_buy():
    # phone: the total and the cart button in a small bar while the real button is out of view
    return ('<div class="so-bar" data-bar><span><b data-o="total"></b><i data-o="barline"></i></span>'
            '<button type="button" class="so-add" data-add>In winkelwagen</button></div>')


def dir_a():
    u = 'soa'
    pics = ('<div class="so-pics" role="group" aria-label="Foto’s"><figure>' + _img(2, '(min-width:900px) 45vw, 86vw')
            + '</figure><figure>' + _img(1, '(min-width:900px) 45vw, 86vw', lazy=True) + '</figure></div>')
    buy = (f'<div class="so-buy" role="group" aria-label="Bestellen">' + sizes(u) + '<div class="so-row">' + qty(u) + subst(u) + '</div>' + CALC + total() + '</div>')
    return (f'<div class="so so-a" data-d="a"><div class="in">' + crumb() + '<div class="so-grid">' + pics
            + '<div class="so-info">' + head(u) + buy + trust() + over(u) + ken(u) + '</div></div></div>' + bar_buy() + '</div>')


def dir_a2():
    # "Легче" (owner, 24 Nov: a was overloaded with text): the same page with less than half the words. No description above
    # the order; what a hint said is in the legend; one phrase under the total; one line under the button; three short trust
    # lines; "Over" in two sentences with five facts under it (no row that repeats the facts line or the photo); the two
    # quiet links (calculator, professionals) close the column
    u = 'sol'
    pics = ('<div class="so-pics" role="group" aria-label="Foto’s"><figure>' + _img(2, '(min-width:900px) 45vw, 86vw')
            + '</figure><figure>' + _img(1, '(min-width:900px) 45vw, 86vw', lazy=True) + '</figure></div>')
    maat = _tiles(u, 'size', [(str(i), f'<b data-s="{i}"></b><em data-p="{i}"></em>') for i in range(4)], '0', 'so-sizes',
                  'Hoogte bij levering<span>, gemeten vanaf de kluit</span>')
    sub = _tiles(u, 'sub', [('1', '<b>Ja, erbij</b>'), ('0', '<b>Nee, niet nodig</b>')], '0', 'so-subst', 'Tuinturf-substraat<span>, € 14,95 per zak van 40&nbsp;L</span>')
    tot = '<div class="so-tot"><p class="so-totl"><b>Totaal</b><small>exclusief bezorgkosten</small></p><p class="so-totv" data-o="total"></p></div>'
    ask = ('<p class="so-note" data-row="big">Groter, tot <span data-o="max"></span>&nbsp;cm? <a ' + WA + '>WhatsApp</a> of bel ' + TEL + '.</p>'
           '<p class="so-note" data-row="ask">Vragen? <a ' + WA + '>WhatsApp</a> of bel ' + TEL + '.</p>')
    buy = '<div class="so-buy" role="group" aria-label="Bestellen">' + maat + '<div class="so-row">' + qty(u).replace('Aantal planten', 'Aantal') + sub + '</div>' + tot + ADD + ask + '</div>'
    trust2 = ('<ul class="so-trust2"><li><a href="garantie.html">3 maanden aangroeigarantie</a></li><li>Bezorgd door heel Nederland, of afhalen in Otterlo</li>'
              '<li>Vers gerooid, met kluit</li></ul>')
    rows = ''.join(f'<div><dt>{l}</dt><dd data-k2="{i}"></dd></div>' for i, l in enumerate(['Volgroeid', 'Groei', 'Winterhard', 'Grond']))
    about = (f'<section class="so-over" aria-labelledby="{u}-ho"><h2 id="{u}-ho" class="so-h3">Over <span data-o="name"></span></h2><p data-o="over2"></p>'
             f'<dl class="so-ken" aria-label="Kenmerken">{rows}</dl>'
             '<p class="so-links"><span>Haag of groep? <a href="index.html#haag">Reken het aantal planten uit</a></span>'
             '<span>Hovenier of grootverbruiker? <a href="index.html#contact">Vraag een prijsopgave aan</a></span></p></section>')
    return ('<div class="so so-a so-a2" data-d="a2"><div class="in">' + crumb() + '<div class="so-grid">' + pics
            + '<div class="so-info">' + head(u, False) + buy + trust2 + about + '</div></div></div>' + bar_buy() + '</div>')


def dir_b():
    u = 'sob'
    top = ('<div class="so-hd"><div>' + head(u, False) + '</div><div><p class="so-desc" data-o="desc"></p><p class="so-from">vanaf <b data-o="from"></b> per plant, met kluit</p></div></div>'
           '<div class="so-pics" role="group" aria-label="Foto’s"><figure>' + _img(2, '(min-width:900px) 45vw, 50vw') + '</figure><figure>'
           + _img(1, '(min-width:900px) 45vw, 50vw') + '</figure></div>')
    ask = (f'<div class="so-ask" role="group" aria-labelledby="{u}-hb"><h2 id="{u}-hb" class="so-h3">Kies maat en aantal</h2>' + sizes(u) + qty(u) + CALC + subst(u) + '</div>')
    mini = f'<a class="so-bar so-mini" data-bar href="#{u}-res"><span><b data-o="total"></b><i data-o="barline"></i></span><em>Bekijk uw bestelling</em></a>'
    return (f'<div class="so so-b" data-d="b"><div class="in">' + crumb() + top + '<div class="so-band">' + ask + slip(u) + trust() + '</div>'
            '<div class="so-band so-more">' + over(u) + ken(u) + '</div></div>' + mini + '</div>')


def dir_c():
    u = 'soc'
    ph = ('<div class="so-cph" data-show="2">' + _img(2, '(min-width:900px) 42vw, 92vw', 'so-p2') + _img(1, '(min-width:900px) 42vw, 92vw', 'so-p1')
          + '<div class="so-th" role="group" aria-label="Foto kiezen"><button type="button" data-pic="2" aria-pressed="true" aria-label="Foto van de struik">' + _img(2, '56px')
          + '</button><button type="button" data-pic="1" aria-pressed="false" aria-label="Foto van de bloem">' + _img(1, '56px') + '</button></div></div>')
    buy = (f'<div class="so-buy" role="group" aria-label="Bestellen">' + sizes(u) + '<div class="so-row">' + qty(u) + subst(u) + '</div>' + CALC + total() + '</div>')
    return (f'<div class="so so-c" data-d="c"><div class="in">' + crumb() + '<div class="so-card">' + ph + '<div class="so-cbody">' + head(u) + buy + '</div></div>'
            + trust() + '<div class="so-more">' + over(u) + ken(u) + '</div></div>' + bar_buy() + '</div>')


def others():
    # the other six varieties, in the language of the homepage's assortment cards; the script hides the current one
    cards = ''
    for s in SOORTEN:
        cards += (f'<article class="so-it" data-slug="{s["slug"]}"><a href="#{s["slug"]}" aria-label="{_html.escape(s["n"])}, vanaf € {s["p"][0]}, van {s["a"]} tot {s["m"]} cm">'
                  f'<div class="so-ph"><img src="img/{s["slug"]}-2-sm.webp" alt="" loading="lazy" style="object-position:{s["pos"]}"></div>'
                  f'<h3>{_html.escape(s["n"])}</h3><p class="so-pr"><span class="so-v">vanaf</span><b>€&nbsp;{s["p"][0]}</b>'
                  f'<span class="so-s">{s["a"]} tot {s["m"]}&nbsp;cm, met kluit</span></p></a></article>')
    return ('<section class="so-oth" aria-labelledby="so-hoth" data-oth><div class="in"><h2 id="so-hoth">Andere soorten</h2><div class="so-ogrid">' + cards + '</div>'
            '<p class="so-pro">Hovenier of grootverbruiker? <a href="index.html#contact">Neem contact op voor een prijsopgave</a>.</p></div></section>')


def main_html():
    return (f'<main id="main" tabindex="-1" class="som" data-so data-soorten="{DATA}">' + dir_a2() + dir_a() + others()
            + '<p class="so-said" data-o="said" aria-live="polite"></p></main>')


def css():
    return (pathlib.Path(__file__).parent / 'soort.css').read_text()


def js():
    return (pathlib.Path(__file__).parent / 'soort.js').read_text()
