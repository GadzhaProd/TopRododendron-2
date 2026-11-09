# Three bold sketches for Waarom wij (9 Nov). Standalone page, site palette + Manrope.
H2='Wij kweken rhododendrons. <span class="nb">Niet meer, niet minder.</span>'
LEAD='Onze planten groeien in de volle grond op veenrijke bodem en ontwikkelen daar een sterk wortelstelsel. Gerooid met kluit, direct van het veld naar uw tuin.'
WHY=[('Aangroeigarantie op elke plant','Niet aangeslagen in het eerste seizoen? Wij vervangen kosteloos.'),
     ('Vers gerooid voor uw levering','Wij stemmen bezorging of afhaal af op uw planning en rooien uw planten pas vlak daarvoor.'),
     ('Persoonlijk advies van de kweker','De kweker helpt u persoonlijk, <span class="nb">ma–za 09:00–17:00</span>.'),
     ('Eigen transport of afhalen','Bezorgd met eigen transport door heel Nederland, of af te halen in Otterlo.')]
V=[('cunninghams-white',"Cunningham's White"),('nova-zembla','Nova Zembla'),('catawbiense-boursault','Catawbiense Boursault'),
   ('catawbiense-grandiflorum','Catawbiense Grandiflorum'),('ponticum','Ponticum'),('ponticum-roseum','Ponticum Roseum'),('roseum-elegans','Roseum Elegans')]
roots=open('roots.svg.html').read()
why_cols=''.join(f'<li><h3>{t}</h3><p>{d}</p></li>' for t,d in WHY)

s1=('<section class="b b1" id="s1"><div class="in">'
    '<div class="b1-head"><div><p class="eb">Waarom wij</p><h2>'+H2+'</h2></div><p class="lead">'+LEAD+'</p></div>'
    '<div class="b1-cap"><b>7 soorten</b><span>in 4 maten, 40 tot 120&nbsp;cm</span></div>'
    '<ul class="b1-row" aria-label="Onze 7 soorten">'+''.join(f'<li><figure><img src="img/{f}.webp" alt="Rhododendron {n}" width="540" height="900" loading="lazy"></figure><span>{n}</span></li>' for f,n in V)+'</ul>'
    '<ul class="b1-facts"><li><b>10.000</b> planten op voorraad</li><li><b>Sinds 2001</b> familiekwekerij in Otterlo</li><li><b>Vanaf 1&nbsp;plant</b> geen minimumbestelling</li></ul>'
    '<ul class="cols">'+why_cols+'</ul>'
    '</div></section>')

s2=('<section class="b b2" id="s2"><div class="in">'
    '<div class="b2-head"><div><p class="eb">Waarom wij</p><h2>'+H2+'</h2></div><p class="lead">'+LEAD+'</p></div>'
    '<div class="b2-plate">'
    '<div class="b2-above"><img src="img/cw-bush.webp" alt="Rhododendron Cunningham\'s White" width="1200" height="1607">'
    '<span class="b2-tag b2-t1"><i></i>Aangroeigarantie op elke plant</span>'
    '<span class="b2-tag b2-t2"><i></i>7 soorten, in 4 maten</span></div>'
    '<div class="b2-ground"><span class="b2-line" aria-hidden="true"></span>'+roots+
    '<span class="b2-tag b2-g1"><i></i>Volle grond, veenrijke bodem</span>'
    '<span class="b2-tag b2-g2"><i></i>Sterk wortelstelsel</span>'
    '<span class="b2-tag b2-g3"><i></i>Gerooid met kluit, vlak voor uw levering</span></div>'
    '</div>'
    '<ul class="b2-facts"><li><b>10.000</b><span>planten op voorraad</span></li><li><b>Sinds 2001</b><span>familiekwekerij in Otterlo</span></li><li><b>7 soorten</b><span>in 4 maten, 40 tot 120&nbsp;cm</span></li><li><b>Vanaf 1&nbsp;plant</b><span>geen minimumbestelling</span></li></ul>'
    '<ul class="cols">'+why_cols+'</ul>'
    '</div></section>')

s3=('<section class="b b3" id="s3"><div class="in">'
    '<p class="eb">Waarom wij</p>'
    '<p class="b3-num" aria-hidden="true">10.000</p>'
    '<p class="b3-sub"><b>planten op voorraad</b>, in de volle grond in Otterlo. Sinds 2001, vanaf 1 plant, in 7 soorten en 4 maten.</p>'
    '<div class="b3-body"><div><h2>'+H2+'</h2><p class="lead">'+LEAD+'</p></div>'
    '<ul class="b3-list">'+''.join(f'<li><h3>{t}</h3><p>{d}</p></li>' for t,d in WHY)+'</ul></div>'
    '</div></section>')

