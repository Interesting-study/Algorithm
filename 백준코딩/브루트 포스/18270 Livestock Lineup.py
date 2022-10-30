from itertools import*
t='Bessie Buttercup Belinda Beatrice Bella Blue Betsy Sue'.split()
t.sort()
l=[]
for T in range(int(input())):
    a,*_,b=input().split();l+=[(a,b)]

for i in permutations(t):

    if all(abs(i.index(v)-i.index(w))==1 for v,w in l):
        print(*i)
        break