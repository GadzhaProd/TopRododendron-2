#!/usr/bin/env python3
# Mockup tool (not site code). Built the three fresh concepts from the previous variants page (see git history before this commit); paths point at the session scratchpad.
"""Assemble review/fresh/index.html from the original mockup: header, hero and founder block untouched,
all old Waarom wij variants (and their CSS) replaced by three fresh concepts + a small review bar."""
import re, pathlib

SRC = pathlib.Path('/home/user/TopRododendron-2/mockup-v3/block-mockups/waarom-kweker/index.html')
OUT = pathlib.Path('/tmp/claude-0/-home-user/c2629853-388a-5a4a-89c1-ca1bace13c36/scratchpad/review/fresh/index.html')
s = SRC.read_text()

# 1. html class: our review group "c" (concept) + the approved founder phone variant (m-n3)
s = s.replace('<html lang="nl" class="w-a m-n3 g-m t-0 d-c lp-r">', '<html lang="nl" class="m-n3 t-0 c-1">', 1)
s = s.replace('<title>Waarom wij · De kweker</title>', '<title>Waarom wij · drie nieuwe concepten</title>', 1)

# 2. review bar
rv_start = s.index('<div class="rv" role="group"')
rv_end = s.index('<div id="root">')
rv = ('<div class="rv" role="group" aria-label="Концепции"><div class="rv-g"><i>Концепт</i>'
      '<button type="button" data-g="c" data-v="1" aria-pressed="true">1<span class="l"> · Veldkaart</span></button>'
      '<button type="button" data-g="c" data-v="2" aria-pressed="false">2<span class="l"> · Grondboek</span></button>'
      '<button type="button" data-g="c" data-v="3" aria-pressed="false">3<span class="l"> · Drie in de rij</span></button>'
      '</div></div>')
s = s[:rv_start] + rv + s[rv_end:]

# 3. drop the old Waarom wij CSS (from its first comment up to the hero→card comment) and stray leftovers
a = s.index('/* ---------- Waarom wij ---------- */')
b = s.index('/* ---------- hero → Waarom wij')
s = s[:a] + s[b:]
for junk in [
    '@media (max-width:1100px){.adv{grid-template-columns:repeat(2,minmax(0,1fr))}}\n',
    '@media (max-width:900px){.srow{grid-template-columns:repeat(2,minmax(0,1fr));row-gap:22px}.srow li:nth-child(3){border-left:0;padding-left:0}.el li{grid-template-columns:40px minmax(0,1fr)}.el-note{display:none}}\n',
    '@media (max-width:420px){.wh-head h2{font-size:8.6vw}.srow b{font-size:clamp(20px,6.4vw,26px);white-space:normal}.srow li{padding:0 12px}.srow li:nth-child(odd){padding-left:0}.srow span{font-size:13.5px}}\n',
    '  .wh-head{grid-template-columns:1fr;gap:16px}\n  .adv{grid-template-columns:1fr;gap:26px}\n  .adv li{flex-direction:row;gap:16px}\n  .adv .ic{width:26px;height:26px;margin-top:2px}\n',
]:
    assert junk in s, junk[:40]
    s = s.replace(junk, '', 1)

GRAIN = ("url(\"data:image/svg+xml;utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='220' height='220'%3E%3Cfilter id='n'%3E"
         "%3CfeTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='3' stitchTiles='stitch'/%3E%3CfeColorMatrix type='saturate' values='0'/%3E"
         "%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E\")")

