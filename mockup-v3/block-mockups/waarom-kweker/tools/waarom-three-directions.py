# Three whole-block directions for Waarom wij (C · Центр, P · Фото, R · Колонки); imported by gen_why.py
def build(icon, WHY, STATS):
    H2 = 'Wij kweken rhododendrons. <span class="nb">Niet meer, niet minder.</span>'
    LEAD = 'Onze planten groeien in de volle grond op veenrijke bodem en ontwikkelen daar een sterk wortelstelsel. Gerooid met kluit, direct van het veld naar uw tuin.'
    def card(extra):
        facts = ''.join(f'<li><b>{v}</b><span>{k}</span></li>' for i, v, k in STATS)
        return (f'<div class="wh2-card {extra}"><div class="wh2-bg" aria-hidden="true"></div><div class="wh-grain" aria-hidden="true"></div>'
                f'<ul class="wh2-facts" aria-label="Feiten">{facts}</ul></div>')
    def item(i, t, d, tag='li'):
        return f'<{tag}>{icon(i)}<div><h3>{t}</h3><p>{d}</p></div></{tag}>'
    eb = '<p class="wy-eb">Waarom wij</p>'
    # C · Центр (21st 2749 "About Us section": centred head, items on both sides of a central object, figures in the middle)
    c = ('<section class="wy wc" id="waarom-c" aria-labelledby="h-waarom-c"><div class="in">'
         f'<div class="wc-head">{eb}<h2 id="h-waarom-c">{H2}</h2><p class="wc-lead">{LEAD}</p></div>'
         '<div class="wc-grid">'
         '<ul class="wc-side wc-l">' + item(*WHY[0]) + item(*WHY[1]) + '</ul>'
         + card('wc-card') +
         '<ul class="wc-side wc-r">' + item(*WHY[2]) + item(*WHY[3]) + '</ul>'
         '</div></div></section>')
    # P · Фото (21st 6289 "About Section" photo + figures, 29418 "Split Feature Section", 37530 "Editorial service list")
    p = ('<section class="wy wp" id="waarom-p" aria-labelledby="h-waarom-p"><div class="in"><div class="wp-grid">'
         f'<div class="wp-head">{eb}<h2 id="h-waarom-p">{H2}</h2><p class="wp-lead">{LEAD}</p></div>'
         '<ul class="wp-list">' + ''.join(item(*w) for w in WHY) + '</ul>'
         '<div class="wp-media"><figure class="wp-ph"><img src="img/cunninghams-white-2-sm.webp" alt="Rhododendron Cunningham\'s White in bloei" width="672" height="900" loading="lazy"></figure>'
         + card('wp-card') + '</div>'
         '</div></div></section>')
    # R · Колонки (21st 10445 "Features": head + four icon columns on hairlines; 1521 "Feature Section with hover effects")
    r = ('<section class="wy wr" id="waarom-r" aria-labelledby="h-waarom-r"><div class="in">'
         f'<div class="wr-top"><div class="wr-head">{eb}<h2 id="h-waarom-r">{H2}</h2><p class="wr-lead">{LEAD}</p></div>' + card('wr-card') + '</div>'
         '<ul class="wr-cols">' + ''.join(item(*w) for w in WHY) + '</ul>'
         '</div></section>')
    return c, p, r

