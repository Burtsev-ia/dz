def rec(x) :
    if x==1 or x==2:
        return 1
    else :
        return(rec(x-1)+rec(x-2))


a=int(input())
print(rec(a))
