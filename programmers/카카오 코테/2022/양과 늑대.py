#https://programmers.co.kr/learn/courses/30/lessons/92343
import sys
sys.setrecursionlimit(10**6)
answer = 1

def solution(info, edges):
    global answer
    global visited
    info_len = len(info)
    graph = [[] for _ in range(info_len)]

    for edge in edges:
        parent, child = edge[0], edge[1]
        graph[parent].append(child)
        graph[child].append(parent)

    visited = [False] * info_len

    def dfs(node, sheep, wolf, visited, node_set):
        global answer
        sheep += info[node] ^ 1
        wolf += info[node]
        print("노드 양 늑대 : ", node, sheep, wolf)

        if wolf >= sheep:
            return

        if answer < sheep:
            answer = sheep

        next_visited = visited[:]
        next_visited[node] = True

        for next_node in node_set:
            if not next_visited[next_node]:
                next_node_set = node_set | set(graph[next_node])
                dfs(next_node, sheep, wolf, next_visited, next_node_set)
        return answer

    return 'answer = ' + str(dfs(0, 0, 0, visited, set(graph[0]))) + '\n'



print(solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))
#print(solution([0,1,0,1,1,0,1,0,0,1,0], [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]))