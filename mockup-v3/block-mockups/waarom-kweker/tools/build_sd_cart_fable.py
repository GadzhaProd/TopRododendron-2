# Mockup tool (not site code): sd-cart-fable.html = the main mockup with an add-to-cart control on the seven variety cards
# (owner, 16 Nov: "a cart icon and a quantity on the cards", and keep the cards clean). Fable's own proposal, next to the
# coordinator's options A/B/C in sd-cart.html.
# The idea: every variety has four sizes at four prices, so the card carries ONE round cart button and nothing else;
# the size, the quantity and the total live in one small panel that the button opens (a popover from 768 px, a bottom
# sheet on phone). The smallest size is preselected, so the quick path is two taps and nobody buys a size unseen.
#   html.fc-1  the button on the price line, right of "vanaf € …" (recommended)
#   html.fc-2  the button on the photo, bottom right corner; the text block stays exactly as it is now
# The card is no longer one <a>: the name carries a stretched link, the button sits above it (no nested interactive
# content). The article itself is now the subgrid item, with the same row and column spans as the old <a>.
# Prices per size from src/data/content.ts. All new Dutch copy is a DRAFT.
# Usage: python3 tools/build_sd_cart_fable.py [dir]
import re, pathlib, sys, html
D = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
s = (D / 'index.html').read_text()
def rep(a, b):
    global s
    assert s.count(a) == 1, (s.count(a), a[:70]); s = s.replace(a, b)

A, B, C = '29,45,65,89', '27,42,60,82', '22,35,50,70'
PRICES = {'nova-zembla': A, 'catawbiense-grandiflorum': A, 'roseum-elegans': B, 'catawbiense-boursault': B,
          'cunninghams-white': '25,39,55,75', 'ponticum-roseum': C, 'ponticum': C}

CART = ('<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="9" cy="20" r="1.2"/><circle cx="18" cy="20" r="1.2"/>'
        '<path d="M2.5 3.5h2.2l2.5 11.2a1.6 1.6 0 0 0 1.6 1.3h8.9a1.6 1.6 0 0 0 1.6-1.2l1.5-6.6H5.9"/></svg>')

card = re.compile(r'<article class="sd-it"><a href="#assortiment" aria-label="([^"]*)">(<div class="sd-ph"><img src="img/([a-z-]+)-2-sm\.webp"[^>]*></div>)'
                  r'<h3>(.*?)</h3>(<p class="sd-b">.*?</p>)(<p class="sd-pr">.*?</p>)</a></article>')
def mk(m):
    label, ph, slug, name, bloom, price = m.groups()
    return (f'<article class="sd-it" data-name="{name}" data-img="img/{slug}-2-sm.webp" data-prices="{PRICES[slug]}">{ph}'
            f'<h3><a href="#assortiment" aria-label="{label}">{name}</a></h3>{bloom}'
            f'{price}<button type="button" class="fc-btn" aria-haspopup="dialog" '
            f'aria-label="{name}: maat kiezen en in winkelwagen leggen">{CART}<span class="fc-n" hidden></span></button></article>')
s, n = card.subn(mk, s)
assert n == 7, n

SIZES = ['40–60', '60–80', '80–100', '100–120']
rows = ''.join(f'<label class="fc-r"><input type="radio" name="fc-m" value="{i}"><span class="fc-l">{z}&nbsp;cm</span>'
               f'<span class="fc-p"></span></label>' for i, z in enumerate(SIZES))
