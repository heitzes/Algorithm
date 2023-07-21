from collections import defaultdict, deque
import heapq
n, m, k = map(int, input().split())
mlines = defaultdict(deque)
def solution():
    global n, m, k, mlines
    for i in range(n):
        d, h = map(int, input().split())
        mlines[i % m].append([-d, -h, i % m, i])
    heap = []
    for n in mlines:
        heapq.heappush(heap, mlines[n][0])
    answer = 0
    while heap:
        hpop = heapq.heappop(heap)
        if hpop[-1] == k:
            return answer
        mlines[hpop[-2]].popleft()
        if mlines[hpop[-2]]:
            heapq.heappush(heap, mlines[hpop[-2]][0])
        answer += 1
    return answer
print(solution())