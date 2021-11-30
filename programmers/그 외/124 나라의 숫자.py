#https://programmers.co.kr/learn/courses/30/lessons/12899
def solution(n):
    answer = ''
    while n:
        if n % 3:
            answer += str(n % 3)
            n //= 3
        else:
            answer += "4"
            n = n//3 - 1
    return answer[::-1]


print(solution(1))
print(solution(2))
print(solution(3))
print(solution(4))