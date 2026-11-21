# Mockup tool (not site code): garantie.html (called garantie4.html until 21 Nov) = the guarantee page after the owner's choice (20 Nov) on garantie-fable3.html:
# the plant label of gb-3 ("Бирка на шнурке") with the seal. Round 2 (owner, 20 Nov): the cord must really go through the
# hole, so the label has a metal eyelet and the cord runs into it at the top and on behind the label (the lower part of the
# hole stays empty); the subtitle sits under the heading as on the other pages; no step numbers; on the phone the page is the
# label with the main points and the pdf, the contacts, and the full conditions behind one "Lees alle voorwaarden" button.
# Desktop (>= 900 px): the label hangs beside the sheet (how it works in four steps, the conditions in short, a tear-off
# contact strip) and stays in view while the sheet scrolls.
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
PDFA = ('<a class="gt-pdfa" href="#" data-page="Aangroeigarantie (pdf)">Alle voorwaarden als pdf<svg viewBox="0 0 16 16" aria-hidden="true">'
        '<path d="M8 2v9M4 8l4 4 4-4M3 14h10"/></svg></a>')


def _press(i, d=1.0):
    # letterpress (Fable): light under the lower right edge, the ink, a shade inside the upper left edge; d is the depth
    return (f'<filter id="{i}" x="-8%" y="-8%" width="116%" height="116%" color-interpolation-filters="sRGB">'
            f'<feOffset in="SourceAlpha" dx="{.8 * d:.2f}" dy="{.9 * d:.2f}" result="o"/><feFlood flood-color="#fff" flood-opacity=".95"/><feComposite in2="o" operator="in" result="hi"/>'
            '<feComponentTransfer in="SourceAlpha" result="inv"><feFuncA type="table" tableValues="1 0"/></feComponentTransfer>'
            f'<feOffset in="inv" dx="{.9 * d:.2f}" dy="{1 * d:.2f}"/><feGaussianBlur stdDeviation="{.35 * d:.2f}" result="ib"/>'
            f'<feFlood flood-color="#141a10" flood-opacity="{min(.95, .7 * d):.2f}"/><feComposite in2="ib" operator="in"/><feComposite in2="SourceAlpha" operator="in" result="sh"/>'
            '<feMerge><feMergeNode in="hi"/><feMergeNode in="SourceGraphic"/><feMergeNode in="sh"/></feMerge></filter>')


def seal_emboss():
    # The seal (owner chose Fable's "4 · Тиснение", garantie8-fable.html, 21 Nov): a blind stamp. The scalloped disc and its two
    # rings are pressed into the paper, light from the upper left and a shade to the lower right, no ink; only the lettering
    # and "3 maanden" are printed in moss. The scallops reach about r 128 from the centre with their stroke, offset and blur,
    # so the viewBox gives 10 units of room round the 240 box (in -4 -4 248 248 they were cut flat at the top, bottom and
    # sides; owner, 21 Nov).
    n, R, r = 28, 111, 12.4
    pp = [(120 + R * math.cos(2 * math.pi * k / n - math.pi / 2), 120 + R * math.sin(2 * math.pi * k / n - math.pi / 2)) for k in range(n)]
    scal = 'M%.2f %.2f' % pp[0] + ''.join('A%.1f %.1f 0 0 1 %.2f %.2f' % (r, r, x, y) for x, y in pp[1:] + pp[:1]) + 'Z'
    relief = f'<path d="{scal}"/><circle cx="120" cy="120" r="101"/><circle cx="120" cy="120" r="57"/>'
    serif, sans = 'Newsreader,Georgia,serif', 'Manrope,system-ui,sans-serif'
    return ('<svg class="gt-seal" viewBox="-10 -10 260 260" role="img" aria-label="Zegel: Top Rhododendrons, Otterlo, sinds 2001. 3 maanden aangroeigarantie">'
            '<defs><path id="gt-st" d="M43 120a77 77 0 0 1 154 0"/><path id="gt-sb" d="M30 120a90 90 0 0 0 180 0"/>'
            '<filter id="gt-ss" x="-10%" y="-10%" width="120%" height="120%"><feGaussianBlur stdDeviation=".7"/></filter>'
            + _press('gt-sp') + _press('gt-sd', 1.7)
            + '<linearGradient id="gt-sg" gradientUnits="userSpaceOnUse" x1="0" y1="86" x2="0" y2="134"><stop offset="0" stop-color="#27301f"/>'
            '<stop offset="1" stop-color="#4c5b41"/></linearGradient></defs>'
            f'<path d="{scal}" fill="#fff" opacity=".3"/>'
            f'<g fill="none" stroke-linejoin="round"><g stroke="rgba(52,62,44,.55)" stroke-width="2.2" transform="translate(1.3 1.5)" filter="url(#gt-ss)">{relief}</g>'
            f'<g stroke="#fff" stroke-width="2.2" transform="translate(-1.2 -1.3)" filter="url(#gt-ss)">{relief}</g></g>'
            # the lettering is letterpressed: the moss ink pressed into the paper (a shade inside the upper left edge of each
            # letter, a hairline of light under the lower right), and the "3" larger and pressed deeper, its ink darker at the
            # top (owner chose Fable's "2 · Глубокая тройка", garantie9-fable.html, 21 Nov)
            f'<g fill="#3a4532" filter="url(#gt-sp)"><text font-family="{sans}" font-size="15" font-weight="700" letter-spacing="2.6"><textPath href="#gt-st" startOffset="50%" text-anchor="middle">TOP RHODODENDRONS</textPath></text>'
            f'<text font-family="{sans}" font-size="13.5" font-weight="700" letter-spacing="2.4"><textPath href="#gt-sb" startOffset="50%" text-anchor="middle">OTTERLO · SINDS 2001</textPath></text></g>'
            f'<g filter="url(#gt-sd)"><text x="120" y="132" text-anchor="middle" font-family="{serif}" font-size="68" font-weight="500" fill="url(#gt-sg)">3</text></g>'
            f'<g fill="#3a4532" filter="url(#gt-sp)"><text x="120" y="153" text-anchor="middle" font-family="{serif}" font-size="19" font-weight="500">maanden</text></g></svg>')


