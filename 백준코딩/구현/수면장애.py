n = int(input())

answer = []
num = 1

while len(answer) <= n:
    split_num = list(str(num))
    num += 1
    answer += split_num

print(split_num)
print(answer[n-1])