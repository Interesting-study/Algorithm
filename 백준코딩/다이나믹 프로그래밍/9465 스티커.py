# https://www.acmicpc.net/problem/9465
T = int(input())

for _ in range(T):
    n = int(input())
    sticker = [[0] * 100000, [0] * 100000]

    for idx, var in enumerate(map(int, input().split())):
        sticker[0][idx] = var
    for idx, var in enumerate(map(int, input().split())):
        sticker[1][idx] = var

    sticker[0][1] += sticker[1][0]
    sticker[1][1] += sticker[0][0]

    for i in range(2, n):
        sticker[0][i] += max(sticker[1][i - 1], sticker[1][i - 2])
        sticker[1][i] += max(sticker[0][i - 1], sticker[0][i - 2])

    print(max(sticker[0][n - 1], sticker[1][n - 1]))

"""
 dp = [[0] * n for _ in range(2)]

    dp[0][0] = sticker[0][0]
    dp[1][0] = sticker[1][0]

    dp[0][1] = dp[1][0] + sticker[0][1]
    dp[1][1] = dp[0][0] + sticker[1][1]
"""
