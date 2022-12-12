import sys
from bisect import bisect_left

def search():
    min_value = float('inf')
    cnt = 1

    for i in range(1, h+1):
        up_idx, down_idx = bisect_left(up_obstacle, (h+1)-i), bisect_left(down_obstacle, i)
        obs_cnt = n - (up_idx + down_idx)
        if obs_cnt < min_value:
            min_value = obs_cnt
            cnt = 1
        elif obs_cnt == min_value:
            cnt += 1

    return [min_value, cnt]

n, h = map(int, sys.stdin.readline().split())
up_obstacle = []
down_obstacle = []

for idx in range(n):
    if idx % 2 == 0:
        down_obstacle.append(int(sys.stdin.readline().strip()))
    else:
        up_obstacle.append(int(sys.stdin.readline().strip()))

up_obstacle.sort()
down_obstacle.sort()

print(*search())