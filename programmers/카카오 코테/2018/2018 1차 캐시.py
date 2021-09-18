#https://programmers.co.kr/learn/courses/30/lessons/17680
from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque()

    if cacheSize == 0:
        return 5 * len(cities)

    for city in cities:
        #참조하는 값이 캐시안에 없으면 가장 오래 전에 참조한 값을 빼고 현재 값을 캐시에 넣어준다.
        city = city.lower()
        if city not in cache:
            if len(cache) == cacheSize:
                cache.pop()
            cache.appendleft(city)
            answer += 5
        # 참조하는 값이 캐시안에 있으면 해당 값을 캐시의 가장 최근 위치에 넣어준다.
        else:
            cache.remove(city)
            cache.appendleft(city)
            answer += 1

    return answer


print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
print(solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))
print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
