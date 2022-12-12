n = int(input())
adventurer = list(map(int, input().split()))

adventurer.sort()

groups = 0
contained = 0

for i in adventurer:
    contained += 1
    if contained >= i:
        groups += 1
        contained = 0

print(groups)
