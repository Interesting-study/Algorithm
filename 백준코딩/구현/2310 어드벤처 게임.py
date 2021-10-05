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

        self.visited = [False] * (n + 1)

    def dfs(self, node, cash):
        now_room =

        if cash >= 0:
            if node == n:
                success = True
                return success
            else:
                for next_room in rooms[node][2:]:
                    if next_room != node and not visited[next_room]:
                        visited[next_room] = True
                        print(cash)
                        print(node, rooms[node], cash, visited)
                        dfs(next_room, cash, visited, success)
                        visited[next_room] = False
        visited[node] = False

        def start(self):
            self.dfs(1, cash=0)



while True:
    n = int(input())
    if n == 0:
        break

    game = Game(n)

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