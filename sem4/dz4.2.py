import matplotlib.pyplot as plt
import random
import numpy as np
pos=0
scale=100
size1=1000
size2=10000
size3=100000
val1=np.random.normal(pos,scale,size1)
val2=np.random.normal(pos,scale,size2)
val3=np.random.normal(pos,scale,size3)


plt.subplot(311)
plt.axis([-400,400,0,10])
plt.hist(val1,1000)

plt.subplot(312)
plt.axis([-400,400,0,50])
plt.hist(val2,1000)


plt.subplot(313)
plt.axis([-400,400,0,500])
plt.hist(val3,1000)


plt.show()

