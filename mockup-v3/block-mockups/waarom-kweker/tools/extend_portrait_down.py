# Mockup tool (not site code). Paths below point at the session scratchpad; adjust before re-running.
# Downward extension v2: low-frequency layout (jacket / shirt V / skin V) + real texture mirrored from the photo's bottom rows.
from PIL import Image, ImageFilter
import numpy as np, sys
D='/tmp/claude-0/-home-user/c2629853-388a-5a4a-89c1-ca1bace13c36/scratchpad/down/'
P=np.asarray(Image.open('/home/user/TopRododendron-2/mockup-v3/block-mockups/waarom-kweker/img/owner-portrait.webp').convert('RGB')).astype(float)
H,W,_=P.shape
K=int(sys.argv[1]) if len(sys.argv)>1 else 240
def blur(a,s): return np.asarray(Image.fromarray(np.clip(a,0,255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(s))).astype(float)
LF=blur(P,7)
base=LF[H-4]                                  # low-frequency bottom row
# jacket colour: the bottom row smoothed horizontally so lapel lines do not continue downward as streaks
_k=np.exp(-0.5*(np.arange(-60,61)/22.0)**2); _k/=_k.sum()
basej=np.stack([np.convolve(np.pad(base[:,c],60,mode='edge'),_k,mode='valid') for c in range(3)],axis=1)
colL=np.median(P[H-40:H,382:424].reshape(-1,3),axis=0); colR=np.median(P[H-40:H,816:856].reshape(-1,3),axis=0)
X=np.arange(W,dtype=float)
cx=640.0; hw0=212.0; TIP=175
sh0=(374.0,862.0); sh1=(505.0,785.0)
T=np.zeros((K,W,3))
for k in range(K):
    t=k/(K-1); vt=min(1,k/TIP)
    hw=hw0*(1-vt)**0.85
    lc=min(1,t*1.25); l=sh0[0]+(sh1[0]-sh0[0])*lc; r=sh0[1]+(sh1[1]-sh0[1])*lc
    row=basej*(1-0.0)+0
    row=basej.copy() if k>=10 else base*(1-k/10)+basej*(k/10)
    inshirt=(X>=l)&(X<=r)
    u=np.clip((X-l)/max(r-l,1),0,1)[:,None]
    shirt=(colL*(1-u)+colR*u)*(1-0.15*t)
    row[inshirt]=shirt[inshirt]
    if hw>1:
        inv=np.abs(X-cx)<=hw
        src=np.clip(cx+(X[inv]-cx)*(hw0/hw),0,W-1).astype(int)
        shade=1-0.38*vt**1.3
        row[inv]=base[src]*shade
    T[k]=row
T=blur(T,3.0)
# texture: mirror of the photo's bottom rows, high-pass only, fading out before the mirrored chin
M=P[H-1-np.arange(K)]; ML=LF[H-1-np.arange(K)]
hp=M-ML
strength=np.clip(1-np.arange(K)/150,0,1)**1.2
# mirrored texture only inside the collar opening (skin + shirt); the jacket gets plain grain (its seams would mirror into chevrons)
mask=np.zeros((K,W))
for k in range(K):
    t=k/(K-1); lc=min(1,t*1.25)
    l=sh0[0]+(sh1[0]-sh0[0])*lc; r=sh0[1]+(sh1[1]-sh0[1])*lc
    mask[k]=((X>=l+6)&(X<=r-6)).astype(float)
mask=blur(np.repeat(mask[...,None]*255,3,axis=2),5)[...,0]/255
jac=P[1300:1418,40:330]; jstd=float((jac-blur(P,7)[1300:1418,40:330]).mean(axis=2).std())
rng=np.random.default_rng(11)
grain=blur(np.repeat((rng.normal(0,1,(K,W))*40+128)[...,None],3,axis=2),0.7)[...,0]-128
grain=grain/ max(grain.std(),1e-3)*jstd
ext=T+hp*(strength[:,None]*mask)[...,None]+(grain*(1-mask))[...,None]
# seam: the first 8 rows blend from the real bottom rows (mirrored) into the synthetic layout
for k in range(8):
    a=(k+1)/9; ext[k]=P[H-1-k]*(1-a)+ext[k]*a
print('jacket grain std',round(jstd,2))
full=np.concatenate([P,ext],axis=0)
out=full.copy()
for sig,k0 in [(1.2,24),(2.5,70),(4.5,120),(7.0,170)]:
    bl=blur(full,sig)
    for k in range(k0,K):
        a=min(1,(k-k0)/45); out[H+k]=out[H+k]*(1-a)+bl[H+k]*a
res=Image.fromarray(np.clip(out,0,255).astype(np.uint8)); res.save(D+'portrait-down.png')
bg=Image.new('RGB',res.size,(35,44,69))
F0=int(sys.argv[2]) if len(sys.argv)>2 else 30
al=np.ones((res.size[1],res.size[0]))
for y in range(H+F0,H+K):
    t=(y-(H+F0))/(K-F0); al[y]=(1-t)**1.7
prev=Image.composite(res,bg,Image.fromarray((al*255).astype(np.uint8)))
prev.crop((0,900,W,H+K)).resize((600,int((H+K-900)/2))).save(D+'down-prev.png')
print(res.size)
