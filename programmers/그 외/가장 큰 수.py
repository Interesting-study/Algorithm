def solution(numbers):
    numbers = list(map(str, numbers))
    answer = sorted(numbers, key = lambda x: x*3, reverse = True) 
    #왜 3이냐면, 1000이하니까
    print(answer)
    return str(int(''.join(answer)))

#https://programmers.co.kr/learn/courses/30/lessons/42746
