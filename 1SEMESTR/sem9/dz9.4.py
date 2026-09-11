n = int(input())
a = []
b = []
for _ in range(n):
    k = list(map(int, input().split()))
    a.append(sorted(k))
    b.append(sorted(k, reverse=True))
a = sorted(a, reverse=True)
b = sorted(b)
print(str(a[0][0]) + '-' + str(b[0][0]))
