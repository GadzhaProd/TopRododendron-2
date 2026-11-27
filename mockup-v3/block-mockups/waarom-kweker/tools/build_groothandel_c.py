# Mockup tool (not site code): groothandel-c.html, variant C of the wholesale page: audience-led, the request always at hand.
# The owner compares it with variant A (groothandel.html, tools/build_groothandel.py; not touched by this script).
# Copy: docs/groothandel-tekst-2026-11-26.md, shortened and regrouped per audience; no new facts (docs/b2b-besluiten-2026-11-26.md).
# Like variant A: header, cart, phone menu and footer come from the main mockup (index.html), <main> is replaced.
# Styles: tools/groothandel.css (variant A's base: type, rows, steps, questions, form) + tools/groothandel_c.css (this variant).
# Layout: from 1024 px two columns, the content left and a compact request card sticky on the right (it ends where the form
# begins); under 1024 px one column and a calm bottom bar "Vraag een offerte aan" (hidden at the head, the form and the footer).
# The audience tabs (hoveniers en tuinarchitecten / gemeenten / projectontwikkelaars) show what matters to each and pre-select
# "Soort organisatie" in the form. The note typed in the sticky card is the form's "Soorten, maten en aantallen" field.
# The form is a mockup: it checks the fields and shows the confirmation, nothing is sent.
# 21st.dev: only the idea of a segmented tab control with a sliding selected background (micka_design "Segmented Tabs");
# no code copied.
# Usage: python3 tools/build_groothandel_c.py [dir]
import pathlib, re, sys
D = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
s = (D / 'index.html').read_text()
i = s.index('<main id="main"'); j = s.index('</main>') + len('</main>')
head, tail = s[:i], s[j:]
head = re.sub(r'<style id="calc3-css">.*?</style>', '', head, count=1, flags=re.S)
tail = re.sub(r'<script id="calc3-js">.*?</script>', '', tail, count=1, flags=re.S)

ARROW = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6" fill="none" stroke="currentColor" '
         'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>')
TEL = '<a href="tel:+31620104312">06&nbsp;20&nbsp;10&nbsp;43&nbsp;12</a>'
FACTS = ['Sinds 2001', '7 soorten', '40 tot 225&nbsp;cm', 'met kluit', '10.000 planten op voorraad']

HEAD = ('<section class="ghc-head" aria-labelledby="h-gh">'
        '<nav class="gh-crumb" aria-label="Kruimelpad"><a href="index.html">Home</a><span aria-hidden="true">/</span>'
        '<span aria-current="page">Groothandel</span></nav>'
        '<h1 id="h-gh"><span>Groothandel in rhododendrons.</span> <span>Rechtstreeks van de kweker.</span></h1>'
        '<p class="gh-lead">Voor hoveniers, tuinarchitecten, gemeenten en projectontwikkelaars: rhododendrons per partij, '
        '<span class="nb">vers gerooid</span> en met kluit.</p>'
        '<div class="gh-cta ghc-cta"><a class="gh-btn" href="#offerte" data-req>Vraag een offerte aan' + ARROW + '</a>'
        '<p class="gh-tel">Of bel ' + TEL + '</p></div>'
        '<ul class="gh-facts" aria-label="In het kort">' + ''.join(f'<li>{f}</li>' for f in FACTS) + '</ul>'
        '<figure class="gh-photo ghc-photo"><img src="img/hero-field.jpg" alt="Ons rhododendronveld in bloei" width="2048" height="1143" '
        'fetchpriority="high" decoding="async"></figure></section>')

