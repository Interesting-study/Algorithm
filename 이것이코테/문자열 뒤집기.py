arr = list(map(int, list(input())))

count0 = 0
count1 = 1

if arr[0] == 0:
    count1 += 1
else:
    count0 += 1

for i in range(len(arr) - 1):
    if arr[i] != arr[i+1]:
        if arr[i+1] == 1:
            count0 += 1
        else:
            count1 += 1

print(min(count1, count0))