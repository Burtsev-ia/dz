def f(matrix):
    d = {}
    for i in range(len(matrix)):
        ne = []
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                ne.append(j)
        d[i] = ne
    return d


matrix = [
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 0],
    [0, 1, 0, 0]
]
print(f(matrix))
