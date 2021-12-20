#https://programmers.co.kr/learn/courses/30/lessons/42747
from bisect import bisect_left
def solution(citations):
    citations.sort()
    start, end = citations[0], citations[-1]
    length = len(citations)
    answer = 0

    for h_index in range(end+1):
        left = bisect_left(citations, h_index)
        right = length - left
        if left <= h_index <= right:
            answer = max(h_index, answer)

    return answer


print(solution([3, 0, 6, 1, 5]))

'''
h가 0일때 : 이상, 이하는 5, 0
h가 1일때 : 이상, 이하는 4, 1
h가 2일때 : 이상, 이하는 3, 2
h가 3일때 : 이상, 이하는 3, 2
'''