# Mockup tool (not site code): groothandel.html, the wholesale page in the new design (plan 2.6, 27 Nov).
# Copy: docs/groothandel-tekst-2026-11-26.md, Fable's final text (the B2B answers of 27 Nov by the project lead on the owner's
# behalf; docs/b2b-besluiten-2026-11-26.md). The company owner still confirms the business guarantee wording (lawyer) and VAT
# (accountant). Header, cart, phone menu and footer come from the main mockup (index.html), as on garantie.html.
# The varieties heading names the plant (owner, 27 Nov: "Zeven soorten rhododendrons"; the other headings stay calm, Yoast SEO 92).
# Blocks: head with our field; "U koopt bij de kweker zelf." (rows); the seven varieties and the large sizes; four steps;
# questions; the request form (a mockup: it checks the fields and shows the confirmation, nothing is sent).
# Usage: python3 tools/build_groothandel.py [dir]
import pathlib, re, sys
D = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
s = (D / 'index.html').read_text()
i = s.index('<main id="main"'); j = s.index('</main>') + len('</main>')
head, tail = s[:i], s[j:]
# the calculator lives in the homepage's main; its style and script are not needed here
head = re.sub(r'<style id="calc3-css">.*?</style>', '', head, count=1, flags=re.S)
tail = re.sub(r'<script id="calc3-js">.*?</script>', '', tail, count=1, flags=re.S)

ARROW = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6" fill="none" stroke="currentColor" '
         'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>')
TEL = '<a href="tel:+31620104312">06&nbsp;20&nbsp;10&nbsp;43&nbsp;12</a>'
CTA = ('<div class="gh-cta"><a class="gh-btn" href="#offerte">Vraag een offerte aan' + ARROW + '</a>'
       '<p class="gh-tel">Of bel ' + TEL + '</p></div>')
FACTS = ['Sinds 2001', '7 soorten', '40 tot 225&nbsp;cm', 'met kluit', '10.000 planten op voorraad']

HEAD = ('<section class="in gh-head" aria-labelledby="h-gh">'
        '<nav class="gh-crumb" aria-label="Kruimelpad"><a href="index.html">Home</a><span aria-hidden="true">/</span>'
        '<span aria-current="page">Groothandel</span></nav>'
        '<h1 id="h-gh"><span>Groothandel in rhododendrons.</span> <span>Rechtstreeks van de kweker.</span></h1>'
        '<p class="gh-lead">Groothandel voor hoveniers, tuinarchitecten, gemeenten en projectontwikkelaars: rhododendrons per partij, '
        '<span class="nb">vers gerooid</span> en met kluit.</p>' + CTA +
        '<ul class="gh-facts" aria-label="In het kort">' + ''.join(f'<li>{f}</li>' for f in FACTS) + '</ul>'
        '<figure class="gh-photo"><img src="img/hero-field.jpg" alt="Ons rhododendronveld in bloei" width="2048" height="1143" '
        'fetchpriority="high" decoding="async"></figure></section>')

ROWS = [('Partij', 'Vanaf 25 planten krijgt u een partijprijs. Hoe groter de partij, hoe lager de prijs per plant.'),
        ('Rooien', 'Pas vlak voor de levering, met kluit.'),
        ('Bezorgen', 'Met eigen transport door heel Nederland, vanaf €&nbsp;75 per bestelling.'),
        ('Afhalen', 'Gratis, op ons veld in Wekerom.'),
        ('Betalen', 'Zakelijk op factuur.'),
        ('Plantenpaspoort', 'Bij elke partij.')]
GET = ('<section class="gh-sec" aria-labelledby="h-get"><div class="in gh-two"><div class="gh-l"><h2 id="h-get">U koopt bij de kweker zelf.</h2></div>'
       '<div class="gh-r"><dl class="gh-dl">' + ''.join(f'<div><dt>{t}</dt><dd>{d}</dd></div>' for t, d in ROWS) + '</dl></div></div></section>')

SORTS = [('nova-zembla', 'Nova Zembla'), ('catawbiense-grandiflorum', 'Catawbiense Grandiflorum'), ('cunninghams-white', "Cunningham's White"),
         ('catawbiense-boursault', 'Catawbiense Boursault'), ('roseum-elegans', 'Roseum Elegans'), ('ponticum', 'Ponticum'),
         ('ponticum-roseum', 'Ponticum Roseum')]
