#https://www.acmicpc.net/problem/1992

n = int(input())
videos = [list(map(int, list(input()))) for _ in range(n)]
answer = []

def compress(x, y, n):
    now = videos[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if now != videos[i][j]:
                answer.append('(')
                compress(x, y, n //2)
                compress(x, y+n//2, n//2)
                compress(x+n//2, y, n//2)
                compress(x+n//2, y+n//2, n//2)
                answer.append(')')
                return

    answer.append(str(now))

compress(0, 0, n)
print(''.join(answer))
'''
8
11110000
11110000
00011100
00011100
11110000
11110000
11110011
11110011
'''