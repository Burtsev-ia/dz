class DSU:
    """Система непересекающихся множеств (Union-Find)"""
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        # Сжатие путей
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # Объединение по рангу
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
    """
    edges: список кортежей (weight, u, v)
    Возвращает: (общий_вес, список_рёбер_mst)
    """
    # Сортируем рёбра по весу
    sorted_edges = sorted(edges, key=lambda edge: edge[0])
    
    dsu = DSU(vertices_count)
    mst_edges = []
    total_weight = 0
    
    for weight, u, v in sorted_edges:
        # Если вершины в разных компонентах, добавляем ребро
        if dsu.union(u, v):
            mst_edges.append((u, v, weight))
            total_weight += weight
            
    return total_weight, mst_edges


def stroki_spisok(edges1):
    edges = []
    for u, v, w in edges1:
        edges.append([u, v])
    adj = {}
    for u, v in edges: 
        if u not in adj:
            adj[u] = []
        adj[u].append(v)
        if v not in adj:
            adj[v] = []
        adj[v].append(u)
    
    return adj


def zikl(graph, start, end):
    # Словарь расстояний от стартовой вершины
    # -1 означает, что вершина еще не посещена
    dist = {v: -1 for v in graph}

    # Словарь для хранения предка каждой вершины (откуда мы пришли)
    parent = {v: None for v in graph}

    # Расстояние до стартовой вершины = 0
    dist[start] = 0

    # Инициализируем очередь стартовой вершиной
    queue = [start]

    visited_order = []

    # Пока очередь не пуста, продолжаем обход
    while queue:
        # Извлекаем вершину из НАЧАЛА очереди (FIFO)
        u = queue.pop(0)

        visited_order.append(u)
        
        # Перебираем всех соседей текущей вершины u
        for v in graph[u]:
            # СЛУЧАЙ 1: Сосед еще не посещен
            if dist[v] == -1:
                # Устанавливаем расстояние до соседа = расстояние до u + 1
                dist[v] = dist[u] + 1
                
                # Запоминаем, что в v мы пришли из u
                parent[v] = u
                
                # Добавляем соседа в конец очереди для последующей обработки
                queue.append(v)
            
            # СЛУЧАЙ 2: Сосед УЖЕ ПОСЕЩЕН и это НЕ РОДИТЕЛЬ текущей вершины
            # Это ключевое условие для обнаружения цикла!
            elif parent[u] != v:
                # Мы нашли цикл! Вычисляем его длину:
                # dist[u] - расстояние от start до u
                # dist[v] - расстояние от start до v
                # +1 - добавляем ребро (u, v), которое замыкает цикл
                cycle_length = dist[u] + dist[v] + 1
                
                # Находим вершины цикла из списка посещенных
                cycle_vertices = []
                for vertex in reversed(visited_order):
                    if dist[vertex] >= dist[v]:
                        cycle_vertices.append(vertex)
                    if vertex == v:
                        break
                
                # Восстанавливаем путь для поиска максимального ребра
                path = []
                x = u
                while x != v and parent[x] is not None:
                    path.append((parent[x], x))
                    x = parent[x]
                
                # Добавляем последнее ребро если нужно
                if x != v and parent[v] is not None:
                    y = v
                    while y != x and parent[y] is not None:
                        path.append((parent[y], y))
                        y = parent[y]
                
    return path, cycle_vertices


def find_max_edge_in_cycle(edges, cycle_path):
    max_weight = -1
    max_edge = None
    
    for edge in cycle_path:
        u, v = edge
        for mu, mv, w in edges:
            if (mu == u and mv == v) or (mu == v and mv == u):
                if w > max_weight:
                    max_weight = w
                    max_edge = (u, v, w)
                break
    
    return max_edge, max_weight


# Пример использования
if __name__ == "__main__":
    # Ввод данных
    n, m = map(int, input().split())
    graph_edges = []
    original_edges_list = []
    
    for i in range(m):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        graph_edges.append((w, u, v))
        original_edges_list.append((u, v, w))
    
    # Строим MST
    total_cost, mst = kruskal_mst(n, graph_edges)
    spisok = stroki_spisok(mst)
    for i in range(m):
        u, v, w = original_edges_list[i]
        into = 0
        for mu, mv, mw in mst:
            if (mu == u and mv == v) or (mu == v and mv == u):
                into = 1
                break
        
        if into == 1:
            print(total_cost)
        else:
            new_mst = mst.copy()
            # print(new_mst)
            new_mst.append((u, v, w))
            new_spisok = stroki_spisok(new_mst)
            cycle_path, cycle_vertices = zikl(new_spisok, u, v)
            max_edge, max_weight = find_max_edge_in_cycle(mst, cycle_path)
            print(total_cost + w - max_weight - 1)

'''
5 7 
1 2 3
1 3 1
1 4 5
2 3 2
2 5 3
3 4 2
4 5 4
'''

     
