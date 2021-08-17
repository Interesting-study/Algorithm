n = int(input())
stairs = [0] + [int(input()) for _ in range(n)] + [0] * 2
dp = [0] * (n+3)

#가장 처음은 무조건 계단의 1번째 칸
dp[1] = stairs[1]
#두번째 계단은 1칸 + 1칸 or 바로 2칸
dp[2] = max(stairs[1] + stairs[2], stairs[2])
#세번째 계단은 1칸 + 2칸, 2칸 + 1칸
dp[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])

for i in range(4, n+1):
    dp[i] = max(dp[i-3] + stairs[i-1] + stairs[i],  dp[i-2] + stairs[i])

print(dp[n])