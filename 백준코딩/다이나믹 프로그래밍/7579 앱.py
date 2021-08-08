#https://www.acmicpc.net/problem/7579
n, m = map(int, input().split())
memory = list(map(int, input().split()))
cost = list(map(int, input().split()))

sum_cost = sum(cost) + 1

#dp[i][cost] = i번째 앱과 j만큼의 cost로 가질 수 있는 최대 메모리 값
dp = [[0] * sum_cost for _ in range(n + 1)]

print(dp)
