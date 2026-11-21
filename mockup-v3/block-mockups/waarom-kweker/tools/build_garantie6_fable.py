# (garantie4.html, which this script read, is garantie.html since 21 Nov; frozen, do not rebuild)
# Mockup tool (not site code): garantie6-fable.html = garantie4.html with four bottoms for the label (Fable, 21 Nov).
# The owner: the pointed (triangle) bottom does not suit us. The colour (A2), the cord (2б), the contents and the tilt stay.
#   bt-0 as it is now (the point)
#   bt-1 "Прямой": a straight foot, the same soft corners as the top
#   bt-2 "Дуга": a gentle arc, the label ends like a rounded garden marker
#   bt-3 "Фестоны": a scalloped edge that echoes the scallops of the seal
#   bt-4 "Срезанные углы": two cut corners, the classic shape of a hang tag
# FROZEN (21 Nov): the owner chose bt-1 "Прямой"; it is now in tools/garantie4.css, so this script no longer applies to
# garantie4.html. Do not rebuild; garantie6-fable.html stays as the record of the round.
# The bottom padding follows the shape, so the pdf link always has air under it. Usage: python3 tools/build_garantie6_fable.py [dir]
import re, pathlib, sys
D = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
s = (D / 'garantie4.html').read_text()
CSS = '''/* ===== Review: the bottom of the label (Fable). bt-0 now · bt-1 straight · bt-2 arc · bt-3 scallops · bt-4 cut corners ===== */
body{padding-top:48px}header.fixed{top:48px}
@media (min-width:900px){ .gt-lab{top:calc(80px + 28px - 40px + 48px)} }
@media (min-width:900px) and (max-height:860px){ .gt-lab{top:calc(80px + 20px - 40px + 48px)} .gt-short{margin-top:8px;padding-top:8px} .gt-short li + li{margin-top:3px} }
@media (max-width:520px){ .rv{justify-content:flex-start} }
html.bt-1 .gt-tag{clip-path:none;border-radius:14px;padding-bottom:30px}
html.bt-2 .gt-tag{clip-path:none;border-radius:14px 14px 50% 50% / 14px 14px 54px 54px;padding-bottom:58px}
html.bt-3 .gt-tag{clip-path:none;padding-bottom:44px;--sc:13px;
  -webkit-mask:linear-gradient(#000 0 0) top / 100% calc(100% - var(--sc) + .5px) no-repeat,radial-gradient(circle at 50% 0,#000 calc(var(--sc) - .6px),transparent var(--sc)) bottom / calc(var(--sc) * 2) var(--sc) round no-repeat;
  mask:linear-gradient(#000 0 0) top / 100% calc(100% - var(--sc) + .5px) no-repeat,radial-gradient(circle at 50% 0,#000 calc(var(--sc) - .6px),transparent var(--sc)) bottom / calc(var(--sc) * 2) var(--sc) round no-repeat}
html.bt-4 .gt-tag{padding-bottom:36px;clip-path:polygon(0 0,100% 0,100% calc(100% - 30px),calc(100% - 30px) 100%,30px 100%,0 calc(100% - 30px))}
@media (min-width:900px) and (max-height:860px){ html.bt-2 .gt-tag{padding-bottom:46px;border-radius:14px 14px 50% 50% / 14px 14px 44px 44px} }
@media (max-width:899.98px){
  html.bt-1 .gt-tag{padding-bottom:36px} html.bt-2 .gt-tag{padding-bottom:64px} html.bt-3 .gt-tag{padding-bottom:54px} html.bt-4 .gt-tag{padding-bottom:48px}
}
'''
mh = re.search(r'<html lang="nl" class="([^"]*)">', s); assert mh and not any(c.startswith('bt-') for c in mh.group(1).split())
s = s.replace(mh.group(0), '<html lang="nl" class="' + mh.group(1) + ' bt-2">', 1)
def btn(v, name, on=False):
    return f'<button type="button" data-g="bt" data-v="{v}" aria-pressed="{"true" if on else "false"}">{v}<span class="l"> · {name}</span></button>'
BAR = ('<div class="rv" role="group" aria-label="Варианты"><div class="rv-g"><i>Низ бирки</i>' + btn(0, 'Сейчас') + btn(1, 'Прямой') + btn(2, 'Дуга', True)
       + btn(3, 'Фестоны') + btn(4, 'Срезанные углы') + '</div></div>')
assert '<div class="rv"' not in s and s.count('<div id="root">') == 1 and s.count('</head>') == 1
s = s.replace('<div id="root">', BAR + '<div id="root">').replace('</head>', '<style id="bottom-fable-css">' + CSS + '</style></head>')
(D / 'garantie6-fable.html').write_text(s)
print('ok', len(s))
