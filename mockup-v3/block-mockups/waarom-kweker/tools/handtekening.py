# Gert's handwritten signature in the founder block (#kweker), drawn by the owner (25 Nov; img/handtekening-gert-top.svg,
# a light copy for dark grounds in img/handtekening-gert-top-licht.svg). apply(html, place) puts it in the block:
#   'a'  under the guarantee text: the grower signs his promise; the line with his typed name follows right under it
#   'b'  at the end of the panel, under the two numbers: a letter's sign-off
#   'c'  the owner's order for A (25 Nov): the question and the two numbers first, then the guarantee and under it the
#        signature, which so both signs the promise and closes the block (the text is moved in the markup, so a screen
#        reader reads it in the order it is seen)
#   'd'  as 'c', but the help comes from the nursery ("Bel of app de kwekerij", as in the cart drawer) and Gert's name
#        stands once, typed under his signature: "Gert Top, oprichter en kweker" (owner, 25 Nov: the name twice, or
#        promising Gert on every call, did not sit right)
#   'e'  as 'd', with a heading for the first part too, in the guarantee heading's style (owner, 26 Nov: the second part
#        had a heading, the first did not): "Advies van de kwekerij." and one line under it
#   'g'  as 'e' on desktop; on the phone Gert's face first (owner, 26 Nov, to compare with 'e', where the portrait closes the
#        card): a plain photo at the top of the card with a straight edge (img/fd-foto-top.webp, tools/fd_foto_top.py), then
#        the guarantee, the signature and his name, and the advice with the two numbers last. A fade of the jacket into the
#        card was tried first and rejected by the owner ("this transition, no")
#   'h'  as 'g', with another transition: the rest of the card is a sheet with rounded top corners that lies over the
#        photo's lower edge, no fading
#   In 'g' and 'h' the phone order is set by CSS, so a screen reader there still reads the desktop order (advice first)
#   'i'  the reviewer's proposal (Fable, 26 Nov; owner: build it to see): the portrait stays at the bottom on the phone; the
#        guarantee first, as it answers the section heading, then the advice and the two numbers, then the signature and the
#        name under the numbers; less air above the head on the phone. The order is in the markup, so desktop, phone and a
#        screen reader read the same order
# In a, b and c the typed name stays in the contact line; in d under the signature. The signature is an image with a plain alt.
import pathlib, re
IMG = ('<img class="fd-sig" src="img/handtekening-gert-top.svg" alt="Handtekening van Gert Top" width="4804" height="1700" '
       'loading="lazy" decoding="async">')

CSS = '''/* Gert's signature (tools/handtekening.py): one dark ink line, about the width of the phone numbers, never a flourish */
#kweker .fd-sig{display:block;width:clamp(150px,12.5vw,184px);height:auto;margin:0}
#kweker .fp-txt + .fd-sig{margin:clamp(16px,1.6vw,22px) 0 clamp(4px,.6vw,8px) -6px}
#kweker .fp-act + .fd-sig{margin:clamp(24px,2.4vw,34px) 0 0 -6px}
/* phone: the card is a one-column grid whose text blocks carry their own 22 px side padding and an order (text 2,
   numbers 3, portrait 4, which overlaps the block above it by about 32 px); the signature takes its neighbour's order */
@media (max-width:860px){
  #kweker .fd-sig{width:150px;justify-self:start}
  #kweker .fp-txt + .fd-sig{order:2;margin:18px 0 0 16px}
  #kweker .fp-act + .fd-sig{order:3;margin:24px 0 40px 16px}
}
@media print{ #kweker .fd-sig{width:140px} }
/* the two numbers a step quieter than the headings (owner, 26 Nov: "louder than the headings"): the text size instead of the
   heading size, medium instead of semibold, a finer and lighter underline; the tap area stays tall (padding, with an equal
   negative margin so the rows keep their spacing) */
/* "Lees de voorwaarden" a 44 px tap target (it was 24 px; reviewer, 26 Nov); margins take the padding back, the line stays put */
#kweker .fp-txt .fp-more{padding-block:10px;margin:-2px 0 -10px}
#kweker .fp-act .fp-num{font-size:var(--t-lead)!important;letter-spacing:-.01em}
#kweker .fp-act .fp-num a{font-weight:500;text-decoration-thickness:1px;text-decoration-color:rgba(63,74,55,.4);text-underline-offset:5px;padding-block:12px;margin-block:-8px}
'''
# 'c': the contact first, the guarantee and the signature last. Desktop: the panel is a centred flex column, the lead
# opens it and the guarantee takes the 34 px the lead had. Phone: the blocks are ordered grid items; the lead takes the
# guarantee's top padding and the guarantee follows the numbers
CSS_C = '''#kweker .fd-pn-c > .fp-lead{margin-top:0}
#kweker .fd-pn-c > .fp-act + .fp-txt{margin-top:34px!important}
@media (max-width:860px){
  #kweker .fd-pn-c > .fp-lead{order:1;padding-top:28px}
  #kweker .fd-pn-c > .fp-act{order:1}
  #kweker .fd-pn-c > .fp-txt{order:2;padding-top:26px}
  #kweker .fd-pn-c > .fp-act + .fp-txt{margin-top:0!important}
}
'''
LEAD_D = 'Vragen over een soort of de garantie? Bel of app de kwekerij:'
CAP = '<p class="fd-sigcap"><b>Gert Top</b>, oprichter en kweker</p>'
# the typed name under the signature: small, the soft ink of the labels, the name itself in the text's ink
CSS_D = '''#kweker .fd-sigcap{margin:6px 0 0;font-size:var(--t-small);line-height:1.4;color:#45443f}
#kweker .fd-sigcap b{font-weight:600;color:#141413}
@media (max-width:860px){
  #kweker .fd-sig + .fd-sigcap{order:2;margin:6px 0 40px;padding:0 22px}
  #kweker .fd-pn-c > .fp-txt + .fd-sig{margin-bottom:0}
}
'''

