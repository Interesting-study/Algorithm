#https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=false
from collections import defaultdict

if __name__ == '__main__':
    score_in_name = defaultdict(list)
    for _ in range(int(input())):
        name = input()
        score = float(input())

        score_in_name[score].append(name)

    dest_score = sorted(score_in_name.keys())[1]

    for person in sorted(score_in_name[dest_score]):
        print(person)