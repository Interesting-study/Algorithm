#https://www.acmicpc.net/problem/2310
actions = {"E": lambda poc, val: poc,
           "L": lambda poc, val: poc if poc > val else val,
           "T": lambda poc, val: poc - val
           }

def dfs(room):
    global success
    global visited
    global cash
    global rooms

    now_room = rooms[room]
    cash = actions[now_room[0]](cash, now_room[1])

    if cash >= 0:
        if room == n:
            success = True
            return 0
        else:
            for next_room in now_room[2:]:
                if next_room != now_room and not visited[next_room]:
                    visited[next_room] = True
                    dfs(next_room)
                    visited[next_room] = False
    visited[room] = False

while True:
    n = int(input())
    if n == 0:
        break

    success = False
    cash = 0
    visited = [False] * (n + 1)
    rooms = [0]

    for _ in range(n):
        room = input().split()
        rooms.append(list(room[0]) + list(map(int, room[1:-1])))

    dfs(1)

    if success:
        print("Yes")
    else:
        print("No")