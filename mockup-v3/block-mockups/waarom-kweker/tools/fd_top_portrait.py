# Mockup tool (not site code): the phone portrait for the founder card with the photo on top (variant F, owner 26 Nov: the face
# first on the phone, with a soft transition into the card instead of a hard edge). Source: img/fd-podpis-bust.webp (the approved
# phone bust; its top and right side already dissolve into the card). Only its bottom changes, nothing is painted: the photo
# goes progressively soft and fades out to fully transparent at the bottom edge, so the jacket dissolves into the card colour
# behind it. The fade follows an arc: under the chin (the face's centre, x 42 %) it begins at 88.5 % of the height, so the chin
# stays whole; towards the edges it begins higher (80 %), so the shoulders dissolve first and there is no straight band (a
# straight fade from 88.5 % left a visible horizontal edge across the jacket). Output: img/fd-podpis-top.webp (1440x1718, RGBA).
# Usage: python3 tools/fd_top_portrait.py [start under the chin] [start at the edges] [blur]
import pathlib, sys
import numpy as np
from PIL import Image, ImageFilter
D = pathlib.Path(__file__).resolve().parent.parent
START = float(sys.argv[1]) if len(sys.argv) > 1 else .885
EDGE = float(sys.argv[2]) if len(sys.argv) > 2 else .80
BLUR = float(sys.argv[3]) if len(sys.argv) > 3 else 26   # source px at the bottom edge (about 6 css px on a 390 px phone)
CX = .42                                                  # the face's centre, as a fraction of the width
src = Image.open(D / 'img' / 'fd-podpis-bust.webp').convert('RGBA')
W, H = src.size
a = np.asarray(src).astype(np.float64) / 255
# premultiplied, so blurring next to the transparent backdrop brings in no dark fringe
pm = a.copy(); pm[..., :3] *= pm[..., 3:4]
blurred = np.asarray(Image.fromarray((pm * 255).round().astype(np.uint8), 'RGBA').filter(ImageFilter.GaussianBlur(BLUR))).astype(np.float64) / 255
y = (np.arange(H) / (H - 1))[:, None]
x = (np.arange(W) / (W - 1))[None, :]
start = START - (START - EDGE) * np.clip(np.abs(x - CX) / max(CX, 1 - CX), 0, 1) ** 2
t = np.clip((y - start) / (1 - start), 0, 1)
smooth = (t * t * (3 - 2 * t))[..., None]
mix = pm * (1 - smooth) + blurred * smooth
fade = 1 - smooth ** .85          # eased: the fade gains speed once the collar is reached, ends fully transparent
out = mix * fade
alpha = out[..., 3:4]
rgb = np.where(alpha > 1e-4, out[..., :3] / np.maximum(alpha, 1e-4), 0)
res = np.concatenate([rgb, alpha], axis=-1)
Image.fromarray(np.clip(res * 255, 0, 255).round().astype(np.uint8), 'RGBA').save(D / 'img' / 'fd-podpis-top.webp', 'WEBP', quality=86, alpha_quality=100, method=6)
print('img/fd-podpis-top.webp', W, H, 'fade from', START, 'under the chin,', EDGE, 'at the edges')
