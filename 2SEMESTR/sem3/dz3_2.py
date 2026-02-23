def is_cyclic(graph_array: list[list[int]]) -> bool:
    used = [False] * len(graph_array)
    res = False

    def dfs(v, p=-1):
        used[v] = True
        for u in graph_array[v]:
            if not used[u]:
                dfs(u, v)
            elif u != p:
                nonlocal res
                res = True
                break

    for i in range(len(graph_array)):
        if not used[i]:
            dfs(i)

    return res


graph: list[list[int]] = [
    [1, 2],
    [3, 4],
    [5],
    [6],
    [6, 1],
    [3],
    []
]
print(is_cyclic(graph))
