#https://www.acmicpc.net/problem/5545
n = int(input())
a, b = map(int, input().split())
dough = int(input())
calo = [int(input()) for _ in range(n)]
calo.sort(reverse=True)

for cal in calo:
    if (dough + cal) / (a + b) > dough / a:
        dough += cal
        a += b
    else:
        break

print(dough//a)