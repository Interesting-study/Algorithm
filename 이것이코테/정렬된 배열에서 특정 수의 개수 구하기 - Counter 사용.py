from collections import Counter

n, x = map(int, input().split())
arr = list(map(int, input().split()))

arr_count = Counter(arr)

if x in arr_count.keys():
    print(arr_count[x])
else:
    print(-1)