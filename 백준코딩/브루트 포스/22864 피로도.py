#https://www.acmicpc.net/problem/22864
a, b, c, m = map(int, input().split())

fatigue = 0 #피로도
works = 0 #일의 양

if a > m:
    print(0)
else:
    for i in range(1, 25):
        if fatigue + a <= m:
            fatigue += a
            works += b
        else:
            if fatigue - c >= 0:
                fatigue -= c
            else:
                fatigue = 0

    print(works)


