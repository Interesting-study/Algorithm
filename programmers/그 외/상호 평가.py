def get_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 50:
        return 'D'
    else:
        return 'F'

def solution(scores):
    #2차원 배열 뒤집기
    scores = list(map(list, zip(*scores)))

    for i in range(len(scores)):
        for j in range(len(scores[i])):
            if i == j:
                mine = scores[i][j]
                if scores[i].count(mine) == 1 and (mine == max(scores[i]) or mine == min(scores[i])):
                    scores[i].remove(mine)
            else:
                continue

    avg = [sum(scores[i]) / len(scores[i]) for i in range(len(scores))]
    answer = [get_grade(avg[i]) for i in range(len(avg))]

    return ''.join(answer)


print(solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]))
print(solution([[50,90],[50,87]]))
print(solution([[70,49,90],[68,50,38],[73,31,100]]))