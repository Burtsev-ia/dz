a = input()
stek = ['n']
ans = ['n']
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

print(*ans[1:])

'''работает для переменных или цифр (крч одиночные символы)
















else :
        if stek[-1] == '+' :
            if i == '*' or i == '/' :
                stek.append(i) 
            if i == '-' or i == '+' :
                ans.append('+')
                stek.pop(-1)
                #a.insert(a[i]+1,i)
                while stek[-1] in ['*','+','/'] :
                    ans.append(stek[-1])
                    stek.pop(-1)
                stek.append(i)


        elif stek[-1] == '-' :
            stek.append(i)

        elif stek[-1] == '*' :
            ans.append('*')
            stek.pop(-1)
            #a.insert(a[i]+1,i)
            while stek[-1] in ['*'] :
                ans.append(stek[-1])
                stek.pop(-1)
            stek.append(i)


        elif stek[-1] == '/' :
            if i == '+' or i == '-' or i == '/' :
                ans.append('/')
                stek.pop(-1)
                #a.insert(a[i]+1,i)
                while stek[-1] in ['*'] :
                    ans.append(stek[-1])
                    stek.pop(-1)
                stek.append(i)
            else :
                stek.append('*')

        else :
            stek.append(i)'''
