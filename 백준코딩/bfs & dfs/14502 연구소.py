#https://www.acmicpc.net/problem/14502
from itertools import combinations
import copy
from collections import deque

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

walls = []
virus = []

def bfs():
    q = deque(virus)
    visited = [[False] * m for _ in range(n)]

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if last_maps[nx][ny] == 0:
                    last_maps[nx][ny] = 2
                    q.append((nx, ny))
                    visited[nx][ny] = True


for i in range(n):
    for j in range(m):
        if maps[i][j] == 0:
            walls.append((i, j))
        elif maps[i][j] == 2:
            virus.append((i, j))

walls_comb = list(combinations(walls, 3))
min_area = -1

for idx in range(len(walls_comb)):
    last_maps = copy.deepcopy(maps)

    for i in range(3):
        last_maps[walls_comb[idx][i][0]][walls_comb[idx][i][1]] = 1

    bfs()

    cnt = 0

    for i in range(n):
        for j in range(m):
            if last_maps[i][j] == 0:
                cnt += 1
    min_area = max(min_area, cnt)
print(min_area)