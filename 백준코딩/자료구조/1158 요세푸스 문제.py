n, k = map(int, input().split())
now = k - 1
answer = []

circle = [i for i in range(1, n+1)]

for i in range(n):
    if len(circle) > now:
        answer.append(str(circle.pop(now)))
        now += k - 1
    else:
        now = now % len(circle)
        answer.append(str(circle.pop(now)))
        now += k - 1


print("<", ", ".join(answer), ">", sep="")