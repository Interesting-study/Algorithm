#https://www.acmicpc.net/problem/18429
from itertools import permutations

n, k = map(int, input().split())
A = list(map(int, input().split()))
answer = 0

for weights in permutations(A, n):
    personal_weight = 500
    for w in weights:
        personal_weight -= k
        personal_weight += w

        if personal_weight < 500:
            break
    else:
        answer += 1

print(answer)
