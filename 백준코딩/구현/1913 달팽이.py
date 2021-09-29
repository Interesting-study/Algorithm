#https://www.acmicpc.net/problem/1913
n = int(input())
goal = int(input())

now = 1
depth = width = n // 2

table = [[0] * n for _ in range(n)]
table[width][depth] = now

dx = [0, 1, 0, -1] #오른
dy = [1, 0, -1, 0]

next_to = 0
ans = [width+1, depth+1]

while width >= 0 and depth >= 0:
    for i in range(4):
        for _ in range(next_to):
            width += dx[i]
            depth += dy[i]
            now += 1
            table[width][depth] = now

            if now == goal:
                ans = [width+1, depth+1]

    width -= 1
    depth -= 1
    next_to += 2

print("\n\n")

for tb in table:
    print(*tb)

print(*ans)

