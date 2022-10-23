n = int(input())
cows = [list(map(int, input().split())) for _ in range(n)]
cows.sort()
R = float("inf")

for i in range(n-1):
    if cows[i][1] + cows[i+1][1] == 1:
        R = min(cows[i+1][0] - cows[i][0], R)

start = 1

for i in range(n-1):
    now_cow = cows[i]
    next_cow = cows[i+1]

    if next_cow[0] - now_cow[0] >= R and next_cow[1] == 1:
        start += 1

print(start)
