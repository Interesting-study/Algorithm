from collections import deque

def get_divisors(num):
    result = []
    reverse_result = []

    for i in range(1, int(num ** 0.5) + 1):

        if num % i == 0:
            result.append(i)
            if i != (num//i):
                reverse_result.append(num // i)

    return result + reverse_result[::-1]

def solution(brown, yellow):
    answer = []
    total_area = brown + yellow

    candidate = deque(get_divisors(total_area))

    while candidate:
        if len(candidate) == 1:
            width = height = candidate.pop()
        else:
            width, height = candidate.popleft(), candidate.pop()

        if (((2 * width) + (2 * height) - 4) == brown) and (((width -2) * (height - 2)) == yellow):
            return [height, width]

        if (((2 * height) + (2 * width) - 4) == brown) and (((height -2) * (width - 2)) == yellow):
            return [width, height]


print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))
