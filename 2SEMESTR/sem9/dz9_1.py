a = input()
a += 's'
maxlist = list()
maxb = -1
while 1:
    p = a.find('_')
    if p == -1:
        break
    num = a[p+1:p+4]
    a = a[p+1:]
    # print(a)
    bal = int(a[3:a.find('s')])
    # print(num, bal)
    if bal > maxb:
        maxb = bal
        maxlist = list()
        maxlist.append(num)
    elif bal == maxb:
        maxlist.append(num)
# print(maxb)
print('-'.join(maxlist))
