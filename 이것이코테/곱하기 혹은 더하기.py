nums = list(map(int, list(input())))

answer = 0

for num in nums:
    if answer <= 1 or num <= 1:
        answer += num
    else:
        answer *= num

print(answer)