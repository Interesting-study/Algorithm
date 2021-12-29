n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort(reverse=True)
routine = [nums[0]] * k + [nums[1]]

q, r = divmod(m, len(routine))

print(routine)

if r == 0:
    answer = sum(routine) * q
else:
    print(routine[:r])
    answer = sum(routine) * q + sum(routine[:r])

print(answer)
