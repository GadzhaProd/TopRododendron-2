# Mockup tool (not site code): fd-fable.html = the main mockup with three new PHONE compositions of the founder block (10 Nov).
# Desktop (>=861 px) is unchanged: every rule below sits inside @media (max-width:860px); the quote's second sentence gets a <span> by script on phone
# widths only, so the desktop DOM is identical to index.html.
#   0 · Сейчас    the approved navy card, untouched.
#   1 · Обложка   one card, light at the top and navy at the bottom, the portrait is the bridge: the name stands above the
#                 head on the photo's own (continued) backdrop, the jacket melts into navy as approved, the quote is on navy.
#   2 · Разворот  type-led and short: the name stacked large on the left, the portrait as a tile in the card's top-right
#                 corner, then the line and the quote full width in large type. Glass-sage card as on desktop.
#   3 · Подпись   all light: name, line and the large quote first, the portrait rises from the bottom edge of the card
#                 (the jacket is cut by the card edge as on desktop, nothing fades below the chin).
# Derived photos (real photo only; the light backdrop above the hair is continued upward and fades out):
#   img/fd-fable-portrait-top.webp   = backdrop extension + owner-portrait-m.webp   (variant 1)
#   img/fd-fable-portrait-bust.webp  = backdrop extension + owner-portrait.webp     (variant 3)
# Switch via html.ff-0/1/2/3. Usage: python3 tools/build_fd_fable.py [dir]
import re, pathlib, sys
D = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')

# ---------- derived photos ----------
def build_photos():
    from PIL import Image
    import numpy as np
    EXT = 300                                   # px of continued backdrop above the photo (of 1200 px width)
    def g1(row, s):                             # 1-D gaussian along x, per channel
        k = np.exp(-0.5 * (np.arange(-3 * s, 3 * s + 1) / s) ** 2); k /= k.sum()
        return np.stack([np.convolve(np.pad(row[:, c], 3 * s, mode='edge'), k, mode='valid') for c in range(3)], 1)
    def extend(src, out):
        im = np.asarray(Image.open(D / 'img' / src).convert('RGBA')).astype(float)
        H, W, _ = im.shape
        top = g1(im[0:10, :, :3].mean(0), 40)   # rows 0-9 are pure backdrop (the hair starts at row ~30)
        ext = np.zeros((EXT, W, 4))
        ext[..., :3] = top[None]
        rng = np.random.default_rng(7)          # the same fine noise as the photo's backdrop, so no band shows
        ext[..., :3] += rng.normal(0, 1.1, (EXT, W, 1))
        t = np.clip((np.arange(EXT) - 20) / (EXT - 20 - 30), 0, 1)   # transparent at the top, opaque 30 px before the photo
        ext[..., 3] = (255 * (3 * t * t - 2 * t ** 3))[:, None]
        res = np.concatenate([ext, im], 0)
        Image.fromarray(np.clip(res, 0, 255).astype(np.uint8), 'RGBA').save(D / 'img' / out, 'WEBP', quality=86, alpha_quality=100, method=6)
        return res.shape
    print(extend('owner-portrait-m.webp', 'fd-fable-portrait-top.webp'), extend('owner-portrait.webp', 'fd-fable-portrait-bust.webp'))
build_photos()

# ---------- page ----------
s = (D / 'index.html').read_text()
def rep(a, b):
    global s
    assert s.count(a) == 1, (s.count(a), a[:70]); s = s.replace(a, b)

# The quote's second sentence starts its own line on the phone. A <span> in the markup would shift the desktop glyphs by a
# fraction of a pixel (the text run is split), so the hook is added by script on phone widths only and removed again on
# desktop: the desktop DOM stays exactly as in index.html. For the code transfer: render the span only in the phone layout.
Q2 = ("<script>(function(){var p=document.querySelector('#kweker .fd-q p'),m=matchMedia('(max-width:860px)');if(!p)return;"
      "function f(){var t=p.textContent,i=t.indexOf('. ');if(m.matches&&i>0){p.textContent=t.slice(0,i+2);var s=document.createElement('span');"
      "s.className='q2';s.textContent=t.slice(i+2);p.appendChild(s)}else{p.textContent=t}}f();m.addEventListener('change',f)})();</script>")
rep('</body>', Q2 + '</body>')

