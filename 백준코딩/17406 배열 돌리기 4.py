#https://www.acmicpc.net/problem/17406
from itertools import permutations
from copy import deepcopy

n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
calc = [list(map(int, input().split())) for _ in range(k)]

ans = float('inf')

for p in permutations(calc, k):
    copy_arr = deepcopy(arr)
    print(p)
    for r, c, s in p:
        r -= 1
        c -= 1

        for i in range(s, 0, -1):

            tmp = copy_arr[r-i][c+i]
            copy_arr[r-i][c-i+1:c+i+1] = copy_arr[r-i][c-i:c+i]

            for row in range(r-i, r+i):
                copy_arr[row][c-i] = copy_arr[row+1][c-i]
            copy_arr[r+i][c-i:c+i] = copy_arr[r+i][c-i+1:c+i+1]

            for row in range(r+i, r-i, -1):
                copy_arr[row][c+i] = copy_arr[row-1][c+i]
            copy_arr[r-i+1][c+i] = tmp

    for row in copy_arr:
        ans = min(ans, sum(row))

print(ans)