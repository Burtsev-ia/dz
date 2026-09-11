import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('C:\\Users\Gram\Downloads\BTC_data.csv')
#print(df['PetalLengthCm'])


t=['listed widths: ', list(df['time'])][1]
pr=['listed widths: ', list(df['close'])][1]
t1=np.arange(0,len(t))
#t1=list(t1)
t2=[]
for i in t1:
    t2.append(int(i))

for i in range(len(pr)) :
    #print(t[i])
    t[i]=t[i][:t[i].rfind('T')]
#print(pr)

m=np.polyfit(t2,pr,20)
#print(len(t),len(m))

p = np.poly1d(m)
plt.figure(figsize=(16,9))
#plt.xticks(['2018-01-01','2019-01-01','2020-01-01','2021-01-01','2022-01-01'])
#plt.grid()
plt.plot(t,pr)
plt.plot(t,[ p(i) for i in range(len(t))])
plt.show()
