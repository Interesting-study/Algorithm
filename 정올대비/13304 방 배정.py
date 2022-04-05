#https://www.acmicpc.net/problem/13304
n, k = map(int, input().split())

rooms = [0, 0, 0, 0, 0]
ans = 0

for _ in range(n):
    gender, grade = map(int, input().split())

    if 1 <= grade <= 2:
        rooms_idx = 0
    elif 3 <= grade <= 4 and gender:
        rooms_idx = 1
    elif 3 <= grade <= 4 and not gender:
        rooms_idx = 2
    elif 5 <= grade <= 6 and gender:
        rooms_idx = 3
    else:
        rooms_idx = 4

    rooms[rooms_idx] += 1

    if rooms[rooms_idx] == 1:
        ans += 1
    if rooms[rooms_idx] == k:
        rooms[rooms_idx] = 0

print(ans)