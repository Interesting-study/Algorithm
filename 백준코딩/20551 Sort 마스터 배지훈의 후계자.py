# https://www.acmicpc.net/problem/20551
import sys
input = sys.stdin.readline

def lower_bound(arr, target):
    left, right = 0, len(arr)-1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] < target:
            left = mid+1
        elif arr[mid] > target:
            right = mid - 1
        elif arr[mid] == target:
            if right == mid:
                break
            right = mid

    if arr[mid] == target:
        return mid
    else:
        return -1


n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
question = [int(input()) for _ in range(m)]

sorted_arr = sorted(arr)

for q in question:
    print(lower_bound(sorted_arr, q))

