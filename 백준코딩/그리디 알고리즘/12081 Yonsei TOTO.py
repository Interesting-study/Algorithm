#https://www.acmicpc.net/problem/12018
from collections import defaultdict

n, m = map(int, input().split())
answer = 0
subject = defaultdict(int) #과목번호 : 마일리지 리스트 정렬

for i in range(n):
    p, l = map(int, input().split())
    mileage = sorted(list(map(int, input().split())), reverse=True)
    if p < l:
        subject[i] = 1
    else:
        subject[i] = mileage[l-1]

applied_order = sorted(subject.keys(), key= lambda x: subject[x])

for ap in applied_order:
    now = subject[ap]

    if m - now >= 0:
        answer += 1
        m -= now

print(answer)
