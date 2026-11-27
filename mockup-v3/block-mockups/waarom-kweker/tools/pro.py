# Plan item 2.6 «Voor professionals» (structure of the homepage, item 7; owner, 18 Nov: missed in the first plan; started 26 Nov):
# a short entrance for professional buyers after "Hoe het werkt", leading to the Groothandel page. Not the wholesale page
# itself: who it is for, three facts, one button and the phone.
#
# Copy: from the current site's /groothandel page (rhododendrons repo, app/groothandel/page.tsx), only what is safe:
#   - who: "Hoveniers en tuinarchitecten", "Openbaar groen en gemeenten", "Vastgoed en wooncomplexen" (its three audiences);
#   - "Vanaf 25 stuks scherpe partijprijzen" (its meta description) -> confirmed for the owner by the project lead, 27 Nov;
#   - "Wij rooien op uw leverdatum" and "eigen transport" (also on this page: Waarom wij, Hoe het werkt);
#   - "zakelijk op factuur" (as in Hoe het werkt; "30 dagen, btw verlegd" is on the old page, to be confirmed).
# Left out until the owner confirms them (plan 2.6, 3.11): the 12/22/30 % discounts, the quote within 24 hours, planting on
# site, the guarantee for businesses ("bij correcte aanplant"), the project cases, NAK membership.
# The button leads to the Groothandel page, groothandel.html (tools/build_groothandel.py, 27 Nov).
#
# apply(html, variant) puts the section between Hoe het werkt and the footer. Both variants: the heading and the line on the
# left, the facts as hairline rows (the variety pages' "Kenmerken") and the button on the right; on the phone one column.
#   'a'  «Строки»: open, on the page itself
#   'b'  «Карточка»: the same in a card in the guarantee card's light (sage and blush glows, grain). The page alternates open
#        and framed blocks (Hoe het werkt above is open, the footer below is dark), so this one would be framed.
# (A card with our field in bloom was tried first and dropped: that photo, B2BHERO, is already the hero's.)
import pathlib, re

# the heading in two lines like the other H2s (a two-sentence heading ran to four lines in the left column)
HEAD = '<h2 id="h-pro" class="pr-h">Voor hoveniers en projecten.</h2>'
LEAD = ('<p class="pr-lead">Ook voor tuinarchitecten, gemeenten en projectontwikkelaars: per partij, '
        '<span class="nb">rechtstreeks van de kwekerij.</span></p>')
# the rows in Fable's final wording (docs/groothandel-tekst-2026-11-26.md, section 7; the B2B answers of 27 Nov): the same words
# as the Groothandel page and the homepage ("pas vlak daarvoor", "zakelijk op factuur")
FACTS = [('Partij', 'Vanaf 25 planten, in een offerte op maat'),
         ('Levering', 'Gerooid vlak voor de levering, bezorgd met eigen transport'),
         ('Betalen', 'Zakelijk op factuur')]
DL = '<dl class="pr-dl">' + ''.join(f'<div><dt>{t}</dt><dd>{d}</dd></div>' for t, d in FACTS) + '</dl>'
ARROW = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6" fill="none" stroke="currentColor" '
         'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>')
CTA = ('<div class="pr-cta"><a class="pr-btn" href="groothandel.html">Vraag een offerte aan' + ARROW + '</a>'
       '<p class="pr-tel">Of bel <a href="tel:+31620104312">06&nbsp;20&nbsp;10&nbsp;43&nbsp;12</a></p></div>')
BODY = '<div class="pr-hd">' + HEAD + LEAD + '</div><div class="pr-bd">' + DL + CTA + '</div>'

MARKUP = {
    'a': '<section class="pr pr-a" id="professionals" aria-labelledby="h-pro"><div class="in pr-in">' + BODY + '</div></section>',
    'b': ('<section class="pr pr-b" id="professionals" aria-labelledby="h-pro"><div class="in"><div class="pr-card pr-in">' + BODY +
          '</div></div></section>'),
}

NOISE = re.search(r'url\("data:image/svg\+xml;utf8,[^"]+"\)', (pathlib.Path(__file__).parent / 'fd-podpis.css').read_text()).group(0)

