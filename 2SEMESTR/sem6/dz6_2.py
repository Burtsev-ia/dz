def findo(dicto, board, m, l):
    found = list()
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    def dfs(x, y, cur, visited):
        if cur in dicto:
            found.append(cur)
        visited[x][y] = 1
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < l and not visited[nx][ny]:
                dfs(nx, ny, cur + board[nx][ny], visited)
        visited[x][y] = 0

    visited = [[0] * l for _ in range(m)]
    for i in range(m):
        for j in range(l):
            dfs(i, j, board[i][j], visited)

    return sorted(found)


if __name__ == "__main__":
    n = int(input())
    words = input().split()
    m, l = map(int, input().split())
    board = []
    for _ in range(m):
        board.append(input().split())

    result = findo(words, board, m, l)
    print(*result)
'''
4
GEEKS FOR QUIZ GO
3 3
G I Z
U E K
Q S E'''
