#https://www.acmicpc.net/problem/11725
import sys
sys.setrecursionlimit(10**9)

n = int(input())
tree = [[] for _ in range(n+1)]
graph = [0 for _ in range(n+1)]

def dfs(start, tree, graph):
    for i in tree[start]:
        if graph[i] == 0:
            graph[i] = start
            dfs(i, tree, graph)

for _ in range(n-1):
    v, i = map(int, input().split())
    tree[v].append(i)
    tree[i].append(v)

dfs(1, tree, graph)

for i in range(2, n+1):
    print(graph[i])

'''
트리의 부모를 찾을 때 양쪽으로 방향 설정 해줄 것
'''