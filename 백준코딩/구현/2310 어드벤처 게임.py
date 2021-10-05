#https://www.acmicpc.net/problem/2310
actions = {"E": lambda poc, val: poc,
           "L": lambda poc, val: poc if poc > val else val,
           "T": lambda poc, val: poc - val
           }

class Game:
    def __init__(self, n):
        self.n = n
        self.rooms = [0]

        for _ in range(n):
            room = input().split()
            self.rooms.append(list(room[0]) + list(map(int, room[1:-1])))
        self.success = False
        self.visited = [False] * (n + 1)

    def dfs(self, node, cash):
        now_room = self.rooms[node]
        now_pocket = actions[now_room[0]](cash, now_room[1])

        if now_pocket >= 0:
            if node == n:
                self.success = True
                return 0
            else:
                for next_room in now_room[2:]:
                    if next_room != now_room and not self.visited[next_room]:
                        self.visited[next_room] = True
                        self.dfs(next_room, now_pocket)
                        self.visited[next_room] = False
        self.visited[node] = False


    def start(self):
        self.dfs(1, cash=0)
        if self.success:
            return "Yes"
        else:
            return "No"



while True:
    n = int(input())
    if n == 0:
        break

    game = Game(n)
    print(game.start())

"""
4
E 0 2 3 0
L 201 2 3 0
L 10 4 0
T 15 2 3 1 0
0

3
E 0 2 0
L 10 3 0
T 15 1 2 0
0
"""