from collections import deque
import heapq
def solution(alp, cop, problems):
    answer = 0
    maxa, maxc = 0, 0
    problems.append([0, 0, 1, 0, 1])
    problems.append([0, 0, 0, 1, 1])
    for p in problems:
        maxa = max(maxa, p[0])
        maxc = max(maxc, p[1])
    arr = [[1e9] * (maxc+1) for _ in range(maxa+1)]
    heap = [[0, -alp, -cop]] # 시간, -알고, -코딩
    while heap:
        time, algo, code = heapq.heappop(heap)
        for p in problems:
            needa, needc = p[0], p[1]
            if needa > -algo or needc > -code: continue
            na, nc = -algo+p[2], -code+p[3]
            if arr[min(na, maxa)][min(nc, maxc)] > time + p[-1]:
                arr[min(na, maxa)][min(nc, maxc)] = time + p[-1]
                heapq.heappush(heap,[time + p[-1], -min(na, maxa), -min(nc, maxc)])
    return arr[-1][-1]