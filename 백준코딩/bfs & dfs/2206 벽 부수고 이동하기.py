import sys
from collections import deque

input = sys.stdin.readline
INF = int(1e9)


def bfs(x, y):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    q = deque()
    visited[0][x][y] = 1  # 시작위치 카운트
    q.append((0, x, y))  # 벽 뚫기전, 시작위치 삽입

    while q:
        block, x, y = q.popleft()
        for i in range(4):
            px = x + dx[i]
            py = y + dy[i]
            # 범위 내
            if 0 <= px and px < n and 0 <= py and py < m:
                # 벽이 아니고 방문한적이 없다면
                if maze[px][py] == 0 and visited[block][px][py] == INF:
                    visited[block][px][py] = visited[block][x][y] + 1
                    q.append((block, px, py))

                # 벽이고 한번도 뚫은적 없고 벽이 뚫린 기록이 없다면
                elif maze[px][py] == 1 and block == 0 and visited[1][px][py] == INF:
                    visited[1][px][py] = visited[block][x][y] + 1
                    q.append((1, px, py))

    return min(visited[0][n - 1][m - 1], visited[1][n - 1][m - 1])


n, m = map(int, input().split())
maze = []
# 방문 테이블 ,  0은 벽 안부숨, 1 벽 부숨
visited = [[[INF] * m for _ in range(n)] for _ in range(2)]

# 그래프 정보
for _ in range(n):
    maze.append(list(map(int, input().rstrip())))

ans = bfs(0, 0)
if ans == INF:
    print(-1)
else:
    print(ans)