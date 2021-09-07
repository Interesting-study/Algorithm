#https://www.acmicpc.net/problem/14501
n = int(input())
timeTable = [tuple(map(int, input().split())) for _ in range(n)]
dp = [0] * (n+1)
days = 0

for i in range(n-2, -1, -1):
    if i + timeTable[i][0] > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(timeTable[i][1] + dp[i + timeTable[i][0]], dp[i+1])

print(dp[0])