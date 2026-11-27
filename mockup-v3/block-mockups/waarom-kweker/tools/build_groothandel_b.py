# Mockup tool (not site code): groothandel-b.html, variant B of the wholesale page: "Stel uw partij samen" (tool-first).
# The owner compares it with variant A (groothandel.html, tools/build_groothandel.py; that page is not touched).
# Concept: the page is a calm working tool. All seven varieties with their sizes and open prices; a size becomes a line
# of the request list ("offertelijst") with a number; the list shows the total and whether the 25-plant lot is reached,
# and it is the first field of the request form. Phone: a bottom bar with the count opens the list as a sheet.
# Copy: docs/groothandel-tekst-2026-11-26.md, shortened and reordered for the tool; small labels in the same tone; no new facts.
# Sizes and prices: tools/calc3.py (SOORTEN): open consumer prices incl. btw, provisional. No money total is shown:
# the lot price is in the quote (idea from 21st.dev "Checkout Summary" by astralyxdev: an amount that is not known yet is
# named as such instead of shown as a false figure; no code copied).
# Header, cart, phone menu and footer come from the main mockup (index.html), as in variant A; A's stylesheet is reused
# (head, pill button, rows, questions, card, form) and tools/groothandel_b.css adds the tool.
# The form is a mockup: it checks the fields in the copy's words and shows the confirmation, nothing is sent.
# Usage: python3 tools/build_groothandel_b.py [dir]
import json, pathlib, re, sys
D = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
sys.path.insert(0, str(D / 'tools'))
from calc3 import SOORTEN, LOWS, TOPS  # noqa: E402

s = (D / 'index.html').read_text()
i = s.index('<main id="main"'); j = s.index('</main>') + len('</main>')
head, tail = s[:i], s[j:]
head = re.sub(r'<style id="calc3-css">.*?</style>', '', head, count=1, flags=re.S)
tail = re.sub(r'<script id="calc3-js">.*?</script>', '', tail, count=1, flags=re.S)

ARROW = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6" fill="none" stroke="currentColor" '
         'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>')
TEL = '<a href="tel:+31620104312">06&nbsp;20&nbsp;10&nbsp;43&nbsp;12</a>'
FACTS = ['Sinds 2001', '7 soorten', '40 tot 225&nbsp;cm', 'met kluit', '10.000 planten op voorraad']
SLUGS = ['nova-zembla', 'catawbiense-grandiflorum', 'cunninghams-white', 'catawbiense-boursault', 'roseum-elegans', 'ponticum', 'ponticum-roseum']
LOT = 25


def euro(x):
    return '€&nbsp;' + ('%.2f' % x).replace('.', ',')


# ---------- the head: compact, the field beside it; the tool starts right under it ----------
HEAD = ('<section class="in gh-head ghb-head" aria-labelledby="h-gh"><div class="ghb-head-t">'
        '<nav class="gh-crumb" aria-label="Kruimelpad"><a href="index.html">Home</a><span aria-hidden="true">/</span>'
        '<span aria-current="page">Groothandel</span></nav>'
        '<h1 id="h-gh"><span>Groothandel in rhododendrons.</span> <span>Rechtstreeks van de kweker.</span></h1>'
        '<p class="gh-lead">Groothandel voor hoveniers, tuinarchitecten, gemeenten en projectontwikkelaars: rhododendrons per partij, '
        '<span class="nb">vers gerooid</span> en met kluit.</p>'
        '<ul class="gh-facts" aria-label="In het kort">' + ''.join(f'<li>{f}</li>' for f in FACTS) + '</ul></div>'
        '<figure class="gh-photo ghb-photo"><img src="img/hero-field.jpg" alt="Ons rhododendronveld in bloei" width="2048" height="1143" '
        'fetchpriority="high" decoding="async"></figure></section>')

# ---------- the tool: the seven varieties with their sizes (left), the request list (right, sticky) ----------
DATA = []      # for the script: name and the sizes of each variety (key, label, price or None = on request)