CSS = r"""
/* ================= Waarom wij · three fresh concepts (9 Nov) =================
   Shared language (bs-soft-gradient-deck, translated to the site): eyebrow → confident H2 → one lead; 30 %+ air;
   grain ONLY where there is a gradient under it; hairlines instead of boxes; no numbering, no icons.
   The gradient (four pastel radial blobs + feTurbulence grain) is never a lone object here: in 1 it is the ground a
   photo dissolves into (the founder card's own photo-in-glass language), in 3 it is one of three equal panels whose
   colours are sampled from the two plant photos beside it, and 2 drops it altogether. */
.wz{background:var(--page);color:var(--ink)}
.wz>.in{padding-top:clamp(72px,8vw,128px);padding-bottom:clamp(72px,8vw,128px)}
.wz-eb{margin:0 0 20px;font-size:12.5px;font-weight:600;letter-spacing:.16em;text-transform:uppercase;color:var(--moss)}
.wz h2{margin:0;font-size:clamp(36px,4.4vw,62px);line-height:1.02;letter-spacing:-.035em;font-weight:600;text-wrap:balance}
.wz h3{margin:0;font-weight:600;letter-spacing:-.015em;line-height:1.2;text-wrap:balance}
.wz-lead{margin:0;font-size:17.5px;line-height:1.65;color:var(--ink2);text-wrap:pretty}
.gr{position:absolute;inset:0;pointer-events:none;background:GRAIN;background-size:220px 220px;opacity:.3;mix-blend-mode:overlay}
#w1,#w2,#w3{display:none}.c-1 #w1,.c-2 #w2,.c-3 #w3{display:block}

/* ---------- 1 · Veldkaart ----------
   One tall card: the field photo (the hero's own subject, continued) dissolves downward into the sage/linen gradient,
   and the four facts stand in that ground. Same radius, same gradient family and the same photo-in-glass idea as the
   founder card below, so hero (photo) → Veldkaart (photo into glass) → Gert (portrait in glass) read as one system.
   Left: H2, lead and the four reasons as hairline rows, title | line (21st 37530 "Editorial service list" row anatomy
   without numbers; 19077 "Editorial Image Hero" for the tagline/headline pairing). */
.vk-grid{display:grid;grid-template-columns:minmax(0,1fr) clamp(360px,36%,480px);grid-template-areas:"head card" "list card";grid-template-rows:auto 1fr;column-gap:clamp(48px,6vw,112px)}
.vk-head{grid-area:head}
.vk-head .wz-lead{margin-top:24px;max-width:54ch}
.rl{grid-area:list;align-self:end;list-style:none;margin:clamp(44px,5vw,72px) 0 0;padding:0;border-bottom:1px solid var(--line)}
.rl li{display:grid;grid-template-columns:minmax(0,.86fr) minmax(0,1.14fr);column-gap:clamp(20px,2.4vw,40px);padding:clamp(18px,2vw,24px) 0;border-top:1px solid var(--line);align-items:start}
.rl h3{font-size:clamp(18px,1.5vw,21px)}
.rl p{margin:0;font-size:15.5px;line-height:1.55;color:var(--soft);max-width:44ch}
.vk{grid-area:card;position:relative;isolation:isolate;overflow:hidden;border-radius:28px;display:flex;flex-direction:column;min-height:580px;
  --p:#e7eadf;--b1:#b9c8a0;--b2:#eadabd;--b3:#c6d3b0;--b4:#e9cfd6}
.vk-bg{position:absolute;inset:0;z-index:-2;background:
  radial-gradient(ellipse 75% 42% at 8% 38%,var(--b1) 0%,transparent 66%),
  radial-gradient(ellipse 60% 38% at 96% 50%,var(--b2) 0%,transparent 66%),
  radial-gradient(ellipse 70% 46% at 12% 102%,var(--b3) 0%,transparent 66%),
  radial-gradient(ellipse 62% 42% at 92% 98%,var(--b4) 0%,transparent 66%),var(--p)}
.vk .gr{z-index:-1}
.vk-ph{margin:0;position:relative;flex:1 1 auto;min-height:250px}
.vk-ph img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:50% 68%;display:block;
  -webkit-mask-image:linear-gradient(to bottom,#000 48%,rgba(0,0,0,.78) 66%,rgba(0,0,0,.4) 82%,rgba(0,0,0,.12) 93%,transparent 100%);
          mask-image:linear-gradient(to bottom,#000 48%,rgba(0,0,0,.78) 66%,rgba(0,0,0,.4) 82%,rgba(0,0,0,.12) 93%,transparent 100%)}
.vk-facts{list-style:none;margin:0;padding:4px clamp(24px,2.6vw,40px) clamp(22px,2.4vw,32px);position:relative}
.vk-facts li{display:grid;grid-template-columns:auto minmax(0,1fr);column-gap:18px;align-items:baseline;padding:14px 0;border-top:1px solid rgba(20,20,19,.14)}
.vk-facts li:first-child{border-top:0}
.vk-facts b{font-size:clamp(26px,2.3vw,34px);font-weight:600;line-height:1;letter-spacing:-.03em;color:var(--moss);white-space:nowrap;font-variant-numeric:tabular-nums}
.vk-facts span{font-size:15px;line-height:1.35;color:#33332e}
@media (max-width:1100px){.vk-grid{grid-template-columns:minmax(0,1fr) clamp(320px,38%,420px);column-gap:clamp(36px,4.5vw,64px)}.rl li{grid-template-columns:1fr;row-gap:8px}.vk-facts b{font-size:clamp(24px,2.4vw,30px)}.vk-facts span{font-size:14px}}
@media (max-width:860px){
  .vk-grid{grid-template-columns:1fr;grid-template-areas:"head" "card" "list";grid-template-rows:auto}
  .vk{margin-top:36px;min-height:0;border-radius:22px}
  .vk-ph{min-height:230px;flex:0 0 auto;height:clamp(230px,56vw,320px)}
  .vk-ph img{object-position:50% 72%}
  .vk-bg{background:radial-gradient(ellipse 80% 50% at 0% 40%,var(--b1) 0%,transparent 66%),radial-gradient(ellipse 70% 50% at 100% 55%,var(--b2) 0%,transparent 66%),radial-gradient(ellipse 80% 60% at 10% 100%,var(--b3) 0%,transparent 66%),radial-gradient(ellipse 70% 55% at 100% 100%,var(--b4) 0%,transparent 66%),var(--p)}
  .vk-facts{padding:0 20px 10px}
  .vk-facts li{padding:13px 0;column-gap:14px}
  .vk-facts b{font-size:23px}
  .vk-facts span{font-size:14px}
  .rl{margin-top:40px}
  .rl li{padding:20px 0}
}

/* ---------- 2 · Grondboek ----------
   No gradient, no photo: the hero has the field and Gert has his portrait; this block is the ledger between them.
   Facts and reasons are not two lists but ONE: each large number stands over the promise it backs
   (10.000 in the field → lifted fresh for your delivery; since 2001 → advice from the grower himself;
   7 varieties in 4 sizes → the guarantee on every plant; from 1 plant → own transport or pick-up).
   21st 18908 "Bold Stats" (large numerals on a hairline, small label) and the deck's stat-row archetype; moss numerals
   echo the 2 px moss rule of Gert's quote. Rows align across the four columns with display:contents + explicit grid rows. */
.gb-head{display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,.85fr);column-gap:clamp(40px,6vw,120px);align-items:end}
.gb-head h2{font-size:clamp(38px,5.2vw,76px);letter-spacing:-.04em;line-height:1}
.gb-head .wz-lead{max-width:46ch;padding-bottom:8px}
.lg{list-style:none;margin:clamp(56px,7vw,104px) 0 0;padding:0;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));border-top:1px solid var(--line)}
.lg li{display:contents}
.lg li>*{margin:0;padding-left:clamp(18px,2.2vw,36px);padding-right:clamp(10px,1.4vw,24px);border-left:1px solid var(--line)}
.lg li:first-child>*{padding-left:0;border-left:0}
.lg li:nth-child(1)>*{grid-column:1}.lg li:nth-child(2)>*{grid-column:2}.lg li:nth-child(3)>*{grid-column:3}.lg li:nth-child(4)>*{grid-column:4}
.lg-v{grid-row:1;display:flex;flex-direction:column;justify-content:flex-end;padding-top:30px;gap:8px}
.lg-v small{font-size:12.5px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:var(--soft)}
.lg-v b{font-size:clamp(44px,4.8vw,70px);font-weight:600;line-height:.92;letter-spacing:-.045em;color:var(--moss);white-space:nowrap;font-variant-numeric:tabular-nums}
.lg-l{grid-row:2;padding-top:14px;font-size:15px;line-height:1.4;color:var(--soft);max-width:24ch}
.lg h3{grid-row:3;padding-top:clamp(40px,4.4vw,68px);font-size:clamp(18px,1.5vw,21px)}
.lg p{grid-row:4;padding-top:10px;padding-bottom:6px;font-size:15.5px;line-height:1.55;color:var(--soft)}
@media (max-width:1100px){
  .lg{grid-template-columns:repeat(2,minmax(0,1fr))}
  .lg li:nth-child(3)>*{grid-column:1;padding-left:0;border-left:0}.lg li:nth-child(4)>*{grid-column:2}
  .lg li:nth-child(n+3) .lg-v{grid-row:6;border-top:1px solid var(--line);margin-top:44px}
  .lg li:nth-child(n+3) .lg-l{grid-row:7}.lg li:nth-child(n+3) h3{grid-row:8}.lg li:nth-child(n+3) p{grid-row:9}
  .lg li:nth-child(4) .lg-v{border-left:1px solid var(--line)}
  .lg h3{padding-top:36px}
}
@media (max-width:640px){
  .lg{display:block;border-top:0;margin-top:48px}
  .lg li{display:block;border-top:1px solid var(--line);padding:24px 0 28px}
  .lg li>*,.lg li:nth-child(4) .lg-v{padding-left:0;padding-right:0;border-left:0}
  .lg li:nth-child(n+3) .lg-v{border-top:0;margin-top:0}
  .lg-v{padding-top:0;justify-content:flex-start;align-items:flex-start;gap:6px}
  .lg-v b{font-size:44px}
  .lg-l{padding-top:8px;max-width:none}
  .lg h3{padding-top:22px}
  .lg p{padding-bottom:0}
  .gb-head{grid-template-columns:1fr}
  .gb-head .wz-lead{margin-top:20px;padding-bottom:0}
}
@media (min-width:641px) and (max-width:860px){.gb-head{grid-template-columns:1fr}.gb-head .wz-lead{margin-top:22px;padding-bottom:0}}

/* ---------- 3 · Drie in de rij ----------
   Three equal portrait panels like plants in a row: a white plant, the facts, a red plant. The facts panel is the
   gradient, but it is one of three identical shapes and its colours come from its neighbours (leaf sage, path linen,
   a trace of the red plant as the founder card's pink glow), so it belongs to the row instead of floating alone.
   Under the row the four reasons on one hairline, four columns (skill content-grid without cards; 21st 1195 "Stats
   Section with Text" for the value+label stack, 26797 "Feature Grid Spotlight Cards" for hairline rails). */
.tr-head{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,.8fr);column-gap:clamp(40px,6vw,120px);align-items:end}
.tr-head .wz-lead{max-width:46ch;padding-bottom:6px}
.trio{list-style:none;margin:clamp(48px,6vw,88px) 0 0;padding:0;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:clamp(14px,1.6vw,24px);align-items:stretch}
.trio>li{position:relative;border-radius:28px;overflow:hidden;aspect-ratio:4/5;isolation:isolate;background:#dfe3d6}
.trio>li>img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;display:block}
.trio .cap{position:absolute;left:18px;bottom:16px;margin:0;padding:7px 13px;border-radius:999px;background:rgba(251,250,248,.9);color:var(--ink);font-size:13px;font-weight:600;letter-spacing:.01em}
.tr-facts{display:flex;flex-direction:column;padding:clamp(20px,2.4vw,36px) clamp(22px,2.6vw,40px);--p:#e7eadf;--b1:#b9c8a0;--b2:#eadabd;--b3:#c6d3b0;--b4:#e9cfd6}
.tr-bg{position:absolute;inset:0;z-index:-2;background:
  radial-gradient(ellipse 60% 55% at 8% 8%,var(--b1) 0%,transparent 62%),
  radial-gradient(ellipse 55% 60% at 92% 12%,var(--b2) 0%,transparent 60%),
  radial-gradient(ellipse 65% 60% at 20% 95%,var(--b3) 0%,transparent 60%),
  radial-gradient(ellipse 60% 55% at 85% 90%,var(--b4) 0%,transparent 65%),var(--p)}
.tr-facts .gr{z-index:-1}
.tr-facts ul{list-style:none;margin:0;padding:0;flex:1;display:flex;flex-direction:column}
.tr-facts ul li{flex:1;display:flex;flex-direction:column;justify-content:center;gap:8px;padding:12px 0;border-top:1px solid rgba(20,20,19,.14)}
.tr-facts ul li:first-child{border-top:0}
.tr-facts b{font-size:clamp(28px,2.6vw,40px);font-weight:600;line-height:1;letter-spacing:-.035em;color:var(--moss);font-variant-numeric:tabular-nums}
.tr-facts span{font-size:15px;line-height:1.4;color:#33332e}
.rr{list-style:none;margin:clamp(56px,6.5vw,96px) 0 0;padding:0;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));border-top:1px solid var(--line)}
.rr li{padding:28px clamp(18px,2.2vw,36px) 0;border-left:1px solid var(--line)}
.rr li:first-child{padding-left:0;border-left:0}
.rr h3{font-size:clamp(18px,1.5vw,21px)}
.rr p{margin:10px 0 0;font-size:15.5px;line-height:1.55;color:var(--soft)}
@media (max-width:1100px){
  .tr-facts b{font-size:clamp(26px,3vw,32px)}.tr-facts span{font-size:14px}
  .rr{grid-template-columns:repeat(2,minmax(0,1fr))}
  .rr li:nth-child(3){border-left:0;padding-left:0}
  .rr li:nth-child(n+3){border-top:1px solid var(--line);margin-top:28px;padding-bottom:0}
}
@media (max-width:860px){
  .tr-head{grid-template-columns:1fr}.tr-head .wz-lead{margin-top:22px;padding-bottom:0}
  .trio{grid-template-columns:1fr 1fr;gap:12px;margin-top:40px}
  .trio>li{border-radius:22px}
  .trio>li.tr-facts{grid-column:1/-1;order:-1;aspect-ratio:auto;padding:6px 20px}
  .tr-facts ul li{padding:13px 0;flex-direction:row;align-items:baseline;gap:14px}
  .tr-facts b{font-size:23px;white-space:nowrap}
  .tr-facts span{font-size:14px}
  .trio .cap{left:12px;bottom:12px;font-size:12px;padding:6px 10px}
}
@media (max-width:640px){
  .rr{grid-template-columns:1fr;margin-top:44px}
  .rr li,.rr li:nth-child(3){padding:22px 0;border-left:0}
  .rr li:nth-child(n+3){margin-top:0;border-top:0}
  .rr li+li{border-top:1px solid var(--line)}
}
@media (max-width:420px){.wz h2,.gb-head h2{font-size:8.8vw}}
""".replace('GRAIN', GRAIN)

