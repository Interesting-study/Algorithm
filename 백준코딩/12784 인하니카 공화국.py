#https://www.acmicpc.net/problem/12784
from collections import defaultdict
import heapq

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    tree = defaultdict(list)

    for _ in range(m):
        a, b, d = map(int, input().split())
        heapq.heappush(tree[a], (d, b))
        heapq.heappush(tree[b], (d, a))

    print(tree)