# the earlier ink stamp (Fable, 20 Nov), kept for the record; not on the page since 21 Nov
def seal(uid, cls=''):
    # Fable's stamp: a scalloped edge, two rings, the name over the top, the place under it, the term in the middle; worn ink;
    # no dashes beside "maanden" (owner, 20 Nov)
    # the scallops reach r 121.2 with their stroke, so the viewBox has 4 units of room round the 240 box (in 0 0 240 240
    # they were cut flat at the top, bottom and sides; owner, 21 Nov)
    n, R, r = 40, 114, 9.6
    pts = [(120 + R * math.cos(2 * math.pi * k / n - math.pi / 2), 120 + R * math.sin(2 * math.pi * k / n - math.pi / 2)) for k in range(n)]
    edge = 'M%.2f %.2f' % pts[0] + ''.join('A%.1f %.1f 0 0 1 %.2f %.2f' % (r, r, x, y) for x, y in pts[1:] + pts[:1]) + 'Z'
    ticks = ''.join('<line x1="%.2f" y1="%.2f" x2="%.2f" y2="%.2f"/>' % (120 + 68 * math.cos(t), 120 + 68 * math.sin(t), 120 + 72 * math.cos(t), 120 + 72 * math.sin(t))
                    for t in [2 * math.pi * k / 60 for k in range(60)])
    return ('<svg class="gt-seal %s" viewBox="-4 -4 248 248" role="img" aria-label="Zegel: Top Rhododendrons, Otterlo, sinds 2001. 3 maanden aangroeigarantie">'
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
            '</g></g></svg>') % (cls, uid, uid, uid, uid, edge, ticks, uid, uid)
# (owner, 20 Nov: the two dashes either side of "maanden" are gone: on the phone, from a distance, they read as a strike-through)


