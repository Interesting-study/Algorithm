n, c = map(int, input().split())
house = [int(input()) for _ in range(n)]
house.sort()

start, end = 1, house[-1] - house[0]
answer = 0

while start <= end:
    mid = (start + end) // 2
    now = house[0]
    count = 1

    for i in range(1, len(house)):
        if house[i] >= now + mid:
            count += 1
            now = house[i]

    if count >= c:
        start = mid + 1
        answer = max(answer, mid)
    else:
        end = mid - 1

print(answer)