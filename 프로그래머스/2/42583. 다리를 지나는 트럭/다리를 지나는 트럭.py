from collections import deque
def solution(bridge_length, weight, truck_weights):
    on = deque([])
    cur = 0
    time = bridge_length
    
    for truck in truck_weights:
        time += 1
        if on and time - bridge_length == on[0][1]:
            gone = on.popleft()
            cur -= gone[0]
        while cur + truck > weight or bridge_length == len(on):
            gone = on.popleft()
            cur -= gone[0]
            if cur + truck <= weight and bridge_length > len(on):
                time = gone[1] + bridge_length
                on.append((truck, time))
                cur += truck
                break
        else:
            on.append((truck, time))
            cur += truck
        
        
    return on[-1][1]