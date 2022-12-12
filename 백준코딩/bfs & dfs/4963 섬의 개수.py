from collections import deque

#상하좌우 + 대각선
dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]

def bfs(i, j):
    visited[i][j] = True
    q = deque()
    q.append((i, j))

    while q:
        x, y = q.popleft()
        for idx in range(8):
            nx = x + dx[idx]
            ny = y + dy[idx]

            if 0 <= nx < h and 0<= ny < w and not visited[nx][ny] and island[nx][ny] == 1:
                visited[nx][ny] = True
                q.append((nx, ny))

while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    island = [list(map(int, input().split())) for _ in range(h)]
    cnt = 0
    visited = [[False] * w for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if island[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                cnt += 1
    print(cnt)