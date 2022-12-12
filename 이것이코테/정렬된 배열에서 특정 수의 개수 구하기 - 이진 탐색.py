def count_by_value(arr, x):

    n = len(arr)

    fir = first_index(arr, x, 0, n - 1)

    if fir == None:
        return 0

    last = last_index(arr, x, 0, n - 1)

    return last - fir + 1

def first_index(arr, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    #원하는 값이 제일 왼쪽에 있을때
    if (mid == 0 or target > arr[mid -1]) and arr[mid] == target:
        return mid
    elif arr[mid] >= target:
        return first_index(arr, target, start, mid - 1)
    else:
        return first_index(arr, target, mid + 1, end)

def last_index(arr, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    #원하는 값이 제일 끝에 있을 때
    if (mid == end - 1 or target < arr[mid + 1]) and arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return last_index(arr, target, start, mid -1)
    else:
        return last_index(arr, target, mid + 1, end)


n, x = map(int, input().split())
arr = list(map(int, input().split()))

answer = count_by_value(arr, x)

if answer == 0:
    print(-1)
else:
    print(answer)