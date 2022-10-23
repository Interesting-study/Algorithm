#https://www.acmicpc.net/problem/21758
from copy import deepcopy

n = int(input())
honey = list(map(int, input().split()))
honey_sum = deepcopy(honey)
result = 0

for i in range(1, n):
    honey_sum[i] += honey_sum[i-1]

for i in range(1, n-1): #벌통이 오른쪽에 있을 때
    result = max(result, 2*honey_sum[-1] - honey[0] - honey[i] - honey_sum[i])

for i in range(1, n-1): #벌통이 왼쪽
    result = max(result, honey_sum[-1] - honey[-1] - honey[i] + honey_sum[i-1])

for i in range(1, n-1): #벌통이 중간
    result = max(result, honey_sum[i] - honey[0] + honey_sum[-1] - honey_sum[i-1] - honey[-1])

print(result)