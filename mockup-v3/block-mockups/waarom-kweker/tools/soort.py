# Mockup tool (not site code): the page of one variety, the page behind a card of the assortment. One static page per
# variety (tools/build_soorten.py -> soort-<slug>.html): the name, the facts, the texts and the photos are in the markup;
# tools/soort.js only does the buying (size, number, substrate, the total, the cart).
# The page (owner chose "Тихая страница", then "Легче", 24–25 Nov): photos on the left, one calm column on the page, no
# cards. Two layouts while the owner compares them (main_html): "galerij" and "nu". The language is the calculator's (tools/calc3.css): soft tiles without borders, the chosen tile glows,
# the cart button with the same glow, hairline rows, the total in Newsreader.
# Prices, size slots, the bag price and the delivery line are read from tools/calc3.py.
# Copy: DRAFT. Texts and facts come from the live site (rhododendrons/lib/products.ts), rewritten without the claims we
# cannot verify; hardiness from docs/winterhardheid.md; the owner confirms them.
import json, html as _html, pathlib
import calc3

WA = 'href="https://wa.me/31620297849" target="_blank" rel="noopener noreferrer"'
TEL = '<a href="tel:+31620104312">06&nbsp;20&nbsp;10&nbsp;43&nbsp;12</a>'
SLUGS = ['nova-zembla', 'catawbiense-grandiflorum', 'cunninghams-white', 'catawbiense-boursault', 'roseum-elegans', 'ponticum', 'ponticum-roseum']
SUN = '; verdraagt zon als de grond vochtig blijft.'
# slug: bloom · height and width when grown (m) · position (zon: half shade, also sun; half: half shade; schaduw: half
# shade to shade) · growth · hardy to −N °C · "Over" in two sentences · the focus of the bush photo on a card
# Cunningham's White: 2,5 m after the RHS ("Max height 1.5–2.5 metres",
# rhs.org.uk/plants/91138/rhododendron-cunninghams-white/details, read 25 Nov); the live site said 2 m, while we sell it up to 225 cm
V = {
    'nova-zembla': ('Mei–juni', '3', '2,5', 'zon', 'Matig', 30,
        'Een van de bekendste rode rhododendrons: helderrode bloemtrossen boven donkergroen, groenblijvend blad. Als solitair, in een groep of als haag' + SUN, '50% 70%'),
    'catawbiense-grandiflorum': ('Mei–juni', '3', '3', 'zon', 'Matig tot snel', 30,
        'Een van de grootste soorten die wij kweken, met lila-roze bloemtrossen en groenblijvend blad. Geschikt voor een hoge haag, een afscherming of een grote groep' + SUN, '50% 50%'),
    'cunninghams-white': ('April–mei', '2,5', '2,5', 'half', 'Langzaam', 25,
        'De vroegste bloeier van ons assortiment: witte bloemen met een lichtroze tint, al in april. Een volle, compacte, groenblijvende struik; als solitair, in een groep of als haag.', '50% 40%'),
    'catawbiense-boursault': ('Mei–juni', '2,5', '2,5', 'zon', 'Matig', 25,
        'Paars-lavendelkleurige bloemtrossen op een compacte, goed vertakte, groenblijvende struik. Als solitair, in een groep of als haag' + SUN, '50% 50%'),
    'roseum-elegans': ('Mei–juni', '2,5', '2,5', 'zon', 'Matig tot snel', 30,
        'Warmroze tot lavendelroze bloemtrossen op een brede, krachtige, groenblijvende struik. Als solitair of als haag in een ruimere tuin' + SUN, '50% 60%'),
    'ponticum': ('Mei–juni', '4', '4', 'schaduw', 'Snel', 20,
        'Violetpaarse bloemen op een snelgroeiende, groenblijvende struik. Geschikt voor een grote tuin of een hoge afscherming, ook in de schaduw.', '50% 50%'),
    'ponticum-roseum': ('Mei–juni', '4', '3,5', 'schaduw', 'Snel', 20,
        'Roze tot lichtpaarse bloemen op een snelgroeiende, groenblijvende struik. Geschikt voor een hoge haag of een afscherming.', '50% 50%'),
}
PLACE = {'zon': 'Halfschaduw of zon', 'half': 'Halfschaduw', 'schaduw': 'Halfschaduw of schaduw'}
PLANT = 'Het hele jaar, behalve bij vorst; het best maart–april of september–oktober'   # the owner's own text (faq of the old site), shortened
# the widths of the photos: img/<slug>-sm.webp and -lg.webp (the flower), the same with "-2" (the bush). The "-lg" files
# are copies of rhododendrons/public/images, at most 1344 px wide
W = {'nova-zembla': ((900, 1024), (672, 896)), 'roseum-elegans': ((900, 1024), (900, 1024)), 'ponticum': ((600, 1024), (672, 1344))}
SOORTEN = []
for slug, (name, prices, rng) in zip(SLUGS, calc3.SOORTEN):
    SOORTEN.append(dict(slug=slug, n=name, p=prices, a=rng[0], m=rng[1], vanaf=calc3.euro(calc3.vanaf(prices)), w=W.get(slug, ((672, 1344), (672, 1344)))))
