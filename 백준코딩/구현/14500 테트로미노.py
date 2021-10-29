import sys
N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def DFS(depth, y, x, sumval):
    global result
    if sumval + (3 - depth) * maxval <= result:
        return
    if depth == 3:
        result = max(result, sumval)
        return
    else:
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 > ny or N <= ny or 0 > nx or M <= nx or visited[ny][nx]:
                continue
            if depth == 1:
                visited[ny][nx] = True
                DFS(depth + 1, y, x, sumval + arr[ny][nx])
                visited[ny][nx] = False

            visited[ny][nx] = True
            DFS(depth + 1, ny, nx, sumval + arr[ny][nx])
            visited[ny][nx] = False

result = 0
maxval = max(map(max, arr))
visited = [[False] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        DFS(0, i, j, arr[i][j])
        visited[i][j] = False

print(result)