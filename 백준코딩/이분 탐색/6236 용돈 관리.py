#https://www.acmicpc.net/problem/6236
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
plans = [int(input()) for _ in range(n)]

left, right = 0, sum(plans)
min_plans = min(plans)
answer = sys.maxsize

while left <= right:
    mid = (left + right) // 2

    cnt, wallet = 0, 0
    lack = False

    for p in plans:
        #돈을 뽑아도 하루를 못 넘길 떄
        if mid - p < 0:
            lack = True
            break
        #하루는 살 수 있을 때
        elif wallet - p < 0:
            wallet = mid
            cnt += 1
        wallet -= p

    if not lack:
        if cnt <= m:
            right = mid - 1
            answer = min(answer, mid)
        elif cnt > m:
            left = mid + 1
    else:
        left = mid + 1

print(answer)