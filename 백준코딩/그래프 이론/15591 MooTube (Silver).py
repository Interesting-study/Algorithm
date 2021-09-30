#https://www.acmicpc.net/problem/15591
from collections import defaultdict

N, Q = map(int, input().split())
usado = defaultdict(list)

for _ in range(N-1):
    p, q, r = map(int, input().split())
    usado[p-1].append((q-1, r))
    usado[q-1].append((p-1, r))

for _ in range(Q):
    k, v = map(int, input().split())

print(usado)