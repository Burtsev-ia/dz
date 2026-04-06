import networkx as nx

f = open(input())
n, m = list(map(int, f.readline().split()))
a = f.readlines()
b = []
for i in a:
    b.append(tuple(map(int, i.split())))
g = nx.Graph()
for i in b:
    g.add_nodes_from(i)
g.add_edges_from(b)

print(g.nodes, len(g.nodes))
print(g.edges, len(g.edges))
print(max(list(nx.connected_components(g))))