# the three audiences: (key, tab label, the form's label, the line, the rows); only facts from the copy deck
AUD = [('hovenier', 'Hoveniers en tuinarchitecten', 'Hovenier of tuinarchitect', 'Voor de tuinen die u ontwerpt en aanlegt.',
        [('Partijprijs', 'Vanaf 25 planten per bestelling. Hoe groter de partij, hoe lager de prijs per plant.'),
         ('Zelf uitzoeken', 'Grote maten kiest u zelf op ons veld in Wekerom, ook zonder afspraak.'),
         ('Afhalen', 'Gratis in Wekerom. Bezorgen kan ook, vanaf €&nbsp;75 per bestelling.')]),
       ('gemeente', 'Gemeenten', 'Gemeente', 'Voor plantsoenen, parken en ander openbaar groen.',
        [('Offerte', 'Binnen één werkdag, met de prijs per soort en maat, exclusief btw.'),
         ('Betalen', 'Zakelijk op factuur.'),
         ('Plantenpaspoort', 'Bij elke partij.')]),
       ('project', 'Projectontwikkelaars', 'Projectontwikkelaar', 'Voor woningbouw en projecten die meteen volume vragen.',
        [('Grote maten', 'Van 120 tot 225&nbsp;cm, op aanvraag.'),
         ('Planning', 'U noemt de week. Wij rooien pas vlak voor de levering.'),
         ('Bezorgen', 'Met eigen transport door heel Nederland.')])]
TABS = ''.join(f'<button type="button" role="tab" id="t-{k}" aria-controls="p-{k}" aria-selected="{"true" if n == 0 else "false"}" '
               f'tabindex="{0 if n == 0 else -1}" data-aud="{k}">{lab}</button>' for n, (k, lab, _, _, _) in enumerate(AUD))
PANELS = ''.join(f'<div class="ghc-panel" role="tabpanel" id="p-{k}" aria-labelledby="t-{k}"{"" if n == 0 else " aria-hidden=\"true\""}>'
                 f'<h3>{line}</h3><dl class="gh-dl">' + ''.join(f'<div><dt>{t}</dt><dd>{d}</dd></div>' for t, d in rows) + '</dl></div>'
                 for n, (k, _, _, line, rows) in enumerate(AUD))
WHO = ('<section class="ghc-sec" aria-labelledby="h-who"><h2 id="h-who">Wat voor u het zwaarst weegt.</h2>'
       '<div class="ghc-tabs" role="tablist" aria-labelledby="h-who"><span class="ghc-ind" aria-hidden="true"></span>' + TABS + '</div>'
       '<div class="ghc-panels">' + PANELS + '</div></section>')

ROWS = [('Partij', 'Vanaf 25 planten krijgt u een partijprijs. Hoe groter de partij, hoe lager de prijs per plant.'),
        ('Rooien', 'Pas vlak voor de levering, met kluit.'),
        ('Bezorgen', 'Met eigen transport door heel Nederland, vanaf €&nbsp;75 per bestelling.'),
        ('Afhalen', 'Gratis, op ons veld in Wekerom.'),
        ('Betalen', 'Zakelijk op factuur.'),
        ('Plantenpaspoort', 'Bij elke partij.')]
GET = ('<section class="ghc-sec" aria-labelledby="h-get"><h2 id="h-get">U koopt bij de kweker zelf.</h2>'
       '<dl class="gh-dl ghc-dl">' + ''.join(f'<div><dt>{t}</dt><dd>{d}</dd></div>' for t, d in ROWS) + '</dl></section>')

SORTS = [('nova-zembla', 'Nova Zembla'), ('catawbiense-grandiflorum', 'Catawbiense Grandiflorum'), ('cunninghams-white', "Cunningham’s White"),
         ('catawbiense-boursault', 'Catawbiense Boursault'), ('roseum-elegans', 'Roseum Elegans'), ('ponticum', 'Ponticum'),
         ('ponticum-roseum', 'Ponticum Roseum')]
SORTS_UL = ('<ul class="ghc-sorts" aria-label="De zeven soorten">' + ''.join(
    f'<li><a href="soort-{sl}.html"><img src="img/{sl}-sm.webp" alt="" width="900" height="900" loading="lazy" decoding="async"><span>{n}</span>{ARROW}</a></li>'
    for sl, n in SORTS) + '<li class="ghc-all"><a href="index.html#assortiment"><span>Alle maten en prijzen</span>' + ARROW + '</a></li></ul>')
