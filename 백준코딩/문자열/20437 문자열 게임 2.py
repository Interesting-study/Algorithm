#https://www.acmicpc.net/problem/20437
from collections import Counter, defaultdict

T = int(input())

for _ in range(T):
    w = input()
    k = int(input())

    w_counter = Counter(w)
    candidate = defaultdict(list)

    for idx in range(len(w)):
        if w_counter[w[idx]] >= k:
            candidate[w[idx]].append(idx)

    if not candidate:
        print(-1)
        continue

    short = float('inf')
    long = 0

    for val in candidate.values():
        for i in range(len(val)-k+1):
            temp = val[i+k-1] - val[i] + 1

            short = min(short, temp)
            long = max(long, temp)


    print(short, long)

