def solution(v):
    #직사각형의 좌표의 경우, x와 y는 전부 짝수개로 나오기 때문에 남아있는 좌표가 필요한 좌표가 됨
    vx = []
    vy = []
    
    for cord in v:
        if not cord[0] in vx:
            vx.append(cord[0])
        else:
            vx.remove(cord[0])
            
        if not cord[1] in vy:
            vy.append(cord[1])
        else:
            vy.remove(cord[1])

    return [vx.pop(), vy.pop()]
