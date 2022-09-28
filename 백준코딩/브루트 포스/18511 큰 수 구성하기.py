#https://www.acmicpc.net/problem/18511
n, k = input().split()
n = list(map(int, list(n)))
k = int(k)
nums = list(map(int, input().split()))
nums.sort(reverse=True)

answer = [nums[0]] * len(nums)

print(n)