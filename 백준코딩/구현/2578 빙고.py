#https://www.acmicpc.net/problem/2578
import sys
from collections import defaultdict

board = defaultdict(tuple)
checked = [[0]*5 for _ in range(5)]

for i in range(5):
    line = list(map(int, input().split()))
    for j in range(5):
        board[line[j]] = (i, j)

called = 0

for _ in range(5):
    line = list(map(int, input().split()))
    for i in range(5):
        called += 1

        if line[i] in board:
            checked[board[line[i]][0]][board[line[i]][1]] = 1

            bingo = 0

            for j in range(5):
                if sum(checked[j]) == 5: #가로로 빙고
                    bingo += 1

                if sum([checked[k][j] for k in range(5)]) == 5: #세로로 빙고
                    bingo += 1


            if checked[0][4] + checked[1][3] + checked[2][2] + checked[3][1] + checked[4][0] == 5: #오른쪽 대각선
                bingo += 1

            if checked[0][0] + checked[1][1] + checked[2][2] + checked[3][3] + checked[4][4] == 5: #왼쪽 대각선
                bingo += 1

            if bingo >= 3:
                print(called)
                sys.exit()



