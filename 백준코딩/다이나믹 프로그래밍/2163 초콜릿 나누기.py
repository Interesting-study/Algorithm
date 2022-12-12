#https://www.acmicpc.net/problem/2163
#가로가 n, 세로가 m
n, m = map(int, input().split())
answer = (m - 1) + (n - 1) * m

print(answer)
