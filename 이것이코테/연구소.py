#조합으로 벽 3개 만들고 안전영역 계산
import itertools

n, m = map(int, input().split())
lab = []

for _ in range(n):
    lab.append(list(map(int, input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def virus(x, y):
    pass

