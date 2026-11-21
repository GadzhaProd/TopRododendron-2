# Mockup tool (not site code): garantie-v1.html (was garantie.html until 21 Nov) = the first draft of the guarantee conditions
# page (phase 2, item 2.2); the page the owner approved is garantie.html, built by tools/build_garantie4.py. The target of
# "Lees de voorwaarden" on the homepage. Header, cart, phone menu and footer are taken from the main mockup (index.html),
# the main content is this page. Copy: the Dutch draft in reports/Гарантия приживаемости у конкурентов.md, rewritten for the
# owner's term (3 months after delivery, 16 Nov) and the pickup at the field (19 Nov). DRAFT: the owner confirms it and a
# lawyer checks it (plan 3.12); the legal name of the company is still a placeholder.
# Usage: python3 tools/build_garantie.py [dir]
import re, pathlib, sys
D = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
s = (D / 'index.html').read_text()
i = s.index('<main id="main"'); j = s.index('</main>') + len('</main>')
head, tail = s[:i], s[j:]

WA = 'href="https://wa.me/31620297849" target="_blank" rel="noopener noreferrer"'
FIELD = 'https://www.google.com/maps/search/?api=1&amp;query=52.0914891%2C5.7283254'
SVG_WA = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/></svg>'
SVG_TEL = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 '
           '19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6'
           'l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>')

SECS = [
 ('extra', 'Wat deze garantie u geeft',
  '<p>Deze garantie komt <b>bovenop</b> uw wettelijke rechten. Wat u extra krijgt:</p><ul>'
  '<li>Gaat een rhododendron binnen <b>3 maanden na levering</b> niet aan, dan krijgt u een nieuwe van <b>dezelfde soort en maat</b>.</li>'
  '<li>U hoeft <b>niet aan te tonen</b> waardoor de plant niet is aangeslagen. Een paar foto’s volstaan.</li>'
  '<li>Kleine, onbedoelde fouten bij de verzorging rekenen wij u niet aan.</li>'
  '<li>De nieuwe plant brengen wij <b>kosteloos</b> met ons eigen transport, of wij zetten hem voor u klaar op de kwekerij.</li></ul>'),
 ('planten', 'Voor welke planten',
  '<p>Voor alle rhododendrons die u als particulier bij ons koopt en in de volle grond plant: bezorgd in Nederland of afgehaald op de kwekerij.</p>'
  '<p>Een plant is <b>niet aangeslagen</b> als hij afsterft, of in het groeiseizoen niet meer uitloopt.</p>'),
 ('vervanging', 'Zo vervangen wij',
  '<p>U krijgt een nieuwe plant van dezelfde soort en maat. Wij bezorgen hem kosteloos in het eerstvolgende geschikte plantseizoen, '
  'of eerder als u dat wilt en het kan. Afhalen kan ook: op de kwekerij, <a href="' + FIELD + '" target="_blank" rel="noopener noreferrer">Apeldoornseweg, Wekerom</a>.</p>'
  '<p>Is de soort of maat niet meer leverbaar, dan kiest u: een andere soort in dezelfde maat, of uw geld terug. '
  'De oude plant hoeft u niet terug te sturen.</p>'),
 ('vragen', 'Wat wij van u vragen',
  '<ul><li>Plant de rhododendron binnen <b>14 dagen</b> na ontvangst en houd de kluit tot dan vochtig.</li>'
  '<li>Plant in <b>kalkvrije, zure, humusrijke</b> en goed doorlatende grond.</li>'
  '<li>Plant <b>niet dieper</b> dan de bovenkant van de kluit.</li>'
  '<li>Geef <b>water in droge periodes</b>, vooral in de eerste zomer.</li></ul>'
  '<p>Bij de levering krijgt u een plantkaart met deze punten.</p>'),
 ('niet', 'Wanneer wij niet vervangen',
  '<p>Wij vervangen niet als vaststaat dat de plant niet is aangeslagen door:</p><ul>'
  '<li>vorst die strenger is dan de winterhardheid die wij bij de soort vermelden;</li>'
  '<li>langdurig staand water op de plantplek;</li>'
  '<li>vraat of schade door dieren, zoals konijnen of wild;</li>'
  '<li>mechanische schade of vandalisme;</li>'
  '<li>verplanten na de eerste aanplant, of planten in kalkhoudende grond.</li></ul>'
  '<p>Twijfelen wij, dan komen wij eerst kijken. Dat kost u niets.</p>'),
 ('melden', 'Zo meldt u het',
  '<ol class="gv-steps">'
  '<li><i>1</i><span>Ziet u dat een plant achteruitgaat? Meld het zo snel mogelijk: dan kijken we eerst samen of hij te redden is.</span></li>'
  '<li><i>2</i><span>Stuur per WhatsApp of e-mail twee of drie foto’s (de hele plant, blad en knoppen, de plantplek) '
  'met uw ordernummer, of uw naam en de datum van levering.</span></li>'
  '<li><i>3</i><span>U krijgt binnen <b>twee werkdagen</b> antwoord, en binnen <b>14 dagen</b> ons besluit.</span></li></ol>'),
 ('wet', 'Uw wettelijke rechten',
  '<p>Ook zonder deze garantie moet een plant bij levering beantwoorden aan wat u mocht verwachten. Is dat niet zo, dan heeft u '
  'kosteloos recht op vervanging, en als dat niet mogelijk is op prijsvermindering of ontbinding. Blijkt een gebrek binnen een jaar '
  'na levering, dan wordt aangenomen dat het er bij levering al was. Deze garantie beperkt die rechten niet.</p>'
  '<p>U ontvangt deze garantie ook als pdf bij uw orderbevestiging en op de plantkaart bij de levering.</p>'),
 ('wie', 'Wie geeft de garantie',
  '<dl class="gv-dl"><dt>Bedrijf</dt><dd><span class="gv-ph">[juridische naam]</span>, handelend onder de naam Top Rhododendrons</dd>'
  '<dt>KvK</dt><dd>82480273</dd>'
  '<dt>Kantoor</dt><dd>Esserbroekweg&nbsp;2, 6731&nbsp;DB Otterlo</dd>'
  '<dt>E-mail</dt><dd><a href="mailto:info@toprhododendrons.nl">info@toprhododendrons.nl</a></dd>'
  '<dt>Telefoon</dt><dd><a href="tel:+31620104312">06&nbsp;20&nbsp;10&nbsp;43&nbsp;12</a></dd>'
  '<dt>WhatsApp</dt><dd><a ' + WA + '>06&nbsp;20&nbsp;29&nbsp;78&nbsp;49</a></dd></dl>'),
]

