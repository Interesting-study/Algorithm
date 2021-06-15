n = int(input())

arr = []

for i in range(n):
    arr.append(int(input()))

print(sorted(arr, reverse=True))