num = list(map(int, list(input())))
answer = num[0]

for i in range(1, len(num)):
    now = num[i]

    if now <= 1 or answer <= 1:
        answer += now
    else:
        answer *= now

print(answer)