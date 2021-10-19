#https://www.acmicpc.net/problem/20055
from collections import deque

n, k = map(int, input().split())
conveyor_belt = deque(map(int, input().split()))

stage = 0

robot = [0] * n
robot = deque(robot)

while conveyor_belt.count(0) < k:
    conveyor_belt.rotate(1)
    robot.rotate(1)
    robot[-1] = 0

    if sum(robot):
        for i in range(n-2, -1, -1):
            if robot[i] == 1 and robot[i+1] == 0 and conveyor_belt[i+1] >= 1:
                robot[i+1] = 1
                robot[i] = 0
                conveyor_belt[i+1] -= 1
        robot[-1] = 0

    if robot[0] == 0 and conveyor_belt[0] >= 1:
        robot[0] = 1
        conveyor_belt[0] -= 1

    stage += 1
print(stage)
