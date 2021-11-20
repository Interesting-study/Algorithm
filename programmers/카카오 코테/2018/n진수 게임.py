#https://programmers.co.kr/learn/courses/30/lessons/17687?language=python3
import string
def solution(n, t, m, p):
    num_in_dict = {i:i for i in range(10)}

    for i in range(10, 17):
        num_in_dict[i] = string.ascii_uppercase[i-10]

    print(num_in_dict)

    answer = ''
    return answer

print(solution(2, 4, 2, 1))
print(solution(16, 16, 2, 1))
print(solution(16, 16, 2, 2))