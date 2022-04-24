#https://www.acmicpc.net/problem/21278
INF = float('inf')
n, m = map(int, input().split())
costs = [[INF] * (n+1) for _ in range(n+1)]
max_time = INF

for i in range(1, n+1):
    costs[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    costs[a][b] = 1
    costs[b][a] = 1

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            costs[a][b] = min(costs[a][b], costs[a][k] + costs[k][b])


for i in range(1, n): #건물 후보 1
    for j in range(i, n+1): #건물 후보 2
        tot = 0
        for k in range(1, n+1): #모든 치킨집 방문
            tot += min(costs[k][i], costs[k][j])
        if max_time > 2 * tot:
            max_time = 2 * tot
            answer = [i, j, 2*tot]

print(*answer)