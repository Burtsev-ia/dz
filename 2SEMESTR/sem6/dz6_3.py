import heapq
import time

class DSU:
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

def kruskal_mst(V, edges):
    start = time.perf_counter()
    dsu = DSU(V)
    sorted_edges = sorted(edges, key=lambda e: e[0])
    total = 0
    for w, u, v in sorted_edges:
        if dsu.union(u, v):
            total += w
    res = time.perf_counter() - start
    return total, res

def prim_mst(V, edges):
    start = time.perf_counter()
    adj = [[] for _ in range(V)]
    for w, u, v in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    in_mst = [False] * V
    pq = []
    in_mst[0] = True
    for to, w in adj[0]:
        heapq.heappush(pq, (w, 0, to))
    
    total = 0
    count = 0
    while pq and count < V - 1:
        w, u, v = heapq.heappop(pq)
        if in_mst[v]:
            continue
        in_mst[v] = True
        total += w
        count += 1
        for to, w2 in adj[v]:
            if not in_mst[to]:
                heapq.heappush(pq, (w2, v, to))
    res = time.perf_counter() - start
    return total, res

# Чтение файла и запуск
def run_tests(filename):
    f = open(filename)
    content = f.read().strip().split('\n\n')
    # print(content)
    print("=" * 80)
    print('тест  ребра  краскал(сек)    прим(сек)')
    print("=" * 80)
    
    for i, block in enumerate(content, 1):
        lines = block.strip().split('\n')
        # print(lines)
        V = int(lines[0])
        print(V)
        edges = [tuple(map(int, line.split())) for line in lines[1:]]
        kruskal_res, kruskal_time = kruskal_mst(V, edges)
        prim_res, prim_time = prim_mst(V, edges)
        print(f"{i:<6} {V:<6} {kruskal_time:<15.6f} {prim_time:<15.6f}")

if __name__ == "__main__":
    run_tests("tests.txt")
