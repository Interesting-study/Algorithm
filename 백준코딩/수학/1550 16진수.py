import string

digit_hex = list(input())[::-1]
alpha_hex = {}
lengh = len(digit_hex)
result = 0

for idx in range(10, 16):
    alpha_hex[string.ascii_uppercase[idx - 10 ]] = idx

for idx in range(lengh):
    if str(digit_hex[idx]).isalpha():
        result +=  ((16 ** idx) * alpha_hex[digit_hex[idx]])
    else:
        result += ((16 ** idx) * int(digit_hex[idx]))

print(result)
