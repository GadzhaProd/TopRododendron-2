# Mockup tool (not site code): garantie-fable3.html = "Het garantiebewijs" refined (Fable, 20 Nov). The owner chose the
# guarantee sheet of garantie-fable2.html (the sheet and its seal are right) but on desktop the left side was empty.
# Three desktop layouts for that side, switched on the review bar (below 1100 px all three are the same page):
#   gb-1 "Коротко слева": a sticky column: H1, lead, the seal large, the promise in four short lines, the three contacts, the pdf
#   gb-2 "Лист по центру": no left column: the head across the page, the sheet wider and centred, the seal stamped over its corner
#   gb-3 "Бирка на шнурке": the head across the page; beside the sheet hangs a tall plant label on a string with the seal
# Copy and facts: the Dutch draft of tools/build_garantie.py, nothing added. Header, cart, phone menu and footer come from
# the main mockup (index.html). Usage: python3 tools/build_garantie_fable3.py [dir]
import math
import re, pathlib, sys
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

# ---- the eight sections of the draft (text unchanged) ----
T = {
 'extra': ('Wat deze garantie u geeft',
  '<p>Deze garantie komt <b>bovenop</b> uw wettelijke rechten. Wat u extra krijgt:</p><ul>'
  '<li>Gaat een rhododendron binnen <b>3 maanden na levering</b> niet aan, dan krijgt u een nieuwe van <b>dezelfde soort en maat</b>.</li>'
  '<li>U hoeft <b>niet aan te tonen</b> waardoor de plant niet is aangeslagen. Een paar foto’s volstaan.</li>'
  '<li>Kleine, onbedoelde fouten bij de verzorging rekenen wij u niet aan.</li>'
  '<li>De nieuwe plant brengen wij <b>kosteloos</b> met ons eigen transport, of wij zetten hem voor u klaar op de kwekerij.</li></ul>'),
 'planten': ('Voor welke planten',
  '<p>Voor alle rhododendrons die u als particulier bij ons koopt en in de volle grond plant: bezorgd in Nederland of afgehaald op de kwekerij.</p>'
  '<p>Een plant is <b>niet aangeslagen</b> als hij afsterft, of in het groeiseizoen niet meer uitloopt.</p>'),
 'vervanging': ('Zo vervangen wij',
  '<p>U krijgt een nieuwe plant van dezelfde soort en maat. Wij bezorgen hem kosteloos in het eerstvolgende geschikte plantseizoen, '
  'of eerder als u dat wilt en het kan. Afhalen kan ook: op de kwekerij, ' + A_FIELD + '.</p>'
  '<p>Is de soort of maat niet meer leverbaar, dan kiest u: een andere soort in dezelfde maat, of uw geld terug. '
  'De oude plant hoeft u niet terug te sturen.</p>'),
 'vragen': ('Wat wij van u vragen',
  '<ul><li>Plant de rhododendron binnen <b>14 dagen</b> na ontvangst en houd de kluit tot dan vochtig.</li>'
  '<li>Plant in <b>kalkvrije, zure, humusrijke</b> en goed doorlatende grond.</li>'
  '<li>Plant <b>niet dieper</b> dan de bovenkant van de kluit.</li>'
  '<li>Geef <b>water in droge periodes</b>, vooral in de eerste zomer.</li></ul>'
  '<p>Bij de levering krijgt u een plantkaart met deze punten.</p>'),
 'niet': ('Wanneer wij niet vervangen',
  '<p>Wij vervangen niet als vaststaat dat de plant niet is aangeslagen door:</p><ul>'
  '<li>vorst die strenger is dan de winterhardheid die wij bij de soort vermelden;</li>'
  '<li>langdurig staand water op de plantplek;</li>'
  '<li>vraat of schade door dieren, zoals konijnen of wild;</li>'
  '<li>mechanische schade of vandalisme;</li>'
  '<li>verplanten na de eerste aanplant, of planten in kalkhoudende grond.</li></ul>'
  '<p>Twijfelen wij, dan komen wij eerst kijken. Dat kost u niets.</p>'),
 'melden': ('Zo meldt u het',
  '<p>Ziet u dat een plant achteruitgaat? Meld het zo snel mogelijk: dan kijken we eerst samen of hij te redden is.</p>'
  '<p>Stuur per WhatsApp of <span class="nb">e-mail</span> twee of drie foto’s (de hele plant, blad en knoppen, de plantplek) '
  'met uw ordernummer, of uw naam en de datum van levering.</p>'
  '<p>U krijgt binnen <b>twee werkdagen</b> antwoord, en binnen <b>14 dagen</b> ons besluit.</p>'),
 'wet': ('Uw wettelijke rechten',
  '<p>Ook zonder deze garantie moet een plant bij levering beantwoorden aan wat u mocht verwachten. Is dat niet zo, dan heeft u '
  'kosteloos recht op vervanging, en als dat niet mogelijk is op prijsvermindering of ontbinding. Blijkt een gebrek binnen een jaar '
  'na levering, dan wordt aangenomen dat het er bij levering al was. Deze garantie beperkt die rechten niet.</p>'
  '<p>U ontvangt deze garantie ook als pdf bij uw orderbevestiging en op de plantkaart bij de levering.</p>'),
 'wie': ('Wie geeft de garantie',
  '<dl class="g2-dl"><dt>Bedrijf</dt><dd><span class="g2-ph">[juridische naam]</span>, handelend onder de naam Top Rhododendrons</dd>'
  '<dt>KvK</dt><dd>82480273</dd>'
  '<dt>Kantoor</dt><dd>Esserbroekweg&nbsp;2, 6731&nbsp;DB Otterlo</dd>'
  '<dt>E-mail</dt><dd>' + A_MAIL + '</dd>'
  '<dt>Telefoon</dt><dd>' + A_TEL + '</dd>'
  '<dt>WhatsApp</dt><dd>' + A_WA + '</dd></dl>'),
}
ORDER = ['extra', 'planten', 'vervanging', 'vragen', 'niet', 'melden', 'wet', 'wie']


