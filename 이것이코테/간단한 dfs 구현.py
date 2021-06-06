def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


graph = [
    [], #시작노드
    [2, 3, 8], #최상단 노드 1과 연결된 노드들
    [1, 7], #노드 2와 연결
    [1, 4, 5], #노드 3과 연결
    [3, 5], #노드 4와 연결
    [3, 4], #노드 5와 연결
    [7], #노드 6과 연결
    [2, 6, 8], #노드 7과 연결
    [1, 7] #노드 8과 연결
]

visited = [False] * len(graph)

dfs(graph, 1, visited)
