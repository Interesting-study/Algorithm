#https://www.acmicpc.net/problem/14716
from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    while q:
        x, y = q.popleft()

        for idx in range(8):
            nx = x + dx[idx]
            ny = y + dy[idx]

            if 0 <= nx < m and 0 <= ny < n:
                if info[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))


m, n = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(m)]
visited = [[False] * n for _ in range(m)]
answer = 0

dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]

for i in range(m):
    for j in range(n):
        if not visited[i][j] and info[i][j] == 1:
            bfs(i, j)
            answer += 1

print(answer)
