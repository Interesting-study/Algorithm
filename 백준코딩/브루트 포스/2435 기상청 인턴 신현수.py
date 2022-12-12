#https://www.acmicpc.net/problem/2435
n, k = map(int, input().split())
temperature = list(map(int, input().split(' ')))
answer = float('-inf')
start = 0
end = k

while end <= n:
    answer = max(answer, sum(temperature[start:end]))

    start += 1
    end += 1

print(answer)