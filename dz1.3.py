def srednegeom(a):
    ans = 1
    for i in a:
        ans *= i
    return (ans ** (1 / (len(a))))


a = list(map(int, input().split()))
print(srednegeom(a))
