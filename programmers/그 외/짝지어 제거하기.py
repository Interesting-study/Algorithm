#https://programmers.co.kr/learn/courses/30/lessons/12973
def solution(s):
    s_len = len(s)
    stack = []

    for i in range(s_len):
        if not stack:
            stack.append(s[i])
        else:
            if s[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(s[i])

    return 1 if not stack else 0

print(solution('baabaa'))
print(solution('cdcd'))