def soort(k, name, prices, rng):
    sl = SLUGS[k]
    sizes = [(str(n), f'{LOWS[n]}–{TOPS[n]}&nbsp;cm', p) for n, p in enumerate(prices) if p is not None]
    if rng[1] > 120:
        sizes.append(('L', f'120–{rng[1]}&nbsp;cm', None))      # the large sizes: on request
    DATA.append({'n': name, 's': [[key, lab.replace('&nbsp;', ' ')] for key, lab, p in sizes]})
    chips = ''.join(
        f'<li><button type="button" class="ghb-chip{"" if p is not None else " big"}" data-act="toggle" data-k="{k}:{key}" aria-pressed="false">'
        f'<b>{lab}</b><span>{euro(p) if p is not None else "op aanvraag"}</span></button></li>' for key, lab, p in sizes)
    low = min(p for p in prices if p is not None)
    return (f'<li class="ghb-soort" data-v="{k}"><img src="img/{sl}-sm.webp" alt="" width="900" height="900" loading="lazy" decoding="async">'
            f'<div class="ghb-soort-h"><h3 id="s-{k}"><a href="soort-{sl}.html">{name}</a></h3>'
            f'<p>{rng[0]} tot {rng[1]}&nbsp;cm <span aria-hidden="true">·</span> vanaf {euro(low)} per plant</p></div>'
            f'<div class="ghb-soort-b"><ul class="ghb-chips" aria-labelledby="s-{k}">{chips}</ul>'
            f'<ul class="ghb-picked" data-picked="{k}" aria-label="Uw keuze: {name}" hidden></ul></div></li>')


SOORTEN_UL = '<ul class="ghb-soorten">' + ''.join(soort(k, n, p, r) for k, (n, p, r) in enumerate(SOORTEN)) + '</ul>'


def lijst(zone, hid, h='h3', cta=True, close=False):
    # the request list, three times from one state: beside the varieties (desktop), in the sheet (phone), in the form
    return (f'<div class="ghb-lijst" data-zone="{zone}">'
            + (f'<div class="ghb-lijst-h"><{h} id="{hid}" tabindex="-1">Uw offertelijst.</{h}>'
               + ('<button type="button" class="ghb-x" data-act="close" aria-label="Sluit de offertelijst"><svg viewBox="0 0 24 24" aria-hidden="true">'
                  '<path d="M6 6l12 12M18 6L6 18" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg></button>' if close else '')
               + '</div>' if hid else '')
            + '<p class="ghb-empty" data-o="empty">Uw lijst is nog leeg. Kies een soort en een maat; het aantal vult u daarna in.</p>'
              f'<ul class="ghb-lines" data-o="lines"{" aria-labelledby=" + chr(34) + hid + chr(34) if hid else " aria-label=" + chr(34) + "Uw offertelijst" + chr(34)}></ul>'
              '<div class="ghb-sum"><p class="ghb-tot"><span>Totaal</span><b data-o="total">0 planten</b></p>'
              '<div class="ghb-meter" aria-hidden="true"><i data-o="bar"></i></div>'
              '<p class="ghb-lot" data-o="lot"></p></div>'
            + ('<dl class="ghb-mini"><div><dt>Prijs</dt><dd>Partijprijs in de offerte, exclusief btw</dd></div>'
               '<div><dt>Offerte</dt><dd>Binnen één werkdag</dd></div></dl>'
               '<a class="gh-btn ghb-go" href="#offerte" data-act="go">Vraag een offerte aan' + ARROW + '</a>' if cta else '')
            + '</div>')


