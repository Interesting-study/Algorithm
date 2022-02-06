import itertools
import bisect

def solution(board, skill):
    width = len(board[0])
    height = len(board)

    durability = [[0 for _ in range(width+1)] for _ in range(height+1)]

    for sk in skill:
        r1, c1, r2, c2 = sk[1], sk[2], sk[3], sk[4]
        if sk[0] == 1:
            degree = -sk[-1]
        else:
            degree = sk[-1]

        durability[r1][c1] += degree
        durability[r1][c2+1] += -degree
        durability[r2+1][c1] += -degree
        durability[r2+1][c2+1] += degree

    #위에서 아래로 누적합
    for idx in range(height):
        accum = [i+j for i, j in zip(durability[idx], durability[idx+1])]
        durability[idx+1] = accum

    durability = list(map(list, zip(*durability)))

    #왼쪽에서 아래로 누적합
    for idx in range(width):
        accum = [i+j for i, j in zip(durability[idx], durability[idx+1])]
        durability[idx+1] = accum
    durability = list(map(list, zip(*durability)))

    for idx in range(height):
        accum = [i+j for i, j in zip(durability[idx][:width], board[idx])]
        board[idx] = accum

    board = list(itertools.chain.from_iterable(board))
    board.sort()

    not_destory_idx = bisect.bisect_right(board, 0)

    return (width * height) - not_destory_idx

print(solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]], [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]))
print(solution([[1,2,3],[4,5,6],[7,8,9]], [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]))

'''
2차원 배열에서 (x1,y1)부터 (x2,y2)까지 n만큼의 변화는 (x1,y1)에 +n, (x1,y2+1)에 -n, (x2+1,y1)에 -n, (x2+1,y2+1)에 +n을 한 것과 같습니다.
'''