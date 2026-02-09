a = list(map(int, input().split()))
co = 0
for i in range(len(a)):
    if i*2+2 <= len(a)-1:
        if a[i] >= a[2*i+1] or a[i] >= a[2*i+2]:
            co += 1
    elif i*2+1 <= len(a)-1:
        if a[i] >= a[2*i+1]:
            co += 1
    else:
        pass
if co == 0:
    print(1)
else:
    print(0)
