import sys
from bisect import bisect_left

n, m = map(int, sys.stdin.readline().split())
name_limit = list(map(list, zip(*[sys.stdin.readline().split() for _ in range(n)])))
name_limit[1] = list(map(int, name_limit[1]))

for _ in range(m):
    strength = int(sys.stdin.readline())
    #print('{} : {}'.format(strength, bisect_left(name_limit[1], strength)))
    print(name_limit[0][bisect_left(name_limit[1], strength)])