n = int(input())
a = list()
ai = list(0 for i in range(n))
for i in range(n):
    c = int(input())
    a.append(c)
    if c == 0:
        ai[i] = 1
print(a)
print(ai)
    
    
