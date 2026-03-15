import math


class DSU:
    """Система непересекающихся множеств (Union-Find)"""
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_root, y_root = self.find(x), self.find(y)
        if x_root == y_root:
            return False
        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        elif self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[y_root] = x_root
            self.rank[x_root] += 1
        return True


def kruskal_mst(vertices_count, edges):
    sorted_edges = sorted(edges, key=lambda edge: edge[0])

    dsu = DSU(vertices_count)
    mst_edges = []
    total_weight = 0

    for weight, u, v in sorted_edges:
        if dsu.union(u, v):
            mst_edges.append((u, v, weight))
            total_weight += weight

    return total_weight, mst_edges


def weights(e):
    edges = []
    n = len(e)
    for i in range(n):
        for j in range(i + 1, n):
            weight = math.hypot(e[i][0] - e[j][0],
                                e[i][1] - e[j][1])
            edges.append((weight, i + 1, j + 1))
    return edges


if __name__ == "__main__":
    n = int(input('edges count'))
    V = n * (n - 1)
    graph_edges = []
    for _ in range(n):
        i = list(map(int, input().split()))
        graph_edges.append(i)
    graph_edges = weights(graph_edges)
    total_cost, mst = kruskal_mst(V, graph_edges)
    print(f"Алгоритм Краскала: Вес MST = {total_cost}")
    print("Рёбра в MST:")
    for u, v, w in mst:
        print(f"{chr(65 + u)} -- {chr(65 + v)} : {w}")
