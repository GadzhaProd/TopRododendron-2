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
# owner, 9 Nov: shorter copy in variant 5 (no repeats of "advies", "familiekwekerij in Otterlo", "eigen transport"); eyebrow removed
LEAD5 = 'Voor uw tuin of uw project kiest u uit eigen kweek.'
WHY5 = [('Aangroeigarantie op elke plant', 'Slaat een plant in het eerste seizoen <span class="nb">niet aan?</span><br class="hl-br"> Dan vervangen wij hem kosteloos.'),
        ('Vers gerooid voor uw levering', 'Wij rooien pas vlak voor uw levering.'),
        ('Persoonlijk advies van de kweker', '<span class="nb">Ma–za 09:00–17:00</span>.'),
        ('Eigen transport of afhalen', 'Bezorgd door heel Nederland, of af te halen in Otterlo.')]
why_in_card = '<ul class="fd-why">' + ''.join(
    (f'<li class="fd-hl"><h3>{t}</h3><p>{d}</p></li>' if n == 0 else f'<li><h3>{t}</h3><p>{d}</p></li>')
    for n, (t, d) in enumerate(WHY5)) + '</ul>'
card5 = card.replace('id="h-kweker-4"', 'id="h-kweker-5"')
card5 = re.sub(r'<p class="fd-txt">.*?</p>', '', card5, count=1, flags=re.S)
card5 = re.sub(r'<div class="fd-qw">.*?</blockquote></div>', '<blockquote class="fd-q kv5-q"><p>Een gezonde plant is geen toeval. Dat is onze standaard.</p></blockquote>' + why_in_card, card5, count=1, flags=re.S)
assert 'fd-why' in card5 and 'kv5-q' in card5 and 'fd-qw' not in card5 and 'fd-txt' not in card5
v5 = (f'<section class="kv kh kv5" id="waarom-5" aria-labelledby="h-waarom-5"><div class="in">'
      f'<div class="kh-top kh-top5"><div class="kh-head"><h2 id="h-waarom-5">{H2}</h2><p class="kv-lead">{LEAD5}</p></div></div>'
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
/* quote one step quieter (owner, 9 Nov): Gert's voice under his name, below the guarantee title in weight and size, above the reason lines */
.kv5 .kv5-q p{font-size:clamp(17px,1.25vw,19px);line-height:1.4;font-weight:400;letter-spacing:-.01em;max-width:34ch;color:#2f2e2a}
/* owner, 9 Nov: the quote on one line where the panel is wide enough (it wraps naturally below that) */
@media (min-width:1200px){.kv5 .kv5-q p{max-width:none;white-space:nowrap}}
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
@media (min-width:861px){.kv5 .fd-pn{padding-bottom:calc(var(--colw) * .2)}}
@media (min-width:861px) and (max-width:1199px){.kv5 .fd-pn{padding-bottom:calc(var(--colw) * .22)}}
@media (min-width:861px) and (max-width:1023px){.kv5 .fd-pn{padding-bottom:calc(var(--colw) * .2)}}
@media (max-width:860px){
  :is(.m-n1,.m-n2,.m-n3) .kv5 .fd-why{border-top-color:rgba(245,242,234,.2)}
  :is(.m-n1,.m-n2,.m-n3) .kv5 .fd-why li{border-bottom-color:rgba(245,242,234,.16)}
  :is(.m-n1,.m-n2,.m-n3) .kv5 .fd-why h3{color:#f5f2ea}
  :is(.m-n1,.m-n2,.m-n3) .kv5 .fd-why .fd-hl h3,:is(.m-n1,.m-n2,.m-n3) .kv5 .fd-why .kv-ic{color:#cdd6b8}
  :is(.m-n1,.m-n2,.m-n3) .kv5 .fd-why p{color:#c9cfdb}
  .kv5 .fd-why li:last-child{border-bottom:0}
  :is(.m-n1,.m-n2,.m-n3) .kv5 .kv5-q p{color:#eef0f4}
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
/* review (9–10 Nov), points 1–2: smaller portrait, larger and darker text; guarantee and quote lead the card */
/* 1 · the photo column narrows to ~36 % and the portrait shrinks to 72 % of the card height, anchored to the bottom (same chin/neck crop);
   its top fades into the card, whose top colour was sampled from the portrait backdrop, so the head gets air above it */
@media (min-width:861px){
  .kv5 .fd-card{--colw:calc((min(100vw,1440px) - 2 * clamp(20px,4vw,80px)) * .36);grid-template-columns:minmax(0,.72fr) minmax(0,1.28fr)}
  .kv5 .fd-ph .ph-in{--w:72cqh;top:auto;bottom:calc(var(--w) * -.0768);left:calc((100cqw - var(--w)) / 2);
    /* owner, 10 Nov: the haze must not touch the hair. the inline alpha mask (395x354) fades the photo's top over 18 % but keeps the head opaque
       (matte taken from the portrait itself, dilated 12 px and feathered), so the backdrop dissolves around the crown, not over it */
    -webkit-mask-image:url(data:image/png;base64,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AgCxAEAsABALAMQCAMQCALEAQCwAEAsAxAIAsQBALAAQCwAQCwDEAgCxAEAsABALAMQCALEAQCwAQCwAEAsAxAIAsQBALAAQCwDEAgCxAACxAEAsABALAMQCALEAQCwAEAsAxAIAxAIAsQBALAAQCwDEAgCxAEAsABALDwEAYgGAWAAgFgCIBQBiAYBYACAWACAWAIgFAGIBgFgAIBYAiAUAYgGAWACAWAAgFgCIBQBiAYBYACAWAIgFAGIBAGIBgFgAIBYAiAUAYgGAWAAgFgCIBQCIBQBiAYBYACAWAIgFAGIBgFgAIBYAIBYAiAUAYgGAWAAgFgCIBQBiAQBiAYBYACAWAIgFAGIBgFgAIBYAiAUAiAUAYgGAWAAgFgCIBQBiAYBYACAWACAWAIgFAGIBgFgAIBYAiAUAYgGAWACAWAAgFgCIBQBiAYBYACAWAIgFAGIBAGIBgFgAIBYAiAUAYgGAWAAgFgCIhYcAALEAQCwAEAsAxAIAsQBALAAQCwAQCwDEAgCxAEAsABALAMQCALEAQCwAQCwAEAsAxAIAsQBALAAQCwDEAgCxAACxAEAsABALAMQCALEAQCwAEAsAxAIAxAIAsQBALAAQCwDEAgCxAEAsABALABALAMQCALEAQCwAEAsAxAIAsQAAsQBALAAQCwDEAgCxAEAsABALAMQCAMQCALEAQCwAEAsAxAIAsQBALAAQCwAQCwDEAgCxAEAsABALAMQCALEAQCwAQCwAEAsAxAIAsQBALAAQCwDEAgCxAACxAEAsABALAMQCALEAQCwAEAsAxMJDAIBYACAWAIgFAGIBgFgAIBYAiAUAiAUAYgGAWAAgFgCIBQBiAYBYACAWACAWAIgFAGIBgFgAIBYAiAUAYgGAWACAWAAgFgCIBQBiAYBYACAWAIgFAIfq//1dY9rLUej3AAAAAElFTkSuQmCC);mask-image:url(data:image/png;base64,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AgCxAEAsABALAMQCAMQCALEAQCwAEAsAxAIAsQBALAAQCwAQCwDEAgCxAEAsABALAMQCALEAQCwAQCwAEAsAxAIAsQBALAAQCwDEAgCxAACxAEAsABALAMQCALEAQCwAEAsAxAIAxAIAsQBALAAQCwDEAgCxAEAsABALDwEAYgGAWAAgFgCIBQBiAYBYACAWACAWAIgFAGIBgFgAIBYAiAUAYgGAWACAWAAgFgCIBQBiAYBYACAWAIgFAGIBAGIBgFgAIBYAiAUAYgGAWAAgFgCIBQCIBQBiAYBYACAWAIgFAGIBgFgAIBYAIBYAiAUAYgGAWAAgFgCIBQBiAQBiAYBYACAWAIgFAGIBgFgAIBYAiAUAiAUAYgGAWAAgFgCIBQBiAYBYACAWACAWAIgFAGIBgFgAIBYAiAUAYgGAWACAWAAgFgCIBQBiAYBYACAWAIgFAGIBAGIBgFgAIBYAiAUAYgGAWAAgFgCIhYcAALEAQCwAEAsAxAIAsQBALAAQCwAQCwDEAgCxAEAsABALAMQCALEAQCwAQCwAEAsAxAIAsQBALAAQCwDEAgCxAACxAEAsABALAMQCALEAQCwAEAsAxAIAxAIAsQBALAAQCwDEAgCxAEAsABALABALAMQCALEAQCwAEAsAxAIAsQAAsQBALAAQCwDEAgCxAEAsABALAMQCAMQCALEAQCwAEAsAxAIAsQBALAAQCwAQCwDEAgCxAEAsABALAMQCALEAQCwAQCwAEAsAxAIAsQBALAAQCwDEAgCxAACxAEAsABALAMQCALEAQCwAEAsAxMJDAIBYACAWAIgFAGIBgFgAIBYAiAUAiAUAYgGAWAAgFgCIBQBiAYBYACAWACAWAIgFAGIBgFgAIBYAiAUAYgGAWACAWAAgFgCIBQBiAYBYACAWAIgFAIfq//1dY9rLUej3AAAAAElFTkSuQmCC);-webkit-mask-size:100% 100%;mask-size:100% 100%;-webkit-mask-repeat:no-repeat;mask-repeat:no-repeat}
}
/* tablets: a narrow photo column would crop the side of the face, so the column stays at ~45 % there */
@media (min-width:861px) and (max-width:1199px){.kv5 .fd-card{--colw:calc((100vw - 2 * clamp(20px,4vw,80px)) * .45);grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr)}}
@media (min-width:861px) and (max-width:1023px){.kv5 .fd-card{--colw:calc((100vw - 2 * clamp(20px,4vw,80px)) * .5);grid-template-columns:minmax(0,1fr) minmax(0,1fr)}.kv5 .fd-ph .ph-in{--w:66cqh}}
.kv5 .fd-why h3{font-size:clamp(17px,1.4vw,20px)}
.kv5 .fd-why p{font-size:clamp(15px,1.12vw,16px);color:#2f2e2a}
.e-a .kv5 .fd-hl h3{font-size:clamp(22px,1.95vw,28px)}
.e-a .kv5 .fd-hl p{font-size:clamp(15.5px,1.2vw,17px)}
/* 2 · quote, the middle option the owner chose: 20 px and darker, still one line on desktop */
.kv5 .kv5-q p{font-size:clamp(18px,1.4vw,20px)!important;color:#262521}
/* B · Полоса on the approved layout (owner, 10 Nov): the band keeps the text on the column line (negative margin = padding),
   the title on the same 28 px step as A, the line on the 16 px step */
@media (min-width:861px){
  .fl-y.e-b .kv5 .fd-why li.fd-hl{margin:16px -24px 8px;padding:24px;border-radius:16px;border-bottom:0}
  .fl-y.e-b .kv5 .fd-why{border-top:0}
  .fl-y.e-b .kv5 .fd-hl h3{font-size:clamp(22px,2.03vw,28px);line-height:1.2}
  .fl-y.e-b .kv5 .fd-hl p{margin-top:8px;font-size:16px;line-height:1.5;color:#2f2e2a}
  .fl-y.e-b .kv5 .fd-hl + li{border-top:0}
}
/* owner, 10 Nov: the band from B, but for the quote (html.q-b). The quote sits on the soft field-colour band instead of the moss rule;
   the guarantee keeps the A treatment. Text stays on the column line (negative margin = padding). */
@media (min-width:861px){
  .fl-y.q-b .kv5 .kv5-q{margin:28px -24px 0;padding:20px 24px;border-left:0;border-radius:16px;
    background:linear-gradient(100deg,rgba(173,187,152,.55) 0%,rgba(222,206,176,.5) 62%,rgba(236,214,210,.45) 100%)}
  .fl-y.q-b .kv5 .fd-why{margin-top:28px}
}
@media (max-width:860px){
  :is(.m-n1,.m-n2,.m-n3).q-b .kv5 .kv5-q{margin:22px -12px 0;padding:16px 12px;border-left:0;border-radius:14px;background:rgba(245,242,234,.09)}
}
/* quote polish (owner, 10 Nov; html.qp-y): the rule is a mid moss-sage #6b7a5e (between the dark moss and the faint site sage; reviewer, 10 Nov) and hangs in the margin,
   so the quote text sits on the same column line as the name and the reasons */
@media (min-width:861px){
  .qp-y.q-l .kv5 .kv5-q{position:relative;border-left:0;padding-left:0}
  .qp-y.q-l .kv5 .kv5-q::before{content:"";position:absolute;left:-22px;top:.15em;bottom:.15em;width:2px;border-radius:2px;background:#6b7a5e}
}
/* the guarantee line breaks after the question when it does not fit on one line (never inside "niet aan") */
.kv5 .hl-br{display:none}
@media (max-width:1279px){.kv5 .hl-br{display:inline}}
/* review bar on phones: the variant buttons are hidden (desktop-only comparisons); the bar scrolls if it still overflows */
@media (max-width:600px){.rv{justify-content:flex-start;overflow-x:auto}.rv .rv-g button{min-width:34px;padding:0 9px}}
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
# reviewer's desktop text layout for variant 5 (10 Nov), scoped to html.fl-y so it can be compared with the previous layout
def scope(css):
    out = []
    for line in css.split('\n'):
        def fix(sel):
            sel = sel.strip()
            if not sel: return sel
            if sel.startswith('.e-a ') or sel.startswith('.fl-l1 '):
                head, rest = sel.split(' ', 1); return f'.fl-y{head} {rest}'
            return f'.fl-y {sel}'
        m = re.match(r'^(\s*)([^@{}/][^{}]*)\{(.*)$', line)
        if m and not m.group(2).strip().startswith('/*'):
            sels = ','.join(fix(x) for x in m.group(2).split(','))
            line = m.group(1) + sels + '{' + m.group(3)
        # selectors inside one-line @media blocks
        line = re.sub(r'(@media[^{]*\{)([^{}]+)\{', lambda mm: mm.group(1) + ','.join(fix(x) for x in mm.group(2).split(',')) + '{', line)
        out.append(line)
    return '\n'.join(out)
FL = scope((D / 'tools' / 'fable-layout.css').read_text())
s = s.replace('</head>', '<style id="fable-layout">' + FL + '</style></head>', 1)
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
      '<button type="button" data-g="e" data-v="c" aria-pressed="false">C<span class="l"> · Линия</span></button></div>'
      '<span class="sep" aria-hidden="true"></span><div class="rv-g"><i>Текст</i>'
      '<button type="button" data-g="fl" data-v="y" aria-pressed="true">Fable</button>'
      '<button type="button" data-g="fl" data-v="n" aria-pressed="false">Было</button></div>'
      '<span class="sep" aria-hidden="true"></span><div class="rv-g"><i>Цитата</i>'
      '<button type="button" data-g="q" data-v="l" aria-pressed="true">Линия</button>'
      '<button type="button" data-g="q" data-v="b" aria-pressed="false">Карточка</button></div>'
      '<span class="sep" aria-hidden="true"></span><div class="rv-g"><i>Правки</i>'
      '<button type="button" data-g="qp" data-v="n" aria-pressed="false">До</button>'
      '<button type="button" data-g="qp" data-v="y" aria-pressed="true">После</button></div></div>')
s = s.replace('<div id="root">', RV + '<div id="root">', 1)
s = re.sub(r'<html lang="nl" class="([^"]*)">', lambda m: f'<html lang="nl" class="{m.group(1)} v-5 e-a fl-y q-l qp-y">', s, count=1)
s = s.replace('<title>Waarom wij · De kweker</title>', '<title>Waarom wij · kritiek</title>', 1)
(D / 'kritiek.html').write_text(s)
print('ok', len(s))
