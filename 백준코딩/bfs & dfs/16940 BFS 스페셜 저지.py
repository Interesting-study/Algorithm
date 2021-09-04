#https://www.acmicpc.net/problem/16940
from collections import deque

def bfs(x):
    q = deque()
    q.append(x)

    visited[x] = True
    answer.append(x)

    while q:
        now = q.popleft()

        for node in graph[now]:
            if not visited[node]:
                q.append(node)
                visited[node] = True
                answer.append(node)

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

predict = list(map(int, input().split()))
visited = [False] * (n+1)

#priority의 인덱스는 노드 번호, value는 우선순위
priority = [0] * (n+1)

for i in range(n):
    priority[predict[i]] = i

answer = []

for i in range(1, n+1):
    graph[i].sort(key=lambda x: priority[x])

bfs(1)

if predict == answer:
    print(1)
else:
    print(0)