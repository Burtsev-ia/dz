fr = set(list(map(int, input().split())))
pl = set(list(map(int, input().split())))
fo = set(list(map(int, input().split())))
print(*sorted(list((fo & pl)-fr)))
