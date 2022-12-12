def count_divisor(num: int) -> int:
    cnt = 0

    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            cnt += 1

            if i != (num // i):
                cnt += 1

    return cnt


def solution(left, right):
    answer = 0

    for num in range(left, right + 1):
        if count_divisor(num) % 2 == 0:
            answer += num
        else:
            answer -= num

    return answer


print(solution(13, 17))
print(solution(24, 27))