#https://www.acmicpc.net/problem/2891
N, S, R = map(int, input().split())
broken = list(map(int, input().split()))
have_spare = list(map(int, input().split()))

boat_condition = [1] * N

for i in broken:
    boat_condition[i-1] -= 1

for j in have_spare:
    boat_condition[j-1] += 1

for k in range(len(boat_condition)):
    if boat_condition[k] == 0:
        if k == 0:
            if boat_condition[k+1] == 2:
                boat_condition[k+1] = 1
                boat_condition[k] = 1
        elif k == len(boat_condition)-1:
            if boat_condition[k-1] == 2:
                boat_condition[k-1] = 1
                boat_condition[k] = 1
        else:
            if boat_condition[k-1] == 2:
                boat_condition[k-1] = 1
                boat_condition[k] = 1
                continue
            if boat_condition[k+1] == 2:
                boat_condition[k+1] = 1
                boat_condition[k] = 1
                continue
    else:
        continue

print(boat_condition.count(0))

'''
9 5 2
1 3 7 8 9
5 9
defaultdict(<class 'int'>, {1: 0, 2: 1, 3: 0, 4: 1, 5: 2, 6: 1, 7: 0, 8: 0, 9: 1})
[0, 1, 0, 1, 2, 1, 0, 0, 1]
'''
