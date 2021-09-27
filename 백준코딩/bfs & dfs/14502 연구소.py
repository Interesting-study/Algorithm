#https://www.acmicpc.net/problem/14502
import copy
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
    visited = [[0] * m for _ in range(n)]

    while q:
        row, col = q.popleft()

        # 상
        if row - 1 >= 0 and last_maps[row - 1][col] == 0 and visited[row - 1][col] == 0:
            visited[row - 1][col] = 1
            last_maps[row - 1][col] = 2
            q.append([row - 1, col])

        # 하
        if row + 1 < n and last_maps[row + 1][col] == 0 and visited[row + 1][col] == 0:
            visited[row + 1][col] = 1
            last_maps[row + 1][col] = 2
            q.append([row + 1, col])

        # 좌
        if col - 1 >= 0 and last_maps[row][col - 1] == 0 and visited[row][col - 1] == 0:
            visited[row][col - 1] = 1
            last_maps[row][col - 1] = 2
            q.append([row, col - 1])

        # 우
        if col + 1 < m and last_maps[row][col + 1] == 0 and visited[row][col + 1] == 0:
            visited[row][col + 1] = 1
            last_maps[row][col + 1] = 2
            q.append([row, col + 1])


for i in range(n):
    for j in range(m):
        if maps[i][j] == 0:
            walls.append((i, j))
        elif maps[i][j] == 2:
            virus.append((i, j))

walls_comb = (combinations(walls, 3))
min_area = -1

for comb in walls_comb:
    last_maps = copy.deepcopy(maps)

    for i in range(3):
        last_maps[comb[0]][comb[1]] = 1

    bfs()

    cnt = 0

    for i in range(n):
        for j in range(m):
            if last_maps[i][j] == 0:
                cnt += 1
    min_area = max(min_area, cnt)
print(min_area)