GRAIN = ("url(\"data:image/svg+xml;utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='220' height='220'%3E%3Cfilter id='n'%3E"
         "%3CfeTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='3' stitchTiles='stitch'/%3E%3CfeColorMatrix type='saturate' values='0'/%3E"
         "%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E\")")

CSS = r'''
/* ===== founder block, phone compositions by Fable (10 Nov); desktop untouched ===== */
body{padding-top:48px}header.fixed{top:48px}#hero{min-height:calc(100svh - 48px)}
@media (max-width:860px){
  /* shared by 1-3 */
  html:is(.ff-1,.ff-2,.ff-3) .fd-card{position:relative;isolation:isolate;padding:0;max-width:520px;margin-inline:auto}
  html:is(.ff-1,.ff-2,.ff-3) .fd-pn{display:contents}
  html:is(.ff-1,.ff-2,.ff-3) .fd-ph{border-radius:0;overflow:hidden}
  html:is(.ff-1,.ff-2,.ff-3) .fd-ph picture{display:none}
  html:is(.ff-1,.ff-2,.ff-3) .fd-ph .ph-in{position:absolute;inset:0;width:100%;height:100%;-webkit-mask-image:none;mask-image:none}
  html:is(.ff-1,.ff-2,.ff-3) .fd-ph .ph-in img.ph-m{display:block;width:100%;height:100%;object-fit:cover}
  html:is(.ff-1,.ff-2,.ff-3) .fd-q .q2{display:block}
  html:is(.ff-1,.ff-2,.ff-3) .fd-q p{max-width:none;text-wrap:balance}
  html:is(.ff-1,.ff-2,.ff-3) .fd-card::before{content:"";position:absolute;inset:0;z-index:1;pointer-events:none;background:GRAIN;background-size:220px 220px;opacity:.26;mix-blend-mode:soft-light}
  html:is(.ff-1,.ff-2,.ff-3) .fd-card > *,html:is(.ff-1,.ff-2,.ff-3) .fd-pn > *{position:relative;z-index:2}

  /* ---------- 1 · Обложка: light top -> portrait -> navy bottom ---------- */
  html.ff-1 .fd-card{grid-template-columns:minmax(0,1fr);
    background:
      radial-gradient(ellipse 70% 150px at 0% 0%,rgba(190,203,170,.55) 0%,transparent 72%),
      radial-gradient(ellipse 60% 130px at 100% 30px,rgba(236,214,210,.6) 0%,transparent 72%),
      #e6e8e5}
  html.ff-1 .fd-name{order:1;padding:30px 22px 0}
  html.ff-1 .fd-name h2{font-size:clamp(54px,16.4vw,72px);line-height:.92;letter-spacing:-.05em;color:#141413}
  html.ff-1 .fd-role{margin-top:12px;font-size:15px;color:#3d3c37}
  html.ff-1 .fd-txt{order:2;margin:14px 0 0;padding:0 22px;font-size:16.5px;line-height:1.5;color:#3d3c37;max-width:34ch}
  /* the photo's continued backdrop reaches up behind the text; its navy tail is backed by the figure's own navy */
  html.ff-1 .fd-ph{order:3;z-index:1;aspect-ratio:1200/1928;margin-top:-18%;
    background:linear-gradient(to bottom,transparent 0,transparent 72%,#263049 72%,#252e48 100%)}
  html.ff-1 .fd-qw{order:4;margin-top:-1px;padding:2px 22px 36px;
    background:
      radial-gradient(ellipse 85% 70% at -6% 104%,rgba(108,126,90,.42) 0%,transparent 70%),
      linear-gradient(to bottom,#252e48 0%,#1c2338 100%)}
  html.ff-1 .fd-q{border-left-color:#a9b894;padding-left:18px}
  html.ff-1 .fd-q p{color:#f5f2ea;font-size:clamp(23px,6.6vw,28px);line-height:1.2}

  /* ---------- 2 · Разворот: name | portrait, then the words ---------- */
  html.ff-2 .fd-card{grid-template-columns:minmax(0,1fr) 57%;
    background:
      radial-gradient(60% 34% at 70% 100%,rgba(224,198,209,.5),transparent 70%),
      linear-gradient(to bottom,#e3e4e4 0%,#d9dcd2 40%,#c9ceb8 72%,#b3bd9f 100%)}
  html.ff-2 .fd-ph{grid-column:2;grid-row:1;aspect-ratio:1200/1418;border-radius:0 0 0 22px}
  html.ff-2 .fd-ph .ph-in img.ph-m{content:url(img/owner-portrait.webp)}
  html.ff-2 .fd-name{grid-column:1;grid-row:1;display:flex;flex-direction:column;justify-content:space-between;padding:22px 0 2px 22px}
  html.ff-2 .fd-name h2{font-size:clamp(50px,14.6vw,84px);line-height:.9;letter-spacing:-.055em;color:#141413;max-width:2.4em}
  html.ff-2 .fd-role{margin:0;font-size:clamp(13px,3.6vw,15px);line-height:1.35;color:#3d3c37;max-width:9.5em}
  html.ff-2 .fd-txt{grid-column:1 / -1;margin:0;padding:24px 22px 0;font-size:16.5px;line-height:1.5;color:#33322e;max-width:none}
  html.ff-2 .fd-qw{grid-column:1 / -1;padding:26px 22px 32px}
  html.ff-2 .fd-q{border-left-color:var(--moss);padding-left:18px}
  html.ff-2 .fd-q p{color:#141413;font-size:clamp(25px,7.1vw,34px);line-height:1.14;letter-spacing:-.03em;font-weight:600}

  /* ---------- 3 · Подпись: the words first, Gert under them, all light ---------- */
  html.ff-3 .fd-card{grid-template-columns:minmax(0,1fr);
    background:
      radial-gradient(ellipse 80% 190px at -10% 40px,rgba(183,198,160,.7) 0%,transparent 72%),
      radial-gradient(ellipse 60% 150px at 106% 150px,rgba(236,214,210,.65) 0%,transparent 72%),
      #e6e8e5}
  html.ff-3 .fd-name{order:1;padding:28px 22px 0}
  html.ff-3 .fd-name h2{font-size:30px;line-height:1.05;letter-spacing:-.035em;color:#141413}
  html.ff-3 .fd-role{margin:6px 0 0;font-size:14.5px;color:#3d3c37}
  html.ff-3 .fd-txt{order:2;margin:16px 0 0;padding:0 22px;font-size:16.5px;line-height:1.5;color:#3d3c37;max-width:34ch}
  html.ff-3 .fd-qw{order:3;padding:24px 22px 0}
  html.ff-3 .fd-q{border-left-color:var(--moss);padding-left:18px}
  html.ff-3 .fd-q p{color:#141413;font-size:clamp(25px,7.1vw,34px);line-height:1.12;letter-spacing:-.035em;font-weight:600}
  html.ff-3 .fd-ph{order:4;z-index:1;aspect-ratio:1200/1718;margin-top:-14%}
  html.ff-3 .fd-ph .ph-in img.ph-m{content:url(img/fd-fable-portrait-bust.webp)}
  html.ff-1 .fd-ph .ph-in img.ph-m{content:url(img/fd-fable-portrait-top.webp)}
}
@media (min-width:861px){.rv::after{content:"Варианты только для телефона";font:500 12px/1 Manrope,system-ui,sans-serif;color:#a9a79f;margin-left:8px}}
'''.replace('GRAIN', GRAIN)
s = s.replace('</head>', '<style id="fd-fable">' + CSS + '</style></head>', 1)
RV = ('<div class="rv" role="group" aria-label="Варианты"><div class="rv-g"><i>Блок Герта</i>'
      '<button type="button" data-g="ff" data-v="0" aria-pressed="false">0<span class="l"> · Сейчас</span></button>'
      '<button type="button" data-g="ff" data-v="1" aria-pressed="true">1<span class="l"> · Обложка</span></button>'
      '<button type="button" data-g="ff" data-v="2" aria-pressed="false">2<span class="l"> · Разворот</span></button>'
      '<button type="button" data-g="ff" data-v="3" aria-pressed="false">3<span class="l"> · Подпись</span></button></div></div>')
rep('<div id="root">', RV + '<div id="root">')
s = re.sub(r'<html lang="nl" class="([^"]*)">', lambda m: f'<html lang="nl" class="{m.group(1)} ff-1">', s, count=1)
s = s.replace('<title>Waarom wij · De kweker</title>', '<title>Gert Top · telefoon · Fable</title>', 1)
(D / 'fd-fable.html').write_text(s)
print('ok', len(s))
