#조합으로 벽 3개 만들고 안전영역 계산
n, m = map(int, input().split())
lab = []
last_lab = [[0] * m for _ in range(n)]

for _ in range(n):
    lab.append(list(map(int, input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

result = 0

def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if last_lab[nx][ny] == 0:
                last_lab = 2
                virus(nx, ny)

def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if last_lab[i][j] == 0:
                score += 1

def dfs(count):
    global result

    if count == 3:
        for i in range(n):
            for j in range(m):
                last_lab[i][j] = lab[i][j]

        for i in range(n):
            for j in range(m):
                if last_lab[i][j] == 2:
                    virus(i, j)
        result = max(result, get_score())
        return

    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0:
                lab[i][j] = 1
                count += 1
                dfs(count)
                lab[i][j] = 0
                count -= 1

dfs(0)
print(result)