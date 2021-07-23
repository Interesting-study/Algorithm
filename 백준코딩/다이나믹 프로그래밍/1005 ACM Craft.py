#https://www.acmicpc.net/problem/1005

T = int(input())

n, k = map(int, input().split())
building = list(map(int, input().split()))

indegree = [[] for i in range(n+1)]

for _ in range(n):
    pass