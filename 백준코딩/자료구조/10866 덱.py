# https://www.acmicpc.net/problem/10866
import sys
from collections import deque

n = int(sys.stdin.readline())
q = deque()

for _ in range(n):
    cmd = sys.stdin.readline().split()

    if cmd[0] == "push_front":
        q.appendleft(cmd[1])

    elif cmd[0] == "push_back":
        q.append(cmd[1])

    elif cmd[0] == "pop_front":

        if not q:
            print(-1)
        else:
            print(q.popleft())

    elif cmd[0] == "pop_back":

        if not q:
            print(-1)
        else:
            print(q.pop())

    elif cmd[0] == "size":
        print(len(q))
    elif cmd[0] == "empty":

        if not q:
            print(1)
        else:
            print(0)

    elif cmd[0] == "front":
        if not q:
            print(-1)
        else:
            print(q[0])

    elif cmd[0] == "back":
        if not q:
            print(-1)
        else:
            print(q[-1])
