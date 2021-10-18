#https://www.acmicpc.net/problem/12100
from copy import deepcopy
INF = int(-1e9)

n = int(input())
board = [list(map(int, input().split()))for _ in range(n)]

def get_max_block():
    max_value = INF

    for idx in range(n):
        max_value = max(max_value, max(board[idx]))

    return max_value

now_max = get_max_block()

print(now_max)