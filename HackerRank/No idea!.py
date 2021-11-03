#https://www.hackerrank.com/challenges/no-idea/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int, input().split())

arr = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

score = 0

for val in arr:
    if val in A:
        score += 1
    if val in B:
        score -= 1

print(score)
