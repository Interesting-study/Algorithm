n = int(input())
problems = []

for _ in range(n):
    problems.append(input())

count = 0
result = 0

for i in range(len(problems)):
    count = 0
    result = 0
    for j in range(len(problems[i])):
        if problems[i][j] == 'O':
            count += 1
            result += count
        else:
            count = 0
    print(result)
