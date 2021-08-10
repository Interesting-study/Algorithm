# https://www.acmicpc.net/problem/1052
# 모든 물병이 물이 1리터씩 들어있고, 무한히 담을 수 있다는 점에서 이진수도 떠올렸어야 했다.
n, k = map(int, input().split())
answer = 0

while bin(n).count('1') > k:
    """
     계속 1씩 더하면 올림 때문에 뒤에서부터 계산해야 내가 원하는 숫자를 구할 수 있다.
     ex) n = 9, k = 1
     총 물이 1, 2, 4병이 필요함
     
     n = 1001 -> 1010 -> 1100 (뒤에서부터 하면, 1, 2, 4)
    """
    bottle = 2 ** (bin(n)[::-1].index("1"))
    answer += bottle
    n += bottle
    
print(answer)