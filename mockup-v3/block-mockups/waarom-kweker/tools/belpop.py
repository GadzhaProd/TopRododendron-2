# The call card ("belkaart"): a small card with the phone, WhatsApp and the opening hours that slides in on its own, as the
# first version of the site did on its product and wholesale pages (rhododendrons repo, components/whatsapp-sticky.tsx).
# Owner, 28 Nov: take the phone line out of the Groothandel head and show the number this way, on the Groothandel page and on
# the variety pages. Reworked the same day after an independent review (all fixes and the hours, owner: "do everything").
#
# When it shows:
#   - only once the visitor has gone far enough to have seen the page: when one of `reach` enters the view (the request form
#     on the Groothandel page, "Andere soorten" on a variety page) or the footer does; desktop and phone alike;
#   - then on a deliberate scroll back up (about 100 px of upward travel, so a finger lift or a bounce does not count), and
#     never on the first screen; it goes again after about 80 px of downward scrolling (so a page's own bottom bar returns);
#   - never while the footer, an `avoid` element (`avoid_phone`: only under 900 px), the phone menu or the cart is open or in view, and not while it holds focus
#     it stays put; a close button hides it for the rest of the visit (sessionStorage, shared by all pages).
# One floating element at a time: a page's bottom bar steps aside while the card shows (html.bpop-on), or the card waits via
# `avoid`. The swap is sequenced: the leaving element goes in 150 ms, the arriving one starts after it.
# Look: a light card with a hairline and a soft shadow, the glowing pill to call, an outline pill for WhatsApp (with the
# variety or the lot prefilled in the message), the hours in one quiet line. The help comes from "de kwekerij" (the team
# answers, not Gert alone). Hours Mon–Fri 08:00–17:00, Sat 09:00–13:00 (the footer's).
# Usage: s = belpop.apply(s, 'Vragen over een partij?', reach='#offerte', avoid='#offerte .ghd-formcard', wa='... een partij ...')
import urllib.parse

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
  box-shadow:0 0 0 1px rgba(63,74,55,.14),0 8px 24px rgba(22,28,20,.10);
  transform:translateY(calc(100% + 40px));opacity:0;visibility:hidden;
  /* leaving: quick, so whatever comes next starts on a clear spot */
  transition:transform .15s ease-in,opacity .15s ease-in,visibility 0s linear .15s}
