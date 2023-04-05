from collections import defaultdict
import heapq
n, m = map(int, input().split())
neighbor = defaultdict(list)
length = [[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(m):
    a,b,v = map(int, input().split())
    neighbor[a].append(b)
    neighbor[b].append(a)
    length[a][b] = v
    length[b][a] = v
def dajikstra(n, start, length, neighbor):
    dist = [float('inf')] * (n+1)
    prev = [0] * (n+1)
    queue = []
    dist[start] = 0
    for ind, value in enumerate(dist[1:]):
        heapq.heappush(queue, [value, ind+1])
    while queue:
        value, node = heapq.heappop(queue)
        if dist[node] < value:
            continue
        for ch in neighbor[node]:
            distance = value + length[node][ch]
            if distance < dist[ch]:
                dist[ch] = distance
                prev[ch] = node
                heapq.heappush(queue, [distance, ch])      
    return prev
results = []
for j in range(1, n+1):
    # 집하장마다 다익스트라 돌림
    # 1->2->5->6이 최단거리인데, 1에서 시작시 prev는 5가 되고 6에서 시작시 prev는 2가 됨
    # 1에서 다음에 가야할 곳은 6에서 시작했을 때의 prev인 2
    results.append(dajikstra(n, j, length, neighbor)[1:])
answer = [[0] * (n) for _ in range(n)]
for i in range(n):
    for j in range(n):
        answer[i][j] = results[j][i]
for row in answer:
    res = ' '.join([str(i) if i !=0 else '-' for i in row])
    print(res)