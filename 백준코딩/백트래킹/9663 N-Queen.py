n = int(input())
answer = 0
row = [0] * n

print(row)

def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x-i):
            return False
    '''
    case 1) 같은 열에 퀸이 있는지 없는지
    
    case 2) 왼쪽 대각선, 오른쪽 대각선에 다른 퀸이 있는지
        (3, 3) - i, j에 퀸이 존재
        왼쪽 대각선 : (2, 2) - x1, y1 / (1, 1) - x2, y2 / (0, 0) - x3, y3
            i - x1 = j - y1
            i - x2 = j - y2
            i - x3 = j - x3
        오른쪽 대각선 : (2, 4) (1, 5) (0, 6)
            i - x1 = -(j - y1)
            i - x2 = -(j - y2)
            i - x3 = -(j - x3)
        
        절댓값을 하면 같은 값이 된다
    
    '''
    return True


def dfs(x):
    global answer

    if x == n:
        answer += 1
        return
    else:
        for i in range(n):
            # [x, i] 자리에 퀸을 놓겠다.
            row[x] = i

            if is_promising(x):
                dfs(x+1)

dfs(0)
print(answer)