def rec(x) :
    a=list()
    #print(';;')
    if x==1 :
        #print('--')
        return 1
    else :
        for i in range(2,int((x)**0.5)+1) :
            if x%i==0 :
                a.append(i)
                print(i)
                return(rec(x/i))
        if len(a)==0 :
            return(int(x))



b=int(input())
print(rec(b))
