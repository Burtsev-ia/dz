n = int(input())
# ведем корды коня индексация 0
x = int(input())
y = int(input())
# теперь нужно эту хрень посчитать


def kni(n, sx, sy):
    moves = [(2, 1), (2, -1), (-2, 1), (-2, -1),
             (1, 2), (1, -2), (-1, 2), (-1, -2)]
    dist = [[-1] * n for _ in range(n)]
    q = list()
    dist[sx][sy] = 0
    q.append((sx, sy))
    while q:
        x, y = q.pop(0)
        cur = dist[x][y]
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if dist[nx][ny] == -1:
                    dist[nx][ny] = cur + 1
                    q.append((nx, ny))
    return dist


ans = kni(n, x, y)
for i in range(n):
    print(ans[i])
