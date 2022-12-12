#https://www.acmicpc.net/problem/16964

def dfs(x):
    if visited[x]:
        return

    answer.append(x)
    visited[x] = True

    for i in graph[x]:
        if not visited[i]:
            dfs(i)

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

predict = list(map(int, input().split()))
answer = []
visited = [False] * (n+1)

priority = [0] * (n+1)

for i in range(n):
    priority[predict[i]] = i

for i in range(1, n+1):
    graph[i].sort(key=lambda x: priority[x])

dfs(1)

if predict == answer:
    print(1)
else:
    print(0)
