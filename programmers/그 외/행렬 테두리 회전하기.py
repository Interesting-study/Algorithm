#https://programmers.co.kr/learn/courses/30/lessons/77485

def solution(rows, columns, queries):
    answer = []
    board = [[i*columns + (j+1) for j in range(columns)] for i in range(rows)]

    for x1, y1, x2, y2 in queries:
        store = board[x1-1][y1-1]
        min_value = store

        for k in range(x1-1, x2-1):
            next = board[k+1][y1-1]
            board[k][y1-1] = next
            min_value = min(min_value, next)

        for k in range(y1-1, y2-1):
            next = board[x2-1][k+1]
            board[x2-1][k] = next
            min_value = min(min_value, next)

        for k in range(x2-1, x1-1, -1):
            next = board[k-1][y2-1]
            board[k][y2-1] = next
            min_value = min(min_value, next)

        for k in range(y2-1, y1-1, -1):
            next = board[x1-1][k-1]
            board[x1-1][k] = next
            min_value = min(min_value, next)

        board[x1-1][y1] = store
        answer.append(min_value)

    return answer

print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))

'''
rows	columns	queries	result
6	6	[[2,2,5,4],[3,3,6,6],[5,1,6,3]]	[8, 10, 25]
3	3	[[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]	[1, 1, 5, 3]
100	97	[[1,1,100,97]]	[1]
'''