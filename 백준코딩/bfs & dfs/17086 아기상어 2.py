#https://www.acmicpc.net/problem/17086
from collections import deque

n, m = map(int, input().split())
space = [list(map(int, input().split())) for _ in range(n)]

#대각선 상하좌우, 상하좌우 -> x가 위 아래, y가 왼오
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

shark = deque()

def bfs(q):
    while q:
        x, y = q.popleft()

        for idx in range(8):
            nx = x + dx[idx]
            ny = y + dy[idx]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if not space[nx][ny]:
                q.append((nx, ny))
                space[nx][ny] = space[x][y] + 1


for i in range(n):
    for j in range(m):
        if space[i][j] == 1:
            shark.append((i, j))

bfs(shark)
print(max(map(max, space))-1)