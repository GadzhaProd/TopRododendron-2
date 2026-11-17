# Mockup tool (not site code): fase1c.html = the main mockup with phase 1, step C (tools/fase1c.py) and a review bar:
#   "Bestellen": bs-0 always in the header (as now) · bs-1 appears once "Bekijk de planten" has scrolled away
#   Phone header: tp-a call + menu (the cart inside the menu) · tp-b cart + menu (calling inside the menu)
# Usage: python3 tools/build_fase1c.py [dir]
import re, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import fase1c
D = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
s = fase1c.apply((D / 'index.html').read_text())
def rep(a, b):
    global s
    assert s.count(a) == 1, (s.count(a), a[:70]); s = s.replace(a, b)
rep('</head>', '<style id="fase1c-rv">body{padding-top:48px}header.fixed{top:48px}#hero{min-height:calc(100svh - 48px)}'
    '.mm{max-height:calc(100svh - 112px)}@media (min-width:768px){.mm{max-height:calc(100svh - 128px)}}</style></head>')
B = lambda g, v, t, on: f'<button type="button" data-g="{g}" data-v="{v}" aria-pressed="{"true" if on else "false"}">{t}</button>'
rep('<div id="root">', '<div class="rv" role="group" aria-label="Варианты">'
    '<div class="rv-g"><i>Bestellen в шапке</i>' + B('bs', '0', 'Всегда', 0) + B('bs', '1', 'После первого экрана', 1) + '</div>'
    '<div class="rv-g"><i>Шапка на телефоне</i>' + B('tp', 'a', 'Звонок + меню', 1) + B('tp', 'b', 'Корзина + меню', 0) + '</div>'
    '</div><div id="root">')
s = re.sub(r'<html lang="nl" class="([^"]*)">', lambda m: f'<html lang="nl" class="{m.group(1)} bs-1 tp-a">', s, count=1)
s = re.sub(r'<title>[^<]*</title>', '<title>Этап 1 · шаг В</title>', s, count=1)
(D / 'fase1c.html').write_text(s)
print('ok', len(s))
