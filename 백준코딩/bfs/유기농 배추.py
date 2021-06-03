from collections import deque

def bfs(y, x):
    queue = deque()
    queue.append((y, x))

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n and field[ny][nx] == 1:
                field[ny][nx] = 0
                queue.append((ny, nx))
             
t = int(input())

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]        

for _ in range(t):
    m, n, k = map(int, input().split(' '))
    field = [[0] * m for _ in range(n)]
    cnt = 0

    for _ in range(k):
         x, y = map(int, input().split(' '))
         field[y][x] = 1

    for i in range(n):
        for j in range(m):
            if field[i][j] == 1:
                field[i][j] = 0
                bfs(i, j)
                cnt += 1

    print(cnt)
