#https://www.acmicpc.net/problem/22860
import sys
from collections import defaultdict
sys.setrecursionlimit(10**8)

file_sys = defaultdict(list)

def search(target):
    if target not in file_sys:
        return

    for title, val in file_sys[target]:
        if val == 0:
            file_set[title] += 1
        else:
            search(title)


n, m = map(int, input().split())

for _ in range(n+m):
    parent, child, code = input().split()
    file_sys[parent].append((child, int(code)))

for _ in range(int(input())):
    query = input().split('/')
    file_set = defaultdict(int)
    search(query[-1])
    print(len(file_set), sum(file_set.values()))

