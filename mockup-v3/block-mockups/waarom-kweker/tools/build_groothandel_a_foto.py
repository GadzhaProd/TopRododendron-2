# Mockup tool (not site code): groothandel-a-foto.html, variant A of the wholesale page with the photo-first head.
# For the owner to compare with groothandel.html (variant A as it is) and to judge his idea "the photo first, the action under it".
# It reuses the existing build: it reads the built groothandel.html (tools/build_groothandel.py, not touched) and changes only
#   1. the head: the same elements and the same copy, in a new order.
#      - phone and tablet (under 1024 px): breadcrumb, OUR FIELD first (the whole photo, 16:9), then heading, line, action, facts;
#      - from 1024 px: the text left and the field right, in one screen (a photo above the heading would push the heading and
#        the action under the fold: 21:9 of 1324 px is 567 px).
#   2. under 1024 px: variant C's calm bottom bar "Vraag een offerte aan" (the action leaves the first screen sooner here);
#   3. the form: an error line now clears while typing, not on leaving the field (in A the line vanishes at the very moment
#      of the next tap, the form jumps about 30 px and the tap on "Bezorgen in Nederland" misses).
# The photo: img/hw-fable-veld.webp, our own field (the same shot as img/hero-field.jpg, 268 KB instead of 497 KB).
# No new copy, no new facts (docs/groothandel-tekst-2026-11-26.md, docs/b2b-besluiten-2026-11-26.md).
# Usage: python3 tools/build_groothandel.py && python3 tools/build_groothandel_a_foto.py [dir]
import pathlib, re, sys
D = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
s = (D / 'groothandel.html').read_text()


def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), a[:70]); s = s.replace(a, b)


# ---------- 1. the head: take A's elements apart and put them back in the new order ----------
m = re.search(r'<section class="in gh-head" aria-labelledby="h-gh">(.*?)</section>', s, flags=re.S)
assert m, 'the head of variant A was not found'
inner = m.group(1)


def part(pat):
    x = re.search(pat, inner, flags=re.S); assert x, pat; return x.group(0)


CRUMB = part(r'<nav class="gh-crumb".*?</nav>')
H1 = part(r'<h1 id="h-gh">.*?</h1>')
LEAD = part(r'<p class="gh-lead">.*?</p>')
CTA = part(r'<div class="gh-cta">.*?</div>')
FACTS = part(r'<ul class="gh-facts".*?</ul>')
assert 'img/hero-field.jpg' in inner
# the text stays first in the source (heading before the picture for screen readers and search); CSS shows the photo first
PHOTO = ('<figure class="gh-photo ghf-photo"><img src="img/hw-fable-veld.webp" alt="Ons rhododendronveld in bloei" width="1800" height="1004" '
         'fetchpriority="high" decoding="async"></figure>')
HEAD = ('<section class="in gh-head ghf-head" aria-labelledby="h-gh">' + CRUMB
        + '<div class="ghf-text">' + H1 + LEAD + CTA.replace('class="gh-cta"', 'class="gh-cta ghf-cta"') + FACTS + '</div>'
        + PHOTO + '</section>')
s = s[:m.start()] + HEAD + s[m.end():]

# ---------- 2. the bottom bar under 1024 px (variant C's idea: one action, hidden at the head, the form and the footer) ----------
ARROW = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6" fill="none" stroke="currentColor" '
         'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>')
BAR = '<div class="ghf-bar" data-off><div class="ghf-bar-in"><a class="gh-btn" href="#offerte">Vraag een offerte aan' + ARROW + '</a></div></div>'
rep('</main>', BAR + '</main>')

