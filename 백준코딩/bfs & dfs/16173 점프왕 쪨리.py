#https://www.acmicpc.net/problem/16173
#https://www.acmicpc.net/problem/16174
from collections import deque

def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = True

    while q:
        x, y = q.popleft()

        if area[x][y] == -1:
            return "HaruHaru"

        jumping = area[x][y]

        for i in range(2):
            nx = x + dx[i] * jumping
            ny = y + dy[i] * jumping

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))
    return "Hing"

n = int(input())
area = [list(map(int, input().split())) for _ in range(n)]

#아래쪽과 오른쪽으로만 움직임
dx = [1, 0]
dy = [0, 1]

visited = [[False] * n for _ in range(n)]
print(bfs(0, 0))