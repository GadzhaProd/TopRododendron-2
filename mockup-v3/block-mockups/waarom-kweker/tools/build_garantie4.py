# Mockup tool (not site code): garantie4.html = the guarantee page after the owner's choice (20 Nov) on garantie-fable3.html:
# the plant label of gb-3 ("Бирка на шнурке") is the one; the cord did not go through the hole, so it is redrawn as a loop with
# a knot, threaded through a reinforced eyelet. The sheet loses the fields to fill in ("nobody fills them in on a website") and
# the hole with its string; instead it says how the guarantee works in four steps, and the conditions are shorter.
# Copy: shortened from the Dutch draft of tools/build_garantie.py (which keeps the full text), no new facts. DRAFT: the owner
# confirms it and a lawyer checks it (plan 3.12). Header, cart, phone menu and footer come from the main mockup (index.html).
# The seal is Fable's (tools/build_garantie_fable3.py). Usage: python3 tools/build_garantie4.py [dir]
import math, re, pathlib, sys
D = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
s = (D / 'index.html').read_text()
i = s.index('<main id="main"'); j = s.index('</main>') + len('</main>')
head, tail = s[:i], s[j:]

WA = 'href="https://wa.me/31620297849" target="_blank" rel="noopener noreferrer"'
FIELD = 'https://www.google.com/maps/search/?api=1&amp;query=52.0914891%2C5.7283254'
A_WA = '<a ' + WA + '>06&nbsp;20&nbsp;29&nbsp;78&nbsp;49</a>'
A_TEL = '<a href="tel:+31620104312">06&nbsp;20&nbsp;10&nbsp;43&nbsp;12</a>'
A_MAIL = '<a href="mailto:info@toprhododendrons.nl">info@toprhododendrons.nl</a>'
A_FIELD = '<a href="' + FIELD + '" target="_blank" rel="noopener noreferrer">Apeldoornseweg, Wekerom</a>'
PDFA = ('<a class="gt-pdfa" href="#" data-page="Aangroeigarantie (pdf)">Download als pdf<svg viewBox="0 0 16 16" aria-hidden="true">'
        '<path d="M8 2v9M4 8l4 4 4-4M3 14h10"/></svg></a>')


def seal(uid, cls=''):
    # Fable's stamp: a scalloped edge, two rings, the name over the top, the place under it, the term in the middle; worn ink
    n, R, r = 40, 114, 9.6
    pts = [(120 + R * math.cos(2 * math.pi * k / n - math.pi / 2), 120 + R * math.sin(2 * math.pi * k / n - math.pi / 2)) for k in range(n)]
    edge = 'M%.2f %.2f' % pts[0] + ''.join('A%.1f %.1f 0 0 1 %.2f %.2f' % (r, r, x, y) for x, y in pts[1:] + pts[:1]) + 'Z'
    ticks = ''.join('<line x1="%.2f" y1="%.2f" x2="%.2f" y2="%.2f"/>' % (120 + 68 * math.cos(t), 120 + 68 * math.sin(t), 120 + 72 * math.cos(t), 120 + 72 * math.sin(t))
                    for t in [2 * math.pi * k / 60 for k in range(60)])
    return ('<svg class="gt-seal %s" viewBox="0 0 240 240" role="img" aria-label="Zegel: Top Rhododendrons, Otterlo, sinds 2001. 3 maanden aangroeigarantie">'
            '<defs><path id="%s-t" d="M36 120a84 84 0 0 1 168 0"/><path id="%s-b" d="M24 120a96 96 0 0 0 192 0"/>'
            '<filter id="%s-ink" x="-5%%" y="-5%%" width="110%%" height="110%%"><feTurbulence type="fractalNoise" baseFrequency="1.05" numOctaves="2" seed="11" result="n"/>'
            '<feColorMatrix in="n" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 -3 2.95" result="m"/><feComposite in="SourceGraphic" in2="m" operator="in"/></filter></defs>'
            '<g filter="url(#%s-ink)" fill="none" stroke="currentColor">'
            '<path d="%s" stroke-width="2.2"/><circle cx="120" cy="120" r="104" stroke-width="1"/>'
            '<circle cx="120" cy="120" r="62" stroke-width="1.6"/><g stroke-width="1">%s</g>'
            '<g fill="currentColor" stroke="none"><circle cx="30" cy="120" r="2.6"/><circle cx="210" cy="120" r="2.6"/>'
            '<text font-family="Manrope,system-ui,sans-serif" font-size="15" font-weight="700" letter-spacing="3.1"><textPath href="#%s-t" startOffset="50%%" text-anchor="middle">TOP RHODODENDRONS</textPath></text>'
            '<text font-family="Manrope,system-ui,sans-serif" font-size="13.5" font-weight="700" letter-spacing="3"><textPath href="#%s-b" startOffset="50%%" text-anchor="middle">OTTERLO · SINDS 2001</textPath></text>'
            '<text x="120" y="130" text-anchor="middle" font-family="Newsreader,Georgia,serif" font-size="66" font-weight="500">3</text>'
            '<text x="120" y="154" text-anchor="middle" font-family="Newsreader,Georgia,serif" font-size="20" font-weight="500">maanden</text>'
            '<rect x="70" y="147" width="12" height="1.4"/><rect x="158" y="147" width="12" height="1.4"/></g></g></svg>') % (cls, uid, uid, uid, uid, edge, ticks, uid, uid)


