n, m = map(int, input().split())
farms = []

for _ in range(n):
    farms.append(list(map(int, input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

print(farms)