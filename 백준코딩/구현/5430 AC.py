#https://www.acmicpc.net/problem/5430
from collections import deque

T = int(input())

for _ in range(T):
    p = input()
    n = int(input())
    nums = deque(input()[1:-1].split(','))

    if n == 0:
        nums = deque()

    is_reverse = False

    for cmd in p:
        if cmd == 'R':
            is_reverse = not is_reverse
            continue

        if len(nums) < 1:
            print('error')
            break

        if is_reverse:
            nums.pop()
        else:
            nums.popleft()

    else:
        if is_reverse:
            nums.reverse()

        answer = '[' + ','.join(nums) + ']'
        print(answer)


