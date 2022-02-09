#https://www.acmicpc.net/problem/5585
n = 1000 - int(input())
money = [500, 100, 50, 10, 5, 1]
answer = 0

for m in money:
    answer += (n // m)
    n %= m

print(answer)