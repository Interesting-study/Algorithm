#https://www.acmicpc.net/problem/2293
n, k = map(int, input().split())
coin_value = [int(input()) for _ in range(n)]

dp = [0] * (k+1)

dp[0] = 1

for value in coin_value:
    for idx in range(value, k+1):
        dp[idx] += dp[idx-value]

print(dp[k])