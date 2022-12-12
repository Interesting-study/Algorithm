#https://www.acmicpc.net/problem/21608
from collections import defaultdict

def change_coord(stu_num):
    return divmod(stu_num-1, n)

def find_near_seat(x, y):
    near_seat = []
    cnt = 0
    for idx in range(4):
        nx = x + dx[idx]
        ny = y + dy[idx]

        if 0 <= nx < n and 0 <= ny < n:
            if cls[nx][ny]:
                near_seat.append(cls[nx][ny])
            else:
                cnt += 1

        return near_seat, cnt

n = int(input())
students_in_fav = defaultdict(list)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(n**2):
    info = list(map(int, input().split()))
    students_in_fav[info[0]] = info[1:]

cls = [[False] * n for _ in range(n)]
satisfaction = {0: 0, 1: 1, 2: 10, 3: 100, 4: 1000}

for stu in students_in_fav.keys():
    cnt = 0

    for i in range(n):
        for j in range(n):
            if cls[i][j]:
                continue

            near_seat, emp_cnt = find_near_seat(i, j)

            for fav in students_in_fav[stu]:
                if fav in near_seat:
                    cnt += 1