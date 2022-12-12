a, b = map(int, input().split())
answer = 0
origin = 0

if (a < 0 and b > 0) or (a > 0 and b < 0):
    answer = abs(a - origin) + abs(b - origin)
else:
    answer = abs(a - b)

print(answer)
