#https://www.acmicpc.net/problem/2573
#https://wookcode.tistory.com/155?category=1008519
from collections import deque

n, m = map(int ,input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

is_separate = False
days = 0

def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        visited[x][y] = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] != 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                elif arr[nx][ny] == 0:
                    count[x][y] += 1

    return True

while True:
    visited = [[False] * m for _ in range(n)]
    count = [[0]*m for _ in range(n)]
    result = 0

    for i in range(n):
        for j in range(m):
            if arr[i][j] != 0 and not visited[i][j]:
                if bfs(i, j):
                    result += 1
    #빙산 깍는 중
    for i in range(n):
        for j in range(m):
            arr[i][j] -= count[i][j]
            if arr[i][j] < 0:
                arr[i][j] = 0

    if result == 0:#다 바다가 되어도 분리가 되지 않는 경우
        break

    if result >= 2:
        is_separate = True
        break
    days += 1

if is_separate:
    print(days)
else:
    print(0)
