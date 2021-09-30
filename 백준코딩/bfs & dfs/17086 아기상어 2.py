#https://www.acmicpc.net/problem/17086
n, m = map(int, input().split())
space = [list(map(int, input().split())) for _ in range(n)]

#대각선 상하좌우, 상하좌우 -> x가 위 아래, y가 왼오
dx = [-1, -1, -1, 0, ]
dy = [-1, 0, 1, -1, ]

#(1, 1)
"""
(0, 0) (0, 1) (0, 2)
(1, 0) (1, 1) (1, 2)
(2, 0) (2, 1) (2, 2)
"""

for i in range(n):
    for j in range(m):
        pass