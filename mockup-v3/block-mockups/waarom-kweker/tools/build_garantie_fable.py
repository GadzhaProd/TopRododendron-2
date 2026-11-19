# Mockup tool (not site code): garantie-fable.html = the guarantee conditions page in the homepage's handwriting (Fable, 19 Nov).
# The copy, the facts and the eight sections come from tools/build_garantie.py (the draft, unchanged); this build only gives them
# a composition: a woven promise card beside the H1, the planting conditions as the "plantkaart" on a woven sage surface with the
# peat photo dissolving into it, the claim as a route of three (the homepage's "Hoe het werkt" line), and the closing card where
# Gert's portrait dissolves into a warm woven surface (the homepage guarantee card). Header, cart, phone menu and footer are
# taken from the main mockup (index.html). DRAFT text: the owner confirms it and a lawyer checks it.
# Usage: python3 tools/build_garantie_fable.py [dir]
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
WOVEN = '<div class="gf-bg" aria-hidden="true"></div><div class="gf-grain" aria-hidden="true"></div>'

# the planting conditions: the draft's four sentences, each under a short key (the card the customer gets with the delivery)
ASK = ('<div class="gf-card gf-plant">' + WOVEN +
       '<img class="gf-soil" src="img/tuinturf-sm.webp" alt="" loading="lazy">'
       '<ul class="gf-ask">'
       '<li><b>Binnen 14 dagen</b><p>Plant de rhododendron binnen <b>14 dagen</b> na ontvangst en houd de kluit tot dan vochtig.</p></li>'
       '<li><b>In zure grond</b><p>Plant in <b>kalkvrije, zure, humusrijke</b> en goed doorlatende grond.</p></li>'
       '<li><b>Niet te diep</b><p>Plant <b>niet dieper</b> dan de bovenkant van de kluit.</p></li>'
       '<li><b>Water geven</b><p>Geef <b>water in droge periodes</b>, vooral in de eerste zomer.</p></li></ul>'
       '<p class="gf-note">Bij de levering krijgt u een plantkaart met deze punten.</p></div>')
# the claim: the draft's three steps as a route (the line of "Hoe het werkt" on the homepage)
ROUTE = ('<ol class="gf-route">'
         '<li><h3><i aria-hidden="true">1</i>Melden</h3><p>Ziet u dat een plant achteruitgaat? Meld het zo snel mogelijk: dan kijken we eerst samen of hij te redden is.</p></li>'
         '<li><h3><i aria-hidden="true">2</i>Foto’s sturen</h3><p>Stuur per WhatsApp of <span class="nb">e-mail</span> twee of drie foto’s (de hele plant, blad en knoppen, de plantplek) '
         'met uw ordernummer, of uw naam en de datum van levering.</p></li>'
         '<li><h3><i aria-hidden="true">3</i>Antwoord</h3><p>U krijgt binnen <b>twee werkdagen</b> antwoord, en binnen <b>14 dagen</b> ons besluit.</p></li></ol>')

