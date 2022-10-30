n= int(input())
tips = [int(input()) for _ in range(n)]
tips.sort(reverse=True)
answer = 0

for i in range(n):
    tip = tips[i] - i

    if tip > 0:
        answer += tip

print(answer)