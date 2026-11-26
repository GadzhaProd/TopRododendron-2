# Gert's handwritten signature in the founder card (#kweker), approved by the owner on 26 Nov (variant E; the history of
# variants A–I is in docs/mockup-decisions.md). The signature is his own drawing (img/handtekening-gert-top.svg; a light copy
# for dark grounds in img/handtekening-gert-top-licht.svg). Applied by tools/finalize_main.py as the last step.
#
# The card's panel, top to bottom (the same order on desktop, on the phone and for a screen reader):
#   1. "Advies van de kwekerij." with one line, then the two numbers: the help comes from the nursery, not from Gert alone
#      (owner, 25–26 Nov: the whole team answers the phone, so his name is not promised on every call)
#   2. the guarantee, "3 maanden aangroeigarantie na levering." with its text and "Lees de voorwaarden"
#   3. the signature under the guarantee (Gert signs the promise) and under it, typed, "Gert Top, oprichter en kweker",
#      the only place his name stands in the card
# On the phone the portrait follows and closes the card, so signature, name and face read as one.
# Also here: the two numbers a step quieter than the headings and a 44 px tap area for "Lees de voorwaarden" (owner and
# reviewer, 26 Nov); on the phone about 26 px less air between the name and the portrait (reviewer, 26 Nov).
#
# For the code transfer: the markup order above; the CSS below; the signature is an <img> with a plain alt.
IMG = ('<img class="fd-sig" src="img/handtekening-gert-top.svg" alt="Handtekening van Gert Top" width="4804" height="1700" '
       'loading="lazy" decoding="async">')
CAP = '<p class="fd-sigcap"><b>Gert Top</b>, oprichter en kweker</p>'
LEAD = '<b class="fd-ask">Advies van de kwekerij.</b>Over een soort, de maat of de garantie: bel of app ons.'

CSS = '''/* Gert's signature (tools/handtekening.py): one dark ink line, about the width of the phone numbers, never a flourish */
#kweker .fd-sig{display:block;width:clamp(150px,12.5vw,184px);height:auto;margin:0}
#kweker .fp-txt + .fd-sig{margin:clamp(16px,1.6vw,22px) 0 clamp(4px,.6vw,8px) -6px}
/* phone: the card is a one-column grid whose text blocks carry their own 22 px side padding and an order (the portrait,
   order 4, overlaps the block above it); the signature and its name take the guarantee's order */
@media (max-width:860px){
  #kweker .fd-sig{width:150px;justify-self:start}
  #kweker .fp-txt + .fd-sig{order:2;margin:18px 0 0 16px}
}
@media print{ #kweker .fd-sig{width:140px} }
/* "Lees de voorwaarden" a 44 px tap target (it was 24 px); margins take the padding back, the line stays put */
#kweker .fp-txt .fp-more{padding-block:10px;margin:-2px 0 -10px}
/* the two numbers a step quieter than the headings: the text size, medium, a finer and lighter underline; the tap area
   stays tall (padding, with an equal negative margin so the rows keep their spacing) */
#kweker .fp-act .fp-num{font-size:var(--t-lead)!important;letter-spacing:-.01em}
#kweker .fp-act .fp-num a{font-weight:500;text-decoration-thickness:1px;text-decoration-color:rgba(63,74,55,.4);text-underline-offset:5px;padding-block:12px;margin-block:-8px}
/* the order: desktop, the panel is a centred flex column, the advice opens it and the guarantee takes the 34 px gap
   (the page's own #kweker .fp-txt{margin-top:0!important} needs the !important); phone, the blocks are ordered grid items */
#kweker .fd-pn-sig > .fp-lead{margin-top:0}
#kweker .fd-pn-sig > .fp-act + .fp-txt{margin-top:34px!important}
@media (max-width:860px){
  #kweker .fd-pn-sig > .fp-lead{order:1;padding-top:28px}
  #kweker .fd-pn-sig > .fp-act{order:1}
  #kweker .fd-pn-sig > .fp-txt{order:2;padding-top:26px}
  #kweker .fd-pn-sig > .fp-act + .fp-txt{margin-top:0!important}
}
/* the typed name under the signature: small, the soft ink of the labels, the name itself in the text's ink */
#kweker .fd-sigcap{margin:6px 0 0;font-size:var(--t-small);line-height:1.4;color:#45443f}
#kweker .fd-sigcap b{font-weight:600;color:#141413}
@media (max-width:860px){
  #kweker .fd-sig + .fd-sigcap{order:2;margin:6px 0 40px;padding:0 22px}
  #kweker .fd-pn-sig > .fp-txt + .fd-sig{margin-bottom:0}
}
/* the advice in the guarantee's type: its heading the guarantee heading's size (--t-sub), its line the guarantee text's
   (--t-lead); the page's own rules set those sizes with !important, so these do too */
#kweker .fd-pn-sig > .fp-lead{font-size:var(--t-lead)!important;line-height:1.55;color:#3d3c37;max-width:50ch}
#kweker .fd-pn-sig .fd-ask{display:block;margin-bottom:clamp(10px,1vw,14px);font-size:var(--t-sub)!important;line-height:1.14;letter-spacing:-.028em;font-weight:600;color:#141413;text-wrap:balance}
@media (max-width:860px){
  #kweker .fd-pn-sig > .fp-lead{line-height:1.5}
  #kweker .fd-pn-sig .fd-ask{line-height:1.2;margin-bottom:8px}
  /* the portrait's top is its own backdrop fading out; it slides 26 px further under the name than before (9 %), so about
     64 px stay between the name and the hair at 390 px */
  #kweker .fd-card-sig > .fd-ph{margin-top:calc(-9% - 26px)}
}
'''


def apply(html):
    s = html
    start = s.index('id="kweker"')
    assert 'class="fd-sig"' not in s
    # the guarantee moves after the numbers (in the markup, so it is read in the order it is seen); the signature and the
    # typed name follow it
    t0 = s.rindex('<p', 0, s.index('class="fp-txt"', start)); t1 = s.index('</p>', t0) + len('</p>')
    txt = s[t0:t1]; s = s[:t0] + s[t1:]
    a = s.index('class="fp-act"', start); e = s.index('</dl></div>', a) + len('</dl></div>')
    s = s[:e] + txt + IMG + CAP + s[e:]
    # the advice line with its own heading (it named Gert before)
    l0 = s.index('class="fp-lead"', start); l1 = s.index('>', l0) + 1; l2 = s.index('</p>', l1)
    s = s[:l1] + LEAD + s[l2:]
    assert s.count('class="fd-pn"') == 1 and s.count('class="fd-card"') == 1 and s.count('</head>') == 1
    s = s.replace('class="fd-pn"', 'class="fd-pn fd-pn-sig"', 1).replace('class="fd-card"', 'class="fd-card fd-card-sig"', 1)
    return s.replace('</head>', '<style id="handtekening-css">' + CSS + '</style></head>', 1)
