#https://www.acmicpc.net/problem/5014
from collections import deque

F, S, G, U, D = map(int, input().split())

def bfs(F, S, G, U, D):
    q = deque()
    visited = [False] * (F+1)
    q.append([S, 0])

    while q:
        now, cnt = q.popleft()

        if now == G:
            return cnt

        if now + U <= F and not visited[now+U]:
            q.append([now+U, cnt+1])
            visited[now+U] = True

        if now - D >= 1 and not visited[now-D]:
            q.append([now-D, cnt+1])
            visited[now-D] = True

    return "use the stairs"


print(bfs(F, S, G, U, D))