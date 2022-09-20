def solution(s):
    check = set()
    answer = []

    s = s[2:-2]
    s = s.split('},{')

    s.sort(key=len)

    for i in s:
        new_i = i.split(',')
        for j in new_i:
            if int(j) not in check:
                check.add(int(j))
                answer.append(int(j))

    return answer