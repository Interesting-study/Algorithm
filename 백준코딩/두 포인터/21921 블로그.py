from collections import defaultdict

n, x = map(int, input().split())
visitors = list(map(int, input().split()))

max_visitors = now = sum(visitors[:x]) #[0, 1]
cnt = 1

for idx in range(x, n):
    now -= visitors[idx-x]
    now += visitors[idx]

    if max_visitors < now:
        max_visitors = now
        cnt = 1
    elif max_visitors == now:
        cnt += 1

if max_visitors == 0:
    print("SAD")
else:
    print(max_visitors)
    print(cnt)