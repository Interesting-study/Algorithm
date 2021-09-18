#https://programmers.co.kr/learn/courses/30/lessons/72412
from collections import defaultdict
from itertools import combinations
from bisect import bisect_left

def solution(info, query):
    answer = []
    condi_dic = {}
    index = list(range(4))

    for inf in info:
        conditions = inf.split()
        score = int(conditions.pop())

        for i in range(5):
            for combs in list(combinations(index, i)):
                temp = conditions.copy()
                for idx in combs:
                    temp[idx] = "-"
                keys = "".join(temp)
                if keys in condi_dic:
                    condi_dic[keys].append(score)
                else:
                    condi_dic[keys] = [score]

    for value in condi_dic.values():
        value.sort()

    refined_query = [q.replace("and", "").split() for q in query]

    for q in refined_query:
        target = int(q.pop())
        keys = "".join(q)

        if keys in condi_dic:
            scores = condi_dic[keys]

            lower_index = bisect_left(scores, target)
            answer.append(len(scores) - lower_index)
        else:
            answer.append(0)

    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
               ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))