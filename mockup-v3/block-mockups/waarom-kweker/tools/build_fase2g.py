# Mockup tool (not site code): fase2g.html = the main mockup with the generated field photos in the Hoe het werkt block
# (owner, 19 Nov: generate our own picture instead of the example photo). Generated with google/gemini-3-pro-image-preview
# on OpenRouter (owner's key), text-only prompts A and B from docs/prompt-foto-veld.md; originals 5504 x 3072 on branch
# gen/veld-foto, here 3:1 bands (3840 x 1280) cropped so the shrubs sit in the sharp zone (docs/img/schema-kadra-16x9.png).
# Review bar on <html>: gp-0 the example photo (as now) · gp-1..4 A1, A2, B1, B2 (text only) · gp-5..8 R1..R4 (owner, 19 Nov:
# shrubs as large as in the example; generated with the example photo as the image reference, so these are derivatives of
# a CC BY-SA 4.0 photo by JoachimKohler-HB: mockup only).
# Usage: python3 tools/build_fase2g.py [dir]
import re, pathlib, sys
D = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
s = (D / 'index.html').read_text()
def rep(a, b):
    global s
    assert s.count(a) == 1, (s.count(a), a[:70]); s = s.replace(a, b)
OLD = '<img src="img/voorbeeld/hw-v3-veld.webp" alt="Voorbeeldfoto: bloeiende rhododendrons op een veld" loading="lazy">'
GEN = [('A1', 'gp-1'), ('A2', 'gp-2'), ('B1', 'gp-3'), ('B2', 'gp-4'), ('R1', 'gp-5'), ('R2', 'gp-6'), ('R3', 'gp-7'), ('R4', 'gp-8')]
NEW = OLD.replace('<img ', '<img class="g0" ') + ''.join(
    f'<img class="g{k}" src="img/gen/veld-{n}-band.webp" alt="Rhododendronveld (gegenereerde afbeelding)" loading="lazy">' for k, (n, _) in enumerate(GEN, 1))
rep(OLD, NEW)
CSS = ('body{padding-top:48px}header.fixed{top:48px}#hero{min-height:calc(100svh - 48px)}'
       '.hwo-band img{display:none}' + ','.join(f'html.gp-{k} .hwo-band .g{k}' for k in range(9)) + '{display:block}'
       'html:not(.gp-0) .hwo-band img{object-position:50% 50%}'
       '@media (max-width:860px){html:not(.gp-0) .hwo-band img{object-position:46% 50%}}'
       'html:not(.gp-0) .hw-cr{display:none}')
rep('</head>', '<style id="fase2g-rv">' + CSS + '</style></head>')
Bt = lambda g, v, t, on: f'<button type="button" data-g="{g}" data-v="{v}" aria-pressed="{"true" if on else "false"}">{t}</button>'
rep('<div id="root">', '<div class="rv" role="group" aria-label="Варианты"><div class="rv-g"><i>Фото поля</i>'
    + Bt('gp', '0', 'Пример', 0) + ''.join(Bt('gp', str(k), n, n == 'R2') for k, (n, _) in enumerate(GEN, 1))
    + '</div></div><div id="root">')
s = re.sub(r'<html lang="nl" class="([^"]*)">', lambda m: f'<html lang="nl" class="{m.group(1)} gp-6">', s, count=1)
s = re.sub(r'<title>[^<]*</title>', '<title>Hoe het werkt · сгенерированные фото</title>', s, count=1)
(D / 'fase2g.html').write_text(s)
print('ok', len(s))
