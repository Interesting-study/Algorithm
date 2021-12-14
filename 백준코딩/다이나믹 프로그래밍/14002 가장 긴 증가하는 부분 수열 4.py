#https://www.acmicpc.net/problem/14002
n = int(input())
arr = list(map(int, input().split()))
dp = [1] * n

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

seq_len = max(dp)
print(seq_len)

seq_idx = dp.index(seq_len)
lis = []

while seq_idx >= 0:
    if dp[seq_idx] == seq_len:
        lis.append(arr[seq_idx])
        seq_len -= 1
    seq_idx -= 1

lis.reverse()
print(*lis)