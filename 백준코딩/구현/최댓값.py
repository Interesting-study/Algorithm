import heapq

data = []

for i in range(1, 10):
    heapq.heappush(data, (-int(input()), i))

result = heapq.heappop(data)
print(-result[0])
print(result[1])