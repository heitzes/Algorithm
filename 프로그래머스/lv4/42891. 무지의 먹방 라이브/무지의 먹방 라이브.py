import heapq
from collections import deque
def solution(food_times, k):
    """
    음식 양을 기준으로 최소 힙 구성
    다 먹은 음식은 힙에서 제거
    """
    heap = []
    if k >= sum(food_times):
        return -1
    for ind, time in enumerate(food_times):
        heapq.heappush(heap, [time, ind+1])
    hlen = len(heap)
    remember = 0
    while k and heap:
        if k - (heap[0][0]-remember) * hlen < 0:
            break
        k -= (heap[0][0]-remember) * hlen
        hlen -= 1
        remember = heapq.heappop(heap)[0]
    dq = sorted([[h[1], h[0]-remember] for h in heap])
    if not dq:
        return -1
    else:
        return dq[k % len(dq)][0]
    