# Mockup tool (not site code): garantie-fable2.html = three NEW concepts for the guarantee conditions page (Fable, 20 Nov),
# after the owner rejected garantie-fable.html for reusing homepage components. None of the three uses a homepage component
# (no woven facts card, no portrait card, no step route on a hairline, no rows of reasons, no columns of figures).
#   gc-1 "Uw drie maanden": a calendar of the guarantee, spans on a 13-week scale
#   gc-2 "Wet + garantie": what the law gives next to what we add; the rest as native <details>
#   gc-3 "Het garantiebewijs": the guarantee as the paper the buyer gets with the plant, with a tear-off contact strip
# Copy and facts: the Dutch draft of tools/build_garantie.py, restructured, nothing added. Header, cart, phone menu and footer
# come from the main mockup (index.html). Usage: python3 tools/build_garantie_fable2.py [dir]
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

def hd(extra=''):
    return ('<nav class="g2-crumb" aria-label="Kruimelpad"><a href="index.html" data-page="Home">Home</a><span aria-hidden="true">/</span><span>Aangroeigarantie</span></nav>'
            '<h1><span>Slaat een plant niet aan?</span> <span>Dan krijgt u een nieuwe.</span></h1>'
            '<p class="g2-lead"><b>3 maanden aangroeigarantie na levering</b>, bovenop uw wettelijke rechten. '
            'Dezelfde soort en maat, kosteloos bezorgd of voor u klaargezet. De oorzaak hoeft u niet aan te tonen: een paar foto’s volstaan.</p>'
            '<p class="g2-draft">Concepttekst: de eigenaar en een jurist controleren deze voorwaarden nog.</p>' + extra)

# the closing contact for concepts 1 and 2: one sentence in the heading's serif, the three ways as links in the line
def contact(n):
    return ('<section class="in g2-end" aria-labelledby="h-end-%d"><h2 id="h-end-%d">Gaat een plant achteruit?</h2>'
            '<p class="g2-say">Stuur ons een paar foto’s via WhatsApp <a %s>06&nbsp;20&nbsp;29&nbsp;78&nbsp;49</a>, '
            'bel <a href="tel:+31620104312">06&nbsp;20&nbsp;10&nbsp;43&nbsp;12</a> of mail '
            '<a href="mailto:info@toprhododendrons.nl">info@toprhododendrons.nl</a>.</p>'
            '<p class="g2-who">U spreekt met Gert Top, oprichter en kweker, of met zijn team.</p></section>') % (n, n, WA)

# ================= 1 · Uw drie maanden =================
def row(cls, title, text, bar):
    return f'<li class="c1-row {cls}"><h3>{title}</h3><div class="c1-bar" aria-hidden="true">{bar}</div><div class="c1-tx">{text}</div></li>'
CAL = ('<ol class="c1-cal">'
       '<li class="c1-scale" aria-hidden="true"><div class="c1-ticks"><span style="--c:1">Levering</span><span style="--c:3">2 weken</span>'
       '<span style="--c:5.33">1 maand</span><span style="--c:9.67">2 maanden</span><span class="is-end" style="--c:14">3 maanden</span></div></li>'
       + row('is-g', 'Uw garantie loopt drie maanden',
             '<p>Gaat een rhododendron binnen <b>3 maanden na levering</b> niet aan, dan krijgt u een nieuwe van <b>dezelfde soort en maat</b>. '
             'U hoeft niet aan te tonen waardoor: een paar foto’s volstaan.</p>', '<i style="grid-column:1/14"></i>')
       + row('is-p', 'Planten: binnen 14 dagen',
             '<p>Plant de rhododendron binnen <b>14 dagen</b> na ontvangst en houd de kluit tot dan vochtig. In <b>kalkvrije, zure, humusrijke</b> '
             'en goed doorlatende grond, <b>niet dieper</b> dan de bovenkant van de kluit.</p>', '<i style="grid-column:1/3"></i>')
       + row('is-w', 'Water geven in droge periodes',
             '<p>Geef <b>water in droge periodes</b>, vooral in de eerste zomer. Kleine, onbedoelde fouten bij de verzorging rekenen wij u niet aan.</p>',
             '<i style="grid-column:1/14"></i>')
       + row('is-m', 'Gaat de plant achteruit? Meld het meteen',
             '<p>Op elk moment in deze drie maanden. Stuur twee of drie foto’s per WhatsApp of <span class="nb">e-mail</span>. U krijgt binnen <b>twee werkdagen</b> '
             'antwoord en binnen <b>14 dagen</b> ons besluit.</p><p class="c1-key"><span class="k1">antwoord: 2 werkdagen</span><span class="k2">besluit: 14 dagen</span></p>',
             '<b style="grid-column:7"></b><i style="grid-column:7/9"></i>')
       + row('is-e', 'Na drie maanden',
             '<p>De aangroeigarantie eindigt. Uw wettelijke rechten blijven gelden: deze garantie beperkt die niet.</p>', '<b style="grid-column:13"></b>')
       + '</ol>')
