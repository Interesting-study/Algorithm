import time

n, m , k = map(int, input().split())
data = list(map(int, input().split()))

start_time = time.time()

data.sort()

first = data[-1]
second = data[-2]
#first + second가 한 루프

arr = ([first] * k) + [second]
length = len(arr)

quote = m // length
remain = m % length

result = quote * sum(arr) + sum(arr[:remain])

end_time = time.time()

print(result)
print(end_time - start_time)

#걸린 시간 : 1.3113021850585938e-05

