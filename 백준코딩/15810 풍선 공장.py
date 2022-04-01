#https://www.acmicpc.net/problem/15810
#프로그래머스 입국 심사와 똑같은 문제
n, m = map(int, input().split())
times = list(map(int, input().split()))
answer = 0

start = 0
end = max(times)*m

while start <= end:
    complete = 0
    mid = (start + end) // 2

    for time in times:
        complete += (mid // time)

        if complete >= m:
            break

    if complete >= m:
        answer = mid
        end = mid -1

    elif complete < m:
        start = mid + 1

print(answer)