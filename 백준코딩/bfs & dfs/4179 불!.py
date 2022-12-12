from collections import deque
from copy import deepcopy

def bfs():

    while fire_q:
        x, y = fire_q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= r or ny >= c:
                continue

            if fire_visited[nx][ny] != 0 or maze[nx][ny] == "#":
                continue

            fire_visited[nx][ny] = fire_visited[x][y] + 1
            fire_q.append((nx, ny))

    while jihoon_q:
        x, y = jihoon_q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= r or ny >= c:
                return jihoon_visited[x][y] + 1

            if jihoon_visited[nx][ny] != 0 or maze[nx][ny] == "#" or (fire_visited[nx][ny] != 0 and fire_visited[nx][ny] <= jihoon_visited[x][y] + 1):
                continue


            jihoon_visited[nx][ny] = jihoon_visited[x][y] + 1
            jihoon_q.append((nx, ny))

    return 'IMPOSSIBLE'

r, c = map(int, input().split())
maze = [list(input()) for _ in range(r)]

fire_q = deque()
jihoon_q = deque()

fire_visited = [[0] * c for _ in range(r)]
jihoon_visited = [[0] * c for _ in range(r)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


for i in range(r):
    for j in range(c):
        if maze[i][j] == "F":
            fire_q.append((i, j))
        elif maze[i][j] == "J":
            jihoon_q.append((i, j))

print(bfs())
"""
4 4
####
#F#J
#..#
#..#
"""