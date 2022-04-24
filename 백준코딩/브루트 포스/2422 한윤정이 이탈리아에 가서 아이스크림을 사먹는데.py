#https://www.acmicpc.net/problem/2422
from itertools import combinations

n, m = map(int, input().split())
ban = [[False] * (n+1) for _ in range(n+1)]
cnt = 0

for _ in range(m):
    a, b = map(int, input().split())
    ban[a][b] = True
    ban[b][a] = True

for comb in combinations(range(1, n+1), 3):
    if ban[comb[0]][comb[1]] or ban[comb[0]][comb[2]] or ban[comb[1]][comb[2]]:
        continue
    cnt += 1

print(cnt)