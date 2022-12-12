#https://www.acmicpc.net/problem/9012
def check_vps(data):
    cnt = 0
    for i in data:
        if i == "(":
            cnt += 1
        else:
            if cnt == 0:
                return "NO"
            cnt -= 1

    return "YES" if cnt == 0 else "NO"

n = int(input())

for _ in range(n):
    print(check_vps(input()))