#https://www.acmicpc.net/problem/1915
n, m = map(int, input().split())
rect = [list(map(int, list(input()))) for _ in range(n)]
dp = [[0]*m for _ in range(n)]

answer = 0

for i in range(n):
    for j in range(m):
        if i == 0 or j == 0:
            dp[i][j] = rect[i][j]
        elif rect[i][j] == 0:
            dp[i][j] = 0
        else:
            dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        answer = max(dp[i][j], answer)

print(answer*answer)