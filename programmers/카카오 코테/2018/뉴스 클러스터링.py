#https://programmers.co.kr/learn/courses/30/lessons/17677
from collections import Counter, defaultdict
from math import floor

def solution(str1, str2):
    answer = 65536

    str1 = str1.lower()
    str2 = str2.lower()

    new_str1 = []
    new_str2 = []

    for i in range(len(str1)-1):
        keyword = str1[i:i+2]
        if keyword.isalpha():
            new_str1.append(keyword)

    for i in range(len(str2)-1):
        keyword = str2[i:i+2]
        if keyword.isalpha():
            new_str2.append(keyword)

    if not new_str1 and not new_str2:
        return answer

    new_str1_cnt = Counter(new_str1)
    new_str2_cnt = Counter(new_str2)

    intersect = defaultdict(int)
    union = defaultdict(int)

    all_keys = list(set(new_str1 + new_str2))

    for key in all_keys:
        if key in new_str1_cnt.keys() and key in new_str2_cnt.keys():
            intersect[key] = min(new_str1_cnt[key], new_str2_cnt[key])
            union[key] = max(new_str1_cnt[key], new_str2_cnt[key])
        elif key in new_str1_cnt.keys() and key not in new_str2_cnt.keys():
            union[key] = new_str1_cnt[key]
        elif key not in new_str1_cnt.keys() and key in new_str2_cnt.keys():
            union[key] = new_str2_cnt[key]

    jacquard = sum(intersect.values()) / sum(union.values())
    answer = floor(answer * jacquard)

    return answer

print(solution("FRANCE", "french"))
print(solution("handshake",	"shake hands"))
print(solution("aa1+aa2", "AAAA12"))
print(solution("E=M*C^2", "e=m*c^2"))