from collections import deque

n, k = map(int, input().split())

tube = []
virus = []

for i in range(n):
    tube.append(list(map(int, input().split())))

    for j in range(n):
        if tube[i][j] != 0:
            virus.append((tube[i][j], 0,  i, j))

virus.sort()
seconds, find_x, find_y = map(int, input().split())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

#바이러스가 동시에 움직여야 하므로
q = deque(virus)

while q:
    prio, sec, x, y = q.popleft()

    if sec == seconds:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<= nx <n and 0<= ny <n:
             if tube[nx][ny] == 0:
                 tube[nx][ny] = prio
                 q.append((prio, sec + 1, nx, ny))

print(tube)
print(tube[find_x-1][find_y-1])