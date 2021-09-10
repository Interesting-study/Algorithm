#https://programmers.co.kr/learn/courses/30/lessons/42885
def solution(people, limit):
    people.sort()
    answer = len(people)

    left, right = 0, len(people) - 1

    while left < right:
        if people[left] + people[right] <= limit:
            left += 1
            answer -= 1
        right -= 1

    return answer

print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))
print(solution([10, 20, 80, 90], 100))