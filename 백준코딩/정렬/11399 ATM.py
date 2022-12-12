#https://www.acmicpc.net/problem/11399

n = int(input())
people = list(map(int, input().split()))
new_people = []
result = 0
answer = 0
#(시간, 순서)

for i in range(len(people)):
    new_people.append([people[i], i])

new_people.sort(key = lambda x: x[0])

for people in new_people:
    result += people[0]
    people[0] = result

for people in new_people:
    answer += people[0]

print(answer)