SORTS_UL = ('<ul class="gh-sorts" aria-label="De zeven soorten">' + ''.join(
    f'<li><a href="soort-{sl}.html"><img src="img/{sl}-sm.webp" alt="" width="900" height="900" loading="lazy" decoding="async"><span>{n}</span></a></li>'
    for sl, n in SORTS) + '</ul>')
MORE = ('<p class="gh-more"><a href="index.html#assortiment">Alle maten en prijzen<svg viewBox="0 0 24 24" aria-hidden="true">'
        '<path d="M5 12h14M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></a></p>')
# the heading spans the block (in the left column it ran to three lines), the line and the large sizes under it
VAR = ('<section class="gh-sec" aria-labelledby="h-var"><div class="in"><h2 id="h-var" class="gh-hb"><span>Zeven soorten rhododendrons,</span> '
       '<span>van 40 tot 225&nbsp;cm.</span></h2><div class="gh-two gh-two-t"><div class="gh-l">'
       '<p class="gh-p">Nova Zembla, Catawbiense Grandiflorum, Cunningham’s White, Catawbiense Boursault, Roseum Elegans, Ponticum en Ponticum Roseum. '
       'Alle planten groeien in de volle grond en wij leveren ze met kluit. Welke maten er zijn, verschilt per soort.</p></div>'
       '<div class="gh-r"><div class="gh-big"><h3>Grote maten</h3><p>Voor projecten die meteen volume vragen, hebben wij ook grote maten, '
       'van 120 tot 225&nbsp;cm. Die leveren wij op aanvraag. U kunt ze zelf uitzoeken op ons veld.</p></div>' + MORE + '</div></div>'
       + SORTS_UL + '</div></section>')

STEPS = [('Aanvragen', 'U stuurt ons de soorten, maten en aantallen, en de week waarin u de planten nodig heeft.'),
         ('Offerte', 'U krijgt binnen één werkdag een offerte met de prijs per soort en maat, exclusief btw.'),
         ('Afspreken', 'Na uw akkoord kiezen wij samen de dag van bezorgen of afhalen.'),
         ('Ontvangen', 'Wij rooien vlak voor de levering. U krijgt de planten bezorgd, of u haalt ze af in Wekerom.')]
STEP = ('<section class="gh-sec" aria-labelledby="h-st"><div class="in"><h2 id="h-st">Van aanvraag tot levering, in vier stappen.</h2>'
        '<ol class="gh-steps">' + ''.join(f'<li><h3>{t}</h3><p>{p}</p></li>' for t, p in STEPS) + '</ol></div></section>')

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
FAQ = ('<section class="gh-sec" aria-labelledby="h-faq"><div class="in gh-two"><div class="gh-l"><h2 id="h-faq">Veelgestelde vragen.</h2></div>'
       '<div class="gh-r gh-faq">' + ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in QA) + '</div></div></section>')


def field(fid, label, kind='input', req=True, hint='', wide=False, attrs=''):
    opt = '' if req else ' <i>(optioneel)</i>'
    desc = (f'h-{fid} ' if hint else '') + f'e-{fid}'
    ctl = (f'<textarea id="{fid}" name="{fid}" rows="4"{" required" if req else ""} aria-describedby="{desc}"{attrs}></textarea>' if kind == 'textarea'
           else f'<input id="{fid}" name="{fid}" type="{kind}"{" required" if req else ""} aria-describedby="{desc}"{attrs}>')
    return (f'<div class="gh-f{" w" if wide else ""}" data-f="{fid}"><label for="{fid}">{label}{opt}</label>{ctl}'
            + (f'<p class="gh-hint" id="h-{fid}">{hint}</p>' if hint else '') + f'<p class="gh-err" id="e-{fid}" aria-live="polite"></p></div>')


