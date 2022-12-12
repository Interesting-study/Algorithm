# https://www.acmicpc.net/problem/1260
from collections import deque

n, m, v = map(int, input().split())

# 그래프 초기화
graph = [[0] * (n + 1) for i in range(n + 1)]

for idx in range(m):
    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1

dfs_visited = [False] * (n + 1)
bfs_visited = [False] * (n + 1)


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")

    for i in range(1, n+1):
        if (not visited[i]) and graph[v][i] == 1:
            dfs(graph, i, visited)



def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True

    while queue:
        x = queue.popleft()
        print(x, end=" ")

        for i in range(1, n+1):
            if (not visited[i]) and graph[x][i] == 1:
                queue.append(i)
                visited[i] = True

dfs(graph, v, dfs_visited)
print()
bfs(graph, v, bfs_visited)
