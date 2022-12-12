#https://programmers.co.kr/learn/courses/30/lessons/81302
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(place):
    person = []

    for i in range(5):
        for j in range(5):
            if place[i][j] == "P":
                person.append((i, j))

    for p in person:
        q = deque()
        q.append(p)
        visited = [[False] * 5 for _ in range(5)]
        distance = [[0] * 5 for _ in range(5)]

        while q:
            x, y = q.popleft()
            visited[x][y] = True

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:

                    if place[nx][ny] == 'O':
                        q.append((nx, ny))
                        visited[nx][ny] = True
                        distance[nx][ny] = distance[x][y] + 1

                    #내 상하좌우에 사람이 있는데 거리가 1보다 작을때
                    if place[nx][ny] == 'P' and distance[x][y] <= 1:
                        return 0
    return 1


def solution(places):
    answer = []

    for place in places:
        answer.append(bfs(place))

    return answer



print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))