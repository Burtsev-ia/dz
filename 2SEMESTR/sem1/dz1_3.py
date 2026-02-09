a = eval(input())
for i in list(a.values()):
    if i in a.keys():
        if type(i) != list:
            a[i] = [a[i]]
        pass
    else:
        a[i] = []
        end = i
for i in list(a.keys()):
    if type(a[i]) == str:
        start = i
        a[i] = [a[i]]
print(a)
# print(start,end)

color = dict()
for i in a.keys():
    color[i] = 'white'


# okurok = 0
def dfs_visit(graph, v):
    color[v] = 'gray'
    # print(v)
    global lele
    lele.append(v)

    for u in graph[v]:
        # print(v)
        # print(u)
        if color[u] == 'white':
            dfs_visit(graph, u)
        if color[u] == 'gray':
            lele = []
            return 0

    color[v] = 'black'
    # print(v)


lele = []
'''for m in a.keys():
    color = dict()
    for i in a.keys():
        color[i] = 'white'
    dfs_visit(a, m)'''
dfs_visit(a, start)
# print(list(a.keys())[0])
# dfs_visit(a, a[list(a.keys())[0]])
print(lele)
