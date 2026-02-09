# ['ANT', 'OSTRICH', 'DEER', 'TURKEY', 'KANGAROO',/
# 'TIGER', 'RABBIT', 'RAT', 'TOAD', 'YAK', 'HYENA']
a = eval(input())
nachalo = []
konez = []
for i in a:
    nachalo.append(i[0])
    konez.append(i[-1])

nachalo.sort()
konez.sort()
print(nachalo == konez)
