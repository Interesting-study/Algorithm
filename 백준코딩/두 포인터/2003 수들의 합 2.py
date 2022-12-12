#https://www.acmicpc.net/problem/2003

n, m = map(int, input().split())
nums = list(map(int, input().split()))

answer = 0
end = 0
current_sum = 0

for start in range(n):

    while current_sum < m and end < n:
        current_sum += nums[end]
        end += 1

    if current_sum == m:
        answer += 1
    current_sum -= nums[start]

print(answer)
