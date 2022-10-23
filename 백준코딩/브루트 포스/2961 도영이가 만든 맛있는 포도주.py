from itertools import combinations

n = int(input())
taste = [list(map(int, input().split())) for _ in range(n)]
combs = [combinations(taste, i) for i in range(1, n+1)]
answer = float('inf')

for comb in combs:
    for each in comb:
        sour = 1
        bitter = 0

        for e in each:
            sour *= e[0]
            bitter += e[1]

        answer = min(answer, abs(sour - bitter))

print(answer)