from collections import deque

def find_location(maze, wanted):
    for i in range(r):
        for j in range(c):
            if maze[i][j] == wanted:
                return (i, j)

def bfs(x, y, what):
    pass

r, c = map(int, input().split())
maze = [list(input()) for _ in range(r)]



dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(r):
    for j in range(c):
        if maze[i][j] == "#":
            continue
        else:
            bfs(i, j, maze[i][j])
            print(maze, end="\n\n")

print(start, fire)

"""
4 4
####
#F#J
#..#
#..#
"""