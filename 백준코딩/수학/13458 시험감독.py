#https://www.acmicpc.net/problem/13458
import math

n = int(input())
a = map(int, input().split())
b, c = map(int, input().split())

answer = 0

for i in a:
    #총감독 하나 빼기
    i -= b
    answer += 1

    if i <= 0:
        continue
    else:
        answer += math.ceil(i / c)

print(answer)