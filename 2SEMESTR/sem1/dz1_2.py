n = int(input())
a = dict()
li = list()
co = 0
st = input()
start, end = list(map(int, input().split()))
para = []
for i in st:
    if len(para) == 2:
        li.append(para)
        para = []
    if i.isdigit():
        para.append(int(i))
print(li)
for i in li:
    if i[0] in list(a.keys()):
        pre = a[i[0]]
        pre.append(i[1])
        a[i[0]] = pre
    else:
        o = list()
        o.append(i[1])
        a[i[0]] = o

for i in range(n):
    if i in list(a.keys()):
        pass
    else:
        a[i] = []
print(a)
color = ['white' for i in a.keys()]


def dfs_visit(graph, v):
    color[v] = 'gray'
    # print(v)
    lele.append(v)

    for u in graph[v]:
        if color[u] == 'white':
            dfs_visit(graph, u)

    color[v] = 'black'
    # print(v)


lele = []
dfs_visit(a, start)
print(end in lele)
