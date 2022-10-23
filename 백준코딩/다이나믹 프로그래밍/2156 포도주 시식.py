n = int(input())
dp = [0] * 10002
wine = [0] * 10002

for i in range(1, n+1):
    wine[i] = int(input())

dp[1] = wine[1]
dp[2] = wine[1] + wine[2]

for i in range(3, n+1):
    dp[i] = max(dp[i - 1], dp[i - 3] + wine[i - 1] + wine[i], dp[i - 2] + wine[i])

print(dp[n])