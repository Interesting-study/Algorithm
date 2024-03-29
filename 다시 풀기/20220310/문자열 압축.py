def solution(s):
    answer = len(s)

    for step in range(1, (len(s)//2) + 1):
        count = 1
        prev = s[0:step]
        compressed = ""

        for i in range(step, len(s), step):
            if prev == s[i:i+step]:
                count += 1
            else:
                compressed += (str(count) + prev) if count >= 2 else prev
                prev = s[i:i+step]
                count = 1

        compressed += str(count) + prev if count >= 2 else prev
        answer = min(answer, len(compressed))

    return answer

print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))