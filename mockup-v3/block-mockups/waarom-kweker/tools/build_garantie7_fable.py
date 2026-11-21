# Mockup tool (not site code): garantie7-fable.html = garantie4.html with the guarantee sheet as an official document
# (Fable, 21 Nov; a try-out). The owner: "closer to an official document: no names, no fields to fill in; just how the
# guarantee conditions work". Only the sheet changes; the label beside it stays.
#   dc-0 the sheet as it is now · dc-1 "Документ": a title block, eight articles with a small "Artikel n" label in the type of
#   the text, restrained rules, the issuer in one small line at the foot. No perforation, no tear-off strip (the contacts
#   are in Artikel 5), no personal names, no placeholders. On the phone the same document sits behind the toggle, and the
#   help block loses the name. The Dutch copy is the owner's, word for word. Usage: python3 tools/build_garantie7_fable.py [dir]
import re, pathlib, sys
D = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
s = (D / 'garantie4.html').read_text()
WA = '<a href="https://wa.me/31620297849" target="_blank" rel="noopener noreferrer">06&nbsp;20&nbsp;29&nbsp;78&nbsp;49</a>'
MAIL = '<a href="mailto:info@toprhododendrons.nl">info@toprhododendrons.nl</a>'
FIELD = '<a href="https://www.google.com/maps/search/?api=1&amp;query=52.0914891%2C5.7283254" target="_blank" rel="noopener noreferrer">Apeldoornseweg in Wekerom</a>'
ARTS = [
 ('De garantie', '<p>Slaat een rhododendron binnen drie maanden na levering niet aan, dan vervangen wij hem kosteloos door een plant van dezelfde soort en maat. '
                 'Deze garantie geldt naast uw wettelijke rechten en beperkt die niet.</p>'),
 ('Toepassing', '<p>De garantie geldt voor rhododendrons die u als particulier bij ons koopt en in de volle grond plant, bezorgd in Nederland of afgehaald op de kwekerij. '
                'Een plant is niet aangeslagen als hij afsterft, of in het groeiseizoen niet meer uitloopt.</p>'),
 ('Wat wij van u vragen', '<p>U plant de rhododendron binnen 14&nbsp;dagen na ontvangst en houdt de kluit tot dan vochtig. U plant in kalkvrije, zure, humusrijke en goed '
                          'doorlatende grond, niet dieper dan de bovenkant van de kluit, en u geeft water in droge periodes, vooral in de eerste zomer. '
                          'Kleine, onbedoelde fouten bij de verzorging rekenen wij u niet aan.</p>'),
 ('Uitsluitingen', '<p>De garantie geldt niet als vaststaat dat de plant niet is aangeslagen door:</p><ol class="d7-abc">'
                   '<li>vorst die strenger is dan de vermelde winterhardheid;</li><li>langdurig staand water op de plantplek;</li><li>vraat of schade door dieren;</li>'
                   '<li>mechanische schade of vandalisme;</li><li>verplanten na de eerste aanplant, of planten in kalkhoudende grond.</li></ol>'),
 ('Melding', '<p>Gaat een plant achteruit, meld het dan zo snel mogelijk, zodat wij eerst kunnen kijken of hij te redden is. Stuur per WhatsApp (' + WA + ') of '
             '<span class="nb">e-mail</span> (' + MAIL + ') twee of drie foto’s van de plant en de plantplek, met uw ordernummer. U hoeft de oorzaak niet aan te tonen.</p>'),
 ('Beoordeling', '<p>U ontvangt binnen twee werkdagen een reactie en binnen 14&nbsp;dagen ons besluit. Twijfelen wij, dan komen wij eerst kijken, zonder kosten voor u.</p>'),
 ('Vervanging', '<p>De nieuwe plant wordt kosteloos bezorgd in het eerstvolgende geschikte plantseizoen, of op uw verzoek klaargezet op de kwekerij aan de ' + FIELD + '. '
                'De oude plant hoeft u niet terug te sturen. Is de soort of maat niet meer leverbaar, dan kiest u een andere soort in dezelfde maat, of terugbetaling van de koopprijs.</p>'),
 ('Uw wettelijke rechten', '<p>Voldoet een plant bij levering niet aan wat u mocht verwachten, dan heeft u op grond van de wet kosteloos recht op vervanging, '
                           'en als dat niet mogelijk is op prijsvermindering of ontbinding. Deze garantie doet daar niets aan af.</p>'),
]
DOC = ('<article class="gt-doc d7" aria-labelledby="h-d7"><header class="d7-top"><p class="d7-kick">Top Rhododendrons · familiekwekerij in Otterlo</p>'
       '<h2 id="h-d7">Garantievoorwaarden</h2><p class="d7-sub">Aangroeigarantie van drie maanden op rhododendrons</p></header>'
       + ''.join(f'<section class="d7-art" aria-labelledby="h-d7-{n}"><h3 id="h-d7-{n}"><span class="d7-n">Artikel {n}</span><span class="d7-t">{t}</span></h3><div class="d7-b">{b}</div></section>'
                 for n, (t, b) in enumerate(ARTS, 1))
       + '<footer class="d7-foot"><p>Garantiegever: Top Rhododendrons · Esserbroekweg&nbsp;2, 6731&nbsp;DB Otterlo · KvK&nbsp;82480273</p></footer></article>')
