n, m = map(int, input().split())
graph = [list(map(int, list(input()))) for _ in range(n)]
answer = float("-inf")

for i in range(n):
    for j in range(m):
        target = graph[i][j] # 현재 꼭짓점에 쓰여 있는 수
        # 반복문을 통해 j축에 target과 똑같은 수를 확인
        for k in range(j, m):
            # target과 똑같은 수가 있다면 정사각형 위치가 범위 내에 있고 똑같은 수가 있는지 확인
           # print(f"i= {i}, j = {j}, k = {k}, target = {target}, graph[{i}][{k}] = {graph[i][k]}")
            if graph[i][k] == target and i + k - j < n and k < m:
                if graph[i + k - j][j] == target and graph[i + k - j][k] == target:

                    # 정사각형 위치에 모두 똑같은 수가 있다면 길이를 제곱
                    answer = max(answer, (k - j + 1) ** 2)
# 제일 큰 정사각형의 크기를 출력
print(answer)