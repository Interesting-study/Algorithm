#https://www.acmicpc.net/problem/20055
from collections import deque

n, k = map(int, input().split())
conveyor_belt = deque(map(int, input().split()))