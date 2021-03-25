from collections import deque
def solution(progresses, speeds):
    answer = []
    count = 0
    days = 0
    progresses = deque(progresses)
    speeds = deque(speeds)
    #앞에서 하나씩 뺄 거기 때문에, 큐로 만든다.
    #문제에서 몇일째에 몇개 이 부분을 체크했어야 했다. 문제에 답이 전부 있다.
    
    while len(progresses):
        if progresses[0] + (speeds[0] * days) >= 100:
            progresses.popleft()
            speeds.popleft()
            count += 1
            #첫 기능이 100 % 가 아니면, 배포하지 않기 때문에 days로 날짜를 계속 체크해본다. 
        else:
            if count > 0 :
                answer.append(count)
                count = 0
            days += 1
            
    answer.append(count)
    return answer