# ---- the cord of the label (SVG 120 x 172; the top edge of the label at y 128, the eyelet centred at 60,156) ----
# a hanging loop (top at y 40), a knot with two loose ends, two strands down to the label: the back one goes behind the top edge,
# the front one runs over the paper into the eyelet (a sage reinforcement ring), and through it you see the cord go in.
def _tw(d, cls=''):
    # a strand of twine: the cord, then a lighter broken line over it for the twist
    return f'<path class="gt-c {cls}" d="{d}"/><path class="gt-tw" d="{d}"/>'


CORD = ('<svg class="gt-cord" viewBox="0 0 120 172" aria-hidden="true">'
        '<defs><filter id="gt-cs" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="1.1"/></filter>'
        '<clipPath id="gt-in"><circle cx="60" cy="156" r="7.5"/></clipPath></defs>'
        # the reinforcement ring and the eyelet, on the paper
        '<circle class="gt-ring" cx="60" cy="156" r="13.5"/><circle class="gt-ring2" cx="60" cy="156" r="10.5"/>'
        '<circle class="gt-eye" cx="60" cy="156" r="7.5"/>'
        # the shadow of the front strand on the paper
        '<path class="gt-csh" d="M59.8 130C59.8 140 60.6 148 61.6 154" filter="url(#gt-cs)"/>'
        # the back strand: from the knot to the top edge, where it goes behind the label
        + _tw('M62.4 84.6C67.4 96 68.2 112 65.6 128.8', 'gt-cb') +
        # the hanging loop and the two loose ends
        _tw('M58.2 82.4C43.6 75 40.2 44.5 59.4 40.2C79.4 41.6 77.6 74 62.4 82.4')
        + _tw('M58.4 85.2C53.4 89.4 51 95 51.8 103') + _tw('M62.6 85.6C67.4 88.4 70.4 92.4 71 99') +
        # the front strand: from the knot over the top edge and down the paper into the eyelet
        _tw('M59.2 85C55.6 98 55.4 114 58 128.8C58.8 138 59.6 146 60 150.6') +
        # inside the eyelet: the cord going through it (clipped to the hole)
        '<path class="gt-c gt-ci" d="M60 147.6C60.1 152 60.2 156 60.2 160" clip-path="url(#gt-in)"/>'
        # the knot
        '<ellipse class="gt-knot" cx="60.4" cy="83.8" rx="5" ry="4" transform="rotate(-14 60.4 83.8)"/>'
        '<path class="gt-kl" d="M57 82.8C59 85 61.8 85.6 63.8 84.6"/><path class="gt-kl" d="M58.2 80.8C60.2 81.2 62 82 63 83.2"/></svg>')

SHORT = ('<ul class="gt-short" aria-label="De garantie in het kort"><li><b>3 maanden</b> na levering</li><li><b>Zelfde soort en maat</b> als vervanging</li>'
         '<li><b>Kosteloos</b> bezorgd of klaargezet</li><li><b>Foto’s volstaan</b>, u hoeft niets aan te tonen</li></ul>')
HEAD = ('<div class="gt-head"><nav class="gt-crumb" aria-label="Kruimelpad"><a href="index.html" data-page="Home">Home</a><span aria-hidden="true">/</span><span>Aangroeigarantie</span></nav>'
        '<h1><span>Slaat een plant niet aan?</span> <span>Dan krijgt u een nieuwe.</span></h1>'
        '<div class="gt-intro"><p class="gt-lead"><b>3 maanden aangroeigarantie na levering</b>, bovenop uw wettelijke rechten. '
        'Dezelfde soort en maat, kosteloos bezorgd of voor u klaargezet. De oorzaak hoeft u niet aan te tonen: een paar foto’s volstaan.</p>'
        '<p class="gt-draft">Concepttekst: de eigenaar en een jurist controleren deze voorwaarden nog.</p>'
        '<p class="gt-pdf">' + PDFA + '<span>U krijgt de garantie ook bij uw orderbevestiging en op de plantkaart bij de levering.</span></p></div></div>')
LABEL = ('<div class="gt-lab">' + CORD + '<div class="gt-tag"><p class="gt-lbrand">Top Rhododendrons</p>' + seal('s1')
         + '<p class="gt-lname">Aangroeigarantie</p>' + SHORT + '<p class="gt-lpdf">' + PDFA + '</p></div></div>')

