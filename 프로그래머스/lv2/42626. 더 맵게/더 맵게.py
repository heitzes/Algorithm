import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville:
        if scoville[0] >= K:
            return answer
        if len(scoville) < 2:
            return -1
        first, second = heapq.heappop(scoville), heapq.heappop(scoville)
        heapq.heappush(scoville, first + 2*(second))
        answer += 1
    return -1