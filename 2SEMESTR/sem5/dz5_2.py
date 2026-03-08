def bellman_ford(matrix, source):

    n, inf = len(matrix), float("inf")
    v = range(n)
    dist = [inf for _ in v]
    dist[source] = 0
    for _ in range(n - 1):
        for i in v:
            for j in v:
                w = matrix[i][j]
                if dist[i] != inf and dist[i] + w < dist[j]:
                    dist[j] = dist[i] + w

    # проверяем ещё раз на наличие отрицательного цикла
    for i in v:
        for j in v:
            w = matrix[i][j]
            if dist[i] != inf and dist[i] + w < dist[j]:
                return "возможно"

    return 'невозможно'


co = int(input())
for _ in range(co):
    n, m = map(int, input().split())
    inf = 9**999
    matrix = [[inf] * n for _ in range(n)]
    for i in range(n):
        matrix[i][i] = 0
    for _ in range(m):
        x, y, w = map(int, input().split())
        matrix[x][y] = w
    # print(matrix)
    print(bellman_ford(matrix, 0))
'''
2
3 3
0 1 1000
1 2 15
2 1 -42
4 4
0 1 10
1 2 20
2 3 30
3 0 -60
'''