# The cord (owner chose "2б", 21 Nov; designed in the cord rounds, tools/build_garantie4_fable.py, now frozen): a closed loop of
# moss cord over a small pin, two taut strands in a narrow V. The left strand runs down the front of the paper into a plain
# metal eyelet (just the ring and the dark hole) and darkens as it goes in; the right strand goes behind the top edge
# (CORD_B is painted before the label, so the paper covers it). SVG 120 x 180: the label's top edge at y 128, the eyelet
# at 60,160, the pin at 60,40 (the point the label turns around). The markup is the generated result, kept as it is.
CORD = '<svg class="gt-cord" viewBox="0 0 120 180" aria-hidden="true"><defs><filter id="gt-bl" x="-60%" y="-60%" width="220%" height="220%"><feGaussianBlur stdDeviation="1.3"/></filter><filter id="gt-bs" x="-60%" y="-60%" width="220%" height="220%"><feGaussianBlur stdDeviation=".8"/></filter><linearGradient id="gt-hol" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#4c4b42"/><stop offset=".6" stop-color="#6b695e"/><stop offset="1" stop-color="#85837a"/></linearGradient><radialGradient id="gt-pin" cx=".36" cy=".3" r=".8"><stop offset="0" stop-color="#b7c3a8"/><stop offset=".55" stop-color="#6f8062"/><stop offset="1" stop-color="#3f4a37"/></radialGradient><linearGradient id="gt-met" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#f4f1e6"/><stop offset=".5" stop-color="#c3c1ad"/><stop offset="1" stop-color="#85846f"/></linearGradient><clipPath id="gt-pap"><rect x="0" y="128.4" width="120" height="60"/></clipPath></defs><g fill="none" stroke-linecap="round" stroke-linejoin="round"><circle cx="61" cy="161.4" r="14" fill="rgba(38,44,32,.3)" filter="url(#gt-bl)"/><circle cx="60" cy="160" r="13.4" fill="url(#gt-met)" stroke="rgba(52,58,44,.5)" stroke-width=".8"/><circle cx="60" cy="160" r="8.8" fill="url(#gt-hol)"/><path d="M52.0 158.2A8.200000000000001 8.200000000000001 0 0 1 68.0 158.2A11.0 10.0 0 0 0 52.0 158.2Z" fill="rgba(28,33,24,.5)" filter="url(#gt-bs)"/><circle cx="60" cy="160" r="8.8" stroke="rgba(52,58,44,.55)" stroke-width=".9"/><g clip-path="url(#gt-pap)"><path d="M58.9 157C58.8 146 58.6 136 58.2 128C57.2 100 55.6 70 54.4 47C53.8 40 56.4 35.6 60 35.6" stroke="rgba(38,44,32,.42)" stroke-width="4.0" filter="url(#gt-bl)" transform="translate(1.7 2.3)"/></g><g opacity="1.0" stroke-linecap="round"><path d="M58.9 157C58.8 146 58.6 136 58.2 128C57.2 100 55.6 70 54.4 47C53.8 40 56.4 35.6 60 35.6" stroke="#333c2d" stroke-width="5.3"/><path d="M58.9 157C58.8 146 58.6 136 58.2 128C57.2 100 55.6 70 54.4 47C53.8 40 56.4 35.6 60 35.6" stroke="#6f8062" stroke-width="4.0"/><path d="M58.9 157C58.8 146 58.6 136 58.2 128C57.2 100 55.6 70 54.4 47C53.8 40 56.4 35.6 60 35.6" stroke="#414c38" stroke-width="4.0" stroke-dasharray=".9 2.1" stroke-linecap="butt" opacity=".34"/><path d="M58.9 157C58.8 146 58.6 136 58.2 128C57.2 100 55.6 70 54.4 47C53.8 40 56.4 35.6 60 35.6" stroke="#a9b89b" stroke-width="1.0" opacity=".7" transform="translate(-0.80 -0.32)"/></g><ellipse cx="58.9" cy="158.6" rx="3.6" ry="2.7" fill="#3d4337" filter="url(#gt-bs)"/><ellipse cx="62.2" cy="43.6" rx="6.4" ry="5.6" fill="rgba(38,44,32,.4)" filter="url(#gt-bl)"/><circle cx="60" cy="40" r="5.8" fill="url(#gt-pin)" stroke="#333c2d" stroke-width=".9"/><ellipse cx="58.1" cy="37.9" rx="2.1" ry="1.5" fill="#fff" opacity=".55"/></g></svg>'
CORD_B = '<svg class="gt-cord gt-cord-b" viewBox="0 0 120 180" aria-hidden="true"><g fill="none" stroke-linecap="round" stroke-linejoin="round"><g opacity="1.0" stroke-linecap="round"><path d="M60 35.6C63.6 35.6 66.2 40 65.6 47C64.6 70 63.4 100 62.9 128C62.9 132 63 137 63 142" stroke="#333c2d" stroke-width="5.3"/><path d="M60 35.6C63.6 35.6 66.2 40 65.6 47C64.6 70 63.4 100 62.9 128C62.9 132 63 137 63 142" stroke="#6f8062" stroke-width="4.0"/><path d="M60 35.6C63.6 35.6 66.2 40 65.6 47C64.6 70 63.4 100 62.9 128C62.9 132 63 137 63 142" stroke="#414c38" stroke-width="4.0" stroke-dasharray=".9 2.1" stroke-linecap="butt" opacity=".34"/><path d="M60 35.6C63.6 35.6 66.2 40 65.6 47C64.6 70 63.4 100 62.9 128C62.9 132 63 137 63 142" stroke="#a9b89b" stroke-width="1.0" opacity=".7" transform="translate(-0.80 -0.32)"/></g></g></svg>'