LEAD_E = '<b class="fd-ask">Advies van de kwekerij.</b>Over een soort, de maat of de garantie: bel of app ons.'
# the first part in the guarantee's type: its heading the guarantee heading's size (--t-sub), its line the guarantee text's
# (--t-lead); the page's own rules set those sizes with !important, so these do too
CSS_E = '''#kweker .fd-pn-e > .fp-lead{font-size:var(--t-lead)!important;line-height:1.55;color:#3d3c37;max-width:50ch}
#kweker .fd-pn-e .fd-ask{display:block;margin-bottom:clamp(10px,1vw,14px);font-size:var(--t-sub)!important;line-height:1.14;letter-spacing:-.028em;font-weight:600;color:#141413;text-wrap:balance}
@media (max-width:860px){
  #kweker .fd-pn-e > .fp-lead{line-height:1.5}
  #kweker .fd-pn-e .fd-ask{line-height:1.2;margin-bottom:8px}
}
'''

# 'g' and 'h', phone only. The card is otherwise a one-column grid with the panel as display:contents; here the panel becomes
# a block of its own under the photo, so it can carry the card's colour, glows and grain (the photo covers the card's own),
# and in 'h' lie over the photo as a sheet
NOISE = re.search(r'url\("data:image/svg\+xml;utf8,[^"]+"\)', (pathlib.Path(__file__).parent / 'fd-podpis.css').read_text()).group(0)
CSS_TOP = '''@media (max-width:860px){
  #kweker .fd-card.fd-top > .fd-ph{order:1;margin:0;aspect-ratio:1440/1546}
  #kweker .fd-top .fd-pn{display:flex;flex-direction:column;order:2;position:relative;z-index:2;margin:0;padding:0 0 40px;
    background:radial-gradient(ellipse 80% 190px at -10% 40px,rgba(183,198,160,.7) 0%,transparent 72%),radial-gradient(ellipse 60% 150px at 106% 150px,rgba(236,214,210,.65) 0%,transparent 72%),#e6e8e5}
  #kweker .fd-top .fd-pn::before{content:"";position:absolute;inset:0;border-radius:inherit;pointer-events:none;background:''' + NOISE + ''';background-size:220px 220px;opacity:.26;mix-blend-mode:soft-light}
  #kweker .fd-top .fd-pn-c > .fp-txt{order:2;padding-top:28px}
  #kweker .fd-top .fd-pn-c > .fp-txt + .fd-sig{order:3;margin:18px 0 0 16px}
  #kweker .fd-top .fd-sig + .fd-sigcap{order:4;margin:6px 0 0}
  #kweker .fd-top .fd-pn-c > .fp-lead{order:5;padding-top:40px}
  #kweker .fd-top .fd-pn-c > .fp-act{order:6;padding-bottom:0}
}
'''
# 'h': the sheet overlaps the photo by 22 px (the chin stays about 30 px clear of it); a faint shadow lifts its edge
CSS_BLAD = '''@media (max-width:860px){
  #kweker .fd-blad .fd-pn{margin-top:-22px;border-radius:24px 24px 0 0;box-shadow:0 -6px 18px rgba(20,24,30,.10)}
}
'''
# 'i': the guarantee opens the panel, the advice follows after the gap the guarantee had (34 px desktop, 32 phone), the
# signature follows the numbers, the same 8 px to the name as in 'e'. Phone: the panel's children keep their markup order (order 1), the portrait stays last (4) and
# slides 26 px further under the caption (its top is its own backdrop fading out), about 64 px from the name to the hair
CSS_I = '''#kweker .fd-pn-i > .fp-txt + .fp-lead{margin-top:34px}
#kweker .fd-pn-i > .fp-act + .fd-sig{margin-bottom:clamp(4px,.6vw,8px)}
@media (max-width:860px){
  #kweker .fd-pn-i > .fp-txt{order:1}
  #kweker .fd-pn-i > .fp-lead{order:1;padding-top:32px}
  #kweker .fd-pn-i > .fp-txt + .fp-lead{margin-top:0}
  #kweker .fd-pn-i > .fp-act{order:1}
  #kweker .fd-pn-i > .fp-act + .fd-sig{order:1;margin:24px 0 0 16px}
  #kweker .fd-pn-i > .fd-sig + .fd-sigcap{order:1;margin:6px 0 40px}
  #kweker .fd-card.fd-i > .fd-ph{margin-top:calc(-9% - 26px)}
}
'''