TOOL = ('<section class="gh-sec ghb-tool" id="partij" aria-labelledby="h-tool"><div class="in">'
        '<div class="ghb-tool-h"><h2 id="h-tool">Stel uw partij samen.</h2>'
        '<p class="gh-p">Kies per soort de maten en vul de aantallen in. Vanaf 25 planten krijgt u een partijprijs. '
        'U krijgt binnen één werkdag een offerte.</p></div>'
        '<div class="ghb-grid"><div class="ghb-left">' + SOORTEN_UL +
        '<p class="ghb-note">De prijzen zijn per plant en inclusief btw, bij een bestelling via de site. Uw partijprijs staat in de offerte, exclusief btw.</p>'
        '<div class="gh-big ghb-big"><h3>Grote maten</h3><p>Voor projecten die meteen volume vragen, hebben wij ook grote maten, '
        'van 120 tot 225&nbsp;cm. Die leveren wij op aanvraag. U kunt ze zelf uitzoeken op ons veld.</p></div></div>'
        '<aside class="ghb-side" aria-labelledby="h-lijst"><div class="gh-card ghb-card">' + lijst('side', 'h-lijst') + '</div>'
        '<p class="gh-tel ghb-side-tel">Liever overleggen? Bel ' + TEL + '</p></aside></div></div>'
        # phone and tablet: the bar with the count, and the list as a sheet
        '<button type="button" class="ghb-bar" data-act="open" aria-haspopup="dialog" hidden><span class="ghb-bar-t"><b>Offertelijst</b>'
        '<span data-o="barline"></span></span><span class="ghb-bar-a">Bekijk<svg viewBox="0 0 24 24" aria-hidden="true">'
        '<path d="M6 14l6-6 6 6" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></span></button>'
        '<dialog class="ghb-sheet" aria-labelledby="h-sheet"><div class="gh-card ghb-card">' + lijst('sheet', 'h-sheet', h='h2', close=True) + '</div></dialog>'
        '<p class="ghb-sr" role="status" aria-live="polite" data-o="say"></p></section>')

# ---------- the request: the list is the first field; then delivery, then who asks ----------
STEPS = [('Offerte', 'Binnen één werkdag, met de prijs per soort en maat, exclusief btw.'),
         ('Afspreken', 'Na uw akkoord kiezen wij samen de dag van bezorgen of afhalen.'),
         ('Ontvangen', 'Wij rooien vlak voor de levering, met kluit.')]


def field(fid, label, kind='input', req=True, hint='', wide=False, attrs=''):
    opt = '' if req else ' <i>(optioneel)</i>'
    desc = (f'h-{fid} ' if hint else '') + f'e-{fid}'
    ctl = (f'<textarea id="{fid}" name="{fid}" rows="3" aria-describedby="{desc}"{attrs}></textarea>' if kind == 'textarea'
           else f'<input id="{fid}" name="{fid}" type="{kind}"{" required" if req else ""} aria-describedby="{desc}"{attrs}>')
    return (f'<div class="gh-f{" w" if wide else ""}" data-f="{fid}"><label for="{fid}">{label}{opt}</label>{ctl}'
            + (f'<p class="gh-hint" id="h-{fid}">{hint}</p>' if hint else '') + f'<p class="gh-err" id="e-{fid}" aria-live="polite"></p></div>')


FORM = ('<form class="gh-form" novalidate>'
        '<fieldset class="gh-f w ghb-f-lijst" data-f="lijst"><legend>Soorten, maten en aantallen</legend>'
        + lijst('form', '', cta=False) +
        '<p class="ghb-add"><a href="#partij">Soort of maat toevoegen</a></p></fieldset>'
        + field('soorten', 'Toelichting <i data-o="opt">(optioneel)</i>', 'textarea',
                hint='Weet u het nog niet precies? Een schatting is genoeg. Bijvoorbeeld: 40&nbsp;× Nova Zembla, <span class="nb">60–80 cm</span>.', wide=True)
        + field('week', 'Gewenste levering', req=False, hint='Bijvoorbeeld: week 12, of maart.', wide=True)
        + '<fieldset class="gh-f w" data-f="wijze"><legend>Bezorgen of afhalen</legend><div class="gh-pick" role="radiogroup" aria-describedby="e-wijze">'
          '<label><input type="radio" name="wijze" value="bezorgen"><span>Bezorgen in Nederland</span></label>'
          '<label><input type="radio" name="wijze" value="afhalen"><span>Afhalen in Wekerom</span></label></div>'
          '<p class="gh-err" id="e-wijze" aria-live="polite"></p></fieldset>'
        + field('plaats', 'Plaats van levering', req=False, wide=True, attrs=' autocomplete="address-level2"').replace('data-f="plaats"', 'data-f="plaats" hidden')
        + field('bedrijf', 'Bedrijfsnaam', attrs=' autocomplete="organization"')
        + field('naam', 'Uw naam', attrs=' autocomplete="name"')
        + field('email', 'E-mailadres', 'email', attrs=' autocomplete="email"')
        + field('tel', 'Telefoonnummer', 'tel', req=False, hint='Handig als wij een vraag hebben over uw aanvraag.', attrs=' autocomplete="tel"')
        + '<div class="gh-send"><button class="gh-btn" type="submit">Vraag een offerte aan' + ARROW + '</button>'
          '<p class="gh-priv">Wij gebruiken uw gegevens alleen om uw aanvraag te beantwoorden. Lees onze <a href="/privacy" data-page="Privacy">privacyverklaring</a>.</p>'
          '<p class="gh-err" id="e-send" aria-live="polite"></p></div></form>'
        '<div class="gh-done" role="status" tabindex="-1"><h3>Uw aanvraag is ontvangen.</h3>'
        '<p>U krijgt binnen één werkdag een offerte per e-mail. Hebben wij eerst een vraag, dan bellen of mailen wij u.</p>'
        '<p>Liever meteen overleggen? Bel ' + TEL + '.</p></div>')
