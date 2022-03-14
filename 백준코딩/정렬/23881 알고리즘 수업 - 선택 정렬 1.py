n, k = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(n-1, 0, -1):
    max_val = 0
    idx = i
    for j in range(i+1):
        if max_val < arr[j]:
            max_val = arr[j]
            idx = j

    if i != idx:
        arr[i], arr[idx] = arr[idx], arr[i]
        k -= 1

        if k == 0:
            break

if k > 0:
    print(-1)
elif k == 0:
    print(arr[idx], arr[i])



