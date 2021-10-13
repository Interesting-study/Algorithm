#https://www.acmicpc.net/problem/22994
INF = int(1e9)
ni, mj = map(int, input().split())
pixels = [list(input()) for _ in range(ni)]
reverse_pixels = list(map(list, zip(*pixels)))

i_cnt = 1001
j_cnt = 1001

for i in range(ni):
    now = pixels[i][0]
    cnt = 1
    for j in range(1, mj):
        if now == pixels[i][j]:
            cnt += 1
        else:
            j_cnt = min(j_cnt, cnt)
            cnt = 1
            now = pixels[i][j]

if j_cnt == 1001:
    j_cnt = mj

if mj % j_cnt != 0:
    j_cnt = 1

for i in range(mj):
    now = reverse_pixels[i][0]
    cnt = 1

    for j in range(1, ni):
        if now == reverse_pixels[i][j]:
            cnt += 1
        else:
            i_cnt = min(i_cnt, cnt)
            cnt = 1
            now = reverse_pixels[i][j]

if i_cnt == 1001:
    i_cnt = ni

if ni % i_cnt != 0:
    i_cnt = 1

print(ni // i_cnt, mj // j_cnt, sep=" ")
for i in range(0, ni, i_cnt):
    for j in range(0, mj, j_cnt):
        print(pixels[i][j], end='')
    print()