def apply(html, place='a'):
    s = html
    start = s.index('id="kweker"')
    if place == 'i':
        s = apply(s, 'e')
        t0 = s.rindex('<p', 0, s.index('class="fp-txt"', start)); t1 = s.index('</p>', t0) + len('</p>')
        txt = s[t0:t1]; s = s[:t0] + s[t1:]
        l0 = s.rindex('<p', 0, s.index('class="fp-lead"', start) + 1)
        s = s[:l0] + txt + s[l0:]
        s = s.replace('class="fd-pn fd-pn-c fd-pn-e"', 'class="fd-pn fd-pn-c fd-pn-e fd-pn-i"', 1).replace('class="fd-card"', 'class="fd-card fd-i"', 1)
        assert s.index('class="fp-txt"', start) < s.index('class="fp-lead"', start) < s.index('class="fp-act"', start) < s.index('class="fd-sig"', start)
        return s.replace('</style></head>', CSS_I + '</style></head>', 1)
    if place == 'h':
        s = apply(s, 'g')
        s = s.replace('class="fd-card fd-top"', 'class="fd-card fd-top fd-blad"', 1)
        return s.replace('</style></head>', CSS_BLAD + '</style></head>', 1)
    if place == 'g':
        s = apply(s, 'e')
        ph = 'class="ph-m" src="img/fd-podpis-bust.webp" alt="Gert Top, oprichter en kweker van Top Rhododendrons" width="1440" height="1718"'
        assert s.count('class="fd-card"') == 1 and s.count(ph) == 1
        s = s.replace('class="fd-card"', 'class="fd-card fd-top"', 1)
        s = s.replace(ph, ph.replace('fd-podpis-bust', 'fd-foto-top').replace('height="1718"', 'height="1546"'), 1)
        return s.replace('</style></head>', CSS_TOP + '</style></head>', 1)
    if place == 'e':
        s = apply(s, 'd')
        l0 = s.index('class="fp-lead"', start); l1 = s.index('>', l0) + 1; l2 = s.index('</p>', l1)
        s = s[:l1] + LEAD_E + s[l2:]
        s = s.replace('class="fd-pn fd-pn-c"', 'class="fd-pn fd-pn-c fd-pn-e"', 1)
        return s.replace('</style></head>', CSS_E + '</style></head>', 1)
    if place == 'd':
        s = apply(s, 'c')
        l0 = s.index('class="fp-lead"', start); l1 = s.index('>', l0) + 1; l2 = s.index('</p>', l1)
        s = s[:l1] + LEAD_D + s[l2:]
        k = s.index('class="fd-sig"'); k = s.index('>', k) + 1
        s = s[:k] + CAP + s[k:]
        return s.replace('</style></head>', CSS_D + '</style></head>', 1)
    if place == 'c':
        t0 = s.rindex('<p', 0, s.index('class="fp-txt"', start)); t1 = s.index('</p>', t0) + len('</p>')
        txt = s[t0:t1]; s = s[:t0] + s[t1:]
        a = s.index('class="fp-act"', start); e = s.index('</dl></div>', a) + len('</dl></div>')
        s = s[:e] + txt + IMG + s[e:]
        assert s.count('class="fd-pn"') == 1
        s = s.replace('class="fd-pn"', 'class="fd-pn fd-pn-c"', 1)
        assert s.count('class="fd-sig"') == 1
        return s.replace('</head>', '<style id="handtekening-css">' + CSS + CSS_C + '</style></head>', 1)
    if place == 'a':
        i = s.index('</p>', s.index('class="fp-txt"', start)) + len('</p>')
    else:
        a = s.index('class="fp-act"', start)
        i = s.index('</dl></div>', a) + len('</dl></div>')
    s = s[:i] + IMG + s[i:]
    assert s.count('class="fd-sig"') == 1 and s.count('</head>') == 1
    return s.replace('</head>', '<style id="handtekening-css">' + CSS + '</style></head>', 1)
