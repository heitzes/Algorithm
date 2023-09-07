from itertools import product
import heapq
def bruteforce(p, k, reqs):
    hlist = [[] for _ in range(k+1)]
    wait = 0
    for req in reqs:
        start, need, tp = req
        if p[tp-1] > 0:
            heapq.heappush(hlist[tp-1], start+need)
            p[tp-1] -= 1
        else:
            end = heapq.heappop(hlist[tp-1])
            if end > start:
                wait += (end-start)
                heapq.heappush(hlist[tp-1], end+need)
            else:
                heapq.heappush(hlist[tp-1], start+need)
    return wait
def solution(k, n, reqs):
    answer = 1e9
    for p in product(range(1, n+2-k), repeat=k):
        if sum(p) == n: 
            answer = min(answer, bruteforce(list(p), k, reqs))
    return answer