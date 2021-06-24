import itertools

n, m = map(int, input().split())
balls = list(map(int, input().split()))
new_balls = {}
answer = 0

for i in range(n):
    new_balls[i+1] = balls[i]

ball_nCr = list(itertools.combinations(new_balls.keys(), 2))


for ball in ball_nCr:
    if balls[ball[0] - 1] == balls[ball[1] - 1]:
        continue
    answer += 1

print(answer)