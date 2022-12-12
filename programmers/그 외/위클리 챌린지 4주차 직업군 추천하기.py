#https://programmers.co.kr/learn/courses/30/lessons/84325
from collections import defaultdict
import heapq


def solution(table, languages, preference):
    job_in_score = defaultdict(dict)
    job_in_langs = defaultdict(list)
    langs_in_prefer = defaultdict(int)
    answer = []

    langs_len = len(languages)

    for t in table:
        new_t = t.split()
        job, langs = new_t[0], new_t[1:]

        job_in_score[job] = {langs[idx]: 5 - idx for idx in range(5)}
        job_in_langs[job] = langs

    for i in range(langs_len):
        langs_in_prefer[languages[i]] = preference[i]

    for job in job_in_score.keys():
        score = 0
        for langs in langs_in_prefer.keys():
            if langs in job_in_langs[job]:
                score += job_in_score[job][langs] * langs_in_prefer[langs]
        heapq.heappush(answer, (-score, job))

    return heapq.heappop(answer)[1]