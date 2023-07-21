import heapq
n = int(input())
pq = sorted(list(map(int, input().split())))
for _ in range(n-1):
    nlist = list(map(int, input().split()))
    for i in range(n):
        heapq.heappush(pq, nlist[i])
        heapq.heappop(pq)
print(heapq.heappop(pq))