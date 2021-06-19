import re

s = input()

re_num = re.compile('[0-9]')
re_alpha = re.compile('[A-Z]')

s_num = sum(list(map(int, re_num.findall(s))))
s_alpha = ''.join(sorted(re_alpha.findall(s)))

result = s_alpha + str(s_num)
print(result)

#K1KA5CB7
