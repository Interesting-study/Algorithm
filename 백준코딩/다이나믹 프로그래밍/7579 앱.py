#https://www.acmicpc.net/problem/7579
n, m = map(int, input().split())
memory = [0] + list(map(int, input().split()))
cost = [0] + list(map(int, input().split()))

sum_cost = sum(cost) + 1
result = sum(cost)

#dp[i][cost] = i번째 앱과 j만큼의 cost로 가질 수 있는 최대 메모리 값
dp = [[0] * sum_cost for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(sum_cost):
        if cost[i] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j - cost[i]] + memory[i] , dp[i - 1][j])

        if dp[i][j] >= m:
            result = min(result, j)

if m != 0:
    print(result)
else:
    print(0)
