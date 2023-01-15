from bisect import bisect_right, bisect_left

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
wanted = list(map(int, input().split()))
answer = []

cards.sort()

for val in wanted:
    left = bisect_left(cards, val)
    right = bisect_right(cards, val)

    answer.append(right - left)

print(*answer)