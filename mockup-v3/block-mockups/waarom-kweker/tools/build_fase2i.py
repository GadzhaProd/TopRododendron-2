# Mockup tool (not site code): fase2i.html = the main mockup with the example field photo edited to add one more shrub on
# the left (owner, 19 Nov), shown with exactly the main mockup's crop and fades. Review bar on <html>:
#   ks-0 the example as now · ks-1 L1 (as large as the main shrub, front row) · ks-2 L2 (smaller, further back) ·
#   ks-3 L3 (front row, lower and wider). Edits of a CC BY-SA 4.0 photo by JoachimKohler-HB (Wikimedia Commons): mockup only.
# Usage: python3 tools/build_fase2i.py [dir]
import re, pathlib, sys
D = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
s = (D / 'index.html').read_text()
def rep(a, b):
    global s
    assert s.count(a) == 1, (s.count(a), a[:70]); s = s.replace(a, b)
OLD = '<img src="img/voorbeeld/hw-v3-veld.webp" alt="Voorbeeldfoto: bloeiende rhododendrons op een veld" loading="lazy">'
rep(OLD, OLD.replace('<img ', '<img class="l0" ') + ''.join(
    f'<img class="l{k}" src="img/gen/veld-L{k}.webp" alt="Rhododendronveld" loading="lazy">' for k in (1, 2, 3)))
CSS = ('body{padding-top:48px}header.fixed{top:48px}#hero{min-height:calc(100svh - 48px)}'
       '.hwo-band img{display:none}' + ','.join(f'html.ks-{k} .hwo-band .l{k}' for k in range(4)) + '{display:block}')
rep('</head>', '<style id="fase2i-rv">' + CSS + '</style></head>')
Bt = lambda g, v, t, on: f'<button type="button" data-g="{g}" data-v="{v}" aria-pressed="{"true" if on else "false"}">{t}</button>'
rep('<div id="root">', '<div class="rv" role="group" aria-label="Варианты"><div class="rv-g"><i>Куст слева</i>'
    + Bt('ks', '0', 'Как сейчас', 0) + Bt('ks', '1', 'L1', 0) + Bt('ks', '2', 'L2', 1) + Bt('ks', '3', 'L3', 0) + '</div></div><div id="root">')
s = re.sub(r'<html lang="nl" class="([^"]*)">', lambda m: f'<html lang="nl" class="{m.group(1)} ks-2">', s, count=1)
s = re.sub(r'<title>[^<]*</title>', '<title>Hoe het werkt · куст слева</title>', s, count=1)
(D / 'fase2i.html').write_text(s)
print('ok', len(s))
