#https://www.acmicpc.net/problem/2667
from collections import deque

def bfs(x, y):
    cnt = 1
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if apart[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))
                cnt += 1
    return cnt


n = int(input())
apart = [list(map(int, list(input()))) for _ in range(n)]

visited = [[False] * n for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

answer = []

for i in range(n):
    for j in range(n):
        if apart[i][j] == 1 and not visited[i][j]:
            answer.append(bfs(i, j))

answer.sort()

print(len(answer))
for i in answer:
    print(i)