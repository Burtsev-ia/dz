a,b=input().split()
c=''
for i in range(0,len(b),int(a)) :
    c+=b[i:i+int(a)][::-1]
print(c)
