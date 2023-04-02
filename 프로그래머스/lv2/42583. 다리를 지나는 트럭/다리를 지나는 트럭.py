from collections import deque
def solution(bridge_length, weight, truck_weights):
    # 트럭 대기열은 큐
    truck = deque(truck_weights)
    
    # 현재 브릿지의 상태도 큐 (트럭이 브릿지를 따라 움직이는 것을 구현하기 위해)
    bridge = deque([0] * bridge_length)
    
    # 현재 브릿지 위의 트럭수, 현재 무게, 시간
    cnt, cur, time = 0, 0, 0
    
    while truck:
        # 브릿지 업데이트 
        bpop = bridge.popleft()
        if bpop != 0: # 트럭이 빠져나간 경우
            cnt -= 1
            cur -= bpop
        # 트럭이 들어올 수 있음
        if cnt + 1 <= bridge_length and cur + truck[0] <= weight:
            # 트럭 넣기
            tpop = truck.popleft()
            bridge.append(tpop)
            cnt += 1
            cur += tpop
        # 트럭이 못 들어옴
        else:
            bridge.append(0)
        time += 1
        
    return time + bridge_length