# Mockup tool (not site code): fase1a.html = the main mockup with the type scale and the section rhythm switched on and off
# (phase 1, step A: 1.4 rhythm, 1.5 the guarantee text larger, 1.6 seven type steps), to compare before / after.
#   html.sc-0  как сейчас · html.sc-1  после (tools/scale.css, scoped to html.sc-1)
# Usage: python3 tools/build_fase1a.py [dir]
import re, pathlib, sys
D = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
s = (D / 'index.html').read_text()
def rep(a, b):
    global s
    assert s.count(a) == 1, (s.count(a), a[:70]); s = s.replace(a, b)
css = (D / 'tools' / 'scale.css').read_text().replace('__R__', 'html.sc-1').replace('__S__', 'html.sc-1 ')
rep('</head>', '<style id="fase1a">body{padding-top:48px}header.fixed{top:48px}#hero{min-height:calc(100svh - 48px)}\n' + css + '</style></head>')
rep('<div id="root">', '<div class="rv" role="group" aria-label="Варианты"><div class="rv-g"><i>Шкала и ритм</i>'
    '<button type="button" data-g="sc" data-v="0" aria-pressed="false">До</button>'
    '<button type="button" data-g="sc" data-v="1" aria-pressed="true">После</button></div></div><div id="root">')
s = re.sub(r'<html lang="nl" class="([^"]*)">', lambda m: f'<html lang="nl" class="{m.group(1)} sc-1">', s, count=1)
s = s.replace('<title>Waarom wij · De kweker</title>', '<title>Этап 1 · шкала и ритм</title>', 1)
(D / 'fase1a.html').write_text(s)
print('ok', len(s))
