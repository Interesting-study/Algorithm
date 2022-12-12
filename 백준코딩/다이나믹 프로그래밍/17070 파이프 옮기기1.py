#https://www.acmicpc.net/problem/17070
n = int(input())
house = [list(map(int, input().split())) for _ in range(n)]

#오른쪽, 아래, 오른쪽 아래 대각선
dx = [0, 1, 1]
dy = [1, 0, 1]