BY = {s['slug']: s for s in SOORTEN}
MINUS = '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M3.5 8h9"/></svg>'
PLUS = '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M3.5 8h9M8 3.5v9"/></svg>'


# The icons of the facts line (owner's idea and choice, 25 Nov): our own drawings, one family: a 24 box, one round moss
# stroke, no fills but the shaded half of the sun's disc. Decoration for the eye only (aria-hidden).
def _icon(key):
    rot = lambda d, n, step: ''.join(f'<path d="{d}" transform="rotate({k * step} 12 12)"/>' for k in range(n))
    disc = '<circle cx="12" cy="12" r="3.7"/><path d="M12 8.3a3.7 3.7 0 0 1 0 7.4z" fill="currentColor" stroke="none"/>'
    ray = 'M12 3.2v2.3'
    d = {
        'bloei': rot('M12 11.3c-2.2-1.6-2.7-4.9 0-7.6 2.7 2.7 2.2 6 0 7.6z', 5, 72) + '<circle cx="12" cy="12" r=".9" fill="currentColor" stroke="none"/>',
        'hoogte': '<path d="M6.5 3.5h11M6.5 20.5h11M12 7v10M8.8 10.2 12 7l3.2 3.2M8.8 13.8 12 17l3.2-3.2"/>',
        # the position as light: rays all round · rays on one side · the sun half hidden behind a tree
        'zon': disc + rot(ray, 8, 45),
        'half': disc + ''.join(f'<path d="{ray}" transform="rotate({a} 12 12)"/>' for a in (180, 225, 270, 315, 0)),
        'schaduw': ('<circle cx="14" cy="12.2" r="6"/><path d="M14 14.6V22M10.6 22h6.8M14 17.6l2.3-2.3"/>'
                    '<path d="M10.6 7.25A3.4 3.4 0 1 0 8.26 10.43M7.2 1.3v1.2M1.3 7.2h1.2M3 3l.85.85"/>'),
        'winter': rot('M12 12V3.6M10.3 5.2 12 6.9l1.7-1.7', 6, 60),
    }[key]
    return f'<svg class="so-ic" viewBox="0 0 24 24" aria-hidden="true" focusable="false">{d}</svg>'


def _tiles(group, items, on, cls, legend, extra=''):
    tiles = ''.join(f'<label><input type="radio" name="so-{group}" data-c="{group}" value="{v}"{" checked" if v == on else ""}><span>{t}</span></label>' for v, t in items)
    return f'<fieldset class="so-set {cls}"{extra}><legend>{legend}</legend><div>{tiles}</div></fieldset>'


def _img(slug, n, sizes, alt, first):
    s = BY[slug]; base = f'img/{slug}' + ('-2' if n == 2 else ''); w = s['w'][1 if n == 2 else 0]
    pos = f' style="object-position:{V[slug][7]}"' if n == 2 else ''
    load = ' fetchpriority="high"' if first else ' loading="lazy"'
    return f'<img src="{base}-sm.webp" srcset="{base}-sm.webp {w[0]}w, {base}-lg.webp {w[1]}w" sizes="{sizes}" alt="{_html.escape(alt)}"{pos}{load}>'


def facts(slug):
    bloei, hoog, breed, ps, groei, winter, over, pos = V[slug]
    items = [('bloei', 'Bloei', bloei), ('hoogte', 'Hoogte, volgroeid', f'Tot {hoog}&nbsp;m hoog'), (ps, 'Standplaats', PLACE[ps]), ('winter', '', 'Winterhard')]
    return '<ul class="so-facts">' + ''.join('<li>' + _icon(k) + (f'<span class="so-vh">{l}: </span>' if l else '') + t + '</li>' for k, l, t in items) + '</ul>'


