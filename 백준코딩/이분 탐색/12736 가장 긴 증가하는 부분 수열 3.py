#https://www.acmicpc.net/problem/12738
from bisect import bisect_left, bisect_right

n = int(input())
arr = list(map(int, input().split()))

dp = [arr[0]]

for i in range(n):
    if arr[i] > dp[-1]:
        dp.append(arr[i])
    else:
        idx = bisect_left(dp, arr[i])
        dp[idx] = arr[i]

print(len(dp))