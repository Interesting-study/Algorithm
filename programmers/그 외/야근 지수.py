import heapq

def solution(works, n):
    if sum(works) <= n:
        return 0

    answer = 0
    q = []
    for w in works:
        heapq.heappush(q, -w)

    for _ in range(n):
        now = heapq.heappop(q)
        if now == 0:
            continue
        heapq.heappush(q, now+1)

    for v in q:
        answer += (v**2)

    return answer

print(solution([4, 3, 3], 4))
print(solution([2, 1, 2], 1))
print(solution([1, 1], 3))