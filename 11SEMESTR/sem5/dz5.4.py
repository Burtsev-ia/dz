a=input()
if len(a)>=4 :
    co=0
    for i in range(4) :
        if a[i].isupper() :
            co+=1
    if co>=3 :
        print(a.upper())
    else :
        print(a)
else :
    co=0
    for i in range(len(a)) :
        if a[i].islower() :
            co+=1
    if co==len(a) :
        print(a.upper())
    else :
        print(a)
        
        