CSS = r'''
/* ---------- Waarom wij · three whole-block directions (8–9 Nov) ----------
   Shared: soft-gradient-deck "eyebrow" + heavy H2 + generous air; grain only on the one gradient object (the facts card from K);
   reasons with the site's duotone icons (21st 37504 Cojeev set), no numbers, no boxes. */
.wy{background:var(--page);color:var(--ink)}
.wy > .in{padding-top:clamp(64px,7vw,112px);padding-bottom:clamp(64px,7vw,112px)}
.wy-eb{margin:0 0 18px;font-size:12.5px;font-weight:600;letter-spacing:.16em;text-transform:uppercase;color:var(--moss)}
.wy h2{margin:0;font-size:clamp(34px,4.2vw,58px);line-height:1.04;letter-spacing:-.035em;font-weight:600;text-wrap:balance}
.wy h3{margin:0;font-weight:600;letter-spacing:-.015em;line-height:1.2}
.wy .ic{color:var(--moss)}
.wy .wh2-card{grid-area:auto}

/* C · Центр */
.wc-head{text-align:center;max-width:900px;margin:0 auto}
.wc-lead{margin:22px auto 0;max-width:58ch;font-size:17.5px;line-height:1.65;color:var(--ink2);text-wrap:pretty}
.wc-grid{margin-top:clamp(52px,6vw,88px);display:grid;grid-template-columns:minmax(0,1fr) minmax(320px,400px) minmax(0,1fr);column-gap:clamp(32px,4.5vw,80px);align-items:stretch}
.wc-side{list-style:none;margin:0;padding:0;display:grid;grid-template-rows:1fr 1fr;row-gap:44px}
.wc-side li{align-self:center}
.wc-side li{display:flex;flex-direction:column;gap:16px}
.wc-side .ic{width:30px;height:30px}
.wc-side h3{font-size:clamp(19px,1.6vw,22px)}
.wc-side p{margin:8px 0 0;font-size:15.5px;line-height:1.55;color:var(--soft);max-width:34ch}
.wc-l li{align-items:flex-end;text-align:right}
.wc-l p{margin-left:auto}
.wc-card{min-height:500px}

/* P · Фото */
.wp-grid{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,.9fr);grid-template-areas:"head media" "list media";grid-template-rows:auto 1fr;column-gap:clamp(40px,6vw,104px)}
.wp-head{grid-area:head}
.wp-lead{margin:22px 0 0;max-width:54ch;font-size:17.5px;line-height:1.65;color:var(--ink2);text-wrap:pretty}
.wp-list{grid-area:list;list-style:none;margin:clamp(36px,4vw,56px) 0 0;padding:0;border-top:1px solid var(--line);align-self:start}
.wp-list li{display:grid;grid-template-columns:30px minmax(0,1fr);gap:20px;padding:24px 0;border-bottom:1px solid var(--line);align-items:start}
.wp-list .ic{width:26px;height:26px;margin-top:1px}
.wp-list h3{font-size:clamp(19px,1.7vw,23px)}
.wp-list p{margin:6px 0 0;font-size:15.5px;line-height:1.55;color:var(--soft);max-width:52ch}
.wp-media{grid-area:media;position:relative;padding-bottom:clamp(110px,11vw,160px);align-self:start}
.wp-ph{margin:0;border-radius:28px;overflow:hidden;aspect-ratio:4/5;background:#dfe3d6}
.wp-ph img{display:block;width:100%;height:100%;object-fit:cover}
.wp-card{position:absolute;left:clamp(-64px,-4.4vw,-28px);bottom:0;width:min(80%,420px);padding:10px 28px;box-shadow:0 28px 60px -34px rgba(20,20,19,.4)}
.wp-card .wh2-facts{display:grid;grid-template-columns:max-content minmax(0,1fr);flex:none}
.wp-card .wh2-facts li{display:grid;grid-column:1/-1;grid-template-columns:auto minmax(0,1fr);grid-template-columns:subgrid;column-gap:20px;align-items:baseline;padding:16px 0}
.wp-card .wh2-facts li:first-child{padding-top:16px}.wp-card .wh2-facts li:last-child{padding-bottom:16px}
.wp-card .wh2-facts b{font-size:clamp(24px,2vw,30px);white-space:nowrap}
.wp-card .wh2-facts span{font-size:14.5px;line-height:1.35}

/* R · Колонки */
.wr-top{display:grid;grid-template-columns:minmax(0,1fr) minmax(400px,540px);column-gap:clamp(40px,6vw,104px);align-items:end}
.wr-lead{margin:22px 0 0;max-width:52ch;font-size:17.5px;line-height:1.65;color:var(--ink2);text-wrap:pretty}
.wr-card{padding:clamp(24px,2.4vw,34px)}
@media (min-width:861px){
  .wr-card .wh2-facts{display:grid;grid-template-columns:1fr 1fr;flex:none}
  .wr-card .wh2-facts li{border-top:0;padding:18px 0;flex:none}
  .wr-card .wh2-facts li:nth-child(odd){padding-right:22px}
  .wr-card .wh2-facts li:nth-child(even){padding-left:24px;border-left:1px solid var(--ln)}
  .wr-card .wh2-facts li:nth-child(-n+2){padding-top:0}
  .wr-card .wh2-facts li:nth-child(n+3){border-top:1px solid var(--ln);padding-bottom:0}
  .wr-card .wh2-facts b{font-size:clamp(24px,2.3vw,32px)}
}
.wr-cols{list-style:none;margin:clamp(56px,6vw,88px) 0 0;padding:0;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));border-top:1px solid var(--line)}
.wr-cols li{padding:30px clamp(18px,2.2vw,32px) 0;display:flex;flex-direction:column;gap:22px}
.wr-cols li:first-child{padding-left:0}
.wr-cols li+li{border-left:1px solid var(--line)}
.wr-cols .ic{width:30px;height:30px}
.wr-cols h3{font-size:clamp(18px,1.5vw,21px);min-height:2.45em}
.wr-cols p{margin:8px 0 0;font-size:15px;line-height:1.55;color:var(--soft)}

/* tablets */
@media (max-width:1100px){
  .wr-cols{grid-template-columns:repeat(2,minmax(0,1fr))}
  .wr-cols li:nth-child(3){border-left:0;padding-left:0}
  .wr-cols li:nth-child(n+3){border-top:1px solid var(--line);margin-top:30px}
  .wr-cols h3{min-height:0}
  .wr-top{grid-template-columns:minmax(0,1fr) minmax(360px,440px)}
}
@media (min-width:861px) and (max-width:1023px){
  .wc-grid{grid-template-columns:1fr 1fr;grid-template-areas:"card card" "l r";row-gap:48px}
  .wc-card{grid-area:card;min-height:0;max-width:560px;width:100%;justify-self:center;padding:10px 28px}
  .wc-l{grid-area:l}.wc-r{grid-area:r}
  .wc-l li{align-items:flex-start;text-align:left}.wc-l p{margin-left:0}
  .wc-card .wh2-facts{display:grid;grid-template-columns:max-content minmax(0,1fr);flex:none}
  .wc-card .wh2-facts li{display:grid;grid-column:1/-1;grid-template-columns:subgrid;column-gap:20px;align-items:baseline;padding:14px 0}
  .wc-card .wh2-facts b{font-size:26px;white-space:nowrap}
  .wp-grid{grid-template-columns:minmax(0,1fr) minmax(0,.85fr)}
}
/* phones */
@media (max-width:860px){
  .wc-head{text-align:left}.wc-lead{margin-left:0}
  .wc-grid{display:flex;flex-direction:column;margin-top:0}
  .wc-card{order:-1;min-height:0}
  .wc-side{display:block}
  .wc-side li,.wc-l li{flex-direction:row;align-items:flex-start;text-align:left;gap:16px;padding:22px 0;border-bottom:1px solid var(--line)}
  .wc-l{margin-top:28px;border-top:1px solid var(--line)}
  .wc-l p{margin-left:0}
  .wc-side .ic{width:26px;height:26px;margin-top:2px}
  .wp-grid{display:flex;flex-direction:column}
  .wp-media{order:2;margin-top:32px;padding-bottom:0}
  .wp-ph{aspect-ratio:5/4}
  .wp-card{position:relative;left:auto;bottom:auto;width:auto;margin:-48px 10px 0;padding:6px 18px;box-shadow:0 22px 50px -30px rgba(20,20,19,.4)}
  .wp-card .wh2-facts li{column-gap:14px;padding:13px 0}
  .wp-card .wh2-facts li:first-child{padding-top:13px}.wp-card .wh2-facts li:last-child{padding-bottom:13px}
  .wp-card .wh2-facts b{font-size:21px}
  .wp-card .wh2-facts span{font-size:13.5px}
  .wp-list{order:3;margin-top:32px}
  .wr-top{grid-template-columns:1fr}
  .wr-cols{grid-template-columns:1fr;margin-top:36px}
  .wr-cols li,.wr-cols li:nth-child(3){flex-direction:row;gap:16px;padding:22px 0;border-left:0}
  .wr-cols li+li{border-top:1px solid var(--line)}
  .wr-cols li:nth-child(n){margin-top:0;border-left:0}
  .wr-cols .ic{width:26px;height:26px;margin-top:2px}
}
'''
