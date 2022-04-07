#https://www.acmicpc.net/problem/16987
n = int(input())
eggs = [list(map(int, input().split())) for _ in range(n)]
answer = 0

def crash(now):
    global answer

    if now == n:
        crashed_eggs = 0
        for egg in eggs:
            if egg[0] <= 0:
                crashed_eggs += 1
        answer = max(answer, crashed_eggs)
        return

    if eggs[now][0] <= 0:
        crash(now+1)
        return

    is_all_broken = True
    for idx in range(n):
        if idx == now:
            continue
        if eggs[idx][0] > 0:
            is_all_broken = False
            break

    if is_all_broken:
        answer = max(answer, n-1)
        return

    for idx in range(n):
        if idx == now:
            continue
        if eggs[idx][0] <= 0:
            continue
        eggs[now][0] -= eggs[idx][1]
        eggs[idx][0] -= eggs[now][1]

        crash(now+1)

        eggs[now][0] += eggs[idx][1]
        eggs[idx][0] += eggs[now][1]

crash(0)
print(answer)