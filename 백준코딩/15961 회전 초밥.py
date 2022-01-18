#https://www.acmicpc.net/problem/15961
#접시의 수 n, 초밥의 가짓수 d, 연속해서 먹는 접시의 수 k, 쿠폰 번호 c
import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(n)]
start, end = 0, k

max_kind = len(set(sushi[start:end]))

while end <= n:
    now = sushi[start:end]
    if c in now:
        max_kind = max(max_kind, len(set(now)))
    else:
        max_kind = max(max_kind, len(set(now)) + 1)

    start += 1
    end += 1

print(max_kind)