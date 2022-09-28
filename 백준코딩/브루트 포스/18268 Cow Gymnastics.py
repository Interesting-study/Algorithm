from itertools import combinations

K, N = map(int, input().split())
session = [list(map(int, input().split())) for _ in range(K)]

cnt = 0
for i, j in combinations(range(1, N+1), 2):
    if (sum([se.index(i) < se.index(j) for se in session]) % K) == 0:
        cnt += 1

print(cnt)