import time

n, m , k = map(int, input().split())
data = list(map(int, input().split()))

start_time = time.time()

data.sort()

first = data[-1]
second = data[-2]
#first + second가 한 루프

count = (m // (k+1)) * k
count += m % (k + 1)

result = 0
result += count * first
result += (m - count) * second
end_time = time.time()

print(result)
print(end_time - start_time)

#걸린 시간 : 7.152557373046875e-06

