from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bsum = 0
    bridge = deque([0] * (bridge_length))
    tq = deque(truck_weights)
    while tq:
        tpop = tq.popleft()
        bpop = bridge.pop()
        bsum -= bpop
        if bsum + tpop <= weight:
            bridge.appendleft(tpop)
            bsum += tpop
        else:
            bridge.appendleft(0)
            tq.appendleft(tpop)
        answer += 1  
    bsum = sum(bridge)
    while bsum != 0:
        answer += 1
        bsum -= bridge.pop()
    return answer