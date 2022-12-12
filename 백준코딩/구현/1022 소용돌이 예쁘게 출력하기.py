#https://www.acmicpc.net/problem/1022
r1, c1, r2, c2 = map(int, input().split())

width = c2 - c1 + 1
height = r2 - r1 + 1

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

swirl = [[0] * width for _ in range(height)]
number_of_board = width * height

x = y = 0
num = 1
cnt = 0
dir_cnt = 1
dir = 0

while number_of_board > 0:
    if r1 <= y <= r2 and c1 <= x <= c2:
        number_of_board -= 1
        swirl[y - r1][x - c1] = num
        max_num = num

    num += 1
    cnt += 1

    y += dy[dir]
    x += dx[dir]

    if cnt == dir_cnt:
        cnt = 0
        dir = (dir + 1) % 4

        #다음이 오른쪽이나 왼쪽으로 꺾을때마다 들어가야할 숫자가 하나씩 늘어난다
        if dir == 0 or dir == 2:
            dir_cnt += 1

max_num_len = len(str(max_num))
for i in range(height):
    for j in range(width):
        print(str(swirl[i][j]).rjust(max_num_len), end=" ")
    print()