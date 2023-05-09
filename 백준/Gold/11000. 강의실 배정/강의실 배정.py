import heapq
from bisect import bisect_right
n = int(input())
lectures = sorted([list(map(int, input().split())) for _ in range(n)])
heap = []
for lecture in lectures:
    start, end = lecture
    ind = bisect_right(heap, start)
    if ind != 0:
        heapq.heappop(heap)
    heapq.heappush(heap, end)
print(len(heap))