C1 = ('<div class="gc gc1"><div class="in g2-hd">' + hd() + '</div>'
      '<section class="in c1" aria-labelledby="h-c1"><h2 id="h-c1" class="g2-h2"><span>Uw drie maanden,</span> <span>van levering tot einde garantie.</span></h2>' + CAL + '</section>'
      '<section class="in c1-all" aria-labelledby="h-c1b"><h2 id="h-c1b" class="g2-h2">De voorwaarden, voluit.</h2><div class="c1-cols">'
      + ''.join(f'<article><h3><i aria-hidden="true">{n}</i>{T[k][0]}</h3>{T[k][1]}</article>' for n, k in enumerate(ORDER, 1))
      + '</div></section>' + contact(1) + '</div>')

# ================= 2 · Wet + garantie =================
def cmp(label, wet, wij):
    return f'<div class="c2-r"><h3>{label}</h3><p class="c2-wet"><span class="c2-m">De wet</span>{wet}</p><p class="c2-wij"><span class="c2-m">Onze garantie</span>{wij}</p></div>'
SUMTAB = ('<div class="c2-t"><div class="c2-glow" aria-hidden="true"></div>'
          '<div class="c2-th" aria-hidden="true"><span></span><span class="c2-wet">De wet</span><span class="c2-plus">+</span><span class="c2-wij">Onze garantie</span></div>'
          + cmp('Wanneer', 'Als de plant bij levering niet beantwoordt aan wat u mocht verwachten.',
                'Als de plant binnen <b>3 maanden na levering</b> niet aanslaat.')
          + cmp('Bewijs', 'Blijkt een gebrek binnen een jaar na levering, dan wordt aangenomen dat het er bij levering al was.',
                'U hoeft <b>niet aan te tonen</b> waardoor de plant niet is aangeslagen. Een paar foto’s volstaan.')
          + cmp('Wat u krijgt', 'Kosteloos vervanging, en als dat niet mogelijk is prijsvermindering of ontbinding.',
                'Een nieuwe plant van <b>dezelfde soort en maat</b>. Is die niet meer leverbaar, dan kiest u: een andere soort in dezelfde maat, of uw geld terug.')
          + '<ul class="c2-more" aria-label="Wat wij er nog bij doen">'
          '<li>Kleine, onbedoelde fouten bij de verzorging rekenen wij u niet aan.</li>'
          '<li>De nieuwe plant brengen wij <b>kosteloos</b> met ons eigen transport, of wij zetten hem voor u klaar op de kwekerij.</li>'
          '<li>De oude plant hoeft u niet terug te sturen.</li></ul>'
          '<p class="c2-note">Deze garantie beperkt uw wettelijke rechten niet. U ontvangt haar ook als pdf bij uw orderbevestiging en op de plantkaart bij de levering.</p></div>')
DET = ''.join(f'<details{" open" if n == 0 else ""}><summary><span>{T[k][0]}</span></summary><div class="c2-d">{T[k][1]}</div></details>'
              for n, k in enumerate(['planten', 'vervanging', 'vragen', 'niet', 'melden', 'wie']))
C2 = ('<div class="gc gc2"><div class="in g2-hd">' + hd() + '</div>'
      '<section class="in c2" aria-labelledby="h-c2"><h2 id="h-c2" class="g2-h2"><span>Wat de wet u geeft,</span> <span>en wat wij erbij doen.</span></h2>' + SUMTAB + '</section>'
      '<section class="in c2-all" aria-labelledby="h-c2b"><h2 id="h-c2b" class="g2-h2">De voorwaarden.</h2><div class="c2-list">' + DET + '</div></section>'
      + contact(2) + '</div>')

# ================= 3 · Het garantiebewijs =================
SEAL = ('<svg class="c3-seal" viewBox="0 0 200 200" role="img" aria-label="Top Rhododendrons, Otterlo, sinds 2001"><defs><path id="c3-ring" d="M100 100m-76 0a76 76 0 1 1 152 0a76 76 0 1 1-152 0"/></defs>'
        '<circle cx="100" cy="100" r="96" fill="none" stroke="currentColor" stroke-width="1.5"/><circle cx="100" cy="100" r="58" fill="none" stroke="currentColor" stroke-width="1"/>'
        '<text font-family="Manrope,system-ui,sans-serif" font-size="15.5" font-weight="600" letter-spacing="2.6" fill="currentColor"><textPath href="#c3-ring" startOffset="0">TOP RHODODENDRONS · OTTERLO · SINDS 2001 ·</textPath></text>'
        '<text x="100" y="96" text-anchor="middle" font-family="Newsreader,Georgia,serif" font-size="30" font-weight="500" fill="currentColor">3</text>'
        '<text x="100" y="122" text-anchor="middle" font-family="Newsreader,Georgia,serif" font-size="19" font-weight="500" fill="currentColor">maanden</text></svg>')