DLG = ('<dialog class="fc-dlg" id="fc-dlg" aria-labelledby="fc-t"><form class="fc-f" method="dialog">'
       '<div class="fc-hd"><img class="fc-th" alt="" width="48" height="60"><div class="fc-tt"><h2 id="fc-t"></h2><p>Alle maten met kluit</p></div>'
       '<button type="button" class="fc-x" aria-label="Sluiten"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg></button></div>'
       '<div class="fc-pick"><fieldset class="fc-sz"><legend>Kies een maat</legend>' + rows + '</fieldset>'
       '<div class="fc-q"><span class="fc-ql" id="fc-ql">Aantal</span><div class="fc-st" role="group" aria-labelledby="fc-ql">'
       '<button type="button" class="fc-m" aria-label="Eén minder"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 12h12"/></svg></button>'
       '<input class="fc-in" type="text" inputmode="numeric" pattern="[0-9]*" maxlength="2" value="1" aria-labelledby="fc-ql" autocomplete="off">'
       '<button type="button" class="fc-pl" aria-label="Eén meer"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 12h12M12 6v12"/></svg></button></div>'
       '<p class="fc-tot" aria-live="polite">Totaal <b></b></p></div>'
       '<button type="submit" class="fc-add">In winkelwagen</button></div>'
       '<div class="fc-done" hidden><p class="fc-ok" role="status" tabindex="-1"><b>In uw winkelwagen</b><span></span><span></span></p>'
       '<div class="fc-act"><button type="button" class="fc-go">Verder kijken</button><a class="fc-add" href="#">Naar winkelwagen</a></div></div>'
       '</form></dialog>')

JS = r'''<script>(function(){
var dlg=document.getElementById('fc-dlg');if(!dlg||!dlg.showModal)return;
var q=function(s){return dlg.querySelector(s)},radios=[].slice.call(dlg.querySelectorAll('input[name="fc-m"]')),inp=q('.fc-in'),
    pick=q('.fc-pick'),done=q('.fc-done'),mq=matchMedia('(max-width:767px)'),cur=null,prices=[],y0=0;
function qty(){var n=parseInt(inp.value,10);return isNaN(n)||n<1?1:Math.min(n,99)}
function sel(){return +radios.filter(function(r){return r.checked})[0].value}
function tot(){q('.fc-tot b').textContent='€ '+prices[sel()]*qty();q('.fc-m').disabled=qty()<=1;q('.fc-pl').disabled=qty()>=99}
function place(){if(mq.matches){dlg.style.left=dlg.style.top='';return}
  var r=cur.querySelector('.fc-btn').getBoundingClientRect(),w=dlg.offsetWidth,h=dlg.offsetHeight,vw=document.documentElement.clientWidth,vh=innerHeight,
      l=Math.max(12,Math.min(r.right-w,vw-w-12)),t=r.bottom+10;
  if(t+h>vh-12){t=r.top-10-h;if(t<60)t=Math.max(60,vh-12-h)}
  dlg.style.left=l+'px';dlg.style.top=t+'px'}
function open(card){cur=card;prices=card.getAttribute('data-prices').split(',').map(Number);
  q('#fc-t').textContent=card.getAttribute('data-name');q('.fc-th').src=card.getAttribute('data-img');
  radios.forEach(function(r,i){r.checked=i===0;r.parentNode.querySelector('.fc-p').textContent='€ '+prices[i]});
  inp.value=1;pick.hidden=false;done.hidden=true;tot();
  dlg.showModal();radios[0].focus();place();y0=scrollY;if(mq.matches)document.documentElement.style.overflow='hidden'}
[].slice.call(document.querySelectorAll('.sd-it .fc-btn')).forEach(function(b){b.addEventListener('click',function(){open(b.closest('.sd-it'))})});
radios.forEach(function(r){r.addEventListener('change',tot)});
q('.fc-m').addEventListener('click',function(){inp.value=qty()-1;tot()});
q('.fc-pl').addEventListener('click',function(){inp.value=qty()+1;tot()});
inp.addEventListener('input',function(){inp.value=inp.value.replace(/\D/g,'');tot()});
inp.addEventListener('blur',function(){inp.value=qty();tot()});
q('.fc-x').addEventListener('click',function(){dlg.close()});
q('.fc-go').addEventListener('click',function(){dlg.close()});
dlg.addEventListener('click',function(e){if(e.target===dlg)dlg.close()});
dlg.addEventListener('close',function(){document.documentElement.style.overflow=''});
addEventListener('scroll',function(){if(dlg.open&&!mq.matches&&Math.abs(scrollY-y0)>60)dlg.close()},{passive:true});
addEventListener('resize',function(){if(dlg.open)place()});
q('.fc-f').addEventListener('submit',function(e){e.preventDefault();var n=qty(),i=sel(),name=cur.getAttribute('data-name'),
  size=radios[i].parentNode.querySelector('.fc-l').textContent,bd=cur.querySelector('.fc-n'),all=(+bd.textContent||0)+n;
  bd.textContent=all;bd.hidden=false;
  cur.querySelector('.fc-btn').setAttribute('aria-label',name+': '+all+' in uw winkelwagen. Nog een maat kiezen');
  var sp=dlg.querySelectorAll('.fc-ok span');sp[0].textContent=n+' × '+name+', '+size;sp[1].textContent='€ '+prices[i]*n;
  pick.hidden=true;done.hidden=false;place();q('.fc-ok').focus()});
})();</script>'''

