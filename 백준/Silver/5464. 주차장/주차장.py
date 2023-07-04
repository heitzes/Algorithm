from collections import deque
import heapq
n, m = map(int, input().split())
parking, weight, wait, using = [], [-1], deque([]), [0] * (m+1)
for i in range(n):
    heapq.heappush(parking, [i, int(input())])
for _ in range(m):
    weight.append(int(input()))

money = 0
for _ in range(m*2):
    car = int(input())
    if car > 0: 
        # 주차할 곳 찾기
        if len(parking) == 0:
            wait.append(car)
            continue
    else:
        # 차 뺌
        heapq.heappush(parking, using[-car])
        if wait:
            car = wait.popleft()
        else:
            continue
    park = heapq.heappop(parking)
    using[car] = park
    money += park[1] * weight[car]
print(money)