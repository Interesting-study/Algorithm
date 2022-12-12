from itertools import combinations

def bfs(cord):
    global answer # funciton 밖에 있는 answer라는 variable의 값을 가져오고 유지할 때 global이라는 키워드를 사용한다
    visited = set() #방문한 꽃을 넣고, 꽃잎이 서로 닿는지 안 닿는지도 확인할 것
    cost = 0 #꽃을 심을 때 생기는 비용

    for r, c in cord: #씨앗의 cordinate
        visited.add((r, c)) #visited = (0, 1) (1,1) (1, 2) (1, 0) (2, 1)
        cost += board[r][c]

        for idx in range(4): #꽃잎의 자리를 visited에 넣는다
            nr = r + dr[idx]
            nc = c + dc[idx]

            if (nr, nc) not in visited: #만약 다른 씨앗의 꽃잎이 예전에 피어난 꽃잎 위에 있다면 이 function을 끝낸다
                visited.add((nr, nc))
                cost += board[nr][nc]
            else:
                return

    answer = min(answer, cost)

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
answer = float("inf")
candidates = [(r, c) for r in range(1, n-1) for c in range(1, n-1)]

dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

for candidate in combinations(candidates, 3):
    bfs(candidate)

print(answer)