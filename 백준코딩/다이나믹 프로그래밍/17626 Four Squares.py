#다이나믹 프로그래밍

from math import sqrt

n = int(input())
dp = [0] * (n+1) # 인덱스가 어떤 특정한 숫자고, dp[5] -> 5가 되기 위해 필요한 제곱수의 갯수를 의미한다.
dp[1] = 1

for i in range(2, n+1):
    min_value = float("inf")

    for j in range(1, int(sqrt(i)) + 1):
        min_value = min(min_value, dp[i - j **2])

    dp[i] = min_value + 1

print(dp[n])