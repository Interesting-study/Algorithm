from collections import deque
#각 징검다리마다 앞으로 가거나, 뒤로 갈 경우 도달할 수 있는 징검다리의 번호를 체크한다.
#앞, 뒤 노드별 이동거리까지 모두 고려해야함
def bfs(a, b):
    q = deque()
    q.append(a-1)
    check = [-1]*N
    check[a-1] = 0
    while q:
        node = q.popleft()
        for n in range(node, N, bridge[node]):
            if check[n] == -1:
                q.append(n)
                check[n] = check[node] + 1
                if n == b-1:
                    return check[n]
        for n in range(node, -1, -bridge[node]):
            if check[n] == -1:
                q.append(n)
                check[n] = check[node] + 1
                if n == b-1:
                    return check[n]
    return -1

N = int(input())
bridge = list(map(int, input().split()))
a, b = map(int, input().split())
print(bfs(a, b))



