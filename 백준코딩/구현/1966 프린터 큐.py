from collections import deque

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    prior = deque(list(map(int, input().split())))
    doc_idx = deque(list(range(n)))

    cnt = 0
    while prior:
        if prior[0] == max(prior):
            cnt += 1
            prior.popleft()
            if doc_idx.popleft() == m:
                 print(cnt)
        else:
            prior.append(prior.popleft())
            doc_idx.append(doc_idx.popleft())