PDFA = '<a class="g3-pdfa" href="#" data-page="Aangroeigarantie (pdf)">Download als pdf<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M8 2v9M4 8l4 4 4-4M3 14h10"/></svg></a>'

def seal(uid, cls=''):
    # a stamp: a scalloped edge, two rings, the name over the top, the place under it, the term in the middle; a little worn ink
    n, R, r = 40, 114, 9.6
    pts = [(120 + R * math.cos(2 * math.pi * k / n - math.pi / 2), 120 + R * math.sin(2 * math.pi * k / n - math.pi / 2)) for k in range(n)]
    edge = 'M%.2f %.2f' % pts[0] + ''.join('A%.1f %.1f 0 0 1 %.2f %.2f' % (r, r, x, y) for x, y in pts[1:] + pts[:1]) + 'Z'
    ticks = ''.join('<line x1="%.2f" y1="%.2f" x2="%.2f" y2="%.2f"/>' % (120 + 68 * math.cos(t), 120 + 68 * math.sin(t), 120 + 72 * math.cos(t), 120 + 72 * math.sin(t))
                    for t in [2 * math.pi * k / 60 for k in range(60)])
    return ('<svg class="g3-seal %s" viewBox="0 0 240 240" role="img" aria-label="Zegel: Top Rhododendrons, Otterlo, sinds 2001. 3 maanden aangroeigarantie">'
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

SHORT = ('<ul class="g3-short" aria-label="De garantie in het kort"><li><b>3 maanden</b> na levering</li><li><b>Zelfde soort en maat</b> als vervanging</li>'
         '<li><b>Kosteloos</b> bezorgd of klaargezet</li><li><b>Foto’s volstaan</b>, u hoeft niets aan te tonen</li></ul>')
HEAD = ('<div class="g3-head"><nav class="g3-crumb" aria-label="Kruimelpad"><a href="index.html" data-page="Home">Home</a><span aria-hidden="true">/</span><span>Aangroeigarantie</span></nav>'
        '<h1><span>Slaat een plant niet aan?</span> <span>Dan krijgt u een nieuwe.</span></h1>'
        '<div class="g3-intro"><p class="g3-lead"><b>3 maanden aangroeigarantie na levering</b>, bovenop uw wettelijke rechten. '
        'Dezelfde soort en maat, kosteloos bezorgd of voor u klaargezet. De oorzaak hoeft u niet aan te tonen: een paar foto’s volstaan.</p>'
        '<p class="g3-draft">Concepttekst: de eigenaar en een jurist controleren deze voorwaarden nog.</p>'
        '<p class="g3-pdf">' + PDFA + '<span>U krijgt dit bewijs ook bij uw orderbevestiging en op de plantkaart bij de levering.</span></p></div></div>')
# gb-1: the sticky "in short" under the head
KORT = ('<div class="g3-kort"><div class="g3-kr">' + seal('s1') + SHORT + '</div>'
        '<dl class="g3-ways"><div><dt>WhatsApp</dt><dd>' + A_WA + '</dd></div><div><dt>Bellen</dt><dd>' + A_TEL + '</dd></div><div><dt>E-mail</dt><dd>' + A_MAIL + '</dd></div></dl>'
        '<p class="g3-kpdf">' + PDFA + '</p></div>')
# gb-3: the plant label hanging beside the sheet
LABEL = ('<div class="g3-lab"><svg class="g3-lstr" viewBox="0 0 120 260" aria-hidden="true"><path d="M60 250C44 190 70 150 58 96 50 60 62 24 56 0"/><path d="M60 250C78 196 52 150 66 100 76 62 60 30 68 0"/></svg>'
         '<div class="g3-tag"><span class="g3-lhole" aria-hidden="true"></span><p class="g3-lbrand">Top Rhododendrons</p>' + seal('s3')
         + '<p class="g3-lname">Aangroeigarantie</p>' + SHORT + '<p class="g3-lpdf">' + PDFA + '</p></div></div>')
DOC = ('<article class="g3-doc" aria-labelledby="h-doc"><span class="g3-hole" aria-hidden="true"></span>'
       '<svg class="g3-string" viewBox="0 0 120 150" aria-hidden="true"><path d="M60 138C40 96 22 70 34 34 42 12 70 4 96 0" /><path d="M60 138C74 100 96 78 92 44 90 24 104 8 120 2"/></svg>'
       + seal('s2', 'is-doc') +
       '<header class="g3-top"><p class="g3-brand">Top Rhododendrons · familiekwekerij in Otterlo</p>'
       '<h2 id="h-doc">Aangroeigarantie</h2>'
       '<p class="g3-sub">3 maanden na levering, bovenop uw wettelijke rechten.</p>'
       '<dl class="g3-fill" aria-label="In te vullen bij de levering"><div><dt>Soort</dt><dd></dd></div><div><dt>Maat</dt><dd></dd></div>'
       '<div><dt>Geleverd op</dt><dd></dd></div><div><dt>Ordernummer</dt><dd></dd></div></dl></header>'
       '<div class="g3-arts">' + ''.join(f'<section><h3><i aria-hidden="true">{n}</i>{T[k][0]}</h3>{T[k][1]}</section>' for n, k in enumerate(ORDER, 1)) + '</div>'
       '<div class="g3-tear" aria-hidden="true"></div>'
       '<footer class="g3-strip"><h3>Gaat een plant achteruit?</h3><p>Stuur ons een paar foto’s. U spreekt met Gert Top, oprichter en kweker, of met zijn team.</p>'
       '<dl><div><dt>WhatsApp</dt><dd>' + A_WA + '</dd></div><div><dt>Bellen</dt><dd>' + A_TEL + '</dd></div><div><dt>E-mail</dt><dd>' + A_MAIL + '</dd></div></dl></footer></article>')
MAIN = ('<main id="main" tabindex="-1" class="g3m"><div class="in g3"><div class="g3-side">' + HEAD + KORT + '</div>' + LABEL
        + '<div class="g3-stage"><div class="g3-air" aria-hidden="true"></div>' + DOC + '</div></div></main>').replace('g2-dl', 'g3-dl').replace('g2-ph', 'g3-ph')
s = head + MAIN + tail

def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), a[:70]); s = s.replace(a, b)
parts = re.split(r'(<script\b.*?</script>)', s, flags=re.S)
for k in range(0, len(parts), 2):
    for a, label in [('#waarom', 'Over ons (homepage)'), ('#kweker', 'Contact (homepage)'), ('#assortiment', 'Planten (homepage)')]:
        parts[k] = re.sub(r'href="' + a + r'"(?![^>]*data-page)', f'href="index.html{a}" data-page="{label}"', parts[k])
s = ''.join(parts)
m = re.search(r'<html lang="nl" class="([^"]*)">', s); assert m and not any(c.startswith('gb-') for c in m.group(1).split())
s = s.replace(m.group(0), '<html lang="nl" class="' + m.group(1) + ' gb-1">', 1)
BAR = ('<div class="rv" role="group" aria-label="Варианты"><div class="rv-g"><i>Слева от листа</i>'
       '<button type="button" data-g="gb" data-v="1" aria-pressed="true">1 · Коротко слева</button>'
       '<button type="button" data-g="gb" data-v="2" aria-pressed="false">2 · Лист по центру</button>'
       '<button type="button" data-g="gb" data-v="3" aria-pressed="false">3 · Бирка на шнурке</button></div></div>')
assert '<div class="rv"' not in s
rep('<div id="root">', BAR + '<div id="root">')
rep('</head>', '<style id="garantie-fable3-css">' + (D / 'tools' / 'garantie-fable3.css').read_text() + '</style></head>')
s = re.sub(r'<title>[^<]*</title>', '<title>Aangroeigarantie · het garantiebewijs | Top Rhododendrons</title>', s, count=1)
(D / 'garantie-fable3.html').write_text(s)
print('ok', len(s))