css=r'''
:root{--page:#f1efea;--card:#fbfaf8;--ink:#141413;--ink2:#45443f;--soft:#5f5e58;--line:#d6d3cb;--moss:#3f4a37;--wash:#8b9a7c;--gut:clamp(20px,4vw,80px)}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--page);color:var(--ink);font-family:Manrope,system-ui,sans-serif;-webkit-font-smoothing:antialiased}
.in{max-width:1440px;margin:0 auto;padding:clamp(72px,8vw,128px) var(--gut)}
.nb{white-space:nowrap}
.eb{margin:0 0 18px;font-size:12.5px;font-weight:600;letter-spacing:.16em;text-transform:uppercase;color:var(--moss)}
h2{margin:0;font-size:clamp(34px,4.4vw,62px);line-height:1.03;letter-spacing:-.035em;font-weight:600;text-wrap:balance}
h3{margin:0;font-size:clamp(17px,1.4vw,19px);line-height:1.25;font-weight:600;letter-spacing:-.01em}
.lead{margin:0;font-size:17.5px;line-height:1.65;color:var(--ink2);max-width:46ch;text-wrap:pretty}
.cols{list-style:none;margin:clamp(48px,5vw,72px) 0 0;padding:0;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));border-top:1px solid var(--line)}
.cols li{padding:26px clamp(16px,2vw,28px) 0}
.cols li:first-child{padding-left:0}.cols li+li{border-left:1px solid var(--line)}
.cols p{margin:8px 0 0;font-size:15px;line-height:1.55;color:var(--soft)}
.sep{height:1px;background:#c9c5bb}
/* 1 · Zeven soorten: the colour of the seven varieties is the hook */
.b1-head{display:grid;grid-template-columns:minmax(0,1.2fr) minmax(0,.8fr);gap:clamp(24px,5vw,96px);align-items:end}
.b1-cap{display:flex;align-items:baseline;gap:14px;margin:clamp(48px,5vw,72px) 0 18px}
.b1-cap b{font-size:clamp(22px,2vw,28px);font-weight:600;letter-spacing:-.02em;color:var(--moss)}
.b1-cap span{font-size:15px;color:var(--soft)}
.b1-row{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(7,minmax(0,1fr));gap:clamp(8px,1vw,14px)}
.b1-row li{display:flex;flex-direction:column;gap:12px}
.b1-row figure{margin:0;aspect-ratio:3/5;border-radius:999px 999px 16px 16px;overflow:hidden;background:#dcdccf}
.b1-row img{display:block;width:100%;height:100%;object-fit:cover}
.b1-row span{font-size:13.5px;line-height:1.3;color:var(--ink2);font-weight:500}
.b1-facts{list-style:none;margin:clamp(36px,4vw,52px) 0 0;padding:0;display:flex;flex-wrap:wrap;gap:10px 36px;font-size:15.5px;color:var(--soft)}
.b1-facts b{color:var(--moss);font-weight:600;font-size:17px;margin-right:6px}
/* 2 · Boven en onder de grond: why the guarantee holds, drawn as a cross-section */
.b2-head{display:grid;grid-template-columns:minmax(0,1.2fr) minmax(0,.8fr);gap:clamp(24px,5vw,96px);align-items:end}
.b2-plate{position:relative;margin-top:clamp(44px,5vw,72px);border-radius:28px;overflow:hidden;background:#2a2219}
.b2-above{position:relative;height:clamp(300px,34vw,500px);overflow:hidden}
.b2-above img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:50% 88%}
.b2-above::after{content:"";position:absolute;left:0;right:0;bottom:0;height:22%;background:linear-gradient(to bottom,transparent,rgba(42,34,25,.55));z-index:1}
.b2-ground{position:relative;height:clamp(280px,27vw,400px);background:linear-gradient(to bottom,rgba(42,34,25,.55),rgba(20,15,10,.82)),url(img/turf.webp) 50% 78%/180% auto;}
.b2-line{position:absolute;left:0;right:0;top:0;height:2px;background:linear-gradient(to right,transparent,rgba(241,239,234,.55) 15%,rgba(241,239,234,.55) 85%,transparent)}
.b2-roots{position:absolute;left:50%;top:0;width:min(70%,860px);transform:translateX(-50%);height:100%}
.b2-kluit{fill:rgba(241,239,234,.06);stroke:rgba(241,239,234,.55);stroke-width:1.6;stroke-dasharray:5 6}
.b2-root path{fill:none;stroke:rgba(236,230,214,.7);stroke-linecap:round}
.b2-tag{position:absolute;z-index:2;display:inline-flex;align-items:center;gap:10px;padding:8px 14px 8px 10px;border-radius:999px;font-size:14px;font-weight:600;white-space:nowrap}
.b2-tag i{width:9px;height:9px;border-radius:50%;flex:none}
.b2-above .b2-tag{background:rgba(251,250,248,.92);color:var(--ink);box-shadow:0 8px 24px -14px rgba(20,20,19,.4)}
.b2-above .b2-tag i{background:var(--moss)}
.b2-ground .b2-tag{background:rgba(20,16,12,.55);color:#f6f3ec;border:1px solid rgba(241,239,234,.28);backdrop-filter:blur(6px)}
.b2-ground .b2-tag i{background:#cdd6b8}
.b2-t1{left:6%;top:24%}.b2-t2{right:6%;top:46%}
.b2-g1{left:5%;top:18%}.b2-g2{right:5%;top:40%}.b2-g3{left:9%;top:70%}
.b2-facts{list-style:none;margin:clamp(36px,4vw,52px) 0 0;padding:0;display:grid;grid-template-columns:repeat(4,minmax(0,1fr))}
.b2-facts li{display:flex;flex-direction:column;gap:6px;padding:0 clamp(16px,2vw,28px)}
.b2-facts li:first-child{padding-left:0}.b2-facts li+li{border-left:1px solid var(--line)}
.b2-facts b{font-size:clamp(26px,2.6vw,38px);font-weight:600;letter-spacing:-.03em;color:var(--moss);line-height:1}
.b2-facts span{font-size:15px;color:var(--soft)}
/* 3 · 10.000: the field inside the number */
.b3-num{margin:0 0 0 -.05em;font-size:clamp(96px,31.5vw,452px);line-height:.86;font-weight:700;letter-spacing:-.065em;
  background:linear-gradient(rgba(16,22,12,.3),rgba(16,22,12,.3)),url(img/field.webp) 40% 70%/cover;-webkit-background-clip:text;background-clip:text;color:transparent}
.b3-sub{margin:20px 0 0;font-size:clamp(18px,1.6vw,22px);line-height:1.5;color:var(--ink2);max-width:52ch}
.b3-sub b{color:var(--ink);font-weight:600}
.b3-body{margin-top:clamp(64px,7vw,104px);padding-top:clamp(36px,4vw,52px);border-top:1px solid var(--line);display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:clamp(32px,6vw,104px)}
.b3-body .lead{margin-top:22px}
.b3-list{list-style:none;margin:0;padding:0}
.b3-list li{padding:20px 0;border-bottom:1px solid var(--line)}
.b3-list li:first-child{padding-top:4px}
.b3-list p{margin:6px 0 0;font-size:15.5px;line-height:1.55;color:var(--soft)}
/* phones */
@media (max-width:860px){
  .b1-head,.b2-head,.b3-body{grid-template-columns:1fr;gap:18px}
  .cols,.b2-facts{grid-template-columns:1fr}
  .cols li,.cols li:first-child{padding:20px 0;border-left:0}.cols li+li{border-top:1px solid var(--line);border-left:0}
  .b2-facts{grid-template-columns:1fr 1fr;row-gap:24px}.b2-facts li:nth-child(3){border-left:0;padding-left:0}
  .b1-row{display:flex;overflow-x:auto;scroll-snap-type:x mandatory;scroll-padding-inline:var(--gut);margin:0 calc(-1 * var(--gut));padding:0 var(--gut);scrollbar-width:none}
  .b3-num{font-size:26.5vw}
  .b1-row li{flex:0 0 38%;scroll-snap-align:start}
  .b2-above{height:280px}.b2-above img{width:92%}
  .b2-ground{height:300px}.b2-roots{width:120%}
  .b2-tag{font-size:12.5px;padding:6px 11px 6px 8px}
  .b2-t1{left:4%;top:8%}.b2-t2{right:4%;top:auto;bottom:10%}
  .b2-g1{left:4%;top:12%}.b2-g2{right:4%;top:44%}.b2-g3{left:4%;top:76%}
}
'''
nav=('<div class="rvb"><a href="#s1">1 · Семь сортов</a><a href="#s2">2 · Над и под землёй</a><a href="#s3">3 · 10.000</a></div>')
rvcss='.rvb{position:sticky;top:0;z-index:9;display:flex;justify-content:center;gap:8px;padding:9px;background:#141413}.rvb a{color:#f1efea;font:600 13px Manrope,sans-serif;text-decoration:none;padding:8px 12px;border:1px solid #3a3a36;border-radius:999px}.b+.b{border-top:8px solid #141413}'
html=('<!doctype html><html lang="nl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Waarom wij · drie schetsen</title>'
      '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400..800&display=swap" rel="stylesheet">'
      '<style>'+css+rvcss+'</style></head><body>'+nav+s1+s2+s3+'</body></html>')
open('index.html','w').write(html); print('ok',len(html))
