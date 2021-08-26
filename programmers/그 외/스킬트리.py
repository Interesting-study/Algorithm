from collections import deque

def solution(skill, skill_trees):
    answer = 0

    for skills in skill_trees:
        skill_list = deque(skill)

        for s in skills:
            if s in skill:
                if s != skill_list.popleft():
                    break
        else:
            answer += 1

    return answer

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))

"""
for - else for문이 끝까지 수행하면 else가 실행됨
"""