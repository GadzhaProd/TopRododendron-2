# Mockup tool (not site code): builds img/owner-portrait-m.webp. Usage: python3 phone_portrait.py <out.webp>
# Phone portrait v2: build photo + colour tail first, then one progressive blur across the seam; alpha fade on the tail.
from PIL import Image, ImageFilter
import numpy as np, sys
OUT=sys.argv[1]
P=np.asarray(Image.open('/home/user/TopRododendron-2/mockup-v3/block-mockups/waarom-kweker/img/owner-portrait.webp').convert('RGB')).astype(float)
H,W,_=P.shape
TAIL=247
def blur(a,s): return np.asarray(Image.fromarray(np.clip(a,0,255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(s))).astype(float)
def g1(a,s):
    k=np.exp(-0.5*(np.arange(-3*s,3*s+1)/s)**2); k/=k.sum()
    return np.stack([np.convolve(np.pad(a[:,c],3*s,mode='edge'),k,mode='valid') for c in range(a.shape[1])],1)
X=np.arange(W)
bottom=g1(P[H-10:H].mean(0),6)
# jacket target: the collar strips replaced by the jacket on either side, then smoothed wide, so no light-blue bands run down
jrow=bottom.copy(); zone=(X>=360)&(X<=880)
for c in range(3): jrow[zone,c]=np.interp(X[zone],[359,881],[bottom[359,c],bottom[881,c]])
jac=g1(jrow,40); neck=g1(bottom,10); navy=np.array([42,52,80.])
w=np.zeros(W); w[(X>=440)&(X<=820)]=1; w=g1(w[:,None],20)[:,0]
target=jac*(1-w[:,None])+(neck*0.55+navy*0.45)*w[:,None]
tail=np.zeros((TAIL,W,3)); A=np.zeros((TAIL,W))
for k in range(TAIL):
    u=k/(TAIL-1); m=min(1,u/0.22)**0.8
    tail[k]=bottom*(1-m)+target*m
    A[k]=(1-u)**1.5*(1-w)+(1-min(1,u/0.45))**1.5*w
# calm the lit chest in the photo's last 5 % (neck zone only) so it does not read as a light bar above the tail
P=P.copy(); yb=int(0.95*H)
for y in range(yb,H):
    r=((y-yb)/(H-1-yb))**1.2*0.55
    P[y]=P[y]*(1-r*w[:,None])+target[None][0]*(r*w[:,None])
bottom2=g1(P[H-10:H].mean(0),6)
for k in range(TAIL):
    u=k/(TAIL-1); m=min(1,u/0.22)**0.8
    tail[k]=bottom2*(1-m)+target*m
canvas=np.concatenate([P,tail],0); HT=H+TAIL
Y0=int(0.885*H)
sig=[0,1,2,3.5,5.5,8,12,17]
Bs=[canvas]+[blur(canvas,s) for s in sig[1:]]
out=canvas.copy()
for y in range(Y0,HT):
    t=(y-Y0)/(H-Y0)                          # 0 at Y0, 1 at the photo's bottom edge, >1 in the tail
    s=min(sig[-1],12.0*t**1.6) if t<=1 else min(sig[-1],12+5*(t-1))
    i=int(np.searchsorted(sig,s)); i=min(max(i,1),len(sig)-1)
    a=(s-sig[i-1])/(sig[i]-sig[i-1])
    out[y]=Bs[i-1][y]*(1-a)+Bs[i][y]*a
alpha=np.concatenate([np.ones((H,W)),A],0)
im=Image.fromarray(np.dstack([np.clip(out,0,255),alpha[...,None]*255]).astype(np.uint8),'RGBA')
im.save(OUT,'WEBP',quality=86,alpha_quality=100,method=6)
bg=Image.new('RGBA',im.size,(36,45,70,255)); Image.alpha_composite(bg,im).convert('RGB').crop((250,1050,950,HT)).save('/tmp/claude-0/-home-user/c2629853-388a-5a4a-89c1-ca1bace13c36/scratchpad/mob/prev.png')
print(im.size)