CSS = r'''
/* ===== add to cart on the variety cards · Fable's proposal (review 16 Nov) ===== */
body{padding-top:48px}header.fixed{top:48px}#hero{min-height:calc(100svh - 48px)}
/* the article is the subgrid item now (it was the <a>); same row and column spans at every breakpoint */
.sd-it{display:grid;grid-row:span 4;grid-template-rows:subgrid;row-gap:0;padding-bottom:clamp(40px,3.6vw,56px);position:relative;border-radius:22px}
.sd-it > *{grid-column:1}
.sd-ph{grid-row:1}.sd-it h3{grid-row:2}.sd-b{grid-row:3}.sd-pr,.fc-btn{grid-row:4}
.sd-it h3 a{display:block}
.sd-it h3 a::after{content:"";position:absolute;inset:0;border-radius:22px}
.sd-it h3 a:focus-visible{outline:none}
.sd-it h3 a:focus-visible::after{outline:2px solid var(--moss);outline-offset:4px}
.sd-it:has(h3 a:hover) .sd-ph img{transform:scale(1.03)}
.sd-it:has(h3 a:hover) h3{color:var(--moss)}
@media (max-width:1279px){.sd-it{grid-column:span 2}.sd-it:nth-child(5){grid-column:2 / span 2}}
@media (max-width:767px){.sd-it:nth-child(5){grid-column:span 2}.sd-it:nth-child(7){grid-column:2 / span 2}}
@media (max-width:599px){.sd-it{grid-row:span 3;padding-bottom:28px}.sd-pr,.fc-btn{grid-row:3}}

/* the round button shares the price row: right of the price, over the free end of that line. The row gets 6 px of air
   above and the size line 6 px more, so the 40 px circle touches neither the bloom line nor the size line on the
   narrowest cards (154 px); the card grows by 12 px */
html.fc-1 .sd .sd-pr{margin-top:6px}
html.fc-1 .sd-s{margin-top:9px}
html.fc-1 .fc-btn{--lh:calc(clamp(24px,2vw,29px)*1.1);justify-self:end;align-self:start;margin-top:calc(6px + (var(--lh) - 40px)/2)}
@media (min-width:1280px){html.fc-1 .fc-btn{--lh:calc(clamp(21px,1.6vw,26px)*1.1)}}
@media (max-width:999px){html.fc-1 .fc-btn{--lh:25.3px}}
@media (max-width:599px){html.fc-1 .fc-btn{--lh:24.2px}}
.fc-btn{position:relative;z-index:1;display:grid;place-items:center;width:40px;height:40px;padding:0;border-radius:50%;
  border:1px solid rgba(20,20,19,.6);background:transparent;color:var(--ink);cursor:pointer;-webkit-tap-highlight-color:transparent;
  transition:background-color .2s ease,color .2s ease,border-color .2s ease}
.fc-btn::before{content:"";position:absolute;inset:-3px}   /* 46 px touch target around the 40 px circle */
.fc-btn svg,.fc-dlg svg{width:20px;height:20px;fill:none;stroke:currentColor;stroke-width:1.6;stroke-linecap:round;stroke-linejoin:round}
.fc-btn svg circle{fill:currentColor;stroke:none}
.fc-btn:hover{background:var(--ink);border-color:var(--ink);color:#fff}
.fc-btn:focus-visible{outline:2px solid var(--moss);outline-offset:3px}
.fc-n{position:absolute;top:-5px;right:-5px;min-width:19px;height:19px;padding:0 5px;border-radius:999px;background:var(--moss);color:#fff;
  font:700 11.5px/19px Manrope,system-ui,sans-serif;text-align:center;font-variant-numeric:tabular-nums;box-shadow:0 0 0 2px #e9ecdd}
.fc-n[hidden]{display:none}

/* state 2: the button on the photo, bottom right; the price row is exactly the current one */
html.fc-2 .fc-btn{grid-row:1;justify-self:end;align-self:end;margin:0 10px 10px 0;border-color:rgba(20,20,19,.16);background:#fff;box-shadow:0 2px 10px rgba(20,20,19,.22)}
html.fc-2 .fc-btn:hover{background:var(--ink);border-color:var(--ink)}
html.fc-2 .fc-btn:focus-visible{outline-color:#fff;box-shadow:0 0 0 5px var(--moss)}
html.fc-2 .fc-n{box-shadow:0 0 0 2px #fff}
@media (max-width:599px){html.fc-2 .fc-btn{margin:0 8px 8px 0}}

/* ---------- the panel: a popover from 768 px, a bottom sheet on phone ---------- */
.fc-dlg{position:fixed;inset:auto;margin:0;padding:0;width:328px;max-width:calc(100vw - 24px);max-height:calc(100dvh - 72px);overflow:auto;
  border:1px solid var(--line);border-radius:20px;background:#fbfaf8;color:var(--ink);font-family:Manrope,system-ui,sans-serif;
  box-shadow:0 28px 64px -16px rgba(20,20,19,.34),0 2px 8px rgba(20,20,19,.06)}
.fc-dlg::backdrop{background:rgba(20,20,19,.08)}
.fc-f{padding:16px}
.fc-dlg :is(h2,p){margin:0}
.fc-hd{display:grid;grid-template-columns:auto minmax(0,1fr) auto;gap:12px;align-items:center}
.fc-th{width:48px;height:60px;border-radius:10px;object-fit:cover;background:#dcd9d0}
.fc-tt h2{font-size:18px;line-height:1.2;font-weight:600;letter-spacing:-.02em}
.fc-tt p{margin-top:3px;font-size:13.5px;line-height:1.4;color:var(--ink2)}
.fc-x{display:grid;place-items:center;width:44px;height:44px;margin:-6px -8px 0 0;align-self:start;padding:0;border:0;border-radius:50%;background:transparent;color:var(--ink);cursor:pointer}
.fc-x:hover{background:rgba(20,20,19,.07)}
.fc-dlg :is(button,a,input):focus-visible{outline:2px solid var(--moss);outline-offset:2px}
.fc-sz{margin:16px 0 0;padding:0;border:0;display:grid;gap:6px;min-width:0}
.fc-sz legend{padding:0;margin-bottom:8px;font-size:14px;font-weight:600;color:var(--ink)}
.fc-r{display:grid;grid-template-columns:auto 1fr auto;align-items:center;gap:10px;min-height:46px;padding:0 14px 0 12px;border:1px solid var(--line);border-radius:12px;
  font-size:15px;cursor:pointer}
.fc-r input{width:18px;height:18px;margin:0;accent-color:var(--moss)}
.fc-r input:focus-visible{outline:none}
.fc-r:has(input:focus-visible){outline:2px solid var(--moss);outline-offset:2px}
.fc-r:hover{border-color:#8d8b83}
.fc-r:has(input:checked){border-color:var(--moss);box-shadow:inset 0 0 0 1px var(--moss);background:#eef0e7}
.fc-p{font-weight:600;font-variant-numeric:tabular-nums}
.fc-q{margin-top:16px;display:grid;grid-template-columns:auto auto 1fr;align-items:center;gap:12px}
.fc-ql{font-size:14px;font-weight:600}
.fc-st{display:inline-flex;align-items:center;height:44px;border:1px solid rgba(20,20,19,.6);border-radius:999px}
.fc-st button{display:grid;place-items:center;width:44px;height:42px;padding:0;border:0;border-radius:999px;background:transparent;color:var(--ink);cursor:pointer}
.fc-st button:hover:not(:disabled){background:rgba(20,20,19,.07)}
.fc-st button:disabled{color:#a3a199;cursor:default}
.fc-st svg{width:16px;height:16px;stroke-width:1.8}
.fc-in{width:30px;height:36px;padding:0;border:0;border-radius:6px;background:transparent;color:var(--ink);text-align:center;font:600 16px/1 Manrope,system-ui,sans-serif;font-variant-numeric:tabular-nums}
.fc-tot{justify-self:end;font-size:14px;color:var(--ink2);white-space:nowrap}
.fc-tot b{margin-left:4px;font-size:20px;font-weight:600;letter-spacing:-.02em;color:var(--moss);font-variant-numeric:tabular-nums}
.fc-add{display:flex;align-items:center;justify-content:center;width:100%;height:52px;margin-top:16px;padding:0 24px;border:0;border-radius:999px;background:var(--moss);color:#fff;
  font:600 15px/1 Manrope,system-ui,sans-serif;text-decoration:none;cursor:pointer;transition:background-color .2s ease}
.fc-add:hover{background:#2c3526}
.fc-done{margin-top:16px}
.fc-ok{padding:14px 16px;border-radius:12px;background:#eef0e7;font-size:15px;line-height:1.45;color:var(--ink2);outline:none}
.fc-ok b{display:block;font-weight:600;color:var(--ink)}
.fc-ok span{display:block}
.fc-ok span + span{font-weight:600;color:var(--moss);font-variant-numeric:tabular-nums}
.fc-act{display:grid;grid-template-columns:auto minmax(0,1fr);gap:8px;margin-top:16px}
.fc-act .fc-add{margin-top:0;padding:0 12px;white-space:nowrap}
.fc-go{height:52px;padding:0 18px;white-space:nowrap;border:1px solid rgba(20,20,19,.6);border-radius:999px;background:transparent;color:var(--ink);font:500 15px/1 Manrope,system-ui,sans-serif;cursor:pointer}
.fc-go:hover{background:var(--ink);color:#fff}
[hidden].fc-pick,[hidden].fc-done{display:none}
@media (max-width:767px){
  .fc-dlg{left:0;right:0;bottom:0;top:auto;width:100%;max-width:none;max-height:calc(100dvh - 56px);border-width:1px 0 0;border-radius:24px 24px 0 0}
  .fc-dlg::backdrop{background:rgba(20,20,19,.45)}
  .fc-f{padding:20px 20px calc(20px + env(safe-area-inset-bottom))}
  .fc-r{min-height:50px}
}
'''
rep('</head>', '<style id="sd-cart-fable">' + CSS + '</style></head>')
rep('<div id="root">', '<div class="rv" role="group" aria-label="Варианты"><div class="rv-g"><i>В корзину · Fable</i>'
    '<button type="button" data-g="fc" data-v="1" aria-pressed="true">1 · Иконка у цены</button>'
    '<button type="button" data-g="fc" data-v="2" aria-pressed="false">2 · Иконка на фото</button></div></div><div id="root">')
rep('</body>', DLG + JS + '</body>')
s = re.sub(r'<html lang="nl" class="([^"]*)">', lambda m: f'<html lang="nl" class="{m.group(1)} fc-1">', s, count=1)
s = s.replace('<title>Waarom wij · De kweker</title>', '<title>В корзину · Fable</title>', 1)
(D / 'sd-cart-fable.html').write_text(s)
print('ok', len(s))
