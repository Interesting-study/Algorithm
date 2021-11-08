# https://www.hackerrank.com/challenges/py-set-add/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
length = int(input())
country = set([input() for _ in range(length)])

print(len(country))