# ---- the sheet: how it works in four steps, then the conditions in short ----
STEPS = [
 ('Planten', 'Plant binnen <b>14&nbsp;dagen</b> na levering, in kalkvrije, zure grond en niet dieper dan de kluit. Geef water in droge periodes.'),
 ('Melden', 'Slaat een plant binnen <b>3&nbsp;maanden</b> niet aan? Stuur twee of drie foto’s met uw ordernummer, per WhatsApp of <span class="nb">e-mail</span>. '
            'De oorzaak hoeft u niet aan te tonen.'),
 ('Antwoord', 'Binnen <b>twee werkdagen</b> hoort u van ons, binnen 14&nbsp;dagen volgt ons besluit. Twijfelen wij, dan komen wij kijken. Dat kost u niets.'),
 ('Nieuwe plant', 'U krijgt een plant van <b>dezelfde soort en maat</b>, in het eerstvolgende plantseizoen kosteloos bezorgd of klaargezet op de kwekerij, '
                  + A_FIELD + '. De oude hoeft niet terug.'),
]
TERMS = [
 ('Voor welke planten', 'Alle rhododendrons die u als particulier bij ons koopt en in de volle grond plant, bezorgd in Nederland of afgehaald. '
                        'Niet aangeslagen betekent: afgestorven, of in het groeiseizoen niet meer uitgelopen.'),
 ('Niet meer leverbaar', 'Dan kiest u: een andere soort in dezelfde maat, of uw geld terug.'),
 ('Wanneer wij niet vervangen', 'Als vaststaat dat de oorzaak vorst is die strenger is dan de vermelde winterhardheid, langdurig staand water, '
                                'vraat door dieren, mechanische schade of vandalisme, verplanten, of kalkhoudende grond.'),
 ('Uw wettelijke rechten', 'Deze garantie komt bovenop uw wettelijke rechten en beperkt ze niet. Voldoet een plant bij levering niet aan wat u mocht '
                           'verwachten, dan heeft u kosteloos recht op vervanging, en anders op prijsvermindering of ontbinding.'),
 ('Wie geeft de garantie', '<span class="gt-ph">[juridische naam]</span>, handelend onder de naam Top Rhododendrons. KvK&nbsp;82480273. '
                           'Esserbroekweg&nbsp;2, 6731&nbsp;DB Otterlo.'),
]
DOC = ('<article class="gt-doc" aria-labelledby="h-doc">' + seal('s2', 'is-doc') +
       '<header class="gt-top"><p class="gt-brand">Top Rhododendrons · familiekwekerij in Otterlo</p>'
       '<h2 id="h-doc">Aangroeigarantie</h2><p class="gt-sub">3 maanden na levering, bovenop uw wettelijke rechten.</p></header>'
       '<section class="gt-how" aria-labelledby="h-how"><h3 class="gt-lbl" id="h-how">Zo werkt het</h3><ol class="gt-steps">'
       + ''.join(f'<li><i aria-hidden="true">{n}</i><div><h4>{t}</h4><p>{p}</p></div></li>' for n, (t, p) in enumerate(STEPS, 1)) +
       '</ol></section>'
       '<section class="gt-terms" aria-labelledby="h-terms"><h3 class="gt-lbl" id="h-terms">Goed om te weten</h3><dl>'
       + ''.join(f'<div><dt>{t}</dt><dd>{p}</dd></div>' for t, p in TERMS) +
       '</dl></section>'
       '<div class="gt-tear" aria-hidden="true"></div>'
       '<footer class="gt-strip"><h3>Gaat een plant achteruit?</h3><p>Meld het zo snel mogelijk, dan kijken we eerst samen of hij te redden is. '
       'U spreekt met Gert Top, oprichter en kweker, of met zijn team.</p>'
       '<dl><div><dt>WhatsApp</dt><dd>' + A_WA + '</dd></div><div><dt>Bellen</dt><dd>' + A_TEL + '</dd></div><div><dt>E-mail</dt><dd>' + A_MAIL + '</dd></div></dl></footer></article>')
MAIN = ('<main id="main" tabindex="-1" class="gtm"><div class="in gt">' + HEAD + LABEL
        + '<div class="gt-stage"><div class="gt-air" aria-hidden="true"></div>' + DOC + '</div></div></main>')
s = head + MAIN + tail


def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), a[:70]); s = s.replace(a, b)


# on this page the homepage anchors become links to the homepage (only in the markup, not in the scripts)
parts = re.split(r'(<script\b.*?</script>)', s, flags=re.S)
for k in range(0, len(parts), 2):
    for a, label in [('#waarom', 'Over ons (homepage)'), ('#kweker', 'Contact (homepage)'), ('#assortiment', 'Planten (homepage)')]:
        parts[k] = re.sub(r'href="' + a + r'"(?![^>]*data-page)', f'href="index.html{a}" data-page="{label}"', parts[k])
s = ''.join(parts)
rep('</head>', '<style id="garantie4-css">' + (D / 'tools' / 'garantie4.css').read_text() + '</style></head>')
s = re.sub(r'<title>[^<]*</title>', '<title>Aangroeigarantie | Top Rhododendrons</title>', s, count=1)
(D / 'garantie4.html').write_text(s)
print('ok', len(s))
