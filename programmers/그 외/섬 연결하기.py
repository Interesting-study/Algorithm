#https://programmers.co.kr/learn/courses/30/lessons/42861
import heapq

def solution(n, costs):
    answer = 0
    INF = int(1e9)
    distance = [INF] * (n+1)

    def dijkstra(start):
        q = []
        heapq.heappush(q, (0, start))
        distance[start] = 0

        while q:
            dist, now = heapq.heappop(q)


    return answer

print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]	))