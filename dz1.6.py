def perevod(a, x):
    m = ''
    while a > 0:
        m += str(a % x)
        a //= x
    return int(m[::-1])


def obr_perevod(a, x):
    return (int(str(a), x))


f = open('input.txt')
f2 = open('output.txt', 'w')
a1 = f.readline()[:-1]
a2 = f.readline()[:-1]
a3 = f.readline()
#print(a1,a2,a3)
anew = list()
for i in a1.split():
    anew.append(str(obr_perevod(i, int(a3))))
#print(anew)
#print(str(a2).join(anew))
a1 = eval(str(a2).join(anew))
#print(a1)
f2.write(str(perevod(a1, int(a3))))
#print(str(perevod(a1,int(a3))))


f.close()
f2.close()
