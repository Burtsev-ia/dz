size,symb = input().split()
size=int(size)
for i in range(int(size/2)) :
    print((i+1)*symb)
if size%2!=0 :
    print(symb*(size//2+1))
for i in range(int(size/2),0,-1) :
    print(i*symb)