H2 = 'Wij kweken rhododendrons. <span class="nb">Niet meer, niet minder.</span>'
LEAD = 'Onze planten groeien in de volle grond op veenrijke bodem en ontwikkelen daar een sterk wortelstelsel. Gerooid met kluit, direct van het veld naar uw tuin.'
REASONS = [
    ('Aangroeigarantie op elke plant', 'Niet aangeslagen in het eerste seizoen? Wij vervangen kosteloos.'),
    ('Vers gerooid voor uw levering', 'Wij stemmen bezorging of afhaal af op uw planning en rooien uw planten pas vlak daarvoor.'),
    ('Persoonlijk advies van de kweker', 'De kweker helpt u persoonlijk, <span class="nb">ma–za 09:00–17:00</span>.'),
    ('Eigen transport of afhalen', 'Bezorgd met eigen transport door heel Nederland, of af te halen in Otterlo.'),
]
FACTS = [('10.000', 'planten op voorraad'), ('Sinds 2001', 'familiekwekerij in Otterlo'),
         ('7 soorten', 'in 4 maten, 40 tot 120&nbsp;cm'), ('Vanaf 1&nbsp;plant', 'geen minimumbestelling')]

def reasons(cls, label='Waarom wij'):
    return f'<ul class="{cls}" aria-label="{label}">' + ''.join(f'<li><h3>{t}</h3><p>{p}</p></li>' for t, p in REASONS) + '</ul>'

