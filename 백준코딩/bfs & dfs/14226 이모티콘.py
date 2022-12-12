#https://www.acmicpc.net/problem/14226
from collections import deque

s = int(input())
dp = [[-1] * (s+1) for _ in range(s+1)]
#dp 에서 i는 화면에 있는 이모티콘, j는 클립보드

def bfs():
    q = deque()
    q.append((1, 0))
    dp[1][0] = 0

    while q:
        x, y = q.popleft()

        #화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장한다.
        if dp[x][x] == -1:
            dp[x][x] = dp[x][y] + 1
            q.append((x, x))

        #클립보드에 있는 모든 이모티콘을 화면에 붙여넣기 한다.
        if x + y <= s and dp[x+y][y] == -1:
            dp[x+y][y] = dp[x][y] + 1
            q.append((x+y, y))

        #화면에 있는 이모티콘 중 하나를 삭제한다.
        if x-1 >= 0 and dp[x-1][y] == -1:
            dp[x-1][y] = dp[x][y] + 1
            q.append((x-1, y))

bfs()

answer = dp[s][1]
for i in range(1, s):
    if dp[s][i] != -1:
        answer = min(answer, dp[s][i])

print(answer)

