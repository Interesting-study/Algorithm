#https://programmers.co.kr/learn/courses/30/lessons/43164
from collections import defaultdict

def solution(tickets):
    def dfs():
        stack = ['ICN']
        answer = []

        while stack:
            now = stack[-1]

            if now not in routes or len(routes[now]) == 0:
                answer.append(stack.pop())
            else:
                stack.append(routes[now][-1])
                routes[now].pop()

        return answer[::-1]

    routes = defaultdict(list)

    for key, value in tickets:
        routes[key].append(value)

    for r in routes:
        routes[r].sort(reverse=True)

    return dfs()


print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))