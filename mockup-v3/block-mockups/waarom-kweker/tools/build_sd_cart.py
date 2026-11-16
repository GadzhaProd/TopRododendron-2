# Mockup tool (not site code): sd-cart.html = the main mockup with an add-to-cart control and a quantity on the variety
# cards (owner, 16 Nov: "an add-to-cart icon and a quantity on the cards", instead of the delivery line). Every variety has
# four sizes with different prices (content.ts), so the options differ in how the size is chosen:
#   html.ct-a  быстро в корзину: under the price a "− 1 +" stepper and a round cart button; it adds the 40–60 cm size the
#              card shows
#   html.ct-b  размер на карточке: a size select (the price follows it), then the stepper and the cart button
#   html.ct-c  значок открывает выбор: only a round cart button on the price line; it opens a small panel with the four
#              sizes and prices, the stepper and "In winkelwagen" (a popover on desktop, a bottom sheet on phone)
# The card link moves to the name and is stretched over the card (::after), so the controls are not inside a link.
# Components looked up on 21st.dev (minimal stepper, pill number field, add-to-cart pill) and redrawn in the page's style.
# Usage: python3 tools/build_sd_cart.py [dir]
import re, json, html, pathlib, sys
D = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.').resolve()
s = (D / 'index.html').read_text()
ts = (D.parent.parent / 'src' / 'data' / 'content.ts').read_text()
e = html.escape
def rep(a, b):
    global s
    assert s.count(a) == 1, (s.count(a), a[:70]); s = s.replace(a, b)

# sizes per slug from content.ts
consts = {m.group(1): m.group(2) for m in re.finditer(r'const (sizes\w+): Size\[\] = (\[.*?\])\n', ts)}
SIZES = {}
for m in re.finditer(r"slug: '([\w-]+)'.*?sizes: (sizes\w+|\[.*?\]),", ts[ts.index('export const varieties'):ts.index('export const bySlug')], re.S):
    raw = consts.get(m.group(2), m.group(2))
    SIZES[m.group(1)] = [(a, b.replace(',00', '')) for a, b in re.findall(r"label: '([^']+)', price: '([^']+)'", raw)]
assert len(SIZES) == 7 and all(len(v) == 4 for v in SIZES.values()), SIZES

BAG = ('<svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 7h12l-1 13H7L6 7Z"/><path d="M9 7V6a3 3 0 0 1 6 0v1"/>'
       '<path d="M12 11v5M9.5 13.5h5"/></svg>')
CHEV = '<svg class="ic ch" viewBox="0 0 24 24" aria-hidden="true"><path d="m7 10 5 5 5-5"/></svg>'
def qty(name):
    return ('<div class="qty" role="group" aria-label="Aantal ' + e(name) + '">'
            '<button type="button" class="q-m" aria-label="Eén minder" aria-disabled="true">−</button>'
            '<output aria-live="polite">1</output><button type="button" class="q-p" aria-label="Eén meer">+</button></div>')

def card(m):
    ph, name, bloom = m.group(1), m.group(2), m.group(3)
    slug = re.search(r'img/([\w-]+)-2-sm', ph).group(1)
    sz = SIZES[slug]; p0 = sz[0][1]; nm = html.unescape(name)
    opts = ''.join('<option value="' + p + '">' + l.replace(' cm', '&nbsp;cm') + '</option>' for l, p in sz)
    return ('<article class="sd-it" data-name="' + e(nm) + '" data-sizes="' + e(json.dumps(sz, ensure_ascii=False)) + '">' + ph +
            '<h3><a class="sd-lk" href="#assortiment">' + name + '</a></h3>' + bloom +
            '<p class="sd-pr"><span class="sd-v">vanaf</span><b class="sd-p">€&nbsp;' + p0 + '</b>'
            '<span class="sd-s"><span class="s-sz">40–60&nbsp;cm, </span>met kluit</span>'
            '<button type="button" class="c-btn cart" aria-haspopup="dialog" aria-label="Kies maat en aantal: ' + e(nm) + '">' + BAG + '</button></p>'
            '<div class="ct">'
            '<label class="sz"><span class="vh">Maat ' + e(nm) + '</span><select>' + opts + '</select>' + CHEV + '</label>'
            '<div class="ct-row">' + qty(nm) +
            '<button type="button" class="cart a-btn" aria-label="' + e(nm) + ' in winkelwagen">' + BAG + '</button></div></div>'
            '</article>')

