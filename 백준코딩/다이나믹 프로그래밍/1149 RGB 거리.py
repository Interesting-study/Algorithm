#https://www.acmicpc.net/problem/1149
n = int(input())

RGB = []

for _ in range(n):
    RGB.append(list(map(int, input().split())))

dp = [[int(1e9)] * 3 for _ in range(n) ]

for i in range(n):
    if i == 0:
        dp[i][0] = RGB[i][0]
        dp[i][1] = RGB[i][1]
        dp[i][2] = RGB[i][2]
    else:
        dp[i][0] = RGB[i][0] + min(dp[i - 1][1], dp[i - 1][2])
        dp[i][1] = RGB[i][1] + min(dp[i - 1][2], dp[i - 1][0])
        dp[i][2] = RGB[i][2] + min(dp[i - 1][0], dp[i - 1][1])

print(min(dp[n-1]))