a, b = input().split()
answer = float('inf')

for i in range(len(b) - len(a) + 1): #range(8-5+1) = range(4)
    count = 0
    for j in range(len(a)):
        # print(f'i = {i}, j = {j}, a = {a[j]}, b = {b[i+j]}')
        if a[j] != b[i+j]:
            count += 1
    answer = min(answer, count)

print(answer)