def buy(slug):
    s = BY[slug]; slots = [i for i, p in enumerate(s['p']) if p is not None]
    maat = _tiles('size', [(str(i), f'<b>{calc3.LOWS[i]}–{calc3.TOPS[i]} cm</b><em>{calc3.euro(s["p"][i])}</em>') for i in slots], str(slots[0]), 'so-sizes',
                  'Hoogte bij levering<span>, gemeten vanaf de kluit</span>', f' data-n="{len(slots)}"')
    qty = ('<div class="so-qty"><label class="so-lab" for="so-qty">Aantal</label><div class="so-step">'
           f'<button type="button" data-step="-1" aria-label="Eén plant minder">{MINUS}</button>'
           '<span class="so-val"><input id="so-qty" data-c="qty" type="text" inputmode="numeric" autocomplete="off" value="1" role="spinbutton" aria-valuemin="1" aria-valuemax="999" aria-valuenow="1"></span>'
           f'<button type="button" data-step="1" aria-label="Eén plant meer">{PLUS}</button></div></div>')
    sub = _tiles('sub', [('1', '<b>Ja, erbij</b>'), ('0', '<b>Nee, niet nodig</b>')], '0', 'so-subst',
                 'Tuinturf-substraat<span>, 1&nbsp;zak (40&nbsp;L) per&nbsp;plant, ' + calc3.euro(calc3.BAG).replace(' ', '&nbsp;') + '&nbsp;per&nbsp;zak</span>')
    tot = (f'<div class="so-tot"><p class="so-totl">Totaal<small>{calc3.EXCL}</small></p><p class="so-totv" data-o="total">' + calc3.euro(s['p'][slots[0]]) + '</p></div>')
    add = '<button type="button" class="so-add" data-add>In winkelwagen</button><p class="so-vh" data-o="status" role="status"></p>'
    return '<div class="so-buy" role="group" aria-label="Bestellen">' + maat + '<div class="so-row">' + qty + sub + '</div>' + tot + add + '</div>'


def info(slug):
    # what a buyer needs to know besides the price: one calm list at a distance under the button, never round it (owner,
    # 25 Nov). Delivery and pick-up (the calculator's rows), the guarantee, fresh-dug, and the way to ask for larger sizes
    s = BY[slug]; contact = f'<a {WA}>WhatsApp</a> of bel {TEL}'
    rows = [calc3.BEZORGEN, calc3.AFHALEN, ('Garantie', '<a href="garantie.html">3 maanden aangroeigarantie</a>'), ('Vers', 'Gerooid vlak voor levering, met kluit'),
            ('Grotere maten', f'Tot {s["m"]}&nbsp;cm, op aanvraag: {contact}') if s['m'] > calc3.TOPS[-1] else ('Vragen', 'Stuur een ' + contact)]
    return ('<h2 class="so-vh">Bezorgen, afhalen en garantie</h2><dl class="so-ken so-info-l">' + ''.join(f'<div><dt>{l}</dt><dd>{v}</dd></div>' for l, v in rows) + '</dl>')


LINKS = ('<p class="so-links"><span>Haag of groep? <a href="index.html#haag">Reken het aantal planten uit</a></span>'
         '<span>Hovenier of grootverbruiker? <a href="index.html#kweker">Vraag een prijsopgave aan</a></span></p>')


def about(slug, links=True):
    bloei, hoog, breed, ps, groei, winter, over, pos = V[slug]
    rows = [('Volgroeid', f'Tot {hoog}&nbsp;m hoog, {breed}&nbsp;m breed'), ('Groei', groei), ('Winterhard', f'Tot ca. −{winter}&nbsp;°C'),
            ('Grond', 'Zuur en los, pH 4,5–6'), ('Planttijd', PLANT)]
    return ('<section class="so-over" aria-labelledby="so-ho"><div><h2 id="so-ho">Over ' + _html.escape(BY[slug]['n']) + '</h2><p>' + over + '</p></div>'
            '<div><h3 class="so-vh">Kenmerken</h3><dl class="so-ken">' + ''.join(f'<div><dt>{l}</dt><dd>{v}</dd></div>' for l, v in rows) + '</dl>'
            + (LINKS if links else '') + '</div></section>')


# the photos of a variety, in the order of the gallery: (file suffix, what it shows). A third one (the dug shrub with its
# root ball; the owner will shoot it) is one more entry here
PHOTOS = [(2, 'bloeiende struik'), (1, 'bloem van dichtbij')]
ARROW = '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M10 3 5 8l5 5"/></svg>'


def gallery(slug):
    # one large photo with a gallery: a row that slides sideways (scroll-snap, so a finger swipes it), two round arrows on
    # the photo and small thumbnails under it on desktop, dots on the phone; no auto-play. tools/soort.js moves it.
    name = BY[slug]['n']; n = len(PHOTOS)
    slides = ''.join(f'<figure role="group" aria-roledescription="dia" aria-label="{i + 1} van {n}">'
                     + _img(slug, k, '(min-width:900px) 45vw, 86vw', f'{name}, {what}', i == 0) + '</figure>' for i, (k, what) in enumerate(PHOTOS))
    thumbs = ''.join(f'<button type="button" data-go="{i}" aria-label="Foto {i + 1}: {what}"{" aria-current=" + chr(34) + "true" + chr(34) if i == 0 else ""}>'
                     f'<img src="img/{slug}{"-2" if k == 2 else ""}-sm.webp" alt="" loading="lazy"{" style=" + chr(34) + "object-position:" + V[slug][7] + chr(34) if k == 2 else ""}></button>'
                     for i, (k, what) in enumerate(PHOTOS))
    return (f'<div class="so-gal" role="group" aria-roledescription="carrousel" aria-label="Foto’s van {_html.escape(name)}" data-gal>'
            f'<div class="so-gal-w"><div class="so-gal-v" tabindex="0" data-track>{slides}</div>'
            f'<button type="button" class="so-gal-a so-gal-p" data-dir="-1" aria-label="Vorige foto" disabled>{ARROW}</button>'
            f'<button type="button" class="so-gal-a so-gal-n" data-dir="1" aria-label="Volgende foto">{ARROW}</button></div>'
            f'<div class="so-gal-t">{thumbs}</div></div>')


