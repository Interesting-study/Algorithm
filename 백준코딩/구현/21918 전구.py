n, m = map(int, input().split())
status = list(map(int, input().split()))

for _ in range(m):
    a, b, c = map(int, input().split())

    if a == 1:
        status[b-1] = c
    elif a == 2:
        for i in range(b-1, c):
            status[i] = (status[i] + 1) % 2
    else:
        status[b-1:c] = [(a+1) % 2] * (c - b + 1)

print(*status)