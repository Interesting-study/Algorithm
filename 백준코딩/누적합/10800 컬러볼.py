#https://www.acmicpc.net/problem/17143
from collections import defaultdict

n = int(input())
balls = [list(map(int, input().split())) + [i] for i in range(n)] #색깔, 크기, 순서
balls.sort(key=lambda x:x[1])

answer = defaultdict(int)
ball_size_sum = defaultdict(int)

tot = 0
j = 0
for i in range(n):
    while balls[j][1] < balls[i][1] and j < n: #i번째 공의 크기가 더 클때까지
        tot += balls[j][1]
        ball_size_sum[balls[j][0]] += balls[j][1]
        j += 1
    answer[balls[i][2]] = tot - ball_size_sum[balls[i][0]] #전체에서 현재 색깔 공의 합을 빼면 다른 색깔 공들을 더한 값만 남는다

for i in range(n):
    print(answer[i])