DOC = ('<article class="c3-doc" aria-labelledby="h-c3"><span class="c3-hole" aria-hidden="true"></span>'
       '<svg class="c3-string" viewBox="0 0 120 150" aria-hidden="true"><path d="M60 138C40 96 22 70 34 34 42 12 70 4 96 0" /><path d="M60 138C74 100 96 78 92 44 90 24 104 8 120 2"/></svg>'
       '<header class="c3-top"><p class="c3-brand">Top Rhododendrons · familiekwekerij in Otterlo</p>'
       '<h2 id="h-c3">Aangroeigarantie</h2>'
       '<p class="c3-sub">3 maanden na levering, bovenop uw wettelijke rechten.</p>'
       '<dl class="c3-fill" aria-label="In te vullen bij de levering"><div><dt>Soort</dt><dd></dd></div><div><dt>Maat</dt><dd></dd></div>'
       '<div><dt>Geleverd op</dt><dd></dd></div><div><dt>Ordernummer</dt><dd></dd></div></dl></header>'
       '<div class="c3-arts">' + ''.join(f'<section><h3><i aria-hidden="true">{n}</i>{T[k][0]}</h3>{T[k][1]}</section>' for n, k in enumerate(ORDER, 1)) + '</div>'
       + SEAL +
       '<div class="c3-tear" aria-hidden="true"></div>'
       '<footer class="c3-strip"><h3>Gaat een plant achteruit?</h3><p>Stuur ons een paar foto’s. U spreekt met Gert Top, oprichter en kweker, of met zijn team.</p>'
       '<dl><div><dt>WhatsApp</dt><dd>' + A_WA + '</dd></div><div><dt>Bellen</dt><dd>' + A_TEL + '</dd></div><div><dt>E-mail</dt><dd>' + A_MAIL + '</dd></div></dl></footer></article>')
PDF = '<p class="c3-pdf"><a href="#" data-page="Aangroeigarantie (pdf)">Download als pdf<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M8 2v9M4 8l4 4 4-4M3 14h10"/></svg></a><span>U krijgt dit bewijs ook bij uw orderbevestiging en op de plantkaart bij de levering.</span></p>'
C3 = ('<div class="gc gc3"><div class="in c3"><div class="c3-side"><div class="g2-hd">' + hd(PDF) + '</div></div><div class="c3-stage"><div class="c3-air" aria-hidden="true"></div>' + DOC + '</div></div></div>')

MAIN = '<main id="main" tabindex="-1" class="g2">' + C1 + C2 + C3 + '</main>'
s = head + MAIN + tail

def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), a[:70]); s = s.replace(a, b)
parts = re.split(r'(<script\b.*?</script>)', s, flags=re.S)
for k in range(0, len(parts), 2):
    for a, label in [('#waarom', 'Over ons (homepage)'), ('#kweker', 'Contact (homepage)'), ('#assortiment', 'Planten (homepage)')]:
        parts[k] = re.sub(r'href="' + a + r'"(?![^>]*data-page)', f'href="index.html{a}" data-page="{label}"', parts[k])
s = ''.join(parts)
m = re.search(r'<html lang="nl" class="([^"]*)">', s); assert m and not any(c.startswith('gc-') for c in m.group(1).split())
s = s.replace(m.group(0), '<html lang="nl" class="' + m.group(1) + ' gc-1">', 1)
BAR = ('<div class="rv" role="group" aria-label="Варианты"><div class="rv-g"><i>Гарантия</i>'
       '<button type="button" data-g="gc" data-v="1" aria-pressed="true">1 · Три месяца</button>'
       '<button type="button" data-g="gc" data-v="2" aria-pressed="false">2 · Закон + мы</button>'
       '<button type="button" data-g="gc" data-v="3" aria-pressed="false">3 · Гарантийный лист</button></div></div>')
assert '<div class="rv"' not in s
rep('<div id="root">', BAR + '<div id="root">')
rep('</head>', '<style id="garantie-fable2-css">' + (D / 'tools' / 'garantie-fable2.css').read_text() + '</style></head>')
s = re.sub(r'<title>[^<]*</title>', '<title>Aangroeigarantie · drie concepten | Top Rhododendrons</title>', s, count=1)
(D / 'garantie-fable2.html').write_text(s)
print('ok', len(s))
