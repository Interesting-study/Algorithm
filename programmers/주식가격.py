def solution(prices):
    answer = []
    
    for i in range(len(prices)):
        answer.append(len(prices) - 1)
        answer[i] = drop_check(prices.pop(0), answer[i], prices)
        
    return answer
        
        
def drop_check(present, period, prices):
    for price in prices:
        if price < present:
            period -= 1
            
    return period

# 정답은 맞았으나, 시간이 너무 오래걸림. 단축 필요
#brute force 말고 다른 방법
