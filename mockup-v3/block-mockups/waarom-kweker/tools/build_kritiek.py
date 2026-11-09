# Mockup tool (not site code): kritiek.html = main mockup + four Waarom wij variants from the critic round (9 Nov).
import re, pathlib, sys
D = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
s = (D / 'index.html').read_text()

EB = '<p class="kv-eb">Waarom Top Rhododendrons</p>'
H2 = 'Wij kweken alleen rhododendrons. <span class="nb">Dat merkt u aan elke plant.</span>'
LEAD = 'Een familiekwekerij in Otterlo, gericht op één gewas. Voor uw tuin of uw project kiest u uit eigen kweek, met advies van de kweker zelf.'
WHY = [('Aangroeigarantie op elke plant', 'Niet aangeslagen in het eerste seizoen? Wij vervangen kosteloos.'),
       ('Vers gerooid voor uw levering', 'Wij stemmen bezorging of afhaal af op uw planning en rooien uw planten pas vlak daarvoor.'),
       ('Persoonlijk advies van de kweker', 'De kweker helpt u persoonlijk, <span class="nb">ma–za 09:00–17:00</span>.'),
       ('Eigen transport of afhalen', 'Bezorgd met eigen transport door heel Nederland, of af te halen in Otterlo.')]
FACTS = [('10.000', 'planten op voorraad'), ('Sinds 2001', 'familiekwekerij in Otterlo'), ('7 soorten', 'in 4 maten, 40 tot 120&nbsp;cm'), ('Vanaf 1&nbsp;plant', 'geen minimumbestelling')]
CHECK = ('<svg class="ic kv-ic" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="10" data-accent="" style="fill:var(--wash);fill-opacity:.55"/>'
         '<path d="m9 12 2 2 4-4" data-accent=""/><circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/></svg>')
GRAIN = '<div class="wh-grain" aria-hidden="true"></div>'

def sec(h, sid):
    i = h.index(f'id="{sid}"'); i = h.rfind('<section', 0, i); j = h.index('</section>', i) + len('</section>'); return h[i:j]

# 1 · Текст: K layout and field card kept; eyebrow, benefit H2, new lead; guarantee first and highlighted; phone: reasons before the card
k = sec(s, 'waarom')
v1 = (k.replace('id="waarom"', 'id="waarom-1"').replace('aria-labelledby="h-waarom"', 'aria-labelledby="h-waarom-1"')
       .replace('class="wh wh2"', 'class="wh wh2 kv1"'))
v1 = re.sub(r'<h2 id="h-waarom" class="wh2-h">.*?</h2>', f'<div class="wh2-h">{EB}<h2 id="h-waarom-1">{H2}</h2></div>', v1, count=1, flags=re.S)
v1 = re.sub(r'<p class="wh2-lead">.*?</p>', f'<p class="wh2-lead">{LEAD}</p>', v1, count=1, flags=re.S)
v1 = v1.replace('<li><div><h3>Aangroeigarantie op elke plant</h3>', f'<li class="kv-hl">{CHECK}<div><h3>Aangroeigarantie op elke plant</h3>', 1)
assert 'kv-hl' in v1 and 'kv-eb' in v1

def tiles():
    out = []
    for n, (t, d) in enumerate(WHY):
        if n == 0:
            out.append(f'<li class="kh-hl"><div class="kh-bg" aria-hidden="true"></div>{GRAIN}{CHECK}<h3>{t}</h3><p>{d}</p></li>')
        else:
            out.append(f'<li><h3>{t}</h3><p>{d}</p></li>')
    return '<ul class="kh-why">' + ''.join(out) + '</ul>'
facts = '<ul class="kh-facts" aria-label="Feiten">' + ''.join(f'<li><b>{v}</b><span>{l}</span></li>' for v, l in FACTS) + '</ul>'

def hybrid(n, figure, extra_head=''):
    return (f'<section class="kv kh kv{n}" id="waarom-{n}" aria-labelledby="h-waarom-{n}"><div class="in">'
            f'<div class="kh-top"><div class="kh-head">{EB}<h2 id="h-waarom-{n}">{H2}</h2><p class="kv-lead">{LEAD}</p>{extra_head}</div>{figure}</div>'
            + tiles() + facts + '</div></section>')

