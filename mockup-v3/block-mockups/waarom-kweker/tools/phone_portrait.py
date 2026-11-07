# Mockup tool (not site code): builds img/owner-portrait-m.webp. Usage: python3 phone_portrait.py <out.webp> [preview.png] [arc_end_y=1330]
# Phone portrait v3: jacket/collars soft-focus and fade into the card (as v2); the neck stays sharp down to an arc
# from collar to collar along the bottom of the neck; below the arc the card shows (alpha 0). Colour/blur only.
from PIL import Image, ImageFilter
import numpy as np, sys
OUT=sys.argv[1]; PREV=sys.argv[2] if len(sys.argv)>2 else None
P=np.asarray(Image.open('/home/user/TopRododendron-2/mockup-v3/block-mockups/waarom-kweker/img/owner-portrait.webp').convert('RGB')).astype(float)
H,W,_=P.shape; TAIL=247; HT=H+TAIL
def blur(a,s): return np.asarray(Image.fromarray(np.clip(a,0,255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(s))).astype(float)
def blur1(m,s): return np.asarray(Image.fromarray(np.clip(m*255,0,255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(s))).astype(float)/255
def g1(a,s):
    k=np.exp(-0.5*(np.arange(-3*s,3*s+1)/s)**2); k/=k.sum()
    return np.stack([np.convolve(np.pad(a[:,c],3*s,mode='edge'),k,mode='valid') for c in range(a.shape[1])],1)
X=np.arange(W)
# --- tail colours: jacket only (collar strips replaced by the jacket), smoothed wide
bottom=g1(P[H-10:H].mean(0),6)
jrow=bottom.copy(); zone=(X>=360)&(X<=880)
for c in range(3): jrow[zone,c]=np.interp(X[zone],[359,881],[bottom[359,c],bottom[881,c]])
jac=g1(jrow,40); jstart=g1(jrow,8)        # under the photo the collars continue as jacket straight away
tail=np.zeros((TAIL,W,3)); TA=np.zeros((TAIL,W))
for k in range(TAIL):
    u=k/(TAIL-1); m=min(1,u/0.22)**0.8
    tail[k]=jstart*(1-m)+jac*m
    TA[k]=(1-u)**1.5
canvas=np.concatenate([P,tail],0)
# collar tips: over the photo's last 70px the collar strips blend into the jacket colour, so they taper off instead of being cut
_xl=lambda y:418+(450-418)*(y-1150)/268; _xr=lambda y:850-(850-811)*(y-1150)/268
for y in range(H-70,H):
    r=((y-(H-70))/70)**1.3
    cz=((X>360)&(X<880)&~((X>_xl(y))&(X<_xr(y)))).astype(float)
    cz=g1(cz[:,None],6)[:,0]
    canvas[y]=canvas[y]*(1-(r*cz)[:,None])+jstart*(r*cz)[:,None]
# --- progressive soft focus (jacket, collars): from 88.5 % to 12 px at the photo edge, 17 px in the tail
Y0=int(0.885*H); sig=[0,1,2,3.5,5.5,8,12,17]
Bs=[canvas]+[blur(canvas,s) for s in sig[1:]]
soft=canvas.copy()
for y in range(Y0,HT):
    t=(y-Y0)/(H-Y0)
    s=min(sig[-1],12.0*t**1.6) if t<=1 else min(sig[-1],12+5*(t-1))
    i=int(np.searchsorted(sig,s)); i=min(max(i,1),len(sig)-1); a=(s-sig[i-1])/(sig[i]-sig[i-1])
    soft[y]=Bs[i-1][y]*(1-a)+Bs[i][y]*a
# --- neck: inner collar edges and the arc
xl=lambda y:418+(450-418)*(y-1150)/268
xr=lambda y:850-(850-811)*(y-1150)/268
YE=int(sys.argv[3]) if len(sys.argv)>3 else 1330; YB=1414
xa,xb=xl(YE),xr(YE); xc=(xa+xb)/2; hw=(xb-xa)/2
Y=np.arange(HT)[:,None]; XX=X[None,:].astype(float)
inzone=(XX>xl(Y))&(XX<xr(Y))&(Y>=1150)
yarc=np.where(np.abs(XX-xc)<hw, YE+(YB-YE)*np.sqrt(np.clip(1-((XX-xc)/hw)**2,0,1)), YE)
above=(Y<yarc)|(Y<YE)
keep=(inzone&above).astype(float)          # sharp neck
below=(inzone&~above).astype(float)        # under the arc: card shows
below[H:,:]=np.maximum(below[H:,:],((X>xl(H))&(X<xr(H))).astype(float)[None,:])   # and the tail under the neck
keep=blur1(keep,8); below=blur1(below,10)
rgb=keep[...,None]*canvas+(1-keep[...,None])*soft
alpha=np.concatenate([np.ones((H,W)),TA],0)*(1-below)
im=Image.fromarray(np.dstack([np.clip(rgb,0,255),np.clip(alpha,0,1)[...,None]*255]).astype(np.uint8),'RGBA')
im.save(OUT,'WEBP',quality=86,alpha_quality=100,method=6)
if PREV:
    bg=Image.new('RGBA',im.size,(36,45,70,255)); Image.alpha_composite(bg,im).convert('RGB').crop((250,1050,1000,HT)).save(PREV)
print(im.size)
