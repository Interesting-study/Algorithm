from collections import deque
def solution(prices):
    answer = []
    prices = deque(prices)
    #큐로 바꿔서 가장 앞에 있는 가격부터 뽑아냄
    
    while prices:
        past = prices.popleft()
        
        seconds = 0
        
        for present in prices:
            if past <= present:
                seconds += 1
                #가격이 떨어지지 않은 기간으로 체크
            else:
                seconds += 1
                #지금 시간부터 1초동안은 유지하는 걸로 보므로 1초를 넣어준다.
                break
            
        answer.append(seconds)
        
    return answer
