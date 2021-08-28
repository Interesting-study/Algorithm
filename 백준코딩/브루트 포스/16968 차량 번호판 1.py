#https://www.acmicpc.net/problem/16968
car = input()
cases = {"c": 26, "d": 10}

before = car[0]
answer = cases[before]

for c in car[1:]:
    now = c

    if before == c:
        if before == "c":
            answer *= (cases["c"] - 1)
        else:
            answer *= (cases["d"] - 1)

    else:
        answer *= cases[now]
        before = c

print(answer)