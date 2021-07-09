#https://www.acmicpc.net/problem/1032

n = int(input())
files = [input() for _ in range(n)]

result = ""

for file in zip(*files):
    if len(set(file)) == 1:
        result += file[0]
    else:
        result += '?'

print(result)