# 2 · Фото: the critic's structure with a real photo (Cunningham's White bush)
v2 = hybrid(2, '<figure class="kh-ph"><img src="img/cw-bush.webp" alt="Rhododendron Cunningham\'s White in bloei" width="1200" height="1607" loading="lazy"></figure>')
# 3 · Герт: the same structure with Gert's portrait and his quote, so the separate founder block can go
QUOTE = '<blockquote class="kh-q"><p>Een gezonde plant is geen toeval. Dat is onze standaard.</p><footer>Gert Top, oprichter</footer></blockquote>'
v3 = hybrid(3, '<figure class="kh-ph kh-gert"><img src="img/owner-portrait.webp" alt="Gert Top, oprichter en kweker van Top Rhododendrons" width="1200" height="1418" loading="lazy"></figure>', QUOTE)
# 4 · Карточка Герта: the approved founder card placed inside the block, between the heading and the reasons
fdcard = sec(s, 'kweker')
i = fdcard.index('<div class="fd-card">'); j = fdcard.rindex('</div></div></section>')
card = fdcard[i:j + len('</div>')].replace('id="h-kweker"', 'id="h-kweker-4"')
v4 = (f'<section class="kv kh kv4" id="waarom-4" aria-labelledby="h-waarom-4"><div class="in">'
      f'<div class="kh-top kh-top4"><div class="kh-head">{EB}<h2 id="h-waarom-4">{H2}</h2></div><p class="kv-lead">{LEAD}</p></div>'
      f'<div class="kv4-card">{card}</div>' + tiles() + facts + '</div></section>')

# 5 · Герт + преимущества: the founder card keeps only the name and role; the four reasons sit in the same card; facts strip below
why_in_card = '<ul class="fd-why">' + ''.join(
    (f'<li class="fd-hl"><h3>{t}</h3><p>{d}</p></li>' if n == 0 else f'<li><h3>{t}</h3><p>{d}</p></li>')
    for n, (t, d) in enumerate(WHY)) + '</ul>'
card5 = card.replace('id="h-kweker-4"', 'id="h-kweker-5"')
card5 = re.sub(r'<p class="fd-txt">.*?</p>', '', card5, count=1, flags=re.S)
card5 = re.sub(r'<div class="fd-qw">.*?</blockquote></div>', '<blockquote class="fd-q kv5-q"><p>Een gezonde plant is geen toeval. Dat is onze standaard.</p></blockquote>' + why_in_card, card5, count=1, flags=re.S)
assert 'fd-why' in card5 and 'kv5-q' in card5 and 'fd-qw' not in card5 and 'fd-txt' not in card5
v5 = (f'<section class="kv kh kv5" id="waarom-5" aria-labelledby="h-waarom-5"><div class="in">'
      f'<div class="kh-top kh-top5"><div class="kh-head">{EB}<h2 id="h-waarom-5">{H2}</h2><p class="kv-lead">{LEAD}</p></div></div>'
      f'<div class="kv4-card">{card5}</div>' + facts + '</div></section>')
s = s.replace(k, k + v1 + v2 + v3 + v4 + v5, 1)

