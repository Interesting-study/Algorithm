#https://www.acmicpc.net/problem/17780
#0은 흰색, 1은 빨간색, 2는 파란색
from collections import defaultdict

n, k = map(int, input().split())
board = [input().split() for _ in range(n)]
chess_piece = defaultdict(list)

for i in range(1, k+1):
    row, col, direction = map(int, input().split())
    chess_piece[i].append([(row, col), direction])

print(chess_piece[1])