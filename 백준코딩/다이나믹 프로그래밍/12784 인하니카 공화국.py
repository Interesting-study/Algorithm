#https://www.acmicpc.net/problem/12784
import math

INF = math.inf

def dfs(x, y):
    global visited, dp
    visited[x] = 1

    if bridge_state[x] == 1 and x != 1:
        return INF
    dynamite = 0

    for next in graph[x]:
        if next[0] != y:
            if visited[next[0]] == 0:
                boom = dfs(next[0], x)
                dynamite += min(boom, next[1])

    dp[x] = dynamite
    return dynamite

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())

    graph = [[] for _ in range(n+1)]
    bridge_state = [0] * (n+1)
    visited = [0] * (n+1)
    dp = [-INF] * (n+1)

    for _ in range(m):
        a, b, d = map(int, input().split())

        bridge_state[a] += 1
        bridge_state[b] += 1

        graph[a].append((b, d))
        graph[b].append((a, d))

    print(dfs(1, 1))
