#https://www.acmicpc.net/problem/1793
MAX = 251
dp = [0] * MAX

dp[0] = 1
dp[1] = 1

def tiling(n):
    if dp[n] != 0:
        return dp[n]

    for i in range(2, n+1):
        dp[i] = dp[i-1] + 2 * dp[i-2]

    return dp[n]

while True:
    try:
        n = int(input())
        print(tiling(n))
    except:
        break
