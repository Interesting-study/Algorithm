from collections import deque

def bfs(x):
    cnt = 1
    q = deque()
    q.append(x)
    visited = [False] * (n + 1)
    visited[x] = True

    while q:
        now = q.popleft()

        for w in pc[now]:
            if not visited[w]:
                visited[w] = True
                q.append(w)
                cnt += 1

    return cnt

n, m = map(int, input().split())
pc = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    pc[b].append(a)

result = []
can_hack = 0

for i in range(1, n+1):

    temp = bfs(i)

    if can_hack == temp:
        result.append(i)
    elif can_hack < temp:
        can_hack = temp
        result = []
        result.append(i)

print(*result)