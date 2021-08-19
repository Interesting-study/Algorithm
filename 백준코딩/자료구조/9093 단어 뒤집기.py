#https://www.acmicpc.net/problem/9093
n = int(input())
sentences = [list(input().split()) for _ in range(n)]

for sentence in sentences:
    for word in sentence:
        print(word[::-1], end=" ")
    print()