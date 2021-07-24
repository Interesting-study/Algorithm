#https://www.acmicpc.net/problem/1005

from collections import deque
from copy import deepcopy
import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    building = [0] + list(map(int, input().split()))
    
    graph = [[] for i in range(n + 1)]
    indegree = [0] * (n + 1)

    queue = deque()

    for _ in range(k):
        x, y = map(int, input().split())
        graph[x].append(y)
        indegree[y] += 1

    win = int(input())

    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)

    result = deepcopy(building)

    while queue:
        now = queue.popleft()
        if now == win:
            break

        for i in graph[now]:
            result[i] = max(result[i], result[now] + building[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                queue.append(i)

    print(result[win])