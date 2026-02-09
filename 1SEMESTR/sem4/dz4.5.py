import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('C:\\Users\Gram\Downloads\BTC_data.csv')
#print(df['PetalLengthCm'])


t=['listed widths: ', list(df['time'])][1]
pr=['listed widths: ', list(df['close'])][1]

for i in range(len(pr)) :
    #print(t[i])
    t[i]=t[i][:t[i].rfind('T')]
#print(pr)

plt.figure(figsize=(16,9))
#plt.xticks(['2018-01-01','2019-01-01','2020-01-01','2021-01-01','2022-01-01'])
#plt.grid()
plt.plot(t,pr)
plt.show()
