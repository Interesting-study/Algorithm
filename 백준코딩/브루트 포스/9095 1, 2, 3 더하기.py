#https://www.acmicpc.net/problem/9095
T = int(input())
targets = [int(input()) for _ in range(T)]

dp = [1, 2, 4]


for i in range(3, max(targets)):
    dp.append(dp[i-1] + dp[i-2] + dp[i-3])

for t in targets:
    print(dp[t-1])