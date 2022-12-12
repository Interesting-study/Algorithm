def check(i, j, visitied):
    for idx in range(4):
        ni = i + dr[idx]
        nj = j + dc[idx]

        if (ni, nj) in visitied:
            return False

    return True

def dfs(visited, cost):
    global answer

    if cost >= answer:
        return

    if len(visited) == 15:
        answer = min(answer, cost)
    else:
        for i in range(1, n-1):
            for j in range(1, n-1):
                if check(i, j, visited) and (i, j) not in visited:
                    temp_cord = [(i, j)]
                    temp_cost = board[i][j]

                    for idx in range(4):
                        ni = i + dr[idx]
                        nj = j + dc[idx]

                        temp_cost += board[ni][nj]
                        temp_cord.append((ni, nj))

                    dfs(visited + temp_cord, cost + temp_cost)

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
answer = float("inf")

dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

dfs([], 0)
print(answer)