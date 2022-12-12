from collections import deque
def solution(priorities, location):
    answer = 0 
    
    priori_queue = deque( [priori, index] for index, priori in enumerate(priorities) )
    #[우선도, 위치]로 된 큐를 만든다.
    #max(priori_queue) = 제일 높은 중요도를 가진 문서를 뽑음 [0][n]이 기준이다. 
    
    while len(priori_queue):
        check_item = priori_queue.popleft()
        
        if priori_queue and max(priori_queue)[0] > check_item[0]:
            priori_queue.append(check_item)
            #중요도가 가장 높은 문서가 맨 앞에 오도록 함
        else:
            answer += 1
            if location == check_item[1]:
                break
            #하나씩 인쇄하면서 내가 인쇄하고자하는 문서가 맞는지 체크한다.
    return answer

#https://programmers.co.kr/learn/courses/30/lessons/42587