m = re.search(r'<article class="gt-doc".*?</article>', s, flags=re.S); assert m and s.count('<article class="gt-doc"') == 1
s = s[:m.end()] + DOC + s[m.end():]
old = '<p>Stuur ons een paar foto’s. U spreekt met Gert Top, oprichter en kweker, of met zijn team.</p>'
assert s.count(old) == 1
s = s.replace(old, '<p class="d7-h0">Stuur ons een paar foto’s. U spreekt met Gert Top, oprichter en kweker, of met zijn team.</p><p class="d7-h1">Stuur ons een paar foto’s.</p>')
CSS = '''/* ===== Review: the sheet as an official document (Fable). dc-0 now · dc-1 the document ===== */
body{padding-top:48px}header.fixed{top:48px}
@media (min-width:900px){ .gt-lab{top:calc(80px + 28px - 40px + 48px)} }
@media (min-width:900px) and (max-height:860px){ .gt-lab{top:calc(80px + 20px - 40px + 48px)} .gt-short{margin-top:8px;padding-top:8px} .gt-short li + li{margin-top:3px} }
.d7,.d7-h1{display:none}
html.dc-1 .gt-doc:not(.d7),html.dc-1 .d7-h0{display:none}
html.dc-1 .d7,html.dc-1 .d7-h1{display:block}
/* the title block: set to the left, closed by a double rule */
.d7-top{padding-bottom:clamp(22px,2.6vw,34px);border-bottom:3px double rgba(63,74,55,.45)}
.d7-kick{font-size:var(--t-small);line-height:1.5;color:var(--color-fg-2)}
.d7-top h2{margin-top:10px;font-size:var(--t-h2)!important;line-height:1.05}
.d7-sub{margin-top:10px;font-size:var(--t-lead);line-height:1.5;color:var(--color-fg-2)}
/* an article: the number in the margin, in the type of the text; the title and the text in one reading column */
.d7-art{display:grid;grid-template-columns:clamp(84px,8vw,112px) minmax(0,1fr);column-gap:clamp(16px,2vw,32px);padding:clamp(18px,2vw,26px) 0;border-bottom:1px solid rgba(63,74,55,.16)}
.d7-art h3{display:contents}
.d7-n{grid-column:1;grid-row:1;font-size:var(--t-small);line-height:1.72;font-weight:600;color:var(--moss);font-variant-numeric:tabular-nums}
.d7-t{grid-column:2;grid-row:1;font-size:var(--t-body);line-height:1.5;font-weight:600;color:var(--color-fg)}
.d7-b{grid-column:2;grid-row:2;margin-top:6px;max-width:68ch}
.d7-b p,.d7-abc li{font-size:var(--t-body);line-height:1.65;color:var(--color-fg-2);text-wrap:pretty}
.d7-abc{margin-top:8px!important;counter-reset:abc}
.d7-abc li{position:relative;padding-left:28px;counter-increment:abc}
.d7-abc li + li{margin-top:4px}
.d7-abc li::before{content:counter(abc,lower-alpha) ".";position:absolute;left:0;color:var(--moss);font-weight:600}
.d7-foot{padding-top:clamp(18px,2vw,26px)}
.d7-foot p{font-size:var(--t-micro);line-height:1.6;color:var(--soft)}
@media (max-width:1099.98px){
  .d7-art{grid-template-columns:minmax(0,1fr)}
  .d7-n,.d7-t,.d7-b{grid-column:1;grid-row:auto}
  .d7-n{line-height:1.5}
}
'''
mh = re.search(r'<html lang="nl" class="([^"]*)">', s); assert mh and not any(c.startswith('dc-') for c in mh.group(1).split())
s = s.replace(mh.group(0), '<html lang="nl" class="' + mh.group(1) + ' dc-1">', 1)
BAR = ('<div class="rv" role="group" aria-label="Варианты"><div class="rv-g"><i>Лист</i><button type="button" data-g="dc" data-v="0" aria-pressed="false">0 · Сейчас</button>'
       '<button type="button" data-g="dc" data-v="1" aria-pressed="true">1 · Документ</button></div></div>')
assert '<div class="rv"' not in s and s.count('<div id="root">') == 1 and s.count('</head>') == 1
s = s.replace('<div id="root">', BAR + '<div id="root">').replace('</head>', '<style id="doc-fable-css">' + CSS + '</style></head>')
(D / 'garantie7-fable.html').write_text(s)
print('ok', len(s))
