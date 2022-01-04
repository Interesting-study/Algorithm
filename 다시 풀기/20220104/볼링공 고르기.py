from itertools import combinations

n, m = map(int, input().split())
weights = list(map(int, input().split()))
weights_combination = combinations(weights, 2)

result = 0

for wc in weights_combination:
    if len(set(wc)) == 1:
        continue

    result += 1

print(result)