#https://www.acmicpc.net/problem/1520
import sys
sys.setrecursionlimit(10**9)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    print(dp)
    if x == m-1 and y == n-1:
        return 1

    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < m and 0 <= ny < n:
            if arr[nx][ny] < arr[x][y]:
                dp[x][y] += dfs(nx, ny)

    return dp[x][y]

m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1]*n for _ in range(m)]

print(dfs(0, 0))
