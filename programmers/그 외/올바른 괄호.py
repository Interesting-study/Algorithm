from collections import deque

def solution(s):
    if s[0] == ')':
        return False

    s = deque(s)
    stack = []

    while s:
        now = s.popleft()

        if not stack:
            stack.append(now)
            continue

        if now == '(':
            stack.append(now)
        elif now == ')':
            stack.pop()

    return not stack

print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))