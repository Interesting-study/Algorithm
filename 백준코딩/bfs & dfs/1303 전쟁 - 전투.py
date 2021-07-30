from collections import deque


def bfs(x, y, color):
    cnt = 0
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    while q:
        x, y = q.popleft()

        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]

            if 0 <= nx < m and 0 <= ny < n:
                if warrior[nx][ny] == color and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    cnt += 1
    return cnt + 1


n, m = map(int, input().split())
warrior = [list(input()) for _ in range(m)]
visited = [[False] * n for _ in range(m)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

white = blue = 0

for i in range(m):
    for j in range(n):
        if warrior[i][j] == "W" and not visited[i][j]:
            white += bfs(i, j, "W") ** 2
        elif warrior[i][j] == "B" and not visited[i][j]:
            blue += bfs(i, j, "B") ** 2

print(white, blue)

"""
5 5
WBWWW
WWWWW
BBBBB
BBBWW
WWWWW
"""