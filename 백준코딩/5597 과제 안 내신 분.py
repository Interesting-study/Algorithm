assignment_students = set([int(input()) for _ in range(28)])
all_students = set([i for i in range(1, 31)])

not_assignment = sorted(list((all_students - assignment_students)))


print(not_assignment[0])
print(not_assignment[-1])
