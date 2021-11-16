#https://www.acmicpc.net/problem/13459

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

#상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]