pat = re.compile(r'<article class="sd-it"><a href="#assortiment" aria-label="[^"]*">(<div class="sd-ph">.*?</div>)<h3>(.*?)</h3>'
                 r'(<p class="sd-b">.*?</p>)<p class="sd-pr">.*?</p></a></article>', re.S)
s, n = pat.subn(card, s); assert n == 7, n

PANEL = ('<div class="cp-bg" hidden></div><div class="cp" role="dialog" aria-labelledby="cp-h" hidden>'
         '<div class="cp-hd"><h3 id="cp-h"></h3><button type="button" class="cp-x" aria-label="Sluiten">'
         '<svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 6l12 12M18 6 6 18"/></svg></button></div>'
         '<p class="cp-sub">Kies een maat, met kluit</p><div class="cp-sz" role="radiogroup" aria-label="Maat"></div>'
         '<div class="cp-row">' + qty('') + '<b class="cp-tot"></b></div>'
         '<button type="button" class="cp-add">In winkelwagen</button></div>')
rep('<div class="sd-ft">', PANEL + '<div class="sd-ft">')

CSS = r'''
/* ===== add to cart on the variety cards (review, 16 Nov) ===== */
body{padding-top:48px}header.fixed{top:48px}#hero{min-height:calc(100svh - 48px)}
.vh{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
.ic{width:20px;height:20px;flex:none;fill:none;stroke:currentColor;stroke-width:1.6;stroke-linecap:round;stroke-linejoin:round}

/* the card is now the article: photo, name, bloom, price, controls on shared subgrid rows; the link sits on the name and is
   stretched over the whole card, the controls sit above it */
.sd-it{display:grid;grid-template-rows:subgrid;grid-row:span 5;row-gap:0;position:relative;padding-bottom:clamp(40px,3.6vw,56px)}
.sd-lk::after{content:"";position:absolute;inset:0;z-index:1;border-radius:22px}
.sd-lk:focus-visible{outline:none}
.sd-lk:focus-visible::after{outline:2px solid var(--moss);outline-offset:4px}
.sd-it:hover .sd-ph img{transform:scale(1.03)}
.sd-it:hover h3{color:var(--moss)}
.sd-pr{position:relative}
.sd-pr b{color:var(--moss)}
.ct,.c-btn{position:relative;z-index:2}
@media (max-width:1279px){ .sd-it{grid-column:span 2} .sd-it:nth-child(5){grid-column:2 / span 2} }
@media (max-width:767px){ .sd-it:nth-child(5){grid-column:span 2} .sd-it:nth-child(7){grid-column:2 / span 2} }
@media (max-width:599px){ .sd-it{grid-row:span 4;padding-bottom:28px} }

/* shared controls: a quiet pill stepper and a round moss cart button (the header's "Bestellen" colour) */
.qty{display:inline-flex;align-items:center;height:40px;border:1px solid rgba(20,20,19,.22);border-radius:999px;background:rgba(255,255,255,.62)}
.qty button{width:32px;height:38px;border:0;background:none;font:inherit;font-size:19px;line-height:1;color:var(--ink);cursor:pointer;border-radius:999px}
.qty button[aria-disabled="true"]{color:rgba(20,20,19,.35);cursor:default}
.qty button:focus-visible{outline:2px solid var(--moss);outline-offset:-2px}
.qty output{min-width:24px;text-align:center;font-size:15px;font-weight:600;font-variant-numeric:tabular-nums}
.cart{display:inline-flex;align-items:center;justify-content:center;width:40px;height:40px;flex:none;border:0;border-radius:999px;
  background:var(--moss);color:#fff;cursor:pointer}
.cart:hover{background:#2f3829}
.cart:focus-visible{outline:2px solid var(--moss);outline-offset:3px}
.ct{margin-top:14px;display:none}
.ct-row{display:flex;align-items:center;gap:8px}
.sz{position:relative;display:none;margin-bottom:8px}
.sz select{appearance:none;-webkit-appearance:none;width:100%;height:36px;padding:0 34px 0 14px;border:1px solid rgba(20,20,19,.22);
  border-radius:999px;background:rgba(255,255,255,.62);font:inherit;font-size:14px;color:var(--ink);cursor:pointer}
.sz select:focus-visible{outline:2px solid var(--moss);outline-offset:2px}
.sz .ch{position:absolute;right:12px;top:8px;width:20px;height:20px;pointer-events:none;color:var(--ink2)}
.c-btn{display:none}

/* A · quick add (40–60 cm) */
html.ct-a .ct{display:block}
/* B · the size on the card: the price is exact, "vanaf" and the size line go */
html.ct-b .ct{display:block}
html.ct-b .sz{display:block}
html.ct-b :is(.sd-v,.s-sz){display:none}
html.ct-b .sd-pr{grid-template-columns:1fr}
/* C · one cart button on the price line; it opens the choice */
html.ct-c .sd-pr{grid-template-columns:auto 1fr auto}
html.ct-c .sd-s{grid-column:1 / 3}
html.ct-c .c-btn{display:inline-flex;grid-column:3;grid-row:1 / span 2;align-self:center}

/* the choice panel (C) */
.cp{position:absolute;z-index:20;width:300px;padding:18px 20px 20px;border-radius:22px;background:#fbfaf6;
  box-shadow:0 1px 2px rgba(20,20,19,.08),0 18px 48px -12px rgba(20,20,19,.28);color:var(--ink)}
.cp[hidden],.cp-bg[hidden]{display:none}
.cp-hd{display:flex;align-items:center;justify-content:space-between;gap:12px}
.cp-hd h3{margin:0;font-size:18px;line-height:1.25;font-weight:600;letter-spacing:-.02em}
.cp-x{display:inline-flex;align-items:center;justify-content:center;width:36px;height:36px;margin:-6px -8px -6px 0;border:0;border-radius:999px;
  background:none;color:var(--ink2);cursor:pointer}
.cp-x:hover{background:rgba(20,20,19,.06)}
.cp-x:focus-visible{outline:2px solid var(--moss);outline-offset:0}
.cp-sub{margin:2px 0 0;font-size:13.5px;color:var(--ink2)}
.cp-sz{display:grid;gap:6px;margin-top:14px}
.cp-sz button{display:flex;align-items:center;justify-content:space-between;height:42px;padding:0 14px;border:1px solid rgba(20,20,19,.18);
  border-radius:14px;background:#fff;font:inherit;font-size:15px;color:var(--ink);cursor:pointer}
.cp-sz button b{font-weight:600;font-variant-numeric:tabular-nums}
.cp-sz button[aria-checked="true"]{border-color:var(--moss);box-shadow:inset 0 0 0 1px var(--moss);background:#f1f3ec}
.cp-sz button:focus-visible{outline:2px solid var(--moss);outline-offset:2px}
.cp-row{display:flex;align-items:center;justify-content:space-between;margin-top:16px}
.cp-tot{font-size:22px;font-weight:600;letter-spacing:-.02em;color:var(--moss);font-variant-numeric:tabular-nums}
.cp-add{width:100%;height:48px;margin-top:14px;border:0;border-radius:999px;background:var(--moss);color:#fff;font:inherit;font-size:15px;font-weight:500;cursor:pointer}
.cp-add:hover{background:#2f3829}
.cp-add:focus-visible{outline:2px solid var(--moss);outline-offset:3px}
/* phone: a bottom sheet */
@media (max-width:599px){
  .cp-bg{position:fixed;inset:0;z-index:19;background:rgba(20,20,19,.32)}
  .cp{position:fixed;left:0;right:0;bottom:0;top:auto!important;width:auto;padding:20px 20px calc(20px + env(safe-area-inset-bottom));border-radius:22px 22px 0 0}
}
'''
JS = r'''<script>(function(){
function qtyClick(ev){var b=ev.target.closest('.qty button');if(!b)return;var q=b.parentNode,o=q.querySelector('output'),n=+o.textContent;
  n=b.classList.contains('q-p')?Math.min(99,n+1):Math.max(1,n-1);o.textContent=n;q.querySelector('.q-m').setAttribute('aria-disabled',n<=1?'true':'false');
  if(q.closest('.cp'))tot();}
document.addEventListener('click',qtyClick);
/* B: the price follows the size */
[].forEach.call(document.querySelectorAll('.sz select'),function(sel){sel.addEventListener('change',function(){
  var c=sel.closest('.sd-it');c.querySelector('.sd-p').innerHTML='€&nbsp;'+sel.value;})});
/* C: the panel */
var cp=document.querySelector('.cp'),bg=document.querySelector('.cp-bg'),inn=cp.parentNode,cur=null,price=0,opener=null;
function tot(){var n=+cp.querySelector('.qty output').textContent;cp.querySelector('.cp-tot').innerHTML='€&nbsp;'+(price*n);}
function pick(btn){[].forEach.call(cp.querySelectorAll('.cp-sz button'),function(x){x.setAttribute('aria-checked',x===btn?'true':'false')});price=+btn.dataset.p;tot();}
function open(btn){var c=btn.closest('.sd-it'),sz=JSON.parse(c.dataset.sizes);opener=btn;
  cp.querySelector('#cp-h').textContent=c.dataset.name;
  var box=cp.querySelector('.cp-sz');box.innerHTML='';
  sz.forEach(function(x,i){var b=document.createElement('button');b.type='button';b.setAttribute('role','radio');b.dataset.p=x[1];
    b.innerHTML='<span>'+x[0].replace(' cm','&nbsp;cm')+'</span><b>€&nbsp;'+x[1]+'</b>';b.addEventListener('click',function(){pick(b)});box.appendChild(b);});
  cp.querySelector('.qty output').textContent='1';cp.querySelector('.q-m').setAttribute('aria-disabled','true');
  cp.hidden=false;bg.hidden=false;pick(box.firstChild);
  if(!matchMedia('(max-width:599px)').matches){var r=inn.getBoundingClientRect(),br=btn.getBoundingClientRect(),cr=c.getBoundingClientRect();
    var left=Math.min(Math.max(cr.left-r.left,0),r.width-cp.offsetWidth);cp.style.left=left+'px';
    /* it opens upwards over its own card, never down over the next block (Gert's portrait) */
    cp.style.top=Math.max(0,br.top-r.top-cp.offsetHeight-10)+'px';}
  else{cp.style.left='';cp.style.top='';}
  cp.querySelector('.cp-x').focus();}
function close(){cp.hidden=true;bg.hidden=true;if(opener)opener.focus();opener=null;}
[].forEach.call(document.querySelectorAll('.c-btn'),function(b){b.addEventListener('click',function(){open(b)})});
cp.querySelector('.cp-x').addEventListener('click',close);bg.addEventListener('click',close);
cp.querySelector('.cp-add').addEventListener('click',close);
document.addEventListener('keydown',function(ev){if(ev.key==='Escape'&&!cp.hidden)close();});
document.addEventListener('click',function(ev){if(!cp.hidden&&!cp.contains(ev.target)&&!ev.target.closest('.c-btn'))close();});
window.sdOpen=function(i){open(document.querySelectorAll('.c-btn')[i||0]);};
})();</script>'''
rep('</head>', '<style id="sd-cart">' + CSS + '</style></head>')
rep('</body>', JS + '</body>')
rep('<div id="root">', '<div class="rv" role="group" aria-label="Варианты"><div class="rv-g"><i>В корзину</i>'
    '<button type="button" data-g="ct" data-v="a" aria-pressed="true">A · Быстро в корзину</button>'
    '<button type="button" data-g="ct" data-v="b" aria-pressed="false">B · Размер на карточке</button>'
    '<button type="button" data-g="ct" data-v="c" aria-pressed="false">C · Значок открывает выбор</button></div></div><div id="root">')
s = re.sub(r'<html lang="nl" class="([^"]*)">', lambda m: f'<html lang="nl" class="{m.group(1)} ct-a">', s, count=1)
s = s.replace('<title>Waarom wij · De kweker</title>', '<title>В корзину · варианты</title>', 1)
(D / 'sd-cart.html').write_text(s)
print('ok', len(s), {k: v[0][1] for k, v in SIZES.items()})
