#https://www.acmicpc.net/problem/6236
n, m = map(int, input().split())
plans = [int(input()) for _ in range(n)]

max_plans = max(plans)
left, right = min(plans), sum(plans)
answer = 0

while left <= right:
    mid = (left + right) // 2
    cnt, wallet = 1, mid

    for p in plans:
        if wallet < p:
            wallet = mid
            cnt += 1
        wallet -= p

    if cnt > m or mid < max_plans:
        left = mid + 1
    else:
        right = mid - 1
        answer = mid

print(mid)

        

