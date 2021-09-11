#https://programmers.co.kr/learn/courses/30/lessons/43236
INF = int(1e10)

def solution(distance, rocks, n):
    #도착지점까지 추가
    rocks.sort()
    rocks.append(distance)
    answer = 0

    left, right = 0, distance

    while left <= right:
        mid = (left + right) // 2
        min_dist = INF
        now = 0
        remove_cnt = 0

        for rock in rocks:
            diff = rock - now
            if diff < mid:
                remove_cnt += 1
            else:
                now = rock
                min_dist = min(min_dist, diff)

        if remove_cnt > n:
            right = mid - 1
        else:
            answer = min_dist
            left = mid + 1

    return answer

print(solution(25, [2, 14, 11, 21, 17], 2))
