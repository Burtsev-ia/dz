'''пусть через пробел все вводится чето слишком тяжело разделять'''

def pol(a) :
    '''вот этой херней я хочу разделить выражение по скобкам,
        и в каждой скобке применить функцию которую я написал в номере 3
        че за пот емае????? '''
    a = a.split()
    anew = []
    kolskobok = a.count('(')
    for i in range(kolskobok) :
        #print(a)
        k=''
        for h in a :
            k+=h
            
        kon = a.index(')')
        nac = k.rfind('(')
        #print(nac)
        #print()
        #print(nac)
        promsp = a[kon+1:nac]
        anew.append(calc(promsp))
        #print(anew)
        print(promsp)
        #print(a[:nac] + ['x'] + a[kon+1:])
        
        a = a[:nac] + ['x'] + a[kon+1:]
        #print(calc(promsp))
    return anew
        




def calc(a) :
    ans = ['n']
    stek = ['n']
    numb = ['+', '-', '/', '*']
    for i in a:
        j = 0
        if i not in numb:
            ans.append(i)

        else:
            if i == '+':
                while stek[-1] in ['*', '/', '+']:
                    ans.append(stek[-1])
                    stek.pop(-1)
                stek.append(i)

            elif i == '-':
                while stek[-1] in ['*', '/', '+', '-']:
                    ans.append(stek[-1])
                stek.pop(-1)
                stek.append(i)
    
            elif i == '*':
                while stek[-1] in ['*']:
                    ans.append(stek[-1])
                    stek.pop(-1)
                stek.append(i)
    
            elif i == '/':
                while stek[-1] in ['*', '/']:
                    ans.append(stek[-1])
                    stek.pop(-1)
                stek.append(i)

    for j in range(len(stek) - 1):
        ans.append(stek[-1 * (1 + j)])
    return ans[1:]

s=input()
print(pol(s))