SHORT = ('<ul class="gt-short" aria-label="De garantie in het kort"><li><b>3 maanden</b> na levering</li><li><b>Zelfde soort en maat</b> als vervanging</li>'
         '<li><b>Kosteloos</b> bezorgd of klaargezet</li><li><b>Foto’s volstaan</b>, u hoeft niets aan te tonen</li></ul>')
HEAD = ('<div class="gt-head"><nav class="gt-crumb" aria-label="Kruimelpad"><a href="index.html">Home</a><span aria-hidden="true">/</span><span>Aangroeigarantie</span></nav>'
        '<h1><span>Slaat een plant niet aan?</span> <span>Dan krijgt u een nieuwe.</span></h1>'
        '<div class="gt-intro"><p class="gt-lead"><b>3 maanden aangroeigarantie na levering</b>, bovenop uw wettelijke rechten. '
        'Dezelfde soort en maat, kosteloos bezorgd of voor u klaargezet. De oorzaak hoeft u niet aan te tonen: een paar foto’s volstaan.</p>'
        '</div></div>')
# (owner, 21 Nov: no "Concepttekst…" chip on the page; the copy is still a draft for the owner and a lawyer, see docs)
LABEL = ('<div class="gt-lab">' + CORD_B + CORD + '<div class="gt-tag"><p class="gt-lbrand">Top Rhododendrons</p>' + seal_emboss()
         + '<p class="gt-lname">Aangroeigarantie</p>' + SHORT + '<p class="gt-lpdf">' + PDFA + '</p></div></div>')

