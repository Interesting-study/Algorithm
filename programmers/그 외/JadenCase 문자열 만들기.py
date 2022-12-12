def solution(s):
    new_s = s.split(" ")
    answer = []

    for w in new_s:
        if w == "":
            answer.append(w)
        else:
            answer.append(w.capitalize())

    return ' '.join(answer)

print(solution("3people unFollowed me"))
print(solution("for the last week"))
print(solution("for    the last week"))