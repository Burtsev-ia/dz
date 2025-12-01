n = int(input())
a = list(map(int, input().split()))
# a = [0,1,2,3,4,5,6,7,8,9,10,11,12]
# n = len(a)


def build_tree(a):
    tree = {}
    for i in range(n):
        tree[n + i] = a[i]
    for i in range(n - 1, 0, -1):
        tree[i] = max(tree[2 * i], tree[2 * i + 1])
    return tree
# print(build_tree(a))


def tree_max(tree, le, r):
    _max = -9**999
    le += n
    r += n
    while le < r:
        if (le & 1 > 0):
            _max = max(_max, tree[le])
            le += 1
        if (r & 1) > 0:
            r -= 1
            _max = max(_max, tree[r])
        le //= 2
        r //= 2
    return _max


k = int(input())
g = list()
for i in range(k):
    le, r = list(map(int, input().split()))
    le -= 1
    g.append(tree_max(build_tree(a), le, r))
print(*g)
