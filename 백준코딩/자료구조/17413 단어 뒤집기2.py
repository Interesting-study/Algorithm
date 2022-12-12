#https://www.acmicpc.net/problem/17413
import sys
s = list(sys.stdin.readline().rstrip())
start = 0
idx = 0
length = len(s)

while idx < length:
    if s[idx] == "<":
        idx += 1
        while s[idx] != ">":
            idx += 1
        idx += 1

    elif s[idx].isalnum():
        start = idx

        while idx < length and s[idx].isalnum():
            idx += 1
        temp = s[start:idx]
        temp.reverse()
        s[start:idx] = temp
    else:
        idx += 1

print("".join(s))