def facts(cls):
    return f'<ul class="{cls}" aria-label="Feiten">' + ''.join(f'<li><b>{v}</b><span>{l}</span></li>' for v, l in FACTS) + '</ul>'

W1 = (f'<section class="wz" id="w1" aria-labelledby="h-w1"><div class="in"><div class="vk-grid">'
      f'<div class="vk-head"><p class="wz-eb">Waarom wij</p><h2 id="h-w1">{H2}</h2><p class="wz-lead">{LEAD}</p></div>'
      f'<div class="vk"><div class="vk-bg" aria-hidden="true"></div><div class="gr" aria-hidden="true"></div>'
      f'<figure class="vk-ph"><img src="img/B2BHERO-sm.webp" alt="Rhododendronveld in bloei, in de volle grond" width="900" height="502" loading="lazy"></figure>'
      f'{facts("vk-facts")}</div>'
      f'{reasons("rl")}'
      f'</div></div></section>')

# Grondboek: one ledger; each number over the promise it backs
LG = [
    ('', '10.000', 'planten op voorraad', REASONS[1]),
    ('Sinds', '2001', 'familiekwekerij in Otterlo', REASONS[2]),
    ('', '7', 'soorten in 4 maten, 40 tot 120&nbsp;cm', REASONS[0]),
    ('Vanaf', '1 plant', 'geen minimumbestelling', REASONS[3]),
]
lg_items = ''.join(
    f'<li><span class="lg-v">{("<small>"+k+"</small>") if k else ""}<b>{v}</b></span><span class="lg-l">{l}</span><h3>{r[0]}</h3><p>{r[1]}</p></li>'
    for k, v, l, r in LG)
