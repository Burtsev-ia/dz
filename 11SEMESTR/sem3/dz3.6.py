import numpy as np
a=list(map(int,input('input in format:x1 y1 x2 y2 ... xn yn  :').split()))
#print(a)
xm=np.array([])
ym=np.array([])
for i in range(len(a)) :
    if i%2==0 :
        xm=np.append(xm,a[i])
    else :
        ym=np.append(ym,a[i])
#print(xm,ym)
srx=np.mean(xm)
sry=np.mean(ym)
srxy=np.mean(xm*ym)
srx2=np.mean(xm*xm)
#print(srx,sry,srxy,srx2)
k=(srxy-srx*sry)/(srx2-srx**2)
b=sry-k*srx
print(k,b)
