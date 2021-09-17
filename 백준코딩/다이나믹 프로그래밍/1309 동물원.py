#https://www.acmicpc.net/problem/1309
n = int(input())

dp = [0] * (n+1)

#한마리도 배치하지 않을 경우
dp[0] = 1
#한마리라도 배치할 경우의 수 = 칸의 갯수
dp[1] = 3

if n == 1:
    print(dp[1])
else:
    for i in range(2, n+1):
        dp[i] = dp[i-2] + (dp[i-1] * 2)
        dp[i] %= 9901

    print(dp[n])