#https://www.acmicpc.net/problem/14889
from itertools import combinations
from itertools import permutations

INF = int(1e9)

n = int(input())
ability = [list(map(int, input().split())) for _ in range(n)]
n_idx = list(range(n))

idx_comb = list(combinations(n_idx, n//2))
answer = INF

def get_score(members):
    score = 0
    mem_permu = permutations(members, 2)

    for i, j in mem_permu:
        score += ability[i][j]

    return score

for comb in idx_comb:
    start = get_score(comb)
    link = get_score(list(set(n_idx) - set(comb)))

    answer = min(answer, abs(start - link))

print(answer)



"""
def get_score(members):
    score = 0
    mem_permu = permutations(members, 2)

    for i, j in mem_permu:
        score += ability[i][j]

    return score
    
    
0 0
0 1
0 4
1 0
1 1
1 4
4 0
4 1
4 4
"""



