#https://www.acmicpc.net/problem/3613
import re

val = input()
java_pattern = re.compile('^([a-z]+)(([A-Z]([a-z]+))*)$')
c_plus_pattern = re.compile('')
print(java_pattern.match(val).group())
