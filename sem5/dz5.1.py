a=input().split('s')
b=[]
for i in a :
    b.append(i[10:])
b=b[1:]
b=list(map(int,b))
l=[]
for i in a :
    if i[10:]==str(max(b)) :
        l.append('s'+i)
print(*l,sep='-')
    
