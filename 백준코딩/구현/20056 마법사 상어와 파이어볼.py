#https://www.acmicpc.net/problem/20056
from collections import deque

n, m, k = map(int, input().split())
board = [[deque() for _ in range(n)] for _ in range(n)]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

fireball = deque()

for _ in range(m):
    r, c, m, s, d = map(int, input().split())
    board[r-1][c-1].append(deque((m, s, d)))
    fireball.append((r-1, c-1))

for _ in range(k):
    for _ in range(len(fireball)):
        r, c = fireball.popleft()
        m, s, d = board[r][c].popleft()

        nr = (r + s*dx[d]) % n
        nc = (c + s*dy[d]) % n

        board[nr][nc].append(deque((m, s, d)))

    for i in range(n):
        for j in range(n):
            if len(board[i][j]) > 1:
                tot_m, tot_s, is_odd, is_even, cnt = 0, 0, 0, 0, 0
                while board[i][j]:
                    m, s, d = board[i][j].popleft()
                    tot_m += m
                    tot_s += s
                    cnt += 1

                    if d % 2 == 0:
                        is_even += 1
                    else:
                        is_odd += 1

                tot_m //= 5
                if tot_m == 0:
                    continue

                tot_s //= cnt

                if is_odd == cnt or is_even == cnt:
                    dir = [0, 2, 4, 6]
                else:
                    dir = [1, 3, 5, 7]

                for d in range(4):
                    fireball.append((i, j))
                    board[i][j].append(deque((tot_m, tot_s, dir[d])))
            elif len(board[i][j]) == 1:
                fireball.append((i, j))

answer = 0
for i in range(n):
    for j in range(n):
        answer += sum([val[0] for val in board[i][j]])

print(answer)