n = int(input())
panic = list(map(int, input().split()))

panic.sort()

result = 0
count = 0

for i in panic:
    count += 1
    #현재 공포도보다 인원수가 더 크면 인원 결성해도 되므로
    if count >= i:
        result += 1
        count = 0

print(result)

