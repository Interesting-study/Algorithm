from collections import deque

def get_next_pos(pos, board):
    next_pos = []
    pos = list(pos)
    
    x1, x2, y1, y2 = pos[0][0], pos[1][0], pos[0][1],  pos[1][1]
    
    #상하좌우 이동
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for i in range(4):
        next_x1, next_x2, next_y1, next_y2 = x1 + dx[i], x2 + dx[i], y1 + dy[i], y2 + dy[i]
        
        #상하좌우 중 비어있으면 무조건 이동
        if board[next_x1][next_y1] == 0 and board[next_x2][next_y2] == 0:
            next_pos.append( { (next_x1, next_y1) ,  (next_x2, next_y2) } )
            
    if x1 == x2:
        for i in [-1, 1]:
            if board[x1 + i][y1] == 0 and board[x2 + i][y2] == 0:
                next_pos.append( { (x1, y1), (x1 + i, y1) } )
                next_pos.append( { (x2, y2), (x2 + i, y2) } )
    elif y1 == y2:
        for i in [-1, 1]:
            if board[x1][y1 + i] == 0 and board[x2][y2 + i] == 0:
                next_pos.append( { (x1, y1), (x1, y1 + i) } )
                next_pos.append( { (x2, y2), (x2, y1 + i) } )

    return next_pos
    
def solution(board):
    
    #NxN에서 N구하기 (좌표를 0부터 N)
    n = len(board)   
    
    # 벽 만들기
    wall_board = [[1] * (n + 2) for _ in range(n + 2)]
    
    # 벽 붙이기
    for i in range(n):
        for j in range(n):
            wall_board[i + 1][j + 1] = board[i][j]
    
    q = deque()
    visited = []
    
    #집합(튜플) 구조
    start = { (1,1), (1,2) }
    
    q.append((start, 0))
    visited.append(start)
    
    while q:
        pos, cost = q.popleft()                                                                                                                                                                                                           
        if (n, n) in pos:
            return cost
        
        for next_pos in get_next_pos(pos, wall_board):
            if next_pos not in visited:
                q.append((next_pos, cost + 1))
                visited.append(next_pos)
                
    return 0                       