REQ = ('<section class="gh-sec" id="offerte" aria-labelledby="h-req"><div class="in"><div class="gh-card gh-two">'
       '<div class="gh-l"><h2 id="h-req">Vraag een offerte aan.</h2>'
       '<p class="gh-p">U krijgt een offerte met de prijs per soort en maat, rechtstreeks van de kwekerij. '
       'Minder dan 25 planten nodig? Die bestelt u <a href="index.html#assortiment">direct via de site</a>.</p>'
       '<ol class="ghb-steps" aria-label="Na uw aanvraag">' + ''.join(f'<li><h3>{t}</h3><p>{p}</p></li>' for t, p in STEPS) + '</ol>'
       '<p class="gh-tel">Of bel ' + TEL + '</p></div>'
       '<div class="gh-r gh-req">' + FORM + '</div></div></div></section>')

# ---------- the trust points and the questions, short, after the work ----------
ROWS = [('Rooien', 'Pas vlak voor de levering, met kluit.'),
        ('Bezorgen', 'Met eigen transport door heel Nederland, vanaf €&nbsp;75 per bestelling.'),
        ('Afhalen', 'Gratis, op ons veld in Wekerom.'),
        ('Betalen', 'Zakelijk op factuur.'),
        ('Plantenpaspoort', 'Bij elke partij.')]
GET = ('<section class="gh-sec" aria-labelledby="h-get"><div class="in gh-two"><div class="gh-l"><h2 id="h-get">U koopt bij de kweker zelf.</h2></div>'
       '<div class="gh-r"><dl class="gh-dl">' + ''.join(f'<div><dt>{t}</dt><dd>{d}</dd></div>' for t, d in ROWS) + '</dl></div></div></section>')
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

