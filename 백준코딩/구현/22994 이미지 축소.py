#https://www.acmicpc.net/problem/22994
from collections import deque, OrderedDict

ni, mj = map(int, input().split())
pixels = [deque(list(input()))  for _ in range(ni)]

same_pixel = deque()
cnt_pixel = 0


