#https://www.acmicpc.net/problem/11399
from copy import deepcopy

n = int(input())
people = list(map(int, input().split()))
result = 0

new_people = deepcopy(people)
new_people.sort()

for idx, val in enumerate(new_people):
    result += val
    new_people[idx] = result

print(sum(new_people))

'''
5
3 1 4 3 2
'''