import string

n = int(input())
data_set = list(input().split())
pw_alpha = {}

for i in range(len(string.ascii_lowercase)):
    pw_alpha[string.ascii_lowercase[i]] = i

alpha_pw = dict(map(reversed, pw_alpha.items()))

for data in data_set:
    word = ''
    for i in range(len(data) // 2):
        start = i*2
        end = (i+1)*2
        check = data[start:end]
        index = pw_alpha[check[0]] + pw_alpha[check[1]] - n
        index %= 26

        word += alpha_pw[index]

    print(word, end=' ')
