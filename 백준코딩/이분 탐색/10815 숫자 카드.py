n = int(input())
cards = list(map(int, input().split()))
m = int(input())
checked_nums = list(map(int, input().split()))

cards = set(cards)
print(cards)

for num in checked_nums: #O(N)
    if num in cards: #O(1)
        print(1, end=" ")
    else:
        print(0, end=" ")

'''
1. bisect
#O(N) * O(logN) = O(NlogN)

500,000 * 6 = 3,000,000

2. set
#O(N) * O(1)  = O(N)
1 * 500,000 = 500,000
'''