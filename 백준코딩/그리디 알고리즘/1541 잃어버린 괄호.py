expression = input().split("-") #최소값을 만들기 위해서는 -기준으로 괄호를 친다. 55-(50+40)-(30+20)
nums = []

for exp in expression:
    plus = 0
    plus_split = exp.split("+")

    for j in plus_split:
        plus += int(j)

    nums.append(plus)
answer = nums[0]

for i in range(1, len(nums)):
    answer -= nums[i]

print(answer)