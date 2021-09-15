#https://www.acmicpc.net/problem/1695
from collections import Counter

n = int(input())
arr = list(map(int, input().split()))
arr_count = Counter(arr)

print(arr_count)