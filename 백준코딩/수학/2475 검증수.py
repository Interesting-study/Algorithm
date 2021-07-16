nums = list(map(int, input().split()))

result = 0

for num in nums:
    result += (num ** 2)

result %= 10
print(result)