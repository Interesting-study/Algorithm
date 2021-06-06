n = int(input())

students = []

#chr_sort = (lambda x: x.sort(reverse = True))

for _ in range(n):
    students.append( input().split() )
    
students.sort(key = lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0] ) )

#students.sort(key = lambda x : (-int(x[1]), int(x[2]), -int(x[3]), chr_sort(x) ) )
# 마지막 조건에서 내림차순 정렬

for student in students:
    print(student[0])

#https://www.acmicpc.net/problem/10825