JS = r'''<script id="groothandel-b-js">(function(){
var root=document.querySelector('.ghm');if(!root)return;
var V=__DATA__,LOT=__LOT__,KEY='tr-offertelijst';
var lines=[];   // {k:"variety:size", n:number}; the order in which the visitor added them
try{var st=JSON.parse(sessionStorage.getItem(KEY)||'[]');if(Array.isArray(st))st.forEach(function(l){if(info(l.k)&&l.n>0)lines.push({k:String(l.k),n:Math.min(9999,Math.round(l.n))})})}catch(e){}
function info(k){var p=String(k).split(':'),v=V[+p[0]];if(!v)return null;for(var i=0;i<v.s.length;i++)if(v.s[i][0]===p[1])return{v:+p[0],name:v.n,size:v.s[i][1],big:p[1]==='L'};return null}
function find(k){for(var i=0;i<lines.length;i++)if(lines[i].k===k)return i;return -1}
function esc(t){return String(t).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/"/g,'&quot;')}
function pl(n){return n+(n===1?' plant':' planten')}
function total(){return lines.reduce(function(a,l){return a+l.n},0)}
var MIN='<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M3.5 8h9"/></svg>',PLUS='<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M3.5 8h9M8 3.5v9"/></svg>',
    DEL='<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 7l10 10M17 7L7 17"/></svg>';
function stepper(l,what){var k=esc(l.k),w=esc(what);
 return '<span class="ghb-step"><button type="button" data-act="dec" data-k="'+k+'" aria-label="'+w+': minder">'+MIN+'</button>'
  +'<input type="text" inputmode="numeric" autocomplete="off" maxlength="4" data-qty data-k="'+k+'" value="'+l.n+'" aria-label="Aantal planten, '+w+'">'
  +'<button type="button" data-act="inc" data-k="'+k+'" aria-label="'+w+': meer">'+PLUS+'</button></span>'
  +'<button type="button" class="ghb-del" data-act="del" data-k="'+k+'" aria-label="Verwijder '+w+'">'+DEL+'</button>'}
// a list is rebuilt only when its lines change; a new number is written into the fields that are there (the focus stays)
function fill(ul,sig,html){if(ul.getAttribute('data-sig')===sig){ul.querySelectorAll('[data-qty]').forEach(function(q){var i=find(q.getAttribute('data-k'));if(i>-1&&q.value!==String(lines[i].n))q.value=lines[i].n});return}
 ul.innerHTML=html;ul.setAttribute('data-sig',sig)}
function render(){
 var t=total(),n=lines.length,lot=t>=LOT;
 // the chips and the chosen sizes under each variety
 root.querySelectorAll('.ghb-chip').forEach(function(c){c.setAttribute('aria-pressed',find(c.getAttribute('data-k'))>-1?'true':'false')});
 root.querySelectorAll('[data-picked]').forEach(function(ul){var v=+ul.getAttribute('data-picked'),h='',sg='';
  V[v].s.forEach(function(sz){var i=find(v+':'+sz[0]);if(i<0)return;var l=lines[i];sg+=l.k+'|';
   h+='<li><span class="ghb-l-t"><b>'+esc(sz[1])+'</b>'+(sz[0]==='L'?'<span>grote maat, op aanvraag</span>':'')+'</span>'+stepper(l,V[v].n+', '+sz[1])+'</li>'});
  fill(ul,sg,h);ul.hidden=!h});
 // the list, in its three places
 var h='',sig=lines.map(function(l){return l.k}).join('|');lines.forEach(function(l){var f=info(l.k);
  h+='<li><span class="ghb-l-t"><b>'+esc(f.name)+'</b><span>'+esc(f.size)+(f.big?', op aanvraag':'')+'</span></span>'+stepper(l,f.name+', '+f.size)+'</li>'});
 var lotText=t===0?'Vanaf '+LOT+' planten krijgt u een partijprijs.':lot?'Partijprijs bereikt. Hoe groter de partij, hoe lager de prijs per plant.'
   :'Nog '+pl(LOT-t)+' tot de partijprijs, vanaf '+LOT+' planten.';
 root.querySelectorAll('.ghb-lijst').forEach(function(box){
  box.classList.toggle('is-empty',!n);box.classList.toggle('is-lot',lot);
  fill(box.querySelector('[data-o=lines]'),sig,h);
  box.querySelector('[data-o=total]').textContent=pl(t);
  box.querySelector('[data-o=lot]').textContent=lotText;
  box.querySelector('[data-o=bar]').style.width=Math.min(100,Math.round(t/LOT*100))+'%'});
 bar.querySelector('[data-o=barline]').textContent=pl(t)+(lot?' · partijprijs bereikt':' · nog '+(LOT-t)+' tot de partijprijs');
 var opt=root.querySelector('[data-o=opt]');if(opt)opt.hidden=!n;
 root.classList.toggle('ghb-has',n>0);showBar();
 try{sessionStorage.setItem(KEY,JSON.stringify(lines))}catch(e){}
}
function say(m){var s=root.querySelector('[data-o=say]');s.textContent='';setTimeout(function(){s.textContent=m},60)}
// after a change the markup is rebuilt: put the focus back on the same control in the same place
function keep(fn){var a=document.activeElement,zone=a&&a.closest&&a.closest('[data-zone],.ghb-soort'),sel=null;
 if(zone&&a.getAttribute('data-k'))sel=(a.hasAttribute('data-qty')?'[data-qty]':'[data-act="'+a.getAttribute('data-act')+'"]')+'[data-k="'+a.getAttribute('data-k')+'"]';
 fn();render();
 if(!zone||!sel)return;var el=zone.querySelector(sel);
 if(!el&&zone.classList.contains('ghb-soort'))el=zone.querySelector('.ghb-chip[data-k="'+a.getAttribute('data-k')+'"]');
 if(!el)el=zone.querySelector('.ghb-lines button[data-act=del]')||zone.querySelector('[id^=h-]')||root.querySelector('.ghb-add a');
 if(el&&el!==document.activeElement)el.focus({preventScroll:true})}
function setN(k,n){var i=find(k);if(i<0)return;n=Math.max(1,Math.min(9999,n));lines[i].n=n}
var bar=root.querySelector('.ghb-bar'),sheet=root.querySelector('.ghb-sheet'),req=document.getElementById('offerte'),reqIn=false;
function showBar(){bar.hidden=!(lines.length&&!reqIn);document.documentElement.classList.toggle('ghb-bar-on',!bar.hidden)}
if('IntersectionObserver' in window)new IntersectionObserver(function(e){reqIn=e[0].isIntersecting;showBar()},{rootMargin:'0px 0px -30% 0px'}).observe(req);
function closeSheet(){if(sheet.open)sheet.close()}
sheet.addEventListener('click',function(e){if(e.target===sheet)closeSheet()});
sheet.addEventListener('close',function(){if(!bar.hidden)bar.focus({preventScroll:true})});
if(window.matchMedia)window.matchMedia('(min-width:1024px)').addEventListener('change',function(m){if(m.matches)closeSheet()});
root.addEventListener('click',function(e){var b=e.target.closest('[data-act]');if(!b||!root.contains(b))return;
 var act=b.getAttribute('data-act'),k=b.getAttribute('data-k'),f=k&&info(k),i=k?find(k):-1;
 if(act==='open'){if(sheet.showModal)sheet.showModal();else sheet.setAttribute('open','');return}
 if(act==='close'){closeSheet();return}
 if(act==='go'){closeSheet();return}
 if(!f)return;
 if(act==='toggle'){keep(function(){if(i>-1)lines.splice(i,1);else lines.push({k:k,n:f.big?5:10})});
  say(f.name+', '+f.size+(i>-1?' verwijderd':' toegevoegd')+'. Totaal '+pl(total())+'.');
  if(i<0){var q=b.closest('.ghb-soort').querySelector('[data-qty][data-k="'+k+'"]');if(q&&window.matchMedia('(hover:hover)').matches){q.focus({preventScroll:true});q.select()}}
  return}
 if(i<0)return;
 if(act==='del'){keep(function(){lines.splice(i,1)});say(f.name+', '+f.size+' verwijderd. Totaal '+pl(total())+'.');if(!lines.length)closeSheet();return}
 // plus and minus go in fives (a lot is counted in fives and tens); under five by one
 var n=lines[i].n;
 if(act==='inc')keep(function(){setN(k,(Math.floor(n/5)+1)*5)});
 if(act==='dec')keep(function(){setN(k,n>5?(Math.ceil(n/5)-1)*5:n-1)});
});
root.addEventListener('change',function(e){var q=e.target;if(!q.hasAttribute||!q.hasAttribute('data-qty'))return;
 var k=q.getAttribute('data-k'),n=parseInt(String(q.value).replace(/\D/g,''),10),i=find(k);if(i<0)return;
 keep(function(){setN(k,isNaN(n)?lines[i].n:n)})});
root.addEventListener('keydown',function(e){var q=e.target;if(!q.hasAttribute||!q.hasAttribute('data-qty'))return;
 if(e.key==='Enter'){e.preventDefault();q.dispatchEvent(new Event('change',{bubbles:true}));q.select()}
 if(e.key==='ArrowUp'||e.key==='ArrowDown'){e.preventDefault();var kk=q.getAttribute('data-k'),v=parseInt(q.value,10)||0;keep(function(){setN(kk,v+(e.key==='ArrowUp'?1:-1))})}});

// the form: a mockup. It checks the required fields in the copy's words, shows "Bezig met verzenden…" and then the confirmation
var box=root.querySelector('.gh-req'),f=box.querySelector('form'),btn=f.querySelector('button[type=submit]');
var MSG={bedrijf:'Vul uw bedrijfsnaam in.',naam:'Vul uw naam in.',email:'Vul een geldig e-mailadres in.',soorten:'Vul in welke soorten u zoekt en hoeveel planten.',wijze:'Kies bezorgen of afhalen.'};
var plaats=f.querySelector('[data-f=plaats]');
function setErr(k,m){var e=document.getElementById('e-'+k);if(e)e.textContent=m||'';var c=k==='wijze'?f.querySelector('.gh-pick'):f.elements[k];if(c&&c.setAttribute)c.setAttribute('aria-invalid',m?'true':'false')}
function check(k){var v;if(k==='wijze'){v=f.querySelector('input[name=wijze]:checked');setErr(k,v?'':MSG[k]);return !!v}
 var el=f.elements[k];v=(el.value||'').trim();var ok=k==='email'?/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v):k==='soorten'?(lines.length>0||v.length>0):v.length>0;setErr(k,ok?'':MSG[k]);return ok}
f.addEventListener('change',function(e){if(e.target.name==='wijze'){plaats.hidden=e.target.value!=='bezorgen';check('wijze')}});
['bedrijf','naam','email','soorten'].forEach(function(k){f.elements[k].addEventListener('blur',function(){if(this.value.trim()||this.getAttribute('aria-invalid')==='true')check(k)})});
f.addEventListener('submit',function(e){e.preventDefault();var first=null;['soorten','wijze','bedrijf','naam','email'].forEach(function(k){if(!check(k)&&!first)first=k});
 if(first){var t=first==='wijze'?f.querySelector('input[name=wijze]'):f.elements[first];t.focus();return}
 btn.disabled=true;btn.firstChild.textContent='Bezig met verzenden…';
 setTimeout(function(){box.classList.add('gh-sent');var d=box.querySelector('.gh-done');d.focus();btn.disabled=false;btn.firstChild.textContent='Vraag een offerte aan';
  lines=[];render()},700)});
var _r=render;render=function(){_r();if(lines.length&&f.elements.soorten.getAttribute('aria-invalid')==='true')check('soorten')};
render();
})();</script>'''
JS = JS.replace('__DATA__', json.dumps(DATA, ensure_ascii=False)).replace('__LOT__', str(LOT))

