import heapq
def solution(food_times, k):

    if sum(food_times) <= k:
        return -1

    new_food = []
    for i in range(len(food_times)):
        # [음식시간, 순서]
        heapq.heappush(new_food, (food_times[i], i+1))

    all_eating_time = 0
    previous = 0
    length = len(new_food)

    while all_eating_time + ((new_food[0][0] - previous) * length) <= k:
        now = heapq.heappop(new_food)[0]
        all_eating_time += (now - previous) * length
        length -= 1
        previous = now

    result = sorted(new_food, key = lambda x: x[1])
    return result[(k - all_eating_time) % length][1]


print(solution([3, 1, 2], 5))