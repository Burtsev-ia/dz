import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('C:\\Users\Gram\Downloads\iris_data.csv')
#print(df['PetalLengthCm'])


sl=['listed widths: ', list(df['SepalLengthCm'])][1]
sw=['listed widths: ', list(df['SepalWidthCm'])][1]
pl=['listed widths: ', list(df['PetalLengthCm'])][1]
pw=['listed widths: ', list(df['PetalWidthCm'])][1]

fig = plt.figure()
fig.subplots_adjust(hspace=0.3, wspace=0.3)

plt.subplot(231)
plt.plot(sl,sw,'.')
plt.legend('sl-sw')


plt.subplot(232)
plt.plot(sl,pl,'.')
plt.legend('sl-pl')


plt.subplot(233)
plt.plot(sl,pw,'.')
plt.legend('sl-pw')



plt.subplot(234)
plt.plot(pl,sw,'.')
plt.legend('pl-sw')



plt.subplot(235)
plt.plot(pw,sw,'.')
plt.legend('pw-sw')


plt.subplot(236)
plt.plot(pl,pw,'.')
plt.legend('pl-pw')



plt.show()
