#https://www.acmicpc.net/problem/2630
n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
result = []

def divide(x, y, n):
    color = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != paper[i][j]:
                divide(x, y, n // 2)
                divide(x, y + n // 2, n // 2)
                divide(x + n // 2, y, n // 2)
                divide(x + n // 2, y + n // 2, n // 2)
                return

    if color == 0:
        result.append(0)
    else:
        result.append(1)

divide(0, 0, n)
print(result.count(0))
print(result.count(1))