# Mockup tool (not site code): the phone portrait as a plain photo for the founder card with the photo on top (owner, 26 Nov:
# no fade; "just as a photograph, and the block continues under it"). Source: img/fd-podpis-bust.webp, the approved phone bust
# (the original portrait with its own backdrop continued upward and the desktop's extended right shoulder). It is laid over its
# own backdrop, so it is an ordinary opaque photo with a straight edge all round: behind each pixel the backdrop's colour
# around it (a blur weighted by transparency), so the shoulder's soft edge stays soft (dropping the alpha left a stair-stepped
# edge on the right shoulder). The top is cropped so about 11 % of air stays above the hair (the original photo alone has
# about 3 %, too tight at the top of a card).
# Output: img/fd-foto-top.webp (1440x1546, RGB).
import pathlib
import numpy as np
from PIL import Image
D = pathlib.Path(__file__).resolve().parent.parent
CROP_TOP = 172
src = Image.open(D / 'img' / 'fd-podpis-bust.webp').convert('RGBA')
a = np.asarray(src).astype(np.float64) / 255
rgb, al = a[..., :3], a[..., 3:4]
def box(x, r, axis):
    # a running mean over 2r+1 pixels along one axis, edges repeated
    pad = [(0, 0)] * x.ndim; pad[axis] = (r + 1, r)
    c = np.cumsum(np.pad(x, pad, mode='edge'), axis=axis)
    hi = np.take(c, np.arange(2 * r + 1, c.shape[axis]), axis=axis); lo = np.take(c, np.arange(0, c.shape[axis] - 2 * r - 1), axis=axis)
    return (hi - lo) / (2 * r + 1)
def blur(x, r=14):
    # three box passes in each direction: close to a Gaussian blur, in floating point
    for _ in range(3):
        x = box(box(x, r, 0), r, 1)
    return x
w = 1 - al
bg = blur(rgb * w) / np.maximum(blur(w), 1e-3)
flat = rgb * al + bg * (1 - al)
flat = Image.fromarray(np.clip(flat * 255, 0, 255).round().astype(np.uint8), 'RGB').crop((0, CROP_TOP, src.width, src.height))
flat.save(D / 'img' / 'fd-foto-top.webp', 'WEBP', quality=86, method=6)
print('img/fd-foto-top.webp', flat.size)
