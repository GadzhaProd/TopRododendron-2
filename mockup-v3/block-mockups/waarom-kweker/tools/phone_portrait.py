# Mockup tool (not site code): builds img/owner-portrait-m.webp. Usage: python3 phone_portrait.py <out.webp> [preview.png] [arc_end_y=1320] [arc_bottom_y=1402]
# Phone portrait v5 (like the shoulder keep-zone): the fade reaches everything except the neck + collars.
# Keep-zone = the collar opening between the lapel edges (collar meets jacket), closed at the bottom by an arc
# from lapel to lapel along the bottom of the neck. Outside it the photo fades out (from 89 %, smoothstep) over a broad
# gradient in the jacket's own tones, which then fades into the card. No blur, so nothing is half sharp.
from PIL import Image, ImageFilter
import numpy as np, sys
OUT=sys.argv[1]; PREV=sys.argv[2] if len(sys.argv)>2 else None
YE=int(sys.argv[3]) if len(sys.argv)>3 else 1320; YB=int(sys.argv[4]) if len(sys.argv)>4 else 1402
P=np.asarray(Image.open('/home/user/TopRododendron-2/mockup-v3/block-mockups/waarom-kweker/img/owner-portrait.webp').convert('RGB')).astype(float)
H,W,_=P.shape; TAIL=210; HT=H+TAIL
def g1(a,s):
    k=np.exp(-0.5*(np.arange(-3*s,3*s+1)/s)**2); k/=k.sum()
    return np.stack([np.convolve(np.pad(a[:,c],3*s,mode='edge'),k,mode='valid') for c in range(a.shape[1])],1)
def blur1(m,s): return np.asarray(Image.fromarray(np.clip(m*255,0,255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(s))).astype(float)/255
X=np.arange(W)
row=P[H-14:H].mean(0)
jrow=row.copy(); zone=(X>=350)&(X<=890)
for c in range(3): jrow[zone,c]=np.interp(X[zone],[349,891],[row[349,c],row[891,c]])
base=g1(jrow,160)
# lapel edges (collar meets jacket), read off the photo
xlo=lambda y: 375.0+0*y
xro=lambda y: 950-(950-865)*(y-1130)/(1418-1130)
xa,xb=xlo(YE),xro(YE); xc=(xa+xb)/2; hw=(xb-xa)/2
Y=np.arange(H)[:,None].astype(float); XX=X[None,:].astype(float)
inside=(XX>xlo(Y))&(XX<xro(Y))&(Y>1050)
yarc=YE+(YB-YE)*np.sqrt(np.clip(1-((XX-xc)/hw)**2,0,1))
keep=(inside&((Y<YE)|(Y<yarc))).astype(float)
keep=blur1(keep,14)                                  # soft edge along the lapels and the arc
# photo alpha: eased fade from F0 for everything, the keep-zone stays opaque
F0=0.89; y0=int(F0*H)
t=np.clip((np.arange(H)-y0)/(H-1-y0),0,1); PA=(1-(3*t*t-2*t**3))[:,None]
A=np.maximum(PA,keep)
# under the arc the neck still has to end softly: fade the keep-zone itself over the last rows below the arc
rgb=np.zeros((HT,W,3)); alpha=np.ones((HT,W))
rgb[:H]=P*A[...,None]+base[None]*(1-A)[...,None]
for k in range(TAIL):
    u=k/(TAIL-1); rgb[H+k]=base; alpha[H+k]=(1-u)**1.6
im=Image.fromarray(np.dstack([np.clip(rgb,0,255),alpha[...,None]*255]).astype(np.uint8),'RGBA')
im.save(OUT,'WEBP',quality=88,alpha_quality=100,method=6)
if PREV:
    bg=Image.new('RGBA',im.size,(35,44,69,255)); comp=Image.alpha_composite(bg,im).convert('RGB')
    comp.crop((0,1000,W,HT)).resize((600,(HT-1000)//2)).save(PREV)
    # outline preview
    from PIL import ImageDraw
    c2=comp.crop((250,1050,1000,HT)).copy(); d=ImageDraw.Draw(c2)
    c2.save(PREV.replace('.png','-zoom.png'))
print(im.size,'arc',round(xa),round(xb),YE,YB)
