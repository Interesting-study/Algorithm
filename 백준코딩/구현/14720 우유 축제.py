#https://www.acmicpc.net/problem/14720
n = int(input())
store = list(map(int, input().split()))
route = [0, 1, 2]

answer = 0

if 0 not in store:
    print(0)
else:
    start = store.index(0)
    drinking = [0]
    last = drinking[-1]

    answer += 1

    for now in store[start:]:

        if not drinking and now == 0:
            drinking.append(now)
            last = drinking[-1]
            answer += 1

        if now - last == 1:
            drinking.append(now)
            last = drinking[-1]
            answer += 1

        if drinking == route:
            drinking = []


print(answer)