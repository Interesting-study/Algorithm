#https://www.acmicpc.net/problem/15988
T = int(input())
cases = [int(input()) for _ in range(T)]
dp = [0] * (max(cases) + 1)
dp[0] = 1
dp[1] = 1
dp[2] = 2

for i in range(3, max(cases) + 1):
    dp[i] = dp[i - 1] % 1000000009 + dp[i - 2] % 1000000009 + dp[i - 3] % 1000000009

for ca in cases:
    print(dp[ca] % 1000000009)