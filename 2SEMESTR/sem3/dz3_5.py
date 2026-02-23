"""7 9
0 1
0 3
0 2
1 4
2 3
3 4
3 5
4 6
5 6
"""

import sys
n, m = list(map(int, input().split()))
s = 0
graf = {}
for _ in range(m):
    u, v = map(int, input().split())
    w = 1
    if u not in graf:
        graf[u] = {}
    graf[u][v] = w
    if v not in graf:
        graf[v] = {}
    graf[v][u] = w


# возвращает красивым списочком все вершины графа
def all_vertex(graf):
    return list(graf.keys())
# print(all_vertex(graf))


# возвращаем не менее красивым списочком всех соседей данной вершины
def vertex_neighbors(graf, vertex):
    return list(graf[vertex].keys())
# print(vertex_neighbors(graf, 'D'))


# возвращаем длину ребра между двумя вершинами
def value(graf, vertex1, vertex2):
    return (graf[vertex1][vertex2])
# print(value(graf, 'A', 'D'))


def dijkstra(graf, start):
    unvisited_vertexes = all_vertex(graf)
    shortest_path = {}
    previous_vertex = {}

# по умолчанию расстояния между любыми двумя
# вершинами задаем равным бесконечности,
# а затем в цикле while переопределяем на минимально возможное
    max_value = sys.maxsize
    for vertex in unvisited_vertexes:
        shortest_path[vertex] = max_value
    shortest_path[start] = 0

    while unvisited_vertexes:
        # ищем вершину с меньшей оценкой
        current_min_vertex = None
        for vertex in unvisited_vertexes:
            if current_min_vertex is None:
                current_min_vertex = vertex
            elif shortest_path[vertex] < shortest_path[current_min_vertex]:
                current_min_vertex = vertex
        neighbors = vertex_neighbors(graf, current_min_vertex)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_vertex] \
                              + value(graf, current_min_vertex, neighbor)
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                previous_vertex[neighbor] = current_min_vertex
        unvisited_vertexes.remove(current_min_vertex)
    return previous_vertex, shortest_path


'''def print_result(previous_vertex, shortest_path,
                 start_vertex, target_vertex):
    path = []
    vertex = target_vertex
    while vertex != start_vertex:
        path.append(vertex)
        vertex = previous_vertex[vertex]
    path.append(start_vertex)
    print("->".join(reversed(list(map(str, path)))))
    print(shortest_path[target_vertex])
'''

previous_vertex, shortest_path = dijkstra(graf, s)
for i in shortest_path.keys():
    print(i, '-->min', shortest_path[i])
# print_result(previous_vertex, shortest_path, s, f)
# dijkstra(graf, s)
