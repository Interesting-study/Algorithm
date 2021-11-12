#https://www.acmicpc.net/problem/13460
from collections import deque
def find_red(board):
    for i in range(n):
        if 'R' in board[i]:
            j = board[i].index('R')
            break
    return (i, j)

def find_exit(board):
    for i in range(n):
        if 'R' in board[i]:
            j = board[i].index('O')
            break
    return (i, j)

def bfs(start):
    q = deque()
    q.append(start)

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if board[nx][ny] == '#' or board[nx][ny] == "B":
                continue

            if board[nx][ny] == "." and not visited[nx][ny]:
                while board[nx][ny] == "." and not visited[nx][ny]:
                    visited[nx][ny] = True


n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

red, ex = find_red(board), find_exit(board)
print(bfs(red))


