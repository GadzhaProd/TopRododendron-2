# Gert's handwritten signature in the founder block (#kweker), drawn by the owner (25 Nov; img/handtekening-gert-top.svg,
# a light copy for dark grounds in img/handtekening-gert-top-licht.svg). apply(html, place) puts it in the block:
#   'a'  under the guarantee text: the grower signs his promise; the line with his typed name follows right under it
#   'b'  at the end of the panel, under the two numbers: a letter's sign-off
# The typed name stays in the text, so the signature is also an image with a plain alt.
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
'''


def apply(html, place='a'):
    s = html
    start = s.index('id="kweker"')
    if place == 'a':
        i = s.index('</p>', s.index('class="fp-txt"', start)) + len('</p>')
    else:
        a = s.index('class="fp-act"', start)
        i = s.index('</dl></div>', a) + len('</dl></div>')
    s = s[:i] + IMG + s[i:]
    assert s.count('class="fd-sig"') == 1 and s.count('</head>') == 1
    return s.replace('</head>', '<style id="handtekening-css">' + CSS + '</style></head>', 1)
