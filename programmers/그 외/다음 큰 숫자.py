def solution(n):
    answer = False
    next_number = ''
    original_one_count = bin(n)[2:].count('1')

    while not answer:
        n += 1

        next_one_count = bin(n)[2:].count('1')

        if original_one_count == next_one_count:
            answer = True

    return n

print(solution(78))
print(solution(15))