SECS = [
 ('extra', 'Wat deze garantie u geeft', '',
  '<p>Deze garantie komt <b>bovenop</b> uw wettelijke rechten. Wat u extra krijgt:</p><ul>'
  '<li>Gaat een rhododendron binnen <b>3 maanden na levering</b> niet aan, dan krijgt u een nieuwe van <b>dezelfde soort en maat</b>.</li>'
  '<li>U hoeft <b>niet aan te tonen</b> waardoor de plant niet is aangeslagen. Een paar foto’s volstaan.</li>'
  '<li>Kleine, onbedoelde fouten bij de verzorging rekenen wij u niet aan.</li>'
  '<li>De nieuwe plant brengen wij <b>kosteloos</b> met ons eigen transport, of wij zetten hem voor u klaar op de kwekerij.</li></ul>'),
 ('planten', 'Voor welke planten', '',
  '<p>Voor alle rhododendrons die u als particulier bij ons koopt en in de volle grond plant: bezorgd in Nederland of afgehaald op de kwekerij.</p>'
  '<p>Een plant is <b>niet aangeslagen</b> als hij afsterft, of in het groeiseizoen niet meer uitloopt.</p>'),
 ('vervanging', 'Zo vervangen wij', '',
  '<p>U krijgt een nieuwe plant van dezelfde soort en maat. Wij bezorgen hem kosteloos in het eerstvolgende geschikte plantseizoen, '
  'of eerder als u dat wilt en het kan. Afhalen kan ook: op de kwekerij, <a href="' + FIELD + '" target="_blank" rel="noopener noreferrer">Apeldoornseweg, Wekerom</a>.</p>'
  '<p>Is de soort of maat niet meer leverbaar, dan kiest u: een andere soort in dezelfde maat, of uw geld terug. '
  'De oude plant hoeft u niet terug te sturen.</p>'),
 ('vragen', 'Wat wij van u vragen', ' is-wide', ASK),
 ('niet', 'Wanneer wij niet vervangen', '',
  '<p>Wij vervangen niet als vaststaat dat de plant niet is aangeslagen door:</p><ul>'
  '<li>vorst die strenger is dan de winterhardheid die wij bij de soort vermelden;</li>'
  '<li>langdurig staand water op de plantplek;</li>'
  '<li>vraat of schade door dieren, zoals konijnen of wild;</li>'
  '<li>mechanische schade of vandalisme;</li>'
  '<li>verplanten na de eerste aanplant, of planten in kalkhoudende grond.</li></ul>'
  '<p>Twijfelen wij, dan komen wij eerst kijken. Dat kost u niets.</p>'),
 ('melden', 'Zo meldt u het', ' is-wide', ROUTE),
 ('wet', 'Uw wettelijke rechten', '',
  '<p>Ook zonder deze garantie moet een plant bij levering beantwoorden aan wat u mocht verwachten. Is dat niet zo, dan heeft u '
  'kosteloos recht op vervanging, en als dat niet mogelijk is op prijsvermindering of ontbinding. Blijkt een gebrek binnen een jaar '
  'na levering, dan wordt aangenomen dat het er bij levering al was. Deze garantie beperkt die rechten niet.</p>'
  '<p>U ontvangt deze garantie ook als pdf bij uw orderbevestiging en op de plantkaart bij de levering.</p>'),
 ('wie', 'Wie geeft de garantie', '',
  '<dl class="gf-dl"><dt>Bedrijf</dt><dd><span class="gf-ph">[juridische naam]</span>, handelend onder de naam Top Rhododendrons</dd>'
  '<dt>KvK</dt><dd>82480273</dd>'
  '<dt>Kantoor</dt><dd>Esserbroekweg&nbsp;2, 6731&nbsp;DB Otterlo</dd>'
  '<dt>E-mail</dt><dd><a href="mailto:info@toprhododendrons.nl">info@toprhododendrons.nl</a></dd>'
  '<dt>Telefoon</dt><dd><a href="tel:+31620104312">06&nbsp;20&nbsp;10&nbsp;43&nbsp;12</a></dd>'
  '<dt>WhatsApp</dt><dd><a ' + WA + '>06&nbsp;20&nbsp;29&nbsp;78&nbsp;49</a></dd></dl>'),
]

TOC = '<nav class="gf-toc" aria-label="Op deze pagina"><p>Op deze pagina</p><ol>' + ''.join(
    f'<li><a href="#{k}"><i aria-hidden="true">{n:02d}</i>{t}</a></li>' for n, (k, t, _, _) in enumerate(SECS, 1)) + '</ol></nav>'
BODY = ''.join(f'<section class="gf-sec{w}" id="{k}" aria-labelledby="h-{k}"><h2 id="h-{k}"><i aria-hidden="true">{n:02d}</i>{t}</h2>{c}</section>'
               for n, (k, t, w, c) in enumerate(SECS, 1))
SUM = ('<div class="gf-card gf-sumc">' + WOVEN + '<ul class="gf-sum" aria-label="De garantie in het kort">'
       '<li><b>3 maanden</b><span>na levering</span></li>'
       '<li><b>Zelfde soort en maat</b><span>als vervanging</span></li>'
       '<li><b>Kosteloos</b><span>bezorgd of klaargezet</span></li>'
       '<li><b>Foto’s volstaan</b><span>u hoeft niets aan te tonen</span></li></ul></div>')
