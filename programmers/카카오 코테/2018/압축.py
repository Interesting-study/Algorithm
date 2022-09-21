from string import ascii_uppercase

def solution(msg):
    new_ascii = {ch: idx+1 for idx, ch in enumerate(ascii_uppercase)}
    end_idx = len(ascii_uppercase) + 1
    pressed = ""
    i = 0

    answer = []

    while i < len(msg):
        pressed += msg[i]

        if pressed in new_ascii:
            i += 1
            continue
        else:
            new_ascii[pressed] = end_idx
            end_idx += 1

            answer.append(new_ascii[pressed[:-1]])

            pressed = ''

    answer.append(new_ascii[pressed])

    return answer

print(solution("KAKAO"))
print(solution("TOBEORNOTTOBEORTOBEORNOT"))
print(solution("ABABABABABABABAB"))