# ---- the sheet: how it works in four steps, then the conditions in short ----
# ---- the sheet: the guarantee conditions as an official document (owner chose Fable's "Документ", garantie7-fable.html,
# 21 Nov): a title and a subtitle (no kicker above the title: thin, bold, thin was one layer too many), eight articles with a
# small "Artikel n" label in the margin, the issuer in one small line at the foot. No names, no fields, no placeholders, no
# perforation or tear-off; the contacts are in Artikel 5. The Dutch copy is written from the draft's facts only.
A_WA_D = '<a ' + WA + '>06&nbsp;20&nbsp;29&nbsp;78&nbsp;49</a>'
A_FIELD_D = '<a href="' + FIELD + '" target="_blank" rel="noopener noreferrer">Apeldoornseweg in Wekerom</a>'
ARTS = [
 ('De garantie', '<p>Slaat een rhododendron binnen drie maanden na levering niet aan, dan vervangen wij hem kosteloos door een plant van dezelfde soort en maat. '
                 'Deze garantie geldt naast uw wettelijke rechten en beperkt die niet.</p>'),
 ('Toepassing', '<p>De garantie geldt voor rhododendrons die u als particulier bij ons koopt en in de volle grond plant, bezorgd in Nederland of afgehaald op de kwekerij. '
                'Een plant is niet aangeslagen als hij afsterft, of in het groeiseizoen niet meer uitloopt.</p>'),
 ('Wat wij van u vragen', '<p>U plant de rhododendron binnen 14&nbsp;dagen na ontvangst en houdt de kluit tot dan vochtig. U plant in kalkvrije, zure, humusrijke en goed '
                          'doorlatende grond, niet dieper dan de bovenkant van de kluit, en u geeft water in droge periodes, vooral in de eerste zomer. '
                          'Kleine, onbedoelde fouten bij de verzorging rekenen wij u niet aan.</p>'),
 ('Uitsluitingen', '<p>De garantie geldt niet als vaststaat dat de plant niet is aangeslagen door:</p><ol class="gt-abc">'
                   '<li>vorst die strenger is dan de vermelde winterhardheid;</li><li>langdurig staand water op de plantplek;</li><li>vraat of schade door dieren;</li>'
                   '<li>mechanische schade of vandalisme;</li><li>verplanten na de eerste aanplant, of planten in kalkhoudende grond.</li></ol>'),
 ('Melding', '<p>Gaat een plant achteruit, meld het dan zo snel mogelijk, zodat wij eerst kunnen kijken of hij te redden is. Stuur per WhatsApp (' + A_WA_D + ') of '
             '<span class="nb">e-mail</span> (' + A_MAIL + ') twee of drie foto’s van de plant en de plantplek, met uw ordernummer. U hoeft de oorzaak niet aan te tonen.</p>'),
 ('Beoordeling', '<p>U ontvangt binnen twee werkdagen een reactie en binnen 14&nbsp;dagen ons besluit. Twijfelen wij, dan komen wij eerst kijken, zonder kosten voor u.</p>'),
 ('Vervanging', '<p>De nieuwe plant wordt kosteloos bezorgd in het eerstvolgende geschikte plantseizoen, of op uw verzoek klaargezet op de kwekerij aan de ' + A_FIELD_D + '. '
                'De oude plant hoeft u niet terug te sturen. Is de soort of maat niet meer leverbaar, dan kiest u een andere soort in dezelfde maat, of terugbetaling van de koopprijs.</p>'),
 ('Uw wettelijke rechten', '<p>Voldoet een plant bij levering niet aan wat u mocht verwachten, dan heeft u op grond van de wet kosteloos recht op vervanging, '
                           'en als dat niet mogelijk is op prijsvermindering of ontbinding. Deze garantie doet daar niets aan af.</p>'),
]
DOC = ('<article class="gt-doc" aria-labelledby="h-doc"><header class="gt-dtop"><h2 id="h-doc">Garantievoorwaarden</h2>'
       '<p class="gt-dsub">Aangroeigarantie van drie maanden op rhododendrons</p></header>'
       + ''.join(f'<section class="gt-art" aria-labelledby="h-art{n}"><h3 id="h-art{n}"><span class="gt-an">Artikel {n}</span><span class="gt-at">{t}</span></h3>'
                 f'<div class="gt-ab">{b}</div></section>' for n, (t, b) in enumerate(ARTS, 1))
       + '<footer class="gt-dfoot"><p>Garantiegever: Top Rhododendrons · Esserbroekweg&nbsp;2, 6731&nbsp;DB Otterlo · KvK&nbsp;82480273</p></footer></article>')
WAYS = '<dl><div><dt>WhatsApp</dt><dd>' + A_WA + '</dd></div><div><dt>Bellen</dt><dd>' + A_TEL + '</dd></div><div><dt>E-mail</dt><dd>' + A_MAIL + '</dd></div></dl>'
# below 900 px the page is the label (with the pdf) and the contacts; the document is desktop only (owner, 21 Nov: on the
# phone the conditions are the pdf)
HELP = '<div class="gt-help"><h2>Gaat een plant achteruit?</h2><p>Stuur ons een paar foto’s.</p>' + WAYS + '</div>'
MAIN = ('<main id="main" tabindex="-1" class="gtm"><div class="in gt">' + HEAD + LABEL + HELP
        + '<div class="gt-stage" id="voorwaarden"><div class="gt-air" aria-hidden="true"></div>' + DOC + '</div></div></main>')
s = head + MAIN + tail


def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), a[:70]); s = s.replace(a, b)


# on this page the homepage anchors become real links to the homepage, and the logo goes home instead of scrolling to the
# top (only in the markup, not in the scripts); since 21 Nov "Lees de voorwaarden" on the homepage opens this page, so the
# way back works too
parts = re.split(r'(<script\b.*?</script>)', s, flags=re.S)
for k in range(0, len(parts), 2):
    for a in ['#waarom', '#kweker', '#assortiment']:
        parts[k] = re.sub(r'href="' + a + r'"(?![^>]*data-page)', f'href="index.html{a}"', parts[k])
    parts[k] = parts[k].replace('<a href="/" data-home ', '<a href="index.html" ')
s = ''.join(parts)
rep('</head>', '<style id="garantie4-css">' + (D / 'tools' / 'garantie4.css').read_text() + '</style></head>')
s = re.sub(r'<title>[^<]*</title>', '<title>Aangroeigarantie | Top Rhododendrons</title>', s, count=1)
(D / 'garantie.html').write_text(s)
print('ok', len(s))