ACT = ('<div class="in gf-end"><div class="gf-card gf-act">' + WOVEN +
       '<figure class="gf-gert"><picture><source media="(min-width:700px)" srcset="img/owner-portrait-ext.webp" width="1580" height="1418">'
       '<img src="img/fd-podpis-bust.webp" alt="Gert Top, oprichter en kweker van Top Rhododendrons" width="1440" height="1718" loading="lazy"></picture></figure>'
       '<div class="gf-actx"><h2>Gaat een plant achteruit?</h2>'
       '<p>Stuur ons een paar foto’s. U spreekt met Gert Top, oprichter en kweker, of met zijn team.</p>'
       '<div class="gf-btns"><a class="gf-pri" ' + WA + '>' + SVG_WA + 'WhatsApp</a>'
       '<a href="tel:+31620104312">' + SVG_TEL + 'Bellen</a>'
       '<a href="mailto:info@toprhododendrons.nl">E-mail</a></div></div></div></div>')
MAIN = ('<main id="main" tabindex="-1" class="gf"><div class="in gf-hd"><div class="gf-hdx">'
        '<nav class="gf-crumb" aria-label="Kruimelpad"><a href="index.html" data-page="Home">Home</a><span aria-hidden="true">/</span><span>Aangroeigarantie</span></nav>'
        '<h1><span>Slaat een plant niet aan?</span> <span>Dan krijgt u een nieuwe.</span></h1>'
        '<p class="gf-lead"><b>3 maanden aangroeigarantie na levering</b>, bovenop uw wettelijke rechten. '
        'Dezelfde soort en maat, kosteloos bezorgd of voor u klaargezet. De oorzaak hoeft u niet aan te tonen: een paar foto’s volstaan.</p>'
        '<p class="gf-draft">Concepttekst: de eigenaar en een jurist controleren deze voorwaarden nog.</p></div>'
        + SUM + '</div>'
        '<div class="in gf-bd">' + TOC + '<div class="gf-txt">' + BODY + '</div></div>' + ACT + '</main>')
SPY = ('<script>(function(){var ls=[].slice.call(document.querySelectorAll(".gf-toc a"));if(!ls.length||!("IntersectionObserver" in window))return;'
       'var m={};ls.forEach(function(a){m[a.getAttribute("href").slice(1)]=a});'
       'var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){ls.forEach(function(a){a.removeAttribute("aria-current")});'
       'm[e.target.id]&&m[e.target.id].setAttribute("aria-current","true")}})},{rootMargin:"-25% 0px -65% 0px"});'
       '[].slice.call(document.querySelectorAll(".gf-sec")).forEach(function(x){io.observe(x)})})();</script>')
s = head + MAIN + tail

def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), a[:70]); s = s.replace(a, b)
# on this page the homepage anchors become links to the homepage (only in the markup, the scripts stay as they are)
parts = re.split(r'(<script\b.*?</script>)', s, flags=re.S)
for k in range(0, len(parts), 2):
    for a, label in [('#waarom', 'Over ons (homepage)'), ('#kweker', 'Contact (homepage)'), ('#assortiment', 'Planten (homepage)')]:
        parts[k] = re.sub(r'href="' + a + r'"(?![^>]*data-page)', f'href="index.html{a}" data-page="{label}"', parts[k])
s = ''.join(parts)
rep('</head>', '<style id="garantie-fable-css">' + (D / 'tools' / 'garantie-fable.css').read_text() + '</style></head>')
rep('</body>', SPY + '</body>')
# a subpage has no hero, so "Bestellen" is in the header from the first frame (no opening animation on load)
s = re.sub(r'<html lang="nl" class="([^"]*)">', lambda m: f'<html lang="nl" class="{m.group(1)} hb-on">', s, count=1)
s = re.sub(r'<title>[^<]*</title>', '<title>Aangroeigarantie | Top Rhododendrons</title>', s, count=1)
(D / 'garantie-fable.html').write_text(s)
print('ok', len(s))
