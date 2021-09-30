#https://www.acmicpc.net/problem/21608
from collections import defaultdict

n = int(input())
students_in_fav = defaultdict(list)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(n**2):
    info = list(map(int, input().split()))
    students_in_fav[info[0]] = info[1:]
