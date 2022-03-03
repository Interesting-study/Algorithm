def get_aliquot(nums):
    aliquot = []
    for i in range(1, int(nums**0.5)+1):
        if nums % i == 0:
            aliquot.append(i)
            if i != (nums // i):
                aliquot.append(nums//i)

    return aliquot

strings = input()
nums = ''

for char in strings:
    if char.isnumeric():
        nums += char

nums = int(nums)
print(nums)
print(len(get_aliquot(nums)))