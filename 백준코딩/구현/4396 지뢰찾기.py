#https://www.acmicpc.net/problem/4396
def check(x, y, result):
    cnt = 0
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if board[nx][ny] == '*':
                cnt += 1

    result[x][y] = str(cnt)

n = int(input())
board = [list(input()) for _ in range(n)] #'*'은 지뢰
user = [list(input()) for _ in range(n)]
result = [['.'] * n for _ in range(n)]

dx = [1, -1, 0, 0, 1, -1, 1, -1] #상하좌우 대각선
dy = [0, 0, 1, -1, 1, 1, -1, -1]
is_tread = False

for i in range(n):
    for j in range(n):
        if user[i][j] == 'x':
            if board[i][j] == '*' and not is_tread:
                is_tread = True
            check(i, j, result)

if is_tread:
    for i in range(n):
        for j in range(n):
            if board[i][j] == '*':
                result[i][j] = '*'

for res in result:
    print(''.join(res))

'''
2
*.
.*
..
.x
'''