TOC = '<nav class="gv-toc" aria-label="Op deze pagina"><p>Op deze pagina</p><ol>' + ''.join(
    f'<li><a href="#{k}">{t}</a></li>' for k, t, _ in SECS) + '</ol></nav>'
BODY = ''.join(f'<section class="gv-sec" id="{k}" aria-labelledby="h-{k}"><h2 id="h-{k}"><i>{n:02d}</i>{t}</h2>{c}</section>'
               for n, (k, t, c) in enumerate(SECS, 1))
ACT = ('<div class="gv-act"><h2>Gaat een plant achteruit?</h2>'
       '<p>Stuur ons een paar foto’s. U spreekt met Gert Top, oprichter en kweker, of met zijn team.</p>'
       '<div class="gv-btns"><a class="gv-pri" ' + WA + '>' + SVG_WA + 'WhatsApp</a>'
       '<a href="tel:+31620104312">' + SVG_TEL + 'Bellen</a>'
       '<a href="mailto:info@toprhododendrons.nl">E-mail</a></div></div>')
MAIN = ('<main id="main" tabindex="-1" class="gv"><div class="in gv-hd">'
        '<nav class="gv-crumb" aria-label="Kruimelpad"><a href="index.html" data-page="Home">Home</a><span aria-hidden="true">/</span><span>Aangroeigarantie</span></nav>'
        '<h1><span>Slaat een plant niet aan?</span> <span>Dan krijgt u een nieuwe.</span></h1>'
        '<p class="gv-lead"><b>3 maanden aangroeigarantie na levering</b>, bovenop uw wettelijke rechten. '
        'Dezelfde soort en maat, kosteloos bezorgd of voor u klaargezet. De oorzaak hoeft u niet aan te tonen: een paar foto’s volstaan.</p>'
        '<p class="gv-draft">Concepttekst: de eigenaar en een jurist controleren deze voorwaarden nog.</p>'
        '<ul class="gv-sum">'
        '<li><b>3 maanden</b><span>na levering</span></li>'
        '<li><b>Zelfde soort en maat</b><span>als vervanging</span></li>'
        '<li><b>Kosteloos</b><span>bezorgd of klaargezet</span></li>'
        '<li><b>Foto’s volstaan</b><span>u hoeft niets aan te tonen</span></li></ul></div>'
        '<div class="in gv-bd">' + TOC + '<div class="gv-txt">' + BODY + ACT + '</div></div></main>')
s = head + MAIN + tail

def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), a[:70]); s = s.replace(a, b)
# on this page the homepage anchors become links to the homepage (a note in the mockup)
# (only in the markup: the scripts select '#hero a[href="#assortiment"]' and must stay as they are)
parts = re.split(r'(<script\b.*?</script>)', s, flags=re.S)
for k in range(0, len(parts), 2):
    for a, label in [('#waarom', 'Over ons (homepage)'), ('#kweker', 'Contact (homepage)'), ('#assortiment', 'Planten (homepage)')]:
        parts[k] = re.sub(r'href="' + a + r'"(?![^>]*data-page)', f'href="index.html{a}" data-page="{label}"', parts[k])
s = ''.join(parts)
rep('</head>', '<style id="garantie-css">' + (D / 'tools' / 'garantie.css').read_text() + '</style></head>')
s = re.sub(r'<title>[^<]*</title>', '<title>Aangroeigarantie | Top Rhododendrons</title>', s, count=1)
(D / 'garantie-v1.html').write_text(s)
print('ok', len(s))
