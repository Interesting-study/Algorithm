import sys

n=int(sys.stdin.readline().strip())
a=[]
s=0

for i in range(n):
    a.append(int(sys.stdin.readline().strip()))

a.sort(reverse=True)

for i in range(n):
    b=a[i] - i

    if b > 0:
        s += b

print(s)