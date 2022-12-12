#https://www.acmicpc.net/problem/11722
#dp = arr[i]를 마지막 원소로 가질 때 가장 긴 증가하는 부분 수열의 길이
n = int(input())
arr = list(map(int, input().split()))
dp = [1] * n

for i in range(n):
    for j in range(i):
        if arr[i] < arr[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))