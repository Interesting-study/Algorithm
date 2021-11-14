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
        if 'O' in board[i]:
            j = board[i].index('O')
            break
    return (i, j)

def bfs(start):
    q = deque()
    q.append(start)
    cnt = 0

    while q:
        x, y = q.popleft()

        print('좌표, x:{}, y:{}'.format(x, y))

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if board[nx][ny] == '#' or board[nx][ny] == "B":
                continue

            if board[nx][ny] == "." and not visited[nx][ny]:
                cnt += 1

                while board[nx][ny] == '.' or board[nx][ny] == 'O':
                    print(nx, ny)
                    visited[nx][ny] = True

                    if board[nx][ny] == 'O':
                        return '\n' + str(cnt) + '번'

                    nx += dx[i]
                    ny += dy[i]

                print("방향 : ", i)
                qx = nx - dx[i]
                qy = ny - dy[i]
                q.append((qx, qy))

                print("\n---\n")
                break


        print(q)





n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

#상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

red, ex = find_red(board), find_exit(board)
print(bfs(red))


