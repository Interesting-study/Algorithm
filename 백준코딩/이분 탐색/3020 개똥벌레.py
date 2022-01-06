from collections import defaultdict

n, h = map(int, input().split())
obstacle = [int(input()) for _ in range(n)]
broken_obstacle = defaultdict(list)

left, right = 0, h