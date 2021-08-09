#https://www.acmicpc.net/problem/7576
from collections import deque

def bfs():
    days = -1

    while q:
        days += 1

        for _ in range(len(q)):

            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < m and store[nx][ny] == 0:
                    store[nx][ny] = store[x][y] + 1
                    q.append((nx, ny))


    for line in store:
        if 0 in line:
            return -1
    return days

m, n = map(int, input().split())
store = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

q = deque()

for i in range(n):
    for j in range(m):
        if store[i][j] == 1:
            q.append((i, j))

print(bfs())