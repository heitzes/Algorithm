import heapq
def solution(operations):
    minh, maxh = [], []
    popped = set()
    cnt = 0
    for op in operations:
        mode, n = op.split(" ")
        if mode == "I":
            heapq.heappush(minh, int(n))
            heapq.heappush(maxh, -int(n))
            cnt += 1
            continue
        if cnt == 0:
            continue
        if int(n) == 1:
            while -maxh[0] in popped:
                heapq.heappop(maxh)
            popped.add(-heapq.heappop(maxh))
        else:
            while minh[0] in popped:
                heapq.heappop(minh)
            popped.add(heapq.heappop(minh))
        cnt -= 1
    maxh = [-i for i in maxh]
    cross = set(minh) & set(maxh)
    if not cross:
        return [0, 0]
    return [max(cross), min(cross)]