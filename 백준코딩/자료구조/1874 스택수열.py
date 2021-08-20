#https://www.acmicpc.net/problem/1874
from collections import deque

n = int(input())
stack = []
wanted = deque([int(input()) for _ in range(n)])
answer = []
cnt = 1
flag = True

for _ in range(n):
    now = wanted.popleft()

    while cnt <= now:
        answer.append("+")
        stack.append(cnt)
        cnt += 1


    if stack[-1] == now:
        stack.pop()
        answer.append("-")
    else:
        print("NO")
        break
else:
    for i in answer:
        print(i)

