#https://programmers.co.kr/learn/courses/30/lessons/67258
from collections import defaultdict

def solution(gems):
    answer = []
    section_len = len(gems) + 1  # 구간의 길이의 초기값은 gems의 길이

    start, end = 0,  0

    contained_gem = defaultdict(int) # 현재 보유중인 보석, 종류 : 갯수
    number_of_gemTypes = len(set(gems)) # 보석의 총 종류수


    while end < len(gems): # end가 gems의 길이보다 작아야 함
        contained_gem[gems[end]] += 1
        end += 1

        if len(contained_gem) == number_of_gemTypes:
            while start < end:
                if contained_gem[gems[start]] > 1:
                    contained_gem[gems[start]] -= 1
                    start += 1
                elif section_len > end - start:
                    section_len = end - start
                    answer = [start+1, end]
                else:
                    break

    return answer

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"],))

'''
적어도 1개 이상을 포함하는, 가장 짧은 구간이라는 말을 체크했어야 함
'''