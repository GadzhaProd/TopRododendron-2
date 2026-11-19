# Mockup tool (not site code): fase2e.html = the main mockup with crop options for the Hoe het werkt field photo
# (owner, 19 Nov: he likes the photo; the bush on the right is cut). The original is cut at that bush too (the frame ends
# there, and the bush stands in front of the second large bush), so a wider crop is not possible. Options on <html>:
#   fc-0 as now · fc-1 soft sides: the left and right edges dissolve into the page like the top and bottom
#   fc-2 mirrored with soft sides: the cut bush moves to the left edge, the open field runs on to the right
# Usage: python3 tools/build_fase2e.py [dir]
import re, pathlib, sys
D = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
s = (D / 'index.html').read_text()
def rep(a, b):
    global s
    assert s.count(a) == 1, (s.count(a), a[:70]); s = s.replace(a, b)
V = 'linear-gradient(to bottom,transparent 0%,rgba(0,0,0,.6) 9%,#000 20%,#000 70%,rgba(0,0,0,.55) 86%,transparent 100%)'
VP = 'linear-gradient(to bottom,transparent 0%,#000 16%,#000 76%,rgba(0,0,0,.55) 89%,transparent 100%)'
H = 'linear-gradient(to right,transparent 0%,#000 9%,#000 78%,transparent 100%)'
HP = 'linear-gradient(to right,transparent 0%,#000 6%,#000 80%,transparent 100%)'
CSS = f'''body{{padding-top:48px}}header.fixed{{top:48px}}#hero{{min-height:calc(100svh - 48px)}}
html:is(.fc-1,.fc-2) .hwo-band img{{-webkit-mask-image:{V},{H};mask-image:{V},{H};-webkit-mask-composite:source-in;mask-composite:intersect}}
html.fc-2 .hwo-band img{{transform:scaleX(-1);-webkit-mask-image:{V},{H.replace("to right","to left")};mask-image:{V},{H.replace("to right","to left")}}}
@media (max-width:860px){{
  html:is(.fc-1,.fc-2) .hwo-band img{{-webkit-mask-image:{VP},{HP};mask-image:{VP},{HP}}}
  html.fc-2 .hwo-band img{{-webkit-mask-image:{VP},{HP.replace("to right","to left")};mask-image:{VP},{HP.replace("to right","to left")}}}
}}'''
rep('</head>', '<style id="fase2e-rv">' + CSS + '</style></head>')
Bt = lambda g, v, t, on: f'<button type="button" data-g="{g}" data-v="{v}" aria-pressed="{"true" if on else "false"}">{t}</button>'
rep('<div id="root">', '<div class="rv" role="group" aria-label="Варианты"><div class="rv-g"><i>Кадр поля</i>'
    + Bt('fc', '0', 'Как сейчас', 0) + Bt('fc', '1', 'Мягкие края', 1) + Bt('fc', '2', 'Зеркально', 0) + '</div></div><div id="root">')
s = re.sub(r'<html lang="nl" class="([^"]*)">', lambda m: f'<html lang="nl" class="{m.group(1)} fc-1">', s, count=1)
s = re.sub(r'<title>[^<]*</title>', '<title>Hoe het werkt · кадр поля</title>', s, count=1)
(D / 'fase2e.html').write_text(s)
print('ok', len(s))