W2 = (f'<section class="wz" id="w2" aria-labelledby="h-w2"><div class="in">'
      f'<div class="gb-head"><div><p class="wz-eb">Waarom wij</p><h2 id="h-w2">{H2}</h2></div><p class="wz-lead">{LEAD}</p></div>'
      f'<ul class="lg" aria-label="Feiten en waarom wij">{lg_items}</ul>'
      f'</div></section>')

W3 = (f'<section class="wz" id="w3" aria-labelledby="h-w3"><div class="in">'
      f'<div class="tr-head"><div><p class="wz-eb">Waarom wij</p><h2 id="h-w3">{H2}</h2></div><p class="wz-lead">{LEAD}</p></div>'
      f'<ul class="trio" aria-label="Onze planten en feiten">'
      f'<li><img src="img/cunninghams-white-2-sm.webp" alt="Rhododendron Cunningham\'s White in bloei" width="672" height="900" loading="lazy"><p class="cap">Cunningham\'s White</p></li>'
      f'<li class="tr-facts"><div class="tr-bg" aria-hidden="true"></div><div class="gr" aria-hidden="true"></div>{facts("")}</li>'
      f'<li><img src="img/nova-zembla-2-sm.webp" alt="Rhododendron Nova Zembla in bloei" width="672" height="900" loading="lazy"><p class="cap">Nova Zembla</p></li>'
      f'</ul>'
      f'{reasons("rr")}'
      f'</div></section>')
W3 = W3.replace('<ul class="" aria-label="Feiten">', '<ul aria-label="Feiten">')

BETWEEN = '<div class="between"><div class="in"><span>… hier volgen Assortiment en Hoe het werkt …</span></div></div>'

# 4. replace all old Waarom sections (+ the old between strip) with ours
a = s.index('<section class="wh" id="waarom"')
b = s.index('<section class="fd" id="kweker"')
s = s[:a] + W1 + W2 + W3 + BETWEEN + s[b:]

# 5. our CSS at the end of the custom stylesheet
s = s.replace('</style></head>', CSS + '</style></head>', 1)

OUT.write_text(s)
print('written', OUT, len(s), 'bytes')
for must in ['id="hero"', 'id="kweker"', 'id="w1"', 'id="w2"', 'id="w3"']:
    assert must in s, must
assert 'id="waarom"' not in s and '.wh-card' not in s