VAR = ('<section class="ghc-sec" aria-labelledby="h-var"><h2 id="h-var"><span>Zeven soorten rhododendrons,</span> <span>van 40 tot 225&nbsp;cm.</span></h2>'
       '<p class="gh-p ghc-p">Alle planten groeien in de volle grond en wij leveren ze met kluit. Welke maten er zijn, verschilt per soort.</p>'
       + SORTS_UL +
       '<div class="ghc-big"><h3>Grote maten</h3><p>Voor projecten die meteen volume vragen, hebben wij ook grote maten, '
       'van 120 tot 225&nbsp;cm. Die leveren wij op aanvraag. U kunt ze zelf uitzoeken op ons veld.</p></div></section>')

STEPS = [('Aanvragen', 'U stuurt ons de soorten, maten en aantallen, en de week waarin u de planten nodig heeft.'),
         ('Offerte', 'U krijgt binnen één werkdag een offerte met de prijs per soort en maat, exclusief btw.'),
         ('Afspreken', 'Na uw akkoord kiezen wij samen de dag van bezorgen of afhalen.'),
         ('Ontvangen', 'Wij rooien vlak voor de levering. U krijgt de planten bezorgd, of u haalt ze af in Wekerom.')]
STEP = ('<section class="ghc-sec" aria-labelledby="h-st"><h2 id="h-st">Van aanvraag tot levering, in vier stappen.</h2>'
        '<ol class="gh-steps ghc-steps">' + ''.join(f'<li><h3>{t}</h3><p>{p}</p></li>' for t, p in STEPS) + '</ol></section>')

FIELD = 'https://www.google.com/maps/dir/?api=1&amp;destination=52.0914891%2C5.7283254'
QA = [('Kan ik de planten vooraf bekijken?',
       'Ja. U bent welkom op ons veld aan de <a href="' + FIELD + '" target="_blank" rel="noopener noreferrer">Apeldoornseweg in Wekerom</a>, '
       'ook zonder afspraak. Wij zijn open van maandag tot en met vrijdag van 08:00 tot 17:00 uur en op zaterdag van 09:00 tot 13:00 uur.'),
      ('Welke garantie krijg ik op een partij?',
       'U krijgt de soort en de maat die u bestelt: gezonde planten, vers gerooid en met een stevige kluit. Controleer de partij bij ontvangst. '
       'Klopt er iets niet, meld het dan binnen 8 dagen; wij vervangen de planten. De <a href="garantie.html">aangroeigarantie</a> op deze site geldt voor particuliere kopers.'),
      ('Kan ik ook een klein aantal bestellen?',
       'Ja. U bestelt vanaf 1 plant, gewoon <a href="index.html#assortiment">via de site</a>. Een offerte maken wij vanaf 25 planten.'),
      ('Bezorgt u ook buiten Nederland?', 'Nee, wij bezorgen alleen in Nederland. Afhalen in Wekerom kan wel.')]
FAQ = ('<section class="ghc-sec" aria-labelledby="h-faq"><h2 id="h-faq">Veelgestelde vragen.</h2>'
       '<div class="gh-faq ghc-faq">' + ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in QA) + '</div></section>')

# the sticky request card (from 1024 px): a note that becomes the form's first big field, the one action, the phone
SIDE = ('<aside class="ghc-side" aria-labelledby="h-side"><div class="ghc-card">'
        '<h2 id="h-side">Offerte binnen één werkdag.</h2>'
        '<p class="ghc-card-p">Vanaf 25 planten. Met de prijs per soort en maat, exclusief btw.</p>'
        '<div class="ghc-note"><label for="c-soorten">Soorten, maten en aantallen</label>'
        '<textarea id="c-soorten" rows="3" aria-describedby="c-hint"></textarea>'
        '<p class="gh-hint" id="c-hint">Bijvoorbeeld: 40 × Nova Zembla, 60–80 cm. De rest vult u in de aanvraag in.</p>'
        '<a class="gh-btn" href="#offerte" data-req>Vraag een offerte aan' + ARROW + '</a></div>'
        '<p class="ghc-card-done">Uw aanvraag is ontvangen. U krijgt binnen één werkdag een offerte per e-mail.</p>'
        '<p class="gh-tel">Of bel ' + TEL + '</p></div></aside>')


