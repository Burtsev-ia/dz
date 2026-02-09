import numpy as np
n,m=list(map(int,input().split()))
a=np.zeros((n,m))
b=np.array([])
a1=np.zeros((n,m-1))
for i in range(n) :
    a[i]+=np.array(list(map(int,input().split())))
    b=np.append(b,a[i][-1])
    a1[i]+=a[i][:-1]
    
    
'''print(a)
print(a1)
print(b)'''

ans=np.linalg.solve(a1,b)
print(ans)
