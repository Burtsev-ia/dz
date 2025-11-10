def poisk(a, m):
    try:
        return a.index(m)
    except ValueError:
        return -1


a_counters = []
a = list()
n = int(input())
for _ in range(n):
    m = input()
    j = poisk(a, m)
    if j != -1:
        a_counters[j] += 1
    else:
        a.append(m)
        a_counters.append(1)
# print(*list(zip(a, a_counters)))
for i in range(len(a)):
    print(a[i] + ' ' + str(a_counters[i]))

