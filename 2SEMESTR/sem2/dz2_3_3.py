import sys


graf = {'A': {'B': 1, 'D': 1, 'C': 3},
        'B': {'A': 1, 'E': 5},
        'C': {'A': 3, 'D': 1},
        'D': {'A': 1, 'C': 1, 'E': 3, 'F': 9},
        'E': {'B': 5, 'D': 3, 'G': 7},
        'G': {'E': 7, 'F': 8},
        'F': {'D': 9, 'G': 8}
        }


def all_vertex(graf):
    return list(graf.keys())


print(all_vertex(graf))


def vertex_neighbors(graf, vertex):
    return list(graf[vertex].keys())


print(vertex_neighbors(graf, 'D'))


def value(graf, vertex1, vertex2):
    return graf[vertex1][vertex2]


print(value(graf, 'A', 'D'))


def dijkstra(graf, start):
    unvisited_vertexes = all_vertex(graf)
    shortest_path = {}
    previous_vertex = {}

    max_value = sys.maxsize
    for vertex in unvisited_vertexes:
        shortest_path[vertex] = max_value
    shortest_path[start] = 0

    while unvisited_vertexes:
        current_min_vertex = None
        for vertex in unvisited_vertexes:
            if current_min_vertex is None:
                current_min_vertex = vertex
            elif shortest_path[vertex] < shortest_path[current_min_vertex]:
                current_min_vertex = vertex
        neighbors = vertex_neighbors(graf, current_min_vertex)
        for neighbor in neighbors:
            tentative_value = int(str(shortest_path[current_min_vertex]) +
                                  str(value(graf,
                                            current_min_vertex, neighbor)))
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                previous_vertex[neighbor] = current_min_vertex
        unvisited_vertexes.remove(current_min_vertex)
    return previous_vertex, shortest_path


def print_result(previous_vertex, shortest_path,
                 start_vertex, target_vertex):
    path = []
    vertex = target_vertex
    while vertex != start_vertex:
        path.append(vertex)
        vertex = previous_vertex[vertex]
    path.append(start_vertex)
    print("->".join(reversed(path)))
    print(shortest_path[target_vertex])


previous_vertex, shortest_path = dijkstra(graf, 'A')
print_result(previous_vertex, shortest_path, 'A', 'F')
