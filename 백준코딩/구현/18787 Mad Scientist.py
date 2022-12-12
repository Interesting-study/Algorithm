N = int(input())
A = input()
B = input()

answer = 0
flag = False# False = A, B가 일치한다, True = A, B가 일치하지 않는다

for cow in range(len(A)):
	if flag or A[cow] != B[cow]:
		flag = True
	if flag and A[cow] == B[cow]:
		flag = False
		answer += 1

print(answer)