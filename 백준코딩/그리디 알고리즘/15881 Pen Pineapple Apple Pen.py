#https://www.acmicpc.net/problem/15881

n = int(input())
arr = input()

arr = arr.replace("pPAp", "..../")
print(arr.count("...."))
