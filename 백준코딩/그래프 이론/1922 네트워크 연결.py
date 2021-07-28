def find_parents(parents, x):
    if parents[x] != x:
        parents[x] = find_parents(parents, parents[x])
    return parents[x]

def union_parent(parents, a, b):
    a = find_parents(parents, a)
    b = find_parents(parents, b)

    if a < b:
        parents[b] = a
    else:
        parents[a] = b

n = int(input())
m = int(input())
parents = [0] * (n+1)

edges = []
result = 0

for i in range(1, n+1):
    parents[i] = i

for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parents(parents, a) != find_parents(parents, b):
        union_parent(parents, a, b)
        result += cost

print(result)