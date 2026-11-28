# The call card ("belkaart"): a small card with the phone and WhatsApp that slides in on its own, as the first version of
# the site did on its product and wholesale pages (rhododendrons repo, components/whatsapp-sticky.tsx). Owner, 28 Nov:
# take the phone line out of the Groothandel head and show the number this way, on the Groothandel page and on the variety pages.
#
# Behaviour as in the first version:
#   - it appears when the visitor has gone far down the page (desktop: the end of the page; phone: past 65 % of it) and then
#     scrolls back up: the moment someone is looking for something;
#   - it hides while the footer is in view (and while any element given in `avoid` is in view, e.g. the request form);
#   - a close button hides it for the rest of this page view.
# In this site's language instead of the first version's dark green with WhatsApp green: a light card with a hairline and a
# soft shadow, the glowing pill for calling, an outline pill for WhatsApp. Copy from the facts: the help comes from the nursery
# ("Bel of app de kwekerij"; the team answers, not Gert alone), 06 20 10 43 12 to call, 06 20 29 78 49 for WhatsApp.
# On the phone it stands above a bottom bar when one is showing (`bars`: the buy bar on the variety pages); a page may instead
# hide its own bar while the card shows (html.bpop-on; the Groothandel page hides its offer bar, so two actions never stack).
# Usage: s = belpop.apply(s, title='Vragen over een partij?', avoid='#offerte .ghd-formcard', bars='.ghd-bar')

PHONE = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 '
         '19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6'
         'l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z" fill="none" stroke="currentColor" stroke-width="1.7" '
         'stroke-linecap="round" stroke-linejoin="round"/></svg>')
WA = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M17.47 14.38c-.3-.15-1.76-.87-2.03-.97-.27-.1-.47-.15-.67.15-.2.3-.77.97-.94 '
      '1.16-.17.2-.35.22-.64.07-.3-.15-1.26-.46-2.39-1.47-.88-.79-1.48-1.76-1.65-2.06-.17-.3-.02-.46.13-.61.13-.13.3-.35.45-.52.15-.17.2-.3.3-.5'
      '.1-.2.05-.37-.03-.52-.07-.15-.67-1.61-.92-2.2-.24-.58-.49-.5-.67-.51h-.57c-.2 0-.52.07-.79.37-.27.3-1.04 1.02-1.04 2.48s1.07 2.88 1.21 '
      '3.07c.15.2 2.1 3.2 5.08 4.49.71.31 1.26.49 1.7.63.71.23 1.36.2 1.87.12.57-.09 1.76-.72 2-1.41.25-.7.25-1.29.17-1.41-.07-.13-.27-.2-.57-.35'
      'M12.05 21.79h-.01a9.87 9.87 0 0 1-5.03-1.38l-.36-.21-3.74.98 1-3.65-.24-.37a9.86 9.86 0 0 1-1.51-5.26c0-5.45 4.44-9.88 9.89-9.88 2.64 0 '
      '5.12 1.03 6.99 2.9a9.82 9.82 0 0 1 2.89 6.99c0 5.45-4.44 9.88-9.88 9.88m8.41-18.3A11.82 11.82 0 0 0 12.05 0C5.5 0 .16 5.34.16 11.89c0 '
      '2.1.55 4.14 1.59 5.95L.06 24l6.3-1.65a11.88 11.88 0 0 0 5.68 1.45h.01c6.55 0 11.89-5.34 11.89-11.89 0-3.18-1.24-6.17-3.48-8.41z"/></svg>')
CLOSE = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18" fill="none" stroke="currentColor" stroke-width="1.8" '
         'stroke-linecap="round"/></svg>')

