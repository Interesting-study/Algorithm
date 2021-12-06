#https://www.acmicpc.net/problem/13305

n = int(input())
len_info = list(map(int, input().split())) + [0]
oil_info = list(map(int, input().split()))
dp = [0] * (n+1)

price = 0
distance = sum(len_info)
cheap = min(oil_info)

for idx in range(n-1):
    now, next = idx, idx+1




