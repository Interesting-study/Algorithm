#https://www.acmicpc.net/problem/16236
from collections import deque, defaultdict

n = int(input())
spaces = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

#사이즈 : 위치
fishes = defaultdict(list)

for i in range(n):
    for j in range(n):
        if spaces[i][j] == 0:
            continue
        elif spaces[i][j] == 9:
            start = (i, j)
        else:
            size = spaces[i][j]
            fishes[size].append((i, j))

class Shark:
    def __init__(self, start):
        self.size = 2
        self.start = start
        self.eating_fish = 0
        self.help = False
        self.seconds = 0

    def upgrade_size(self):
        if self.eating_fish >= self.size:
            self.size += 1
            self.eating_fish = 0

    def move(self, dx, dy, n):
        q = deque()
        q.append(self.start)

        while q:
            sx, sy = q.popleft()

            for i in range(4):
                nx = sx + dx[i]
                ny = sy + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                pass

shark = Shark(start)

# 초반에 먹을 물고기가 아예 한 마리도 없을 때
if len(fishes[1]) == 0:
    print(shark.seconds)
else:
    pass