MAIN = '<main id="main" tabindex="-1" class="ghm ghb">' + HEAD + TOOL + REQ + GET + FAQ + '</main>'
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
    parts[k] = parts[k].replace('href="/groothandel" data-page="Groothandel"', 'href="groothandel-b.html" aria-current="page"')
s = ''.join(parts)
noise = re.search(r'url\("data:image/svg\+xml;utf8,[^"]+"\)', (D / 'tools' / 'fd-podpis.css').read_text()).group(0)
rep('</head>', '<style id="groothandel-css">.ghm{--gh-noise:' + noise + '}\n' + (D / 'tools' / 'groothandel.css').read_text() + '</style>'
    '<style id="groothandel-b-css">' + (D / 'tools' / 'groothandel_b.css').read_text() + '</style></head>')
rep('</body>', JS + '</body>')
s = re.sub(r'<title>[^<]*</title>', '<title>Groothandel rhododendrons van de kweker | Top Rhododendrons</title>'
           '<meta name="description" content="Groothandel in rhododendrons, rechtstreeks van de kweker in Otterlo. Zeven soorten, '
           '40 tot 225 cm, vers gerooid met kluit. Vraag een offerte aan.">', s, count=1)
(D / 'groothandel-b.html').write_text(s)
print('ok', len(s))
