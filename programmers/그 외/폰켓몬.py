#https://programmers.co.kr/learn/courses/30/lessons/1845
def solution(nums):
    length = len(nums)
    kind_of = len(set(nums))
    selected = length // 2

    if kind_of > selected:
        max_kind = selected
    else:
        max_kind = kind_of

    return max_kind


print(solution([3,1,2,3]))
print(solution([3,3,3,2,2,4]))
print(solution([3,3,3,2,2,2]))

