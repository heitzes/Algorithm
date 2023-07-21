import heapq
from collections import deque
def solution(food_times, k):
    """
    음식 양을 기준으로 최소 힙 구성
    다 먹은 음식은 힙에서 제거
    """
    heap = []
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
    """
    [1,1,1,1] / 4 인 경우, 맨 처음 1만 뽑으면 뒤의 음식들은 여전히 heap에 남아있다
    -> 남은 음식양 - remember 값이 0이 아닌 경우에만 deque에 추가
    """
    dq = sorted([[h[1], h[0]-remember] for h in heap if h[0] != remember])
    if not dq:
        return -1
    else:
        return dq[k % len(dq)][0]
    