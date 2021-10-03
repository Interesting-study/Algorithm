#https://www.acmicpc.net/problem/1022
r1, c1, r2, c2 = map(int, input().split())

width = c2 - c1 + 1
height = r2 - r1 + 1

dx = [0, -1, 1,]
dy = [1, 1, 0, ]

swirl = [[0] * width for _ in range(height)]

print(swirl)

"""
r이 위아래, c가 왼오

 -3 -2 -1  0  1  2  3
    --------------------
-3 |37 36 35 34 33 32 31
-2 |38 17 16 15 14 13 30
-1 |39 18  5  4  3 12 29
 0 |40 19  6  1  2 11 28
 1 |41 20  7  8  9 10 27
 2 |42 21 22 23 24 25 26
 3 |43 44 45 46 47 48 49
"""