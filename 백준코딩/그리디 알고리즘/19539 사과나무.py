#https://www.acmicpc.net/problem/19539
n = int(input())
heights = list(map(int, input().split()))

#사과나무를 키우는 데 걸리는 일수
days = sum(heights) // 3

#사과나무 높이의 합은 3의 배수
if sum(heights) % 3 != 0:
    print("NO")
else:
    for h in heights:
        days -= (h // 2)

    if days > 0:
        print("NO")
    else:
        print("YES")