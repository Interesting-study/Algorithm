#https://www.acmicpc.net/problem/5549
#input만 sys로

m, n = map(int, input().split())
k = int(input())
map_info = [list(input()) for _ in range(m)]

jungle = [[0] * (n+1) for _ in range(m+1)]
ocean = [[0] * (n+1) for _ in range(m+1)]
ice = [[0] * (n+1) for _ in range(m+1)]

for i in range(1, m+1):
    for j in range(1, n+1):
        now = map_info[i-1][j-1]

        if now == 'J':
            jungle[i][j] += 1

        if now == 'O':
            ocean[i][j] += 1
        if now == 'I':
            ice[i][j] += 1

        jungle[i][j] = jungle[i][j-1] + jungle[i-1][j] - jungle[i-1][j-1] + jungle[i][j]
        ocean[i][j] = ocean[i][j - 1] + ocean[i - 1][j] - ocean[i - 1][j - 1] + ocean[i][j]
        ice[i][j] = ice[i][j - 1] + ice[i - 1][j] - ice[i - 1][j - 1] + ice[i][j]

for _ in range(k):
    r1, c1, r2, c2 = map(int, input().split())
    print(jungle[r2][c2] - jungle[r2][c1-1] - jungle[r1-1][c2] + jungle[r1-1][c1-1], end=' ')
    print(ocean[r2][c2] - ocean[r2][c1 - 1] - ocean[r1 - 1][c2] + ocean[r1 - 1][c1 - 1], end=' ')
    print(ice[r2][c2] - ice[r2][c1 - 1] - ice[r1 - 1][c2] + ice[r1 - 1][c1 - 1])

'''
4 7
4
JIOJOIJ
IOJOIJO
JOIJOOI
OOJJIJO
3 5 4 7
2 2 3 6
2 2 2 2
1 1 4 7
'''