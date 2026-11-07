# Mockup tool (not site code). Paths below point at the session scratchpad; adjust before re-running.
# Broader right shoulder: continue the original shoulder slope (~0.35 -> 0.5) instead of dropping into the arm early.
from PIL import Image, ImageFilter
import numpy as np, sys
D='/tmp/claude-0/-home-user/c2629853-388a-5a4a-89c1-ca1bace13c36/scratchpad/'
S_END=float(sys.argv[1]) if len(sys.argv)>1 else 0.5   # slope reached 250px past x=1150
P=np.asarray(Image.open(D+'extend/portrait-ext.png').convert('RGB')).astype(float)
H,W,_=P.shape; L=P.mean(axis=2)
def edge(x,start=1000):
    col=L[:,x]
    for y in range(start,H):
        if col[y]<100:
            y0=y-1; return y0+(col[y0]-100)/max(col[y0]-col[y],1e-3)
    return np.nan
X0=925
o=np.full(W,np.nan)
for x in range(X0,1200): o[x]=edge(x)
def movavg(a,k):
    out=a.copy()
    for i in range(len(a)):
        w=a[max(0,i-k):i+k+1]; w=w[~np.isnan(w)]
        if len(w): out[i]=w.mean()
    return out
os_=movavg(o,3)
XS=1150
s0=np.polyfit(np.arange(XS-40,XS+1),os_[XS-40:XS+1],1)[0]; y0=os_[XS]
k=(S_END-s0)/250**2
E=os_.copy()
for x in range(XS,W):
    u=x-XS; E[x]=y0+s0*u+k*u**3/3
print('s0',round(s0,3),'E(1200)',round(E[1200],1),'E(1315)',round(E[1315],1),'E(1450)',round(E[1450],1),'E(1579)',round(E[1579],1))
# crossing of card bottom (93.5%)
yb=0.935*H; xb=next((x for x in range(1200,W) if E[x]>yb),None); print('leaves 93.5% line at x',xb)
# jacket profile below the edge, from the last original columns
XA=range(1150,1196)
prof=np.zeros((400,3))
for d in range(400):
    rows=[P[min(H-1,int(round(E[x]+d))),x] for x in XA]
    prof[d]=np.mean(rows,axis=0)
deep=np.array([16.5,20.0,33.0])
for d in range(60,400): prof[d]=deep+(prof[min(d,59)]-deep)*np.exp(-(d-59)/8)
lastcol=lambda d,x: P[min(H-1,int(round(E[x]+d))),x]
rng=np.random.default_rng(7)
noise=rng.normal(0,1.5,(H,W)); noise=np.asarray(Image.fromarray(((noise+8)*16).clip(0,255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.8))).astype(float)/16-8
G=np.clip((0.84*W-np.arange(W))/((0.84-0.592)*W),0,1)
out=P.copy(); alpha=np.tile(G,(H,1)).astype(float)
RAMP=5.0
for x in range(X0,W):
    ex=E[x]
    if np.isnan(ex): continue
    top=int(max(0,ex-16))
    for y in range(top,H):
        d=y-ex
        if x<1196:
            ox=o[x] if not np.isnan(o[x]) else ex
            B=P[int(min(y,ox-8)),x]; J=P[int(min(H-1,max(y,ox+6))),x]
            a=np.clip((B.mean()-L[y,x])/max(B.mean()-J.mean(),1),0,1) if y<ox+6 else 1.0
            if y<ox-8: a=0.0
        else:
            dd=int(min(399,max(0,round(d))))
            t=min(1,(x-1196)/60)
            seam=np.mean([lastcol(dd,xx) for xx in range(1192,1196)],axis=0)
            J=(1-t)*seam+t*prof[dd]+noise[y,x]
            B=P[int(max(0,min(y,ex-8))),x]
            a=np.clip(d/RAMP+0.5,0,1)
        g=G[x]; ao=a+g*(1-a)
        if ao<=1e-4: alpha[y,x]=0; continue
        out[y,x]=(a*J+g*(1-a)*B)/ao; alpha[y,x]=ao
rgba=np.dstack([np.clip(out,0,255),np.clip(alpha*255,0,255)]).astype(np.uint8)
im=Image.fromarray(rgba,'RGBA'); im.save(D+'fix6/portrait-ext-alpha2.png')
bg=Image.new('RGBA',im.size,(197,202,178,255)); comp=Image.alpha_composite(bg,im).convert('RGB')
comp.crop((0,0,W,int(0.935*H))).resize((632,530),Image.LANCZOS).save(D+'fix6/wide-small.png')
comp.crop((1000,1050,1580,1330)).resize((870,420),Image.LANCZOS).save(D+'fix6/wide-junction.png')
np.save(D+'fix6/E2.npy',E)
