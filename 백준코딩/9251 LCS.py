#https://www.acmicpc.net/problem/9251
val1 = ' '+input()
val2 = ' '+input()

dp = [[0]*len(val2) for _ in range(len(val1))]

for i in range(1, len(val1)):
    for j in range(1, len(val2)):
        if val1[i] == val2[j]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

print(dp[-1][-1])