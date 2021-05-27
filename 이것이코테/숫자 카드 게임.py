n, m = map(int, input().split())

result = 0

for i in range(2):
    data = list(map(int, input().split()))

    min_value = min(data)

    #가장 작은 수 중에 가장 큰 것을 고르는 것이기 때문에
    result = max(result, min_value)

print(result)