CSS = r'''
/* ===== critic round (9 Nov): four Waarom wij variants; switch via html.v-0..v-4 ===== */
body{padding-top:48px}header.fixed{top:48px}#hero{min-height:calc(100svh - 48px)}
#waarom,#waarom-1,#waarom-2,#waarom-3,#waarom-4,#waarom-5{display:none}
.v-0 #waarom,.v-1 #waarom-1,.v-2 #waarom-2,.v-3 #waarom-3,.v-4 #waarom-4,.v-5 #waarom-5{display:block}
.v-3 #kweker,.v-4 #kweker,.v-5 #kweker{display:none}
.kv-eb{display:flex;align-items:center;gap:16px;margin:0 0 20px;font-size:12.5px!important;line-height:1.4!important;font-weight:600!important;letter-spacing:.16em!important;text-transform:uppercase;color:var(--moss)}
.kv-eb::after{content:"";width:72px;height:1px;background:currentColor;opacity:.45}
.kv-ic{width:26px;height:26px;color:var(--moss)}
/* 1 · Текст */
.kv1 .wh2-list li.kv-hl{grid-template-columns:34px minmax(0,1fr);align-items:start}
.kv1 .wh2-list li.kv-hl .kv-ic{margin-top:3px}
.kv1 .wh2-list li.kv-hl h3{color:var(--moss)}
@media (max-width:860px){.kv1 .wh2-grid{grid-template-areas:"h" "l" "list" "card"}.kv1 .wh2-list{margin-top:36px}.kv1 .wh2-card{margin-top:36px}}
/* 2–4 · hybrid: head + photo, reasons as soft tiles (guarantee on the field gradient), facts strip */
.kv{background:var(--page);color:var(--ink)}
.kv > .in{padding-top:clamp(64px,7vw,112px);padding-bottom:clamp(64px,7vw,112px)}
.kv h2{margin:0;font-size:clamp(34px,4.2vw,58px);line-height:1.04;letter-spacing:-.035em;font-weight:600;text-wrap:balance}
.kv h3{margin:0;font-size:clamp(18px,1.5vw,20px);line-height:1.25;font-weight:600;letter-spacing:-.01em}
.kv-lead{margin:22px 0 0;font-size:17.5px;line-height:1.65;color:var(--ink2);max-width:46ch;text-wrap:pretty}
.kh-top{display:grid;grid-template-columns:minmax(0,1.05fr) minmax(0,.95fr);gap:clamp(32px,5vw,88px);align-items:center}
.kh-ph{margin:0;border-radius:24px;overflow:hidden;aspect-ratio:5/4;background:#dfe3d6}
.kh-ph img{display:block;width:100%;height:100%;object-fit:cover;object-position:50% 62%}
.kh-gert{aspect-ratio:1/1}.kh-gert img{object-position:50% 18%}
.kh-q{margin:28px 0 0;padding-left:clamp(18px,1.6vw,24px);border-left:2px solid var(--moss)}
.kh-q p{margin:0;font-size:clamp(20px,1.8vw,26px);line-height:1.25;font-weight:500;letter-spacing:-.02em;max-width:24ch}
.kh-q footer{margin-top:10px;font-size:14px;color:var(--soft)}
.kh-top4{align-items:end}.kh-top4 .kv-lead{margin:0}
.kv4-card{margin-top:clamp(40px,4.5vw,64px)}
.kh-why{list-style:none;margin:clamp(44px,5vw,72px) 0 0;padding:0;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:16px}
.kh-why li{position:relative;isolation:isolate;overflow:hidden;padding:26px 24px 28px;border-radius:20px;background:var(--card);border:1px solid rgba(20,20,19,.07)}
.kh-why p{margin:8px 0 0;font-size:15px;line-height:1.55;color:var(--soft)}
.kh-why .kh-hl{border-color:transparent}
.kh-hl .kv-ic{display:block;margin-bottom:14px}
.kh-hl h3{color:var(--moss)}
.kh-hl p{color:#3d3c37}
.kh-bg{position:absolute;inset:0;z-index:-2;background:radial-gradient(ellipse 80% 70% at 50% -10%,#f1f0e8 0%,transparent 70%),radial-gradient(ellipse 70% 80% at -10% 50%,#adbb98 0%,transparent 68%),radial-gradient(ellipse 120% 60% at 50% 115%,#d9cbb0 0%,transparent 72%),radial-gradient(ellipse 50% 50% at 100% 0%,#ecd6d2 0%,transparent 70%),#ebece3}
.kh-hl .wh-grain{--gr:.3;--gb:overlay}
.kh-facts{list-style:none;margin:clamp(40px,4.5vw,64px) 0 0;padding:28px 0 0;border-top:1px solid var(--line);display:grid;grid-template-columns:repeat(4,minmax(0,1fr))}
.kh-facts li{display:flex;flex-direction:column;gap:6px;padding:0 clamp(16px,2vw,28px)}
.kh-facts li:first-child{padding-left:0}.kh-facts li+li{border-left:1px solid var(--line)}
.kh-facts b{font-size:clamp(26px,2.6vw,40px);line-height:1;font-weight:600;letter-spacing:-.03em;color:var(--moss)}
.kh-facts span{font-size:15px;line-height:1.4;color:var(--soft)}
@media (max-width:1100px){.kh-why{grid-template-columns:repeat(2,minmax(0,1fr))}}
/* 5 · founder card with the reasons inside: name + role, then the reasons on hairlines; the guarantee first with a check */
/* owner, 9 Nov (review point 1): the quote links the portrait and the reasons; the name steps down so the card stops reading as a business card */
.kv5 .fd-name h2{font-size:clamp(32px,2.8vw,40px);letter-spacing:-.035em}
.kv5 .fd-role{margin-top:8px}
.kv5 .kv5-q{margin:clamp(20px,2vw,28px) 0 0}
.kv5 .kv5-q p{font-size:clamp(19px,1.5vw,22px);line-height:1.3;font-weight:500;letter-spacing:-.015em;max-width:30ch}
.fd-why{list-style:none;margin:clamp(24px,2.6vw,36px) 0 0;padding:0;border-top:1px solid rgba(20,20,19,.14)}
.fd-why li{padding:clamp(12px,1.25vw,17px) 0;border-bottom:1px solid rgba(20,20,19,.12)}
.fd-why h3{display:flex;align-items:center;gap:10px;margin:0;font-size:clamp(16.5px,1.3vw,19px);line-height:1.25;font-weight:600;letter-spacing:-.01em}
.fd-why p{margin:4px 0 0;font-size:clamp(14px,1.05vw,15px);line-height:1.5;color:#3d3c37;max-width:52ch}
.fd-why .fd-hl h3{color:var(--moss)}
.fd-why .kv-ic{width:22px;height:22px;flex:none}
.kv5 .kh-facts{margin-top:clamp(36px,4vw,56px)}
.kh-top5{grid-template-columns:minmax(0,1fr)}
.kh-top5 .kv-lead{max-width:44ch}
@media (min-width:1200px){
  .kv5 .fd-pn{padding-left:clamp(8px,1vw,20px);padding-right:clamp(40px,4.4vw,72px)}
  .kv5 .fd-why p{max-width:none}
}
/* keep the last reason clear of the drawn-on shoulder (the quote made the card taller, so the photo and shoulder grow too) */
@media (min-width:861px){.kv5 .fd-pn{padding-bottom:calc(var(--colw) * .24)}}
@media (min-width:861px) and (max-width:1199px){.kv5 .fd-pn{padding-bottom:calc(var(--colw) * .32)}}
@media (min-width:861px) and (max-width:1023px){.kv5 .fd-pn{padding-bottom:calc(var(--colw) * .54)}}
@media (max-width:860px){
  :is(.m-n1,.m-n2,.m-n3) .kv5 .fd-why{border-top-color:rgba(245,242,234,.2)}
  :is(.m-n1,.m-n2,.m-n3) .kv5 .fd-why li{border-bottom-color:rgba(245,242,234,.16)}
  :is(.m-n1,.m-n2,.m-n3) .kv5 .fd-why h3{color:#f5f2ea}
  :is(.m-n1,.m-n2,.m-n3) .kv5 .fd-why .fd-hl h3,:is(.m-n1,.m-n2,.m-n3) .kv5 .fd-why .kv-ic{color:#cdd6b8}
  :is(.m-n1,.m-n2,.m-n3) .kv5 .fd-why p{color:#c9cfdb}
  .kv5 .fd-why li:last-child{border-bottom:0}
  .kv5 .fd-name h2{font-size:30px}
}
/* review point 2 (9 Nov): three ways to lead with the guarantee, no icon; switch via html.e-a / e-b / e-c
   A · Typografie (Impeccable: emphasis from size, weight and rhythm): a bigger ink title, a slightly larger line, more air after it
   B · Band (21st 27506 "Feature List Showcase": the active row on a soft tint): the guarantee row on a light field-colour wash
   C · Lijn (the reviewer's suggestion): a 2px moss rule on the left; Impeccable lists coloured side rules as a category default */
.kv5 .fd-why .fd-hl h3{color:#141413}
.e-a .kv5 .fd-hl{padding:clamp(16px,1.6vw,22px) 0 clamp(18px,1.9vw,26px)}
.e-a .kv5 .fd-hl h3{font-size:clamp(20px,1.7vw,24px);letter-spacing:-.02em;line-height:1.2}
.e-a .kv5 .fd-hl p{margin-top:6px;font-size:clamp(15px,1.15vw,16.5px);color:#2f2e2a}
.e-b .kv5 .fd-hl{margin:10px calc(-1 * clamp(12px,1.2vw,18px)) 6px;padding:clamp(14px,1.3vw,18px) clamp(12px,1.2vw,18px);border-radius:14px;border-bottom-color:transparent;
  background:linear-gradient(100deg,rgba(173,187,152,.55) 0%,rgba(222,206,176,.5) 62%,rgba(236,214,210,.45) 100%)}
.e-b .kv5 .fd-why{border-top-color:transparent}
.e-b .kv5 .fd-hl h3{font-size:clamp(18px,1.45vw,21px)}
.e-c .kv5 .fd-hl{padding-left:16px;border-left:2px solid var(--moss)}
.e-c .kv5 .fd-hl h3{font-size:clamp(18px,1.5vw,21px)}
@media (max-width:860px){
  :is(.m-n1,.m-n2,.m-n3) .kv5 .fd-why .fd-hl h3{color:#f5f2ea}
  :is(.m-n1,.m-n2,.m-n3).e-a .kv5 .fd-hl p{color:#dde2ea}
  :is(.m-n1,.m-n2,.m-n3).e-b .kv5 .fd-hl{background:rgba(245,242,234,.08);margin-left:-12px;margin-right:-12px;padding-left:12px;padding-right:12px}
  :is(.m-n1,.m-n2,.m-n3).e-c .kv5 .fd-hl{border-left-color:#a9b894}
}
/* the second H2 sentence is too long to stay on one line on phones */
@media (max-width:600px){.kv h2 .nb,.kv1 h2 .nb{white-space:normal}}
@media (max-width:860px){
  .kh-top{grid-template-columns:1fr;gap:28px}
  .kh-ph{aspect-ratio:4/3}.kh-gert{aspect-ratio:4/5}
  .kh-why{grid-template-columns:1fr;gap:12px;margin-top:32px}
  .kh-why li{padding:20px}
  .kh-facts{grid-template-columns:1fr 1fr;row-gap:22px}
  .kh-facts li:nth-child(3){border-left:0;padding-left:0}
  .kh-facts b{font-size:26px;white-space:normal}
}
'''
s = s.replace('</head>', '<style id="kritiek">' + CSS + '</style></head>', 1)
RV = ('<div class="rv" role="group" aria-label="Варианты"><div class="rv-g"><i>Блок</i>'
      '<button type="button" data-g="v" data-v="0" aria-pressed="false">0<span class="l"> · Сейчас</span></button>'
      '<button type="button" data-g="v" data-v="1" aria-pressed="false">1<span class="l"> · Текст</span></button>'
      '<button type="button" data-g="v" data-v="2" aria-pressed="false">2<span class="l"> · Фото</span></button>'
      '<button type="button" data-g="v" data-v="3" aria-pressed="false">3<span class="l"> · Герт</span></button>'
      '<button type="button" data-g="v" data-v="4" aria-pressed="false">4<span class="l"> · Карточка Герта</span></button>'
      '<button type="button" data-g="v" data-v="5" aria-pressed="true">5<span class="l"> · Герт + преимущества</span></button></div>'
      '<span class="sep" aria-hidden="true"></span><div class="rv-g"><i>Гарантия</i>'
      '<button type="button" data-g="e" data-v="a" aria-pressed="true">A<span class="l"> · Шрифт</span></button>'
      '<button type="button" data-g="e" data-v="b" aria-pressed="false">B<span class="l"> · Полоса</span></button>'
      '<button type="button" data-g="e" data-v="c" aria-pressed="false">C<span class="l"> · Линия</span></button></div></div>')
s = s.replace('<div id="root">', RV + '<div id="root">', 1)
s = re.sub(r'<html lang="nl" class="([^"]*)">', lambda m: f'<html lang="nl" class="{m.group(1)} v-5 e-a">', s, count=1)
s = s.replace('<title>Waarom wij · De kweker</title>', '<title>Waarom wij · kritiek</title>', 1)
(D / 'kritiek.html').write_text(s)
print('ok', len(s))
