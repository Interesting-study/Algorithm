#https://www.acmicpc.net/problem/13305

n = int(input())
len_info = list(map(int, input().split()))
oil_info = list(map(int, input().split()))

res = 0
min_price = oil_info[0]

for i in range(n-1):

    if oil_info[i] < min_price:
        min_price = oil_info[i]

    res += min_price * len_info[i]

print(res)

'''
4
2 3 1
5 3 4 1

10, 12 = 22
'''

