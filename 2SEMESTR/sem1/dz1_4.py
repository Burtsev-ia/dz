n = int(input())
a = dict()
li = list()
co = 0
while 1:
    inp = list(map(int, input().split()))
    if inp == list():
        break
    # a[co] = inp
    li.append(inp)
    co += 1
# print(l)
# print(a.keys())
for i in li:
    if i[0] in list(a.keys()):
        pre = a[i[0]]
        pre.append(i[1])
        a[i[0]] = pre
    else:
        o = list()
        o.append(i[1])
        a[i[0]] = o
    if i[1] in list(a.keys()):
        pre = a[i[1]]
        pre.append(i[0])
        a[i[1]] = pre
    else:
        o = list()
        o.append(i[0])
        a[i[1]] = o

for i in range(n):
    if i in list(a.keys()):
        pass
    else:
        a[i] = []
print(a)
color = ['white' for i in a.keys()]
labuda = 0


def dfs_visit(graph, v):
    color[v] = 'gray'
    # print(v)
    lele.append(v)

    for u in graph[v]:
        # print(color[u])
        if color[u] == 'black':
            # print('govnostoi slaboser')
            global labuda
            labuda += 1
        if color[u] == 'white':
            dfs_visit(graph, u)

    color[v] = 'black'
    # print(v)


lele = []
dfs_visit(a, 0)
print(labuda)
print(labuda != 0)
