def perevod(a,x) :
    m=''
    while a>0 :
        m+=str(a%x)
        a//=x
    return int(m[::-1])


def obr_perevod(a,x) :
    return(int(str(a),x))

n,b,c= list(map(int,input().split()))
print(perevod(obr_perevod(n,b),c))
