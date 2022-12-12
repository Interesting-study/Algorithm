#https://www.acmicpc.net/problem/1003

n = int(input())

count_zero = [1, 0]
count_one = [0, 1]

#조건에 보면 n은 40이하
#점화식 : An = An-1 + An-2
for i in range(2, 41):
    count_zero.append(count_zero[i-1] + count_zero[i-2])
    count_one.append(count_one[i-1] + count_one[i-2])

for _ in range(n):
    num = int(input())
    print(count_zero[num], end=" ")
    print(count_one[num])
