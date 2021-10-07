# https://programmers.co.kr/learn/courses/30/lessons/77484
def solution(lottos, win_nums):
    answer = []

    rate_in_hits = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}

    cnt_common_nums = len(set(lottos) & set(win_nums))
    cnt_painting = lottos.count(0)

    answer.append(rate_in_hits[cnt_common_nums + cnt_painting])
    answer.append(rate_in_hits[cnt_common_nums])

    return answer