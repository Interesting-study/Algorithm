#https://www.acmicpc.net/problem/14467
n = int(input())
cows_pos = [[] for _ in range(n+1)]
answer = 0

for _ in range(n):
    cow, pos = map(int, input().split())
    if cows_pos[cow] == []:
        cows_pos[cow] = pos
    elif cows_pos[cow] != pos:
        answer += 1
        cows_pos[cow] = pos

print(answer)