CSS = '''/* ===== Voor professionals (plan 2.6, tools/pro.py) ===== */
/* the rhythm of the other blocks: Hoe het werkt ends with one --sec, this adds one more above the heading (2 x --sec), and
   one --sec before the footer */
.pr{padding:var(--sec) 0}
.pr :where(h2,p,dl,dt,dd){margin:0;padding:0}
.pr-h{font-size:var(--t-h2)!important;line-height:1.08;color:#141413;text-wrap:balance}
.pr-lead{margin-top:clamp(16px,1.6vw,22px);font-size:var(--t-lead);line-height:1.55;color:#3d3c37;max-width:36em;text-wrap:pretty}
/* two columns from 861 px: the heading and the line left, the facts and the button right, the facts' top line level with
   the heading's first line */
@media (min-width:861px){
  .pr-in{display:grid;grid-template-columns:minmax(0,5fr) minmax(0,6fr);column-gap:clamp(48px,7vw,128px);align-items:start}
  .pr-bd{padding-top:10px}
}
@media (max-width:860px){ .pr-bd{margin-top:30px} }
/* the facts: hairline rows, the label in the soft ink, the value in the text's ink (the variety pages' Kenmerken) */
.pr-dl > div{display:grid;grid-template-columns:minmax(0,9.5em) minmax(0,1fr);column-gap:20px;padding:15px 0;border-top:1px solid rgba(63,74,55,.2)}
.pr-dl > div:last-child{border-bottom:1px solid rgba(63,74,55,.2)}
.pr-dl dt{font-size:var(--t-body);line-height:1.5;color:#5f5e58}
.pr-dl dd{font-size:var(--t-body);line-height:1.5;font-weight:500;color:#141413;text-wrap:pretty}
/* the button: the site's glowing pill (the buy button on the variety pages and in the calculator), its own width */
.pr-cta{display:flex;flex-wrap:wrap;align-items:center;column-gap:24px;row-gap:14px;margin-top:clamp(28px,2.6vw,36px)}
.pr-btn{display:inline-flex;align-items:center;gap:10px;height:52px;padding:0 26px;border-radius:999px;color:#2f3829;font-size:var(--t-body);font-weight:600;text-decoration:none;white-space:nowrap;
  background:radial-gradient(ellipse 46% 160% at 6% 50%,#b3c39b 0%,transparent 72%),radial-gradient(ellipse 50% 170% at 98% 50%,#e6dcb0 0%,transparent 72%),#d3ddc2;box-shadow:inset 0 0 0 1px rgba(63,74,55,.28);transition:background .3s,box-shadow .3s}
.pr-btn svg{width:18px;height:18px;flex:none;transition:transform .3s}
@media (hover:hover){
  .pr-btn:hover{background:radial-gradient(ellipse 46% 160% at 6% 50%,#a9bb90 0%,transparent 72%),radial-gradient(ellipse 50% 170% at 98% 50%,#e0d5a4 0%,transparent 72%),#c8d3b6;box-shadow:inset 0 0 0 1px rgba(63,74,55,.5)}
  .pr-btn:hover svg{transform:translateX(3px)}
}
.pr-btn:focus-visible{outline:2px solid #3f4a37;outline-offset:3px}
.pr-tel{font-size:var(--t-body);line-height:1.5;color:#5f5e58}
.pr-tel a{display:inline-block;padding-block:11px;margin-block:-11px;color:#141413;font-weight:500;text-decoration:underline;text-decoration-thickness:1px;text-decoration-color:rgba(63,74,55,.4);text-underline-offset:5px;white-space:nowrap}
/* narrow phones: the label above the value */
@media (max-width:420px){
  .pr-dl > div{grid-template-columns:minmax(0,1fr);row-gap:2px;padding:13px 0}
  .pr-dl dt{font-size:var(--t-small)}
}

/* b · Карточка: the guarantee card's light; inside, the same two columns */
.pr-card{position:relative;isolation:isolate;border-radius:28px;overflow:hidden;padding:clamp(40px,5vw,80px) clamp(32px,5vw,80px);
  background:radial-gradient(ellipse 55% 75% at 0% 0%,rgba(183,198,160,.55) 0%,transparent 72%),radial-gradient(ellipse 50% 70% at 100% 100%,rgba(236,214,210,.5) 0%,transparent 72%),#e6e8e2}
.pr-card::before{content:"";position:absolute;inset:0;z-index:0;pointer-events:none;background:''' + NOISE + ''';background-size:220px 220px;opacity:.26;mix-blend-mode:soft-light}
.pr-card > *{position:relative;z-index:1}
@media (min-width:861px){ .pr-card.pr-in{column-gap:clamp(40px,5vw,96px)} }
@media (max-width:860px){ .pr-card{border-radius:22px;padding:30px 22px 34px} }
@media (max-width:640px){ .pr-card{border-radius:20px} }
'''


def apply(html, variant='a'):
    s = html
    assert 'id="professionals"' not in s
    i = s.index('id="hoe"'); j = s.index('</section>', i) + len('</section>')
    s = s[:j] + MARKUP[variant] + s[j:]
    assert s.count('</head>') == 1
    return s.replace('</head>', '<style id="pro-css">' + CSS + '</style></head>', 1)
