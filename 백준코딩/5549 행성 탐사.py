#https://www.acmicpc.net/problem/5549
from copy import deepcopy

m, n = map(int, input().split())
k = int(input())
map_info = [list(input()) for _ in range(m)]

jungle = [[0] * (n+1) for _ in range(m+1)]
ocean = deepcopy(jungle)
ice = deepcopy(jungle)

for i in range(1, m+1):
    for j in range(1, n+1):
        now = map_info[i-1][j-1]

        if now == 'J':
            jungle[i][j] += 1
        elif now == 'O':
            ocean[i][j] += 1

'''
4 7
4
JIOJOIJ
IOJOIJO
JOIJOOI
OOJJIJO
3 5 4 7
2 2 3 6
2 2 2 2
1 1 4 7
'''