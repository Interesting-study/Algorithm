#https://www.acmicpc.net/problem/1036
import string
from collections import Counter

def convert(num):
    q, r = divmod(num, 36)
    base_str = string.digits + string.ascii_uppercase

    if q == 0:
        return base_str[r]
    else:
        return convert(q) + base_str[r]

def solution(n, nums, k):
    nums_counter = Counter({})
    for i in range(n):
        nums_counter += Counter(nums[i])

    nums_counter = dict(sorted(nums_counter.items(), key= lambda x: (-x[1], x[0])))
    print(nums_counter)


if __name__ == '__main__':
    n = int(input())
    nums = [input() for _ in range(n)]
    k = int(input())

    print(solution(n, nums, k))