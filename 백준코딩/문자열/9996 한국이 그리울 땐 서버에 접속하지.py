#유
import re

n = int(input())
pattern = input()
files = [input() for _ in range(n)]

re_pattern = re.compile(pattern.replace('*', '.*'))

for file in files:
    now = re_pattern.search(file)
    if now and now.group() == file:
        print('DA')
    else:
        print('NE')
