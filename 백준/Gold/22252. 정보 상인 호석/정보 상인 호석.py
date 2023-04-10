from collections import defaultdict
import heapq
n = int(input())
infos = defaultdict(list)
money = 0
for _ in range(n):
    info = input().split()
    if info[0] == '1':
        for value in info[3:]:
            heapq.heappush(infos[info[1]], -int(value))
    else:
        buy = info[1]
        if len(infos[buy]) <= int(info[2]):
            money += -sum(infos[buy])
            infos[buy] = []
        else:
            for _ in range(int(info[2])):
                money += -heapq.heappop(infos[buy])
print(money)