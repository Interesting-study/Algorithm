s = list(map(int, list(input())))
zero_cnt = one_cnt = 0

if s[0] == 1:
    zero_cnt += 1
else:
    one_cnt += 1

for i in range(len(s) - 1):
    if s[i] != s[i+1]:
        if s[i+1] == 1:
            zero_cnt += 1
        else:
            one_cnt += 1

print(min(zero_cnt, one_cnt))


