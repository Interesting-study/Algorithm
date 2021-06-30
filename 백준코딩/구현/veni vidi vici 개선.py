import string

n = int(input())
data_set = list(input().split())
alpha = string.ascii_lowercase

for data in data_set:
    word = ''
    length = len(data)

    new_data = [data[i:i+2] for i in range(0, length, 2)]

    for i in new_data:
        sum = 0
        for j in i:
            sum += alpha.index(j)
        sum %= 26
        word += alpha[sum]

    print(word)