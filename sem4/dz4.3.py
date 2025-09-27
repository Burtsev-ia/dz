import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('C:\\Users\Gram\Downloads\iris_data.csv')
#print(df['PetalLengthCm'])
lp=['listed widths: ', list(df['PetalLengthCm'])]

sp=['listed widths: ', list(df['Species'])]
#print(sp)
sp1=sp[1].count('Iris-setosa')
sp2=sp[1].count('Iris-versicolor')
sp3=sp[1].count('Iris-virginica')
lsp=len(sp)
#print(sp1)

plt.subplot(121)
plt.pie([sp1,sp2,sp3],labels=['Iris-setosa','Iris-versicolor','Iris-virginica'])



l1=0
l2=0
l3=0
for i in lp[1]:
    if i<1.2 :
        l1+=1
    elif 1.2<=i<=1.5 :
        l2+=1
    elif i>1.5 :
        l3+=1
#print(l1)
plt.subplot(122)
plt.pie([l1,l2,l3],labels=['<1.2','1.2-1.5','>1.5'])
        
    
plt.show()    
