#https://www.acmicpc.net/problem/17298

n = int(input())
arr = list(map(int, input().split()))
length = len(arr)
answer = [-1] * n
stack = [0]

for i in range(1, n):
    while stack and arr[stack[-1]] < arr[i]:
        answer[stack.pop()] = arr[i]
    stack.append(i)


print(*answer)
