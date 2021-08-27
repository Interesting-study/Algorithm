#https://programmers.co.kr/learn/courses/30/lessons/72411
#combinations, counter 사용

from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for c in course:
        temp = []
        # 코스 메뉴 갯수별 오더 조합 체크
        for order in orders:
            comb = combinations(sorted(order), c)
            temp += comb
        counter = Counter(temp)

        if len(counter) != 0 and max(counter.values()) != 1:
            answer += ["".join(f) for f in counter if counter[f] == max(counter.values())]

    return sorted(answer)



print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
#print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
#print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))

"""
            if len(candidate) < 2:
                continue
            else:
                if candidate not in course_menu.keys():
                    course_menu[candidate] = 0
                elif course_menu[candidate] >= 0:
                    course_menu[candidate] += 1
                    print(course_menu)
        print("\n\n")
"""