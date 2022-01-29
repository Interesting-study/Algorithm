#https://programmers.co.kr/learn/courses/30/lessons/92343
def solution(info, edges):
    answer = 0
    edges_len = len(info) - 1
    graph = [[] for _ in range(edges_len)]
    sheep, wolf = 1, 0

    for i in range(edges_len):
        parent, child = edges[i][0], edges[i][1]
        graph[parent].append(child)

    print(graph)
    return answer

print(solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))
print(solution([0,1,0,1,1,0,1,0,0,1,0], [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]))