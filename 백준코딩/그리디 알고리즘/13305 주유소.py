#https://www.acmicpc.net/problem/13305

n = int(input())
len_info = list(map(int, input().split())) + [0]
oil_info = list(map(int, input().split()))

price = oil_info[0] * len_info[0]
distance = sum(len_info[1:])
cheap = min(oil_info[:-1])

for idx in range(1, n-1):
    now, next = idx, idx+1

    if oil_info[now] == cheap:
        price += (distance * cheap)
        break

    if oil_info[now] * (len_info[now] + len_info[next]):
        pass


print(price)


'''
4
2 3 1
5 3 4 1

10, 12 = 22
'''

