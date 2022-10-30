from itertools import*
cows = 'Bessie Buttercup Belinda Beatrice Bella Blue Betsy Sue'.split()
cows.sort()
order = []

for T in range(int(input())):
#    a, b= input().split("must be milked beside ")
    a, *_, b = input().split()
    order.append((a, b))

for i in permutations(cows):
    if all(abs(i.index(v) - i.index(w)) == 1 for v, w in order):
        print(*i)
        break