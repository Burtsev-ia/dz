'''крч не сказано как конкретно вводятся выражения эти.
пусть пробелы везде натыканы штоб я сплитанул и не парился'''

def calc(a) :
    if len(a) == 1 :
        return int(a[0])
    elif len(a) == 2 :
        return 'error'
    co=0
    for t in ['/', '*', '+', '-'] :
        if t in a :
            co+=1
    if co == 0 :
        return 'error'
    for i in range(len(a)) :
    
        if a[i] in ['/', '*', '+', '-'] :
            if i <= 1 :
                return 'error'
            cr=a[i-1]
            cl=a[i-2]
            ifix=i-2
            if cr in ['/', '*', '+', '-'] or cl in ['/', '*', '+', '-'] :
                return 'error'
            break
    a.insert(ifix, str(eval(cl+a[ifix+2]+cr)))
    a.pop(ifix+1)
    a.pop(ifix+1)
    a.pop(ifix+1)
    return calc(a)

m=input().split()
print(calc(m))

                
                
                            
                
                
                
                    
                
    
