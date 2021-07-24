#https://www.acmicpc.net/problem/12865

n, k = map(int, input().split())

#아이템 갯수별 원하는 무게에 따른 최대가치 dp 테이블
dp = [[0] * (k + 1) for i in range(n + 1)]

# goods= (무게, 가치), 2차원 테이블
goods = [tuple(map(int, input().split())) for _ in range(n)]

for i in range(1, n+1):
    for w in range(1, k+1):
        if goods[i-1][0] > w:
            dp[i][w] = dp[i-1][w]
        else:
            dp[i][w] = max(dp[i-1][w], goods[i-1][1] + dp[i-1][w - goods[i-1][0]])

print(dp[n][k])
