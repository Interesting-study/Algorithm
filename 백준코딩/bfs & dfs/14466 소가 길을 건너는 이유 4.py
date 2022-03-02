#https://www.acmicpc.net/problem/14466
from collections import deque

def bfs(r1, c1):
    q = deque()
    q.append((r1, c1))
    visited[r1][c1] = True

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if visited[nx][ny]:
                continue
            if (nx, ny) in roads[x][y]:
                continue

            q.append((nx, ny))
            visited[nx][ny] = True

n, k, r = map(int, input().split())
roads = [[[] for _ in range(n)] for _ in range(n)]
answer = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(r):
    r1, c1, r2, c2 = map(int, input().split())
    roads[r1-1][c1-1].append((r2-1, c2-1))
    roads[r2-1][c2-1].append((r1-1, c1-1))

cows = []
for _ in range(k):
    a, b = map(int, input().split())
    cows.append((a-1, b-1))

for idx, cow in enumerate(cows):
    visited = [[False] * n for _ in range(n)]
    bfs(cow[0], cow[1])

    for r2, c2 in cows[idx+1:]:
        if not visited[r2][c2]:
            answer += 1

print(answer)