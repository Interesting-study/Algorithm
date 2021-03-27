from collections import deque
def solution(bridge_length, weight, truck_weights):
  answer = 0
  truck_weights = deque(truck_weights)
  pass_bridge = deque([])
  times = 0
    
    

  while sum(pass_bridge) <= 10:
    pass_bridge.append(truck_weights.popleft())
  truck_weights.appendleft(pass_bridge.pop())
  print(pass_bridge, truck_weights)

# 무게가 10kg까지, 다리를 건널 트럭