def field(fid, label, kind='input', req=True, hint='', wide=False, attrs=''):
    opt = '' if req else ' <i>(optioneel)</i>'
    desc = (f'h-{fid} ' if hint else '') + f'e-{fid}'
    ctl = (f'<textarea id="{fid}" name="{fid}" rows="4"{" required" if req else ""} aria-describedby="{desc}"{attrs}></textarea>' if kind == 'textarea'
           else f'<input id="{fid}" name="{fid}" type="{kind}"{" required" if req else ""} aria-describedby="{desc}"{attrs}>')
    return (f'<div class="gh-f{" w" if wide else ""}" data-f="{fid}"><label for="{fid}">{label}{opt}</label>{ctl}'
            + (f'<p class="gh-hint" id="h-{fid}">{hint}</p>' if hint else '') + f'<p class="gh-err" id="e-{fid}" aria-live="polite"></p></div>')


ROL = ('<fieldset class="gh-f w" data-f="rol"><legend>Soort organisatie <i>(optioneel)</i></legend><div class="gh-pick" role="radiogroup">'
       + ''.join(f'<label><input type="radio" name="rol" value="{k}"><span>{lab}</span></label>' for k, _, lab, _, _ in AUD)
       + '<label><input type="radio" name="rol" value="anders"><span>Anders</span></label></div></fieldset>')
FORM = ('<form class="gh-form" novalidate>' + ROL
        + field('bedrijf', 'Bedrijfsnaam', attrs=' autocomplete="organization"')
        + field('naam', 'Uw naam', attrs=' autocomplete="name"')
        + field('email', 'E-mailadres', 'email', attrs=' autocomplete="email"')
        + field('tel', 'Telefoonnummer', 'tel', req=False, hint='Handig als wij een vraag hebben over uw aanvraag.', attrs=' autocomplete="tel"')
        + field('soorten', 'Soorten, maten en aantallen', 'textarea', hint='Bijvoorbeeld: 40 × Nova Zembla, 60–80 cm. Weet u het nog niet precies? Een schatting is genoeg.', wide=True)
        + field('week', 'Gewenste levering', req=False, hint='Bijvoorbeeld: week 12, of maart.')
        + '<fieldset class="gh-f" data-f="wijze"><legend>Bezorgen of afhalen</legend><div class="gh-pick" role="radiogroup" aria-describedby="e-wijze">'
          '<label><input type="radio" name="wijze" value="bezorgen"><span>Bezorgen in Nederland</span></label>'
          '<label><input type="radio" name="wijze" value="afhalen"><span>Afhalen in Wekerom</span></label></div>'
          '<p class="gh-err" id="e-wijze" aria-live="polite"></p></fieldset>'
        + field('plaats', 'Plaats van levering', req=False, wide=True, attrs=' autocomplete="address-level2"').replace('data-f="plaats"', 'data-f="plaats" hidden')
        + '<div class="gh-send"><button class="gh-btn" type="submit">Vraag een offerte aan' + ARROW + '</button>'
          '<p class="gh-priv">Wij gebruiken uw gegevens alleen om uw aanvraag te beantwoorden. Lees onze <a href="/privacy" data-page="Privacy">privacyverklaring</a>.</p>'
          '<p class="gh-err" id="e-send" aria-live="polite"></p></div></form>'
        '<div class="gh-done" role="status" tabindex="-1"><h3>Uw aanvraag is ontvangen.</h3>'
        '<p>U krijgt binnen één werkdag een offerte per e-mail. Hebben wij eerst een vraag, dan bellen of mailen wij u.</p>'
        '<p>Liever meteen overleggen? Bel ' + TEL + '.</p></div>')
REQ = ('<section class="gh-sec ghc-req" id="offerte" aria-labelledby="h-req"><div class="in"><div class="gh-card gh-two">'
       '<div class="gh-l"><h2 id="h-req">Vraag een offerte aan.</h2>'
       '<p class="gh-p">Vertel ons wat u nodig heeft. U krijgt een offerte met de prijs per soort en maat, rechtstreeks van de kwekerij. '
       'Minder dan 25 planten nodig? Die bestelt u <a href="index.html#assortiment">direct via de site</a>.</p>'
       '<p class="gh-tel">Of bel ' + TEL + '</p></div>'
       '<div class="gh-r gh-req">' + FORM + '</div></div></div></section>')

