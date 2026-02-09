import numpy as np
from random import gauss
a=list()
n=int(input())
for i in range(n*2):
    a.append(gauss(0,50))
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
