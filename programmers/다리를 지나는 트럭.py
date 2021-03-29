from collections import deque
def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    pass_bridge = deque([])
    times = 0

    while len(truck_weights):
        while len(truck_weights):
            pass_bridge.append(truck_weights.popleft())
            if sum(pass_bridge) >= weight:
                break
    
        if sum(pass_bridge) > weight or len(pass_bridge) > 2:
            truck_weights.appendleft(pass_bridge.pop())
        print(pass_bridge, times)
        #다리를 건널 트럭을 골라냄, pass_bridge의 sum이 weight 보다 작거나 같아야 함    
    
        while len(pass_bridge):
            times += 1
            if times >= bridge_length:
                pass_bridge.popleft()
        print(pass_bridge, times)
