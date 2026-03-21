import networkx as nx

f = open(input())
fout = open('output.txt', 'w')
n, m = list(map(int, f.readline().split()))
a = f.readlines()
b = []
for i in a:
    b.append(tuple(map(int, i.split())))
g = nx.Graph()
for i in b:
    g.add_nodes_from(i)
g.add_edges_from(b)
ans = nx.is_bipartite(g)
fout.write(str(ans))

f.close()
fout.close()
