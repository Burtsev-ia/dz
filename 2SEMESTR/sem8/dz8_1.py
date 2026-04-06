import collections


class Dinic:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]
        self.level = []

    def add_edge(self, u, v, capacity):
        self.graph[u].append([v, capacity, len(self.graph[v])])
        self.graph[v].append([u, 0, len(self.graph[u]) - 1])

    def bfs(self, s, t):
        """Построение слоистой сети."""
        self.level = [-1] * self.n
        self.level[s] = 0
        queue = collections.deque([s])
        while queue:
            u = queue.popleft()
            for v, cap, rev_idx in self.graph[u]:
                if cap > 0 and self.level[v] == -1:
                    self.level[v] = self.level[u] + 1
                    queue.append(v)
        return self.level[t] != -1

    def dfs(self, u, t, flow, ptr):
        """Поиск блокирующего потока в слоистой сети."""
        if u == t or flow == 0:
            return flow
        
        for i in range(ptr[u], len(self.graph[u])):
            ptr[u] = i
            v, cap, rev_idx = self.graph[u][i]
            if self.level[v] == self.level[u] + 1 and cap > 0:
                pushed = self.dfs(v, t, min(flow, cap), ptr)
                if pushed > 0:
                    self.graph[u][i][1] -= pushed
                    self.graph[v][rev_idx][1] += pushed
                    return pushed
        return 0

    def max_flow(self, s, t):
        max_f = 0
        while self.bfs(s, t):
            ptr = [0] * self.n
            while True:
                pushed = self.dfs(s, t, float('inf'), ptr)
                if pushed == 0:
                    break
                max_f += pushed
        return max_f

if __name__ == '__main__':
    i = int(input())
    while i != 0:
        graph_ivanich = Dinic(i)
        s, t, c = list(map(int, input().split()))
        for _ in range(c):
            u, v, w = list(map(int, input().split()))
            u -= 1
            v -= 1
            # print(u, v, w)
            graph_ivanich.add_edge(u, v, w)
        print('Network: лень вводить номера сетей, уже все написал итак')
        print(f'the bandwith is {graph_ivanich.max_flow(s-1, t-1)}')
        i = int(input())
