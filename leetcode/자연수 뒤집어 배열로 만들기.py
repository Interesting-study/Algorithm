#https://programmers.co.kr/learn/courses/30/lessons/12932
def solution(n):
    #return [int(i) for i in str(n)][::-1]
    
``` 첫번쨰 방법은 코드가 매우 간결했지만, 아래 방법에 비해 시간이 더 오래 걸렸다. 아래 방법은 코드는 길지만, 더 시간이 짧았다. 코드의 간결함과 시간 중 뭘 택해야하는 걸까?
```

    answer = []
    while True:
        if n == 0:
            break
        answer.append((n%10))
        n //= 10
    return answer 

# 아래 방법은 우선 10으로 나눈 나머지는 일의 자릿수부터 나오고, 그 이후에 n을 다시 10으로 나눈 몫으로 정하는 식으로 이어갔다.
    
