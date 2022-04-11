#https://www.acmicpc.net/problem/14891
from collections import deque

wheel = [deque(map(int, list(input()))) for _ in range(4)]
k = int(input())

for _ in range(k):
    k, dir = map(int, input().split())
    k -= 1

    tmp_dir = dir
    tmp_right = wheel[k][2] # 오른쪽 톱니바퀴랑 비교할 때
    tmp_left = wheel[k][-2] # 왼쪽 톱니바퀴랑 비교할 때

    wheel[k].rotate(dir)

    dir = tmp_dir
    for i in range(k-1, -1, -1):
        if wheel[i][2] != tmp_left:
            tmp_left = wheel[i][-2]
            wheel[i].rotate(dir*-1)
            dir *= -1
        else:
            break

    dir = tmp_dir
    for i in range(k+1, 4):
        if wheel[i][-2] != tmp_right:
            tmp_right = wheel[i][2]
            wheel[i].rotate(dir*-1)
            dir *= -1
        else:
            break

answer = 0
for i in range(4):
    if wheel[i][0] == 1:
        answer += (2**i)
print(answer)
