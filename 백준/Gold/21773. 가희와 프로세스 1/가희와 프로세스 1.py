import heapq
from collections import defaultdict
t, n = map(int, input().split())
maxheap, count = [], defaultdict(int)
for i in range(n):
    a, b, c = map(int, input().split())
    count[-c] += 1
    heapq.heappush(maxheap, [-c, a, b])
cnt = 0    
while maxheap and cnt < t:
    hpop = heapq.heappop(maxheap)
    if hpop[-1] != 1:
        heapq.heappush(maxheap, [hpop[0]+1, hpop[1], hpop[-1]-1])
    cnt += 1
    print(hpop[1])