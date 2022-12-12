n, m = map(int, input().split())

curr = []
for i in range(n):
    curr.append(int(input()))

d = [10001] * (m+1)
d[0] = 0
for i in range(n):
    for j in range(curr[i], m+1):
        if d[j - curr[i]] != 10001:
            d[j] = min(d[j], d[j - curr[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])