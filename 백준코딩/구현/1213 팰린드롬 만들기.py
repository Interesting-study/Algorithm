from collections import Counter

name = sorted(input())
name_count = Counter(name)
length = len(name)

odd_count = 0
odd_char = ''
palin = ''

for char in name_count.keys():
    if name_count[char] % 2 == 1:
        odd_char = char
        odd_count += 1

    palin += (char * (name_count[char] // 2))

#팰린드롬은 반만 만들어도 된다.
if odd_count > 1:
    print("I'm Sorry Hansoo")
else:
    print(palin + odd_char + palin[::-1])