CSS = r'''
/* ===== Groothandel, variant A with the photo-first head (tools/build_groothandel_a_foto.py) ===== */
/* phone and tablet: breadcrumb, the field, then heading, line, action, facts */
.ghf-head{display:grid;grid-template-columns:minmax(0,1fr)}
.ghf-head .gh-crumb{order:0;margin-bottom:14px}
.ghf-head .gh-crumb a{padding-inline:4px;margin-inline:-4px}
.ghf-head .ghf-photo{order:1;margin-top:0;aspect-ratio:16/9}
.ghf-head .ghf-photo img{object-position:50% 50%}
.ghf-head .ghf-text{order:2;margin-top:clamp(24px,3.4vw,36px)}
@media (max-width:767px){ .ghf-head{padding-top:calc(64px + 18px)} .ghf-head .gh-lead{margin-top:14px} .ghf-head .gh-cta{margin-top:22px} }
@media (min-width:768px) and (max-width:1023px){ .ghf-head .ghf-photo{aspect-ratio:2/1} }
/* from 1024 px: the text left, the field right, in one screen. The text column is the wider one, so the heading keeps its two
   lines as in A, and the photo takes the text's height (no fixed height): no empty field under the button (owner, 27 Nov:
   with a tall photo and the facts pinned to its foot the left column had a whole block of empty space) */
@media (min-width:1024px){
  .ghf-head{grid-template-columns:minmax(0,1.55fr) minmax(0,1fr);grid-template-rows:auto auto;column-gap:clamp(40px,4.4vw,80px);padding-top:calc(80px + clamp(28px,3.4vw,56px))}
  .ghf-head .gh-crumb{grid-column:1;grid-row:1;margin-bottom:clamp(22px,2.4vw,36px);align-self:start}
  .ghf-head .ghf-text{grid-column:1;grid-row:2;margin-top:0}
  .ghf-head .ghf-photo{position:relative;grid-column:2;grid-row:1 / 3;aspect-ratio:auto;height:auto;min-height:clamp(340px,28vw,440px);align-self:stretch}
  .ghf-head .ghf-photo img{position:absolute;inset:0;width:100%;height:100%;object-position:46% 55%}
  .ghm .ghf-head h1{font-size:clamp(38px,3.65vw,52px)}
}
/* the bottom bar */
.ghf-bar{position:fixed;left:0;right:0;bottom:0;z-index:40;padding:10px var(--gut) calc(10px + env(safe-area-inset-bottom,0px));
  background:rgba(241,239,234,.88);-webkit-backdrop-filter:blur(14px) saturate(1.2);backdrop-filter:blur(14px) saturate(1.2);box-shadow:0 -1px 0 rgba(63,74,55,.16);
  transition:transform .35s cubic-bezier(.3,.7,.2,1),visibility 0s}
.ghf-bar[data-off]{transform:translateY(105%);visibility:hidden;transition:transform .3s ease-in,visibility 0s .3s}
@media (prefers-reduced-motion:reduce){ .ghf-bar,.ghf-bar[data-off]{transition:none} }
@media (min-width:1024px){ .ghf-bar{display:none} }
.ghf-bar-in{display:flex;justify-content:center}
.ghf-bar .gh-btn{flex:1;min-width:0;max-width:420px;padding:0 16px}
'''

JS = r'''<script id="groothandel-foto-js">(function(){
var main=document.querySelector('.ghm'),bar=document.querySelector('.ghf-bar'),cta=document.querySelector('.ghf-cta'),req=document.getElementById('offerte'),box=document.querySelector('.gh-req');
if(!main||!bar||!cta||!req||!box)return;var f=box.querySelector('form'),tick=false;
/* the bar: shown once the head's button has left the screen, gone when the form (and the footer after it) arrives */
function show(){tick=false;var on=cta.getBoundingClientRect().bottom<64&&req.getBoundingClientRect().top>window.innerHeight-40&&!box.classList.contains('gh-sent');
 if(on)bar.removeAttribute('data-off');else bar.setAttribute('data-off','')}
function q(){if(!tick){tick=true;requestAnimationFrame(show)}}
window.addEventListener('scroll',q,{passive:true});window.addEventListener('resize',q);show();
/* the form: an error line clears while typing, so the form does not jump under the next tap */
['bedrijf','naam','email','soorten'].forEach(function(k){var el=f.elements[k];el.addEventListener('input',function(){
 if(el.getAttribute('aria-invalid')!=='true')return;var v=el.value.trim(),ok=k==='email'?/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v):v.length>0;
 if(ok){el.setAttribute('aria-invalid','false');var e=document.getElementById('e-'+k);if(e)e.textContent=''}})});
})();</script>'''

rep('</head>', '<style id="groothandel-foto-css">' + CSS + '</style></head>')
rep('</body>', JS + '</body>')
rep('href="groothandel.html" aria-current="page"', 'href="groothandel-a-foto.html" aria-current="page"', s.count('href="groothandel.html" aria-current="page"'))
assert 'gen/veld-L2' not in s[s.index('<main'):s.index('</main>')]
(D / 'groothandel-a-foto.html').write_text(s)
print('ok', len(s))