CSS = '''/* ===== the call card (tools/belpop.py) ===== */
.bpop{position:fixed;z-index:45;right:clamp(16px,2vw,28px);bottom:clamp(16px,2vw,28px);width:min(380px,calc(100vw - 32px));
  padding:16px 16px 16px 20px;border-radius:22px;background:#fbfaf7;color:#141413;font-family:Manrope,system-ui,sans-serif;
  box-shadow:0 0 0 1px rgba(63,74,55,.14),0 18px 44px rgba(22,28,20,.18);
  transform:translateY(calc(100% + 40px));opacity:0;visibility:hidden;
  transition:transform .45s cubic-bezier(.2,.7,.2,1),opacity .3s ease,visibility 0s linear .45s,bottom .3s ease}
.bpop.is-on{transform:none;opacity:1;visibility:visible;transition:transform .45s cubic-bezier(.2,.7,.2,1),opacity .3s ease,visibility 0s,bottom .3s ease}
@media (prefers-reduced-motion:reduce){ .bpop,.bpop.is-on{transition:none} }
.bpop :where(p,b){margin:0}
.bpop-t{padding-right:40px;font-size:var(--t-body,16px);line-height:1.35;font-weight:600}
.bpop-l{margin-top:4px!important;padding-right:40px;font-size:var(--t-small,14px);line-height:1.45;color:#5f5e58}
.bpop-x{position:absolute;top:6px;right:6px;display:grid;place-items:center;width:44px;height:44px;padding:0;border:0;border-radius:999px;background:none;color:#5f5e58;cursor:pointer}
.bpop-x svg{width:18px;height:18px}
.bpop-x:hover{color:#141413;background:rgba(63,74,55,.08)}
.bpop-b{display:flex;flex-wrap:wrap;gap:8px;margin-top:14px}
.bpop-b a{display:inline-flex;align-items:center;justify-content:center;gap:8px;flex:1 1 auto;height:46px;padding:0 16px;border-radius:999px;
  font-size:var(--t-small,14px);font-weight:600;line-height:1;color:#2f3829;text-decoration:none;white-space:nowrap}
.bpop-b svg{flex:none;width:17px;height:17px}
.bpop-call{background:radial-gradient(ellipse 46% 160% at 6% 50%,#b3c39b 0%,transparent 72%),radial-gradient(ellipse 50% 170% at 98% 50%,#e6dcb0 0%,transparent 72%),#d3ddc2;
  box-shadow:inset 0 0 0 1px rgba(63,74,55,.28)}
.bpop-wa{background:#fff;box-shadow:inset 0 0 0 1px rgba(63,74,55,.3)}
.bpop-wa svg{color:#3f4a37}
@media (hover:hover){ .bpop-call:hover{box-shadow:inset 0 0 0 1px rgba(63,74,55,.5)} .bpop-wa:hover{box-shadow:inset 0 0 0 1px rgba(63,74,55,.55)} }
.bpop :is(a,button):focus-visible{outline:2px solid #3f4a37;outline-offset:2px}
@media (max-width:560px){ .bpop{left:16px;right:16px;bottom:12px;width:auto} }
@media print{ .bpop{display:none!important} }
'''

JS = r'''<script id="belpop-js">(function(){
var pop=document.querySelector('.bpop');if(!pop)return;
var AVOID=pop.getAttribute('data-avoid')||'',BARS=pop.getAttribute('data-bars')||'';
var reached=false,lastY=scrollY,wanted=false,closed=false,tick=false;
function inView(el){var r=el.getBoundingClientRect();return r.top<innerHeight&&r.bottom>0}
function blocked(){var foot=document.querySelector('footer');if(foot&&inView(foot))return true;
 return AVOID?[].some.call(document.querySelectorAll(AVOID),inView):false}
/* above a bottom bar that is showing (phone): sit just over it */
function lift(){var off=0;if(BARS)[].forEach.call(document.querySelectorAll(BARS),function(b){var cs=getComputedStyle(b);
 if(cs.display==='none'||cs.visibility==='hidden'||parseFloat(cs.opacity)<0.05)return;var r=b.getBoundingClientRect();
 if(r.height&&r.top<innerHeight-2&&r.bottom>innerHeight-140)off=Math.max(off,innerHeight-r.top)});
 pop.style.bottom=off?(off+10)+'px':''}
function update(){tick=false;var y=scrollY,h=document.documentElement.scrollHeight,mobile=innerWidth<1024;
 var near=mobile?h*.35:10;if(y+innerHeight>=h-near)reached=true;
 if(reached&&y<lastY-2)wanted=true;lastY=y;
 var on=wanted&&!closed&&!blocked();pop.classList.toggle('is-on',on);document.documentElement.classList.toggle('bpop-on',on);pop.setAttribute('aria-hidden',on?'false':'true');
 pop.querySelectorAll('a,button').forEach(function(e){e.tabIndex=on?0:-1});if(on)lift()}
function q(){if(!tick){tick=true;requestAnimationFrame(update)}}
addEventListener('scroll',q,{passive:true});addEventListener('resize',q);update();
pop.querySelector('.bpop-x').addEventListener('click',function(){closed=true;update()});
})();</script>'''


def apply(html, title, avoid='', bars=''):
    """Add the call card to a built page: its markup before </body>, its CSS in the head, its script after the markup."""
    assert 'class="bpop"' not in html and html.count('</body>') == 1 and html.count('</head>') == 1
    card = (f'<aside class="bpop" aria-label="Contact met de kwekerij" aria-hidden="true" data-avoid="{avoid}" data-bars="{bars}">'
            f'<p class="bpop-t">{title}</p><p class="bpop-l">Bel of app de kwekerij.</p>'
            '<div class="bpop-b"><a class="bpop-call" href="tel:+31620104312" tabindex="-1">' + PHONE + 'Bel 06&nbsp;20&nbsp;10&nbsp;43&nbsp;12</a>'
            '<a class="bpop-wa" href="https://wa.me/31620297849" target="_blank" rel="noopener noreferrer" tabindex="-1">' + WA + 'WhatsApp</a></div>'
            '<button class="bpop-x" type="button" aria-label="Sluiten" tabindex="-1">' + CLOSE + '</button></aside>')
    html = html.replace('</head>', '<style id="belpop-css">' + CSS + '</style></head>', 1)
    return html.replace('</body>', card + JS + '</body>', 1)
