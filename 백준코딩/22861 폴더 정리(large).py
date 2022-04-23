#https://www.acmicpc.net/problem/22861
import sys
from collections import defaultdict
sys.setrecursionlimit(10**8)

file_sys = defaultdict(set)
file_info = defaultdict(int)

file_info['main'] = 1

def search(target):

    if target not in file_sys:
        return

    for title in file_sys[target]:
        if file_info[title] == '1':
            search(title)
        elif file_info[title] == '0':
            file_set[title] += 1

n, m = map(int, input().split())

for _ in range(n+m):
    parent, child, code = input().split()
    file_sys[parent].add(child)
    file_info[child] = code

route = []
moving = set()

for _ in range(int(input())):
    route = []
    for val in input().split():
        route.append(val.split('/'))

    if route[0][-1] in file_sys:
        for val in file_sys[route[0][-1]]:
            file_sys[route[1][-1]].add(val)

        for val in file_sys.values():
            if route[0][-1] in val:
                val.remove(route[0][-1])

for _ in range(int(input())):
    query = input().split('/')
    file_set = defaultdict(int)
    search(query[-1])
    print(len(file_set), sum(file_set.values()))

'''
3 6
main FolderA 1
main FolderB 1
FolderA File1 0
FolderA File2 0
FolderB FolderC 1
FolderC File4 0
FolderC File5 0
FolderB File1 0
FolderB File3 0
1
main/FolderB main/FolderA
1
main
main/FolderA
main/FolderA/FolderC
'''