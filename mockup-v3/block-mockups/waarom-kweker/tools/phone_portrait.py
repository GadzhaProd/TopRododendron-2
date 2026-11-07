# Mockup tool (not site code): builds img/owner-portrait-m.webp. Usage: python3 phone_portrait.py <out.webp> [preview.png] [fade_start=0.89]
# Phone portrait v4: one uniform treatment across the full width (no zones):
# below the chin the photo goes progressively soft and fades out; underneath lies a broad gradient in the jacket's own
# tones (lit left, shadow right; collar/neck replaced by the jacket, smoothed very wide), which then fades into the card.
from PIL import Image, ImageFilter
import numpy as np, sys
OUT=sys.argv[1]; PREV=sys.argv[2] if len(sys.argv)>2 else None
F0=float(sys.argv[3]) if len(sys.argv)>3 else 0.89     # photo fade starts here (fraction of photo height)
P=np.asarray(Image.open('/home/user/TopRododendron-2/mockup-v3/block-mockups/waarom-kweker/img/owner-portrait.webp').convert('RGB')).astype(float)
H,W,_=P.shape; TAIL=210; HT=H+TAIL
def blur(a,s): return np.asarray(Image.fromarray(np.clip(a,0,255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(s))).astype(float)
def g1(a,s):
    k=np.exp(-0.5*(np.arange(-3*s,3*s+1)/s)**2); k/=k.sum()
    return np.stack([np.convolve(np.pad(a[:,c],3*s,mode='edge'),k,mode='valid') for c in range(a.shape[1])],1)
X=np.arange(W)
row=P[H-14:H].mean(0)
jrow=row.copy(); zone=(X>=350)&(X<=890)
for c in range(3): jrow[zone,c]=np.interp(X[zone],[349,891],[row[349,c],row[891,c]])
base=g1(jrow,160)                                    # very broad: a smooth left-to-right jacket gradient, no detail
# background layer: jacket gradient under the photo's fading part, then a tail that fades into the card
BG=np.repeat(base[None],HT,0); BA=np.ones((HT,W))
for k in range(TAIL):
    u=k/(TAIL-1); BA[H+k]=(1-u)**1.6
# photo layer: progressive soft focus + eased alpha fade, identical across the width
Y0=int(F0*H)-30; sig=[0,1,2,3.5,5.5,8]
Bs=[P]+[blur(P,s) for s in sig[1:]]
ph=P.copy()
for y in range(Y0,H):
    t=(y-Y0)/(H-1-Y0); s=8.0*t**1.5
    i=int(np.searchsorted(sig,s)); i=min(max(i,1),len(sig)-1); a=(s-sig[i-1])/(sig[i]-sig[i-1])
    ph[y]=Bs[i-1][y]*(1-a)+Bs[i][y]*a
PA=np.ones(H); y0=int(F0*H)
for y in range(y0,H):
    t=(y-y0)/(H-1-y0); PA[y]=1-(3*t*t-2*t*t*t)       # smoothstep: soft start, soft end
# composite photo over background
rgb=BG.copy(); alpha=BA.copy()
a=PA[:,None]
rgb[:H]=ph*a[...,None]+BG[:H]*(1-a)[...,None]
im=Image.fromarray(np.dstack([np.clip(rgb,0,255),alpha[...,None]*255]).astype(np.uint8),'RGBA')
im.save(OUT,'WEBP',quality=86,alpha_quality=100,method=6)
if PREV:
    bg=Image.new('RGBA',im.size,(35,44,69,255)); Image.alpha_composite(bg,im).convert('RGB').crop((0,1000,W,HT)).resize((600,(HT-1000)//2)).save(PREV)
print(im.size, base[[0,300,600,900,1199]].astype(int).tolist())
