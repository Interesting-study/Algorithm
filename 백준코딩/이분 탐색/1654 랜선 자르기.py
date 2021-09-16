#https://wwcvw.acmicpc.net/problem/1654

k, n = map(int, input().split())
lans = [int(input()) for _ in range(k)]
lans.sort()

start, end = 1, lans[-1]

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for lan in lans:
        cnt += lan // mid

    if cnt >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)