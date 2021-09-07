#https://www.acmicpc.net/problem/15558
from collections import deque

def bfs(i, j):
    q = deque()
    q.append((i, j))
    sec = 0

    while q:
        for _ in range(len(q)):
            x, y = q.popleft()

            for nx, ny in ((x, y+1), (x, y-1), (not x, y+k)):
                if ny >= n:
                    return 1

                if sec < ny < n and board[nx][ny] == 1 and not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = True
        sec += 1
    return 0


n, k = map(int, input().split())

board = [list(map(int, str(input()))) for _ in range(2)]
visited = [[False] * n for _ in range(2)]

print(bfs(0, 0))