FORM = ('<form class="gh-form" novalidate>'
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
REQ = ('<section class="gh-sec" id="offerte" aria-labelledby="h-req"><div class="in"><div class="gh-card gh-two">'
       '<div class="gh-l"><h2 id="h-req">Vraag een offerte aan.</h2>'
       '<p class="gh-p">Vertel ons wat u nodig heeft. U krijgt een offerte met de prijs per soort en maat, rechtstreeks van de kwekerij. '
       'Minder dan 25 planten nodig? Die bestelt u <a href="index.html#assortiment">direct via de site</a>.</p>'
       '<p class="gh-tel">Of bel ' + TEL + '</p></div>'
       '<div class="gh-r gh-req">' + FORM + '</div></div></div></section>')

# the form is a mockup: it checks the required fields in the copy's words, shows "Bezig met verzenden…" and then the confirmation
JS = r'''<script id="groothandel-js">(function(){
var box=document.querySelector('.gh-req');if(!box)return;var f=box.querySelector('form'),btn=f.querySelector('button[type=submit]');
var MSG={bedrijf:'Vul uw bedrijfsnaam in.',naam:'Vul uw naam in.',email:'Vul een geldig e-mailadres in.',soorten:'Vul in welke soorten u zoekt en hoeveel planten.',wijze:'Kies bezorgen of afhalen.'};
var plaats=f.querySelector('[data-f=plaats]');
function setErr(k,m){var e=document.getElementById('e-'+k);if(e)e.textContent=m||'';var c=k==='wijze'?f.querySelector('.gh-pick'):f.elements[k];if(c&&c.setAttribute)c.setAttribute('aria-invalid',m?'true':'false')}
function check(k){var v;if(k==='wijze'){v=f.querySelector('input[name=wijze]:checked');setErr(k,v?'':MSG[k]);return !!v}
 var el=f.elements[k];v=(el.value||'').trim();var ok=k==='email'?/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v):v.length>0;setErr(k,ok?'':MSG[k]);return ok}
f.addEventListener('change',function(e){if(e.target.name==='wijze'){plaats.hidden=e.target.value!=='bezorgen';check('wijze')}});
['bedrijf','naam','email','soorten'].forEach(function(k){f.elements[k].addEventListener('blur',function(){if(this.value.trim()||this.getAttribute('aria-invalid')==='true')check(k)})});
f.addEventListener('submit',function(e){e.preventDefault();var first=null;['bedrijf','naam','email','soorten','wijze'].forEach(function(k){if(!check(k)&&!first)first=k});
 if(first){var t=first==='wijze'?f.querySelector('input[name=wijze]'):f.elements[first];t.focus();return}
 btn.disabled=true;btn.firstChild.textContent='Bezig met verzenden…';
 setTimeout(function(){box.classList.add('gh-sent');var d=box.querySelector('.gh-done');d.focus();btn.disabled=false;btn.firstChild.textContent='Vraag een offerte aan'},700)});
})();</script>'''

MAIN = '<main id="main" tabindex="-1" class="ghm">' + HEAD + GET + VAR + STEP + FAQ + REQ + '</main>'
s = head + MAIN + tail


def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), a[:70]); s = s.replace(a, b)


# as on garantie.html: the homepage anchors become links to the homepage, the logo goes home; the Groothandel links lead to
# this page (in the header the current page)
parts = re.split(r'(<script\b.*?</script>)', s, flags=re.S)
for k in range(0, len(parts), 2):
    for a in ['#waarom', '#kweker', '#assortiment', '#hoe', '#haag']:
        parts[k] = re.sub(r'href="' + a + r'"(?![^>]*data-page)', f'href="index.html{a}"', parts[k])
    parts[k] = parts[k].replace('<a href="/" data-home ', '<a href="index.html" ')
    parts[k] = parts[k].replace('href="/groothandel" data-page="Groothandel"', 'href="groothandel.html" aria-current="page"')
s = ''.join(parts)
noise = re.search(r'url\("data:image/svg\+xml;utf8,[^"]+"\)', (D / 'tools' / 'fd-podpis.css').read_text()).group(0)
rep('</head>', '<style id="groothandel-css">.ghm{--gh-noise:' + noise + '}\n' + (D / 'tools' / 'groothandel.css').read_text() + '</style></head>')
rep('</body>', JS + '</body>')
s = re.sub(r'<title>[^<]*</title>', '<title>Groothandel rhododendrons van de kweker | Top Rhododendrons</title>'
           '<meta name="description" content="Groothandel in rhododendrons, rechtstreeks van de kweker in Otterlo. Zeven soorten, '
           '40 tot 225 cm, vers gerooid met kluit. Vraag een offerte aan.">', s, count=1)
(D / 'groothandel.html').write_text(s)
print('ok', len(s))
