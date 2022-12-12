import itertools

n = int(input())
coins = list(map(int, input().split()))

vaild_value  = set(coins)
length = len(coins)
max_coin = sum(coins)
min_coin = min(coins)

vaild_value.add(max_coin)
predict_value = set(range(min_coin, max_coin))

for num in range(2, length):
    for comb in itertools.combinations(coins, num):
        vaild_value.add(sum(comb))

print(min(predict_value - vaild_value))

#시간 : 2.574920654296875e-05 secs