#https://www.acmicpc.net/problem/2667
n = int(input())
apart = [list(map(int, list(input()))) for _ in range(n)]

visited = [[False] * n for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

answer = []

def dfs(x, y):
    global cnt

    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if apart[x][y] == 1 and not visited[x][y]:
        visited[x][y] = True
        cnt += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True

    return False

cnt = 0

for i in range(n):
    for j in range(n):
        if dfs(i, j):
            answer.append(cnt)
            cnt = 0

answer.sort()

print(len(answer))
for i in answer:
    print(i)