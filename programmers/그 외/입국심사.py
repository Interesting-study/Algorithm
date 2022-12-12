#https://programmers.co.kr/learn/courses/30/lessons/43238
#범위와 기준을 뭐로 할 것인지
def solution(n, times):
    answer = 0
    left, right = 1, max(times) * n

    while left <= right:
        complete = 0
        mid = (left + right) // 2

        for time in times:
            complete += mid // time

            if complete >= n:
                break

        if complete >= n:
            answer = mid
            right = mid - 1

        elif complete < n:
            left = mid + 1



    return answer

print(solution(6, [7, 10]))