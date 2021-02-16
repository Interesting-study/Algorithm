def solution(clothes):
    cloth = {}
    for name, kind in clothes:
        if kind in cloth:
            cloth[kind] += 1
        else:
            cloth[kind] = 1
    print(cloth)
    answer = 1
    for i in cloth.values():
        answer *= (i+1)
        
    return answer - 1

#https://programmers.co.kr/learn/courses/30/lessons/42578
