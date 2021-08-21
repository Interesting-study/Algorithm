#https://www.acmicpc.net/problem/1406
#append, pop만 이용해서 O(1)로 해결해야함
import sys

code = list(input())
stack = []
m = int(input())

for _ in range(m):
    cmd = sys.stdin.readline().strip().split()

    if cmd[0] == 'P':
        code.append(cmd[1])
    elif cmd[0] == 'L' and code != []:
        stack.append(code.pop())
    elif cmd[0] == 'D' and stack != []:
        code.append(stack.pop())
    elif cmd[0] == "B" and code != []:
        code.pop()

print("".join(code + stack[::-1]))