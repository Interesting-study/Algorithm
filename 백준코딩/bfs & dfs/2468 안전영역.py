#https://www.acmicpc.net/problem/2468
from collections import deque

def bfs(x, y, height):
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

             if area[nx][ny] > height and not visited[nx][ny]:
                 visited[nx][ny] = True
                 q.append((nx, ny))

n = int(input())
area = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

heights = set()

for i in area:
    heights.update(set(i))

length = max(heights)
answer = {i:0 for i in range(length)}

#비가 안 오는 상황도 고려
for height in range(length):
    visited = [[False] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if area[i][j] > height and not visited[i][j]:
                bfs(i, j, height)
                answer[height] += 1

print(max(answer.values()))