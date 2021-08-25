#https://programmers.co.kr/learn/courses/30/lessons/72411
from itertools import combinations

def solution(orders, course):
    answer = []
    orders_length = len(orders)
    orders_index = list(range(orders_length))
    course_menu = {}

    for c in course:
        for comb in combinations(orders_index, c):
            check = set(orders[comb[0]])

            for idx in comb[1:]:
                now = set(orders[idx])
                candidate = "".join(sorted(list(check.intersection(now))))

            if candidate not in course_menu.keys() and len(candidate) >= 2:
                course_menu[candidate] = 0

    for o in orders:
        for key in course_menu.keys():
            if key in o:
                course_menu[key] += 1

    print(course_menu)

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))

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