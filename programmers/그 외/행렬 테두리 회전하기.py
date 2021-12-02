#https://programmers.co.kr/learn/courses/30/lessons/77485
from collections import defaultdict
def get_border(coord, columns):
    x1, y1, x2, y2 = coord[0], coord[1], coord[2], coord[3]
    border = {}

    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            if x1 < i < x2 and y1 < j < y2:
                #print(i, j)
                continue
            num = (i - 1) * columns + j
            border[num] = [i, j]

    return border

def rotate(border):
    pass

def solution(rows, columns, queries):
    answer = []
    board = defaultdict(int)

    for query in queries:
        border = get_border(query, columns)
        print(border)

    return answer

print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))