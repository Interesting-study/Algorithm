#https://www.acmicpc.net/problem/2891
N, S, R = map(int, input().split())
broken = list(map(int, input().split()))
have_spare = list(map(int, input().split()))

cannot_start = 0

for team in broken:
    if team-1 in have_spare:
        have_spare.remove(team-1)
    elif team+1 in have_spare:
        have_spare.remove(team+1)
    else:
        cannot_start += 1

print(cannot_start)

'''
9 5 2
1 3 7 8 9
5 9
'''