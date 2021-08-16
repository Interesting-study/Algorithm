n, m = map(int, input().split())
floor = [list(input()) for _ in range(n)]

cnt = 0

#"-" 바닥장식 체크, 행채크
for i in range(n):
    pre = "/"
    for j in range(m):
        if floor[i][j] == "-":
            if floor[i][j] != pre : cnt += 1
        pre = floor[i][j]

#"|" 바닥장식체크, 열체크
for j in range(m):
    pre = "/"
    for i in range(n):
        if floor[i][j] == "|":
            if floor[i][j] != pre: cnt += 1
        pre = floor[i][j]

print(cnt)