/* arriving: after the leaving element has gone (150 ms) */
.bpop.is-on{transform:none;opacity:1;visibility:visible;transition:transform .45s cubic-bezier(.2,.7,.2,1) .15s,opacity .3s ease .15s,visibility 0s .15s}
@media (prefers-reduced-motion:reduce){ .bpop,.bpop.is-on{transition:none} }
.bpop :where(p,b){margin:0}
.bpop-t{padding-right:40px;font-size:var(--t-body,16px);line-height:1.35;font-weight:600}
.bpop-nb{white-space:nowrap}
.bpop-l{margin-top:4px!important;padding-right:40px;font-size:var(--t-small,14px);line-height:1.45;color:#5f5e58}
.bpop-x{position:absolute;top:6px;right:6px;display:grid;place-items:center;width:44px;height:44px;padding:0;border:0;border-radius:999px;background:none;color:#5f5e58;cursor:pointer}
.bpop-x svg{width:18px;height:18px}
.bpop-x:hover{color:#141413;background:rgba(63,74,55,.08)}
.bpop-b{display:flex;flex-wrap:nowrap;gap:8px;margin-top:14px}
.bpop-b a{display:inline-flex;align-items:center;justify-content:center;gap:8px;flex:1 1 auto;height:46px;padding:0 16px;border-radius:999px;
  font-size:var(--t-small,14px);font-weight:600;line-height:1;color:#2f3829;text-decoration:none;white-space:nowrap}
.bpop-b svg{flex:none;width:17px;height:17px}
.bpop-call{background:radial-gradient(ellipse 46% 160% at 6% 50%,#b3c39b 0%,transparent 72%),radial-gradient(ellipse 50% 170% at 98% 50%,#e6dcb0 0%,transparent 72%),#d3ddc2;
  box-shadow:inset 0 0 0 1px rgba(63,74,55,.28)}
.bpop-wa{flex:0 1 auto!important;background:#fff;box-shadow:inset 0 0 0 1px rgba(63,74,55,.3)}
.bpop-wa svg{color:#3f4a37}
@media (hover:hover){ .bpop-call:hover{box-shadow:inset 0 0 0 1px rgba(63,74,55,.5)} .bpop-wa:hover{box-shadow:inset 0 0 0 1px rgba(63,74,55,.55)} }
.bpop :is(a,button):focus-visible{outline:2px solid #3f4a37;outline-offset:2px}
@media (max-width:560px){ .bpop{left:16px;right:16px;bottom:calc(12px + env(safe-area-inset-bottom,0px));width:auto} }
/* narrow phones: one row of pills (the card stays about 16 % of the screen) */
@media (max-width:379.98px){ .bpop{padding:14px} .bpop-b{gap:6px} .bpop-b a{gap:6px;padding:0 10px} }
@media (max-width:349.98px){ .bpop-wa span{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap} .bpop-wa{width:46px;padding:0!important} }
/* landscape phones: the short form (title and the two pills) */
@media (max-height:500px) and (orientation:landscape){ .bpop-l{display:none} .bpop{padding:12px 14px} .bpop-b{margin-top:10px} }
/* the hand-over with a page's bottom bar: the leaving one goes in 150 ms, the arriving one waits for it
   (variety pages: the buy bar; the Groothandel page sets its own rules for its offer bar) */
@media (max-width:899.98px){
  .so-bar{transition:opacity .15s ease-in,transform .15s ease-in,visibility 0s linear .15s}
  .so-bar.is-on{transition:opacity .3s ease .15s,transform .3s ease .15s,visibility 0s .15s}
}
@media print{ .bpop{display:none!important} }
'''

JS = r'''<script id="belpop-js">(function(){
var pop=document.querySelector('.bpop');if(!pop)return;var root=document.documentElement,KEY='tr-belkaart-dicht';
var REACH=pop.getAttribute('data-reach')||'',AVOID=pop.getAttribute('data-avoid')||'',AVOID_M=pop.getAttribute('data-avoid-phone')||'';
var closed=false;try{closed=sessionStorage.getItem(KEY)==='1'}catch(e){}
var reached=false,wanted=false,lastY=scrollY,up=0,down=0,tick=false,on=false;
function inView(el){var r=el.getBoundingClientRect();return r.height>0&&r.top<innerHeight&&r.bottom>0}
function any(sel){return sel?[].some.call(document.querySelectorAll(sel),inView):false}
function blocked(){return any('footer')||any(AVOID)||(innerWidth<900&&any(AVOID_M))||root.classList.contains('mm-open')||root.classList.contains('cd-open')}
function set(v){if(v===on)return;on=v;pop.classList.toggle('is-on',v);root.classList.toggle('bpop-on',v);pop.inert=!v;
 if(v)pop.removeAttribute('aria-hidden');else pop.setAttribute('aria-hidden','true')}
function update(){tick=false;var y=scrollY,d=y-lastY;lastY=y;
 if(!reached&&(any(REACH)||any('footer')))reached=true;
 if(d<0){up-=d;down=0}else if(d>0){down+=d;up=0}
 if(reached&&up>=100)wanted=true;
 if(down>=80)wanted=false;
 var focusIn=pop.contains(document.activeElement);
 set(focusIn||(wanted&&!closed&&y>innerHeight*.9&&!blocked()))}
function q(){if(!tick){tick=true;requestAnimationFrame(update)}}
addEventListener('scroll',q,{passive:true});addEventListener('resize',q);
new MutationObserver(q).observe(root,{attributes:true,attributeFilter:['class']});
pop.inert=true;update();
pop.querySelector('.bpop-x').addEventListener('click',function(){closed=true;try{sessionStorage.setItem(KEY,'1')}catch(e){}
 var m=document.getElementById('main');if(m)m.focus({preventScroll:true});set(false)});
})();</script>'''


def apply(html, title, reach='', avoid='', avoid_phone='', wa='Hallo, ik heb een vraag over uw rhododendrons.'):
    """Add the call card to a built page: its markup right after </main> (so it comes before the footer in the reading and
    tab order), its CSS in the head, its script before </body>."""
    assert 'class="bpop"' not in html and html.count('</main>') == 1 and html.count('</body>') == 1 and html.count('</head>') == 1
    wa_url = 'https://wa.me/31620297849?text=' + urllib.parse.quote(wa)
    card = (f'<aside class="bpop" aria-label="Contact met de kwekerij" aria-hidden="true" data-reach="{reach}" data-avoid="{avoid}" data-avoid-phone="{avoid_phone}">'
            f'<p class="bpop-t">{title}</p>'
            '<p class="bpop-l">Bel of app de kwekerij: <span class="bpop-nb">ma–vr 08:00–17:00,</span> <span class="bpop-nb">za 09:00–13:00.</span></p>'
            '<div class="bpop-b"><a class="bpop-call" href="tel:+31620104312">' + PHONE + 'Bel 06&nbsp;20&nbsp;10&nbsp;43&nbsp;12</a>'
            f'<a class="bpop-wa" href="{wa_url}" target="_blank" rel="noopener noreferrer" aria-label="WhatsApp, 06 20 29 78 49">' + WA + '<span>WhatsApp</span></a></div>'
            '<button class="bpop-x" type="button" aria-label="Sluiten">' + CLOSE + '</button></aside>')
    html = html.replace('</head>', '<style id="belpop-css">' + CSS + '</style></head>', 1)
    html = html.replace('</main>', '</main>' + card, 1)
    return html.replace('</body>', JS + '</body>', 1)
