#https://programmers.co.kr/learn/courses/30/lessons/42860

def solution(name):
    moving = [min((ord(ch) - ord('A')), (ord('Z') - ord(ch) + 1)) for ch in name]
    cursor, answer = 0, 0
    left_right = len(name) - 1

    for i in range(len(name)):
        answer += moving[i]

        cursor += 1

        while cursor < len(name) and name[cursor] == 'A':
            cursor += 1

        left_right = min(left_right, i + i + len(name) - cursor)

    answer += left_right
    return answer

print(solution("JEROEN"))
print(solution("JAN"))
print(solution("AAAJ"))
print(solution("BAAAJ"))