# under 1024 px: the request stays at hand in a calm bar (hidden while the head's button, the form or the footer is in view);
# the phone is already in the header there, so the bar holds the one action only
BAR = ('<div class="ghc-bar" data-off><div class="ghc-bar-in"><p>Offerte binnen één werkdag.</p>'
       '<a class="gh-btn" href="#offerte" data-req>Vraag een offerte aan' + ARROW + '</a>'
       '</div></div>')

JS = r'''<script id="groothandel-c-js">(function(){
var main=document.querySelector('.ghc'),box=document.querySelector('.gh-req');if(!main||!box)return;
var f=box.querySelector('form'),btn=f.querySelector('button[type=submit]');
/* --- the form: variant A's checks and messages --- */
var MSG={bedrijf:'Vul uw bedrijfsnaam in.',naam:'Vul uw naam in.',email:'Vul een geldig e-mailadres in.',soorten:'Vul in welke soorten u zoekt en hoeveel planten.',wijze:'Kies bezorgen of afhalen.'};
var plaats=f.querySelector('[data-f=plaats]');
function setErr(k,m){var e=document.getElementById('e-'+k);if(e)e.textContent=m||'';var c=k==='wijze'?f.querySelector('[data-f=wijze] .gh-pick'):f.elements[k];if(c&&c.setAttribute)c.setAttribute('aria-invalid',m?'true':'false')}
function check(k){var v;if(k==='wijze'){v=f.querySelector('input[name=wijze]:checked');setErr(k,v?'':MSG[k]);return !!v}
 var el=f.elements[k];v=(el.value||'').trim();var ok=k==='email'?/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v):v.length>0;setErr(k,ok?'':MSG[k]);return ok}
f.addEventListener('change',function(e){if(e.target.name==='wijze'){plaats.hidden=e.target.value!=='bezorgen';check('wijze')}});
['bedrijf','naam','email','soorten'].forEach(function(k){f.elements[k].addEventListener('blur',function(){if(this.value.trim()||this.getAttribute('aria-invalid')==='true')check(k)})});
f.addEventListener('submit',function(e){e.preventDefault();var first=null;['bedrijf','naam','email','soorten','wijze'].forEach(function(k){if(!check(k)&&!first)first=k});
 if(first){var t=first==='wijze'?f.querySelector('input[name=wijze]'):f.elements[first];t.focus();return}
 btn.disabled=true;btn.firstChild.textContent='Bezig met verzenden…';
 setTimeout(function(){box.classList.add('gh-sent');main.classList.add('ghc-sent');var d=box.querySelector('.gh-done');d.focus();btn.disabled=false;btn.firstChild.textContent='Vraag een offerte aan';bar()},700)});
/* --- the note in the sticky card is the form's "Soorten, maten en aantallen" --- */
var note=document.getElementById('c-soorten'),so=f.elements.soorten;
if(note){note.addEventListener('input',function(){so.value=note.value;if(so.getAttribute('aria-invalid')==='true')check('soorten')});so.addEventListener('input',function(){note.value=so.value})}
/* --- every "Vraag een offerte aan" link leads to the form and puts the cursor in the first field still empty --- */
document.querySelectorAll('a[data-req]').forEach(function(a){a.addEventListener('click',function(){
 if(main.classList.contains('ghc-sent'))return;
 var t=null;['bedrijf','naam','email','soorten'].some(function(k){if(!f.elements[k].value.trim()){t=f.elements[k];return true}});
 if(t)setTimeout(function(){t.focus({preventScroll:true})},0)})});
/* --- the audience tabs: arrows, Home and End move and select; the choice pre-selects "Soort organisatie" in the form --- */
var list=main.querySelector('.ghc-tabs'),tabs=[].slice.call(list.querySelectorAll('[role=tab]')),ind=list.querySelector('.ghc-ind');
function place(){var t=list.querySelector('[aria-selected=true]');ind.style.width=t.offsetWidth+'px';ind.style.height=t.offsetHeight+'px';ind.style.transform='translate('+t.offsetLeft+'px,'+t.offsetTop+'px)'}
function pick(t,user){tabs.forEach(function(x){var on=x===t;x.setAttribute('aria-selected',on?'true':'false');x.tabIndex=on?0:-1;
  var p=document.getElementById(x.getAttribute('aria-controls'));if(on)p.removeAttribute('aria-hidden');else p.setAttribute('aria-hidden','true')});
 place();if(user){var r=f.querySelector('input[name=rol][value="'+t.dataset.aud+'"]');if(r)r.checked=true}}
tabs.forEach(function(t,n){t.addEventListener('click',function(){pick(t,true)});
 t.addEventListener('keydown',function(e){var k=e.key,m=k==='ArrowRight'||k==='ArrowDown'?n+1:k==='ArrowLeft'||k==='ArrowUp'?n-1:k==='Home'?0:k==='End'?tabs.length-1:null;
  if(m===null)return;e.preventDefault();var x=tabs[(m+tabs.length)%tabs.length];x.focus();pick(x,true)})});
place();list.classList.add('is-ready');window.addEventListener('resize',place);window.addEventListener('load',place);
if(document.fonts&&document.fonts.ready)document.fonts.ready.then(place);
if(window.ResizeObserver)new ResizeObserver(place).observe(list);
/* --- the bottom bar: shown once the head's button has left the screen, gone when the form (and the footer after it) arrives --- */
var barEl=document.querySelector('.ghc-bar'),cta=main.querySelector('.ghc-cta'),req=document.getElementById('offerte'),tick=false;
function bar(){tick=false;var h=window.innerHeight,on=cta.getBoundingClientRect().bottom<64&&req.getBoundingClientRect().top>h-40&&!main.classList.contains('ghc-sent');
 if(on)barEl.removeAttribute('data-off');else barEl.setAttribute('data-off','')}
function q(){if(!tick){tick=true;requestAnimationFrame(bar)}}
window.addEventListener('scroll',q,{passive:true});window.addEventListener('resize',q);bar();
})();</script>'''

MAIN = ('<main id="main" tabindex="-1" class="ghm ghc"><div class="in ghc-wrap"><div class="ghc-col">' + HEAD + WHO + GET + VAR + STEP + FAQ
        + '</div>' + SIDE + '</div>' + REQ + BAR + '</main>')
s = head + MAIN + tail


def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), a[:70]); s = s.replace(a, b)


# as in variant A: the homepage anchors become links to the homepage, the logo goes home; the Groothandel links lead to this page
parts = re.split(r'(<script\b.*?</script>)', s, flags=re.S)
for k in range(0, len(parts), 2):
    for a in ['#waarom', '#kweker', '#assortiment', '#hoe', '#haag']:
        parts[k] = re.sub(r'href="' + a + r'"(?![^>]*data-page)', f'href="index.html{a}"', parts[k])
    parts[k] = parts[k].replace('<a href="/" data-home ', '<a href="index.html" ')
    parts[k] = parts[k].replace('href="/groothandel" data-page="Groothandel"', 'href="groothandel-c.html" aria-current="page"')
s = ''.join(parts)
noise = re.search(r'url\("data:image/svg\+xml;utf8,[^"]+"\)', (D / 'tools' / 'fd-podpis.css').read_text()).group(0)
rep('</head>', '<style id="groothandel-css">.ghm{--gh-noise:' + noise + '}\n' + (D / 'tools' / 'groothandel.css').read_text() + '</style>'
    '<style id="groothandel-c-css">' + (D / 'tools' / 'groothandel_c.css').read_text() + '</style></head>')
rep('</body>', JS + '</body>')
s = re.sub(r'<title>[^<]*</title>', '<title>Groothandel rhododendrons van de kweker | Top Rhododendrons</title>'
           '<meta name="description" content="Groothandel in rhododendrons, rechtstreeks van de kweker in Otterlo. Zeven soorten, '
           '40 tot 225 cm, vers gerooid met kluit. Vraag een offerte aan.">', s, count=1)
(D / 'groothandel-c.html').write_text(s)
print('ok', len(s))