def others(slug, sfx=''):
    # the other six varieties, in the language of the homepage's assortment cards
    cards = ''.join(
        f'<article class="so-it"><a href="soort-{s["slug"]}{sfx}.html" aria-label="{_html.escape(s["n"])}, vanaf {s["vanaf"]}">'
        f'<div class="so-ph"><img src="img/{s["slug"]}-2-sm.webp" alt="" loading="lazy" style="object-position:{V[s["slug"]][7]}"></div>'
        f'<h3>{_html.escape(s["n"])}</h3><p class="so-pr"><span>vanaf</span><b>{s["vanaf"].replace(" ", "&nbsp;")}</b></p></a></article>'
        for s in SOORTEN if s['slug'] != slug)
    return '<section class="so-oth" aria-labelledby="so-hoth" data-oth><div class="in"><h2 id="so-hoth">Andere soorten</h2><div class="so-ogrid">' + cards + '</div></div></section>'


def main_html(slug, layout='galerij', sfx=''):
    # layout "galerij" (owner's idea, 25 Nov, in review): one photo with a gallery, the plant's text and facts under it; the
    # order, the purchase list and the two links on the right. Layout "nu": the page as it was: two photos, "Over" under the order.
    s = BY[slug]; name = _html.escape(s['n'])
    # what the script needs for the sums: the prices of this variety, the size slots and the bag price (all from calc3)
    data = _html.escape(json.dumps({'name': s['n'], 'p': s['p'], 'lows': calc3.LOWS, 'tops': calc3.TOPS, 'bag': calc3.BAG}, ensure_ascii=False), quote=True)
    crumb = ('<nav class="so-crumb" aria-label="Kruimelpad"><a href="index.html">Home</a><span aria-hidden="true">›</span>'
             f'<a href="index.html#assortiment">Assortiment</a><span aria-hidden="true">›</span><span aria-current="page">{name}</span></nav>')
    head = f'<div class="so-head"><h1>{name}</h1>' + facts(slug) + '</div>'
    bar = '<div class="so-bar" data-bar><span><b data-o="total"></b><i data-o="barline"></i></span><button type="button" class="so-add" data-add>In winkelwagen</button></div>'
    if layout == 'galerij':
        body = ('<div class="so-grid"><div class="so-l">' + gallery(slug) + about(slug, False) + '</div>'
                '<div class="so-r"><div class="so-info">' + head + buy(slug) + info(slug) + '</div>' + LINKS + '</div></div>')
        cls = 'so so-g'
    else:
        pics = ('<div class="so-pics" role="group" aria-label="Foto’s"><figure>' + _img(slug, 2, '(min-width:900px) 45vw, 86vw', s['n'] + ', bloeiende struik', True)
                + '</figure><figure>' + _img(slug, 1, '(min-width:900px) 45vw, 86vw', s['n'] + ', bloem van dichtbij', False) + '</figure></div>')
        body = '<div class="so-grid">' + pics + '<div class="so-info">' + head + buy(slug) + info(slug) + '</div>' + about(slug) + '</div>'
        cls = 'so so-n'
    return (f'<main id="main" tabindex="-1" class="som" data-so="{data}"><div class="{cls}"><div class="in">' + crumb + body + '</div>' + bar + '</div>'
            + others(slug, sfx) + '<p class="so-vh" data-o="said" aria-live="polite"></p></main>')


def title(slug):
    return BY[slug]['n'] + ' kopen | Top Rhododendrons'


def description(slug):
    # the first half of "Over" (what the plant looks like), the "vanaf" price and what sets the nursery apart
    look = V[slug][6].split('. ')[0].split(': ')[-1].rstrip('.')
    return (f'Rhododendron {BY[slug]["n"]}: {look[0].lower() + look[1:]}. Vanaf {BY[slug]["vanaf"]} per plant, met kluit, '
            'rechtstreeks van de kwekerij en met 3 maanden aangroeigarantie.')


def css():
    return (pathlib.Path(__file__).parent / 'soort.css').read_text()


def js():
    return (pathlib.Path(__file__).parent / 'soort.js').read_text()
