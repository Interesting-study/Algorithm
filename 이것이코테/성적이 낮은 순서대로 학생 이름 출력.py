n = int(input())
students = []

for i in range(n):
    input_data = input().split()
    students.append((input_data[0], int(input_data[1])))

students = sorted(students, key=lambda x: x[1])

for student in students:
    print(student[0], end=' ')