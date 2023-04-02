import heapq
from collections import deque
def solution(jobs):
    """
    어느 요청을 먼저 처리할까?
    
    작업의 요청부터 종료까지 걸린 시간 = [현재 시간 + 소요시간 - 요청 시간]
    이 중 소요 시간과 요청 시간은 고정 => 평균을 줄이려면 현재 시간을 최소화 해야함
    현재 시간 = 소요시간의 누적 합 => 소요시간이 작은 것 요청부터 처리
    a,b,c의 경우 요청 마무리시 현재 시간은 3, 12, 18 -> 합은 33
    a,c,b의 경우 요청 마무리시 현재 시간은 3, 9, 18 -> 합은 30
    
    요청 시점이 현재 시간 이후 -> 기다리지 않음 (먼저 들어온 요청부터 처리)
    예시 -  [0,3] / [4,6] / [1,9]
    0,3 처리 후 다음 요청 시간인 4가 현재 시간인 3보다 큼 -> [1, 9]부터 실행
    단, 요청 목록을 queue로 구현시 우선순위가 깨짐 -> 최소힙을 사용하여 우선순위를 유지
    """
    
    heap, njobs = [], len(jobs)
    jobs = sorted(jobs, key = lambda x: (x[0], x[1]))
    req, time = jobs.pop(0) # 처음엔 아무것도 안하고 있으므로 맨 처음 요청 수행
    cur_time = time + req # 첫 요청 시점이 0이 아닐 수 있음
    sum_time = cur_time - req
    
    while True:
        jobs_ref = jobs[:]
        for req, time in jobs_ref:
            if req > cur_time: # jobs는 정렬되어 있으므로 뒤를 더 볼 필요가 없다 (몽땅 다 현재 시간보다 요청 시간이 뒤임)
                break
            jobs.pop(0)
            heapq.heappush(heap, [time, req]) # 주의1: 모든 job을 최소힙에 넣는게 아니라 조건을 만족하는 job만 최소힙에 넣는다
        if heap: # 힙에서 꺼낼게 있음 -> heap에서 꺼냄
            time, req = heapq.heappop(heap)
            cur_time += time
        elif jobs: # 힙에서 꺼낼게 없음 -> jobs에서 다음 요청을 꺼냄
            req, time = jobs.pop(0)
            cur_time = req + time # 주의2: 다음 요청 시간에 실행 시간을 더한게 현재 시간이 됨
        else: # 힙과 jobs가 모두 비었음 -> 종료
            break
        sum_time += (cur_time - req)

    return sum_time // njobs