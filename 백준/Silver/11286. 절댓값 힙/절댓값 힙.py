import sys
import heapq
def input():
    return sys.stdin.readline().rstrip()
hq = []
n = int(input())
for _ in range(n):
    op = int(input())
    if op != 0:
        heapq.heappush(hq, [abs(op), op])
    else:
        if hq:
            hpop = heapq.heappop(hq)
            print(hpop[-1])
        else:
            print(0)