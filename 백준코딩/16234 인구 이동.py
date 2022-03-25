#https://www.acmicpc.net/problem/16234
from collections import deque

n, l, r = map(int, input().split())
lands = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))

    union = set()
    union.add((x, y))

    visited[x][y] = True

    people = lands[x][y]

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            if not visited[nx][ny] and l <= abs(lands[x][y] - lands[nx][ny]) <= r:
                union.add((nx, ny))
                visited[nx][ny] = True

                q.append((nx, ny))
                people += lands[nx][ny]

    for x, y in union:
        lands[x][y] = people // len(union)

    return len(union)

answer = 0

while True:
    visited = [[False] * n for _ in range(n)]
    flag = False
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                if bfs(i, j) > 1:
                    flag = True
    if not flag:
        break
    answer += 1

print(answer)

'''
2 20 50
50 30
20 40

국경선을 공유하는 두 나라의 인구 차이가 L명 이상, R명 이하라면, 두 나라가 공유하는 국경선을 오늘 하루 동안 연다.
'''