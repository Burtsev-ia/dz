a=list(input().split())

for i in range(1,int(a[0])+1) :

    if str(i) not in a[1:] :

        print(i)
        break
