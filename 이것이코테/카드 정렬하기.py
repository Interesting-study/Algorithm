import heapq

n = int(input())
cards = []

for _ in range(n):
    data = int(input())
    heapq.heappush(cards, data)

result = 0

while len(cards) != 1:
    card1 = heapq.heappop(cards)
    card2 = heapq.heappop(cards)

    sum_cards = card1 + card2
    result += sum_cards
    heapq.heappush(cards, sum_cards)

print(result)