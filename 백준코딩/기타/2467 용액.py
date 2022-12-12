#https://www.acmicpc.net/problem/2467
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

left, right = 0, n-1
zero_diff = float('inf')
answer = []

while left < right:
    if abs(arr[left] + arr[right]) <= zero_diff:
        answer = [arr[left], arr[right]]
        zero_diff = abs(arr[left] + arr[right])

    if arr[left] + arr[right] < 0:
        left += 1
    elif arr[left] + arr[right] > 0:
        right -= 1
    else:
        break

print(*answer)