#https://www.acmicpc.net/problem/7562
from collections import deque

T = int(input())

dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

answer = []


def bfs(sx, sy, tx, ty):
    q = deque()
    q.append((sx, sy))
    board[sx][sy] = 1

    while q:
        x, y = q.popleft()

        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < l and 0 <= ny < l:
                if board[nx][ny] == 0:
                    board[nx][ny] = board[x][y] + 1

                    if nx == tx and ny == ty:
                        return board[nx][ny] - 1

                    q.append((nx, ny))

for i in range(T):
    l = int(input())
    board = [[0] * l for _ in range(l)]

    #sx = start_x, tx = target_x
    sx, sy = map(int, input().split())
    tx, ty = map(int, input().split())

    answer.append(bfs(sx, sy, tx, ty))

for x in answer:
    if x == None:
        print(0)
    else:
        print(x)