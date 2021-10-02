#https://www.acmicpc.net/problem/15591
from collections import defaultdict, deque
import sys

def count_related(k, v):
    q = deque()
    q.append((v, int(1e9)))
    cnt = 0
    visited = [False] * (N+1)

    while q:
        cv, c_usado = q.popleft()

        if not visited[cv] and c_usado >= k:
            visited[cv] = True
            q.extend(videos[cv])

    cnt = visited.count(True)
    return cnt - 1

N, Q = map(int, sys.stdin.readline().split())
videos = defaultdict(list)

for _ in range(N-1):
    p, q, r = map(int, sys.stdin.readline().split())
    videos[p].append((q, r))
    videos[q].append((p, r))

for _ in range(Q):
    #k가 유사도, v는 비디오 번호
    k, v = map(int, sys.stdin.readline().split())
    print(count_related(k, v))