from collections import defaultdict
import heapq
n, m = int(input()), int(input())
graph = defaultdict(set)
values = dict()
for _ in range(m):
    i, j, v = map(int, input().split())
    if i not in values:
        values[i] = dict()
    if j not in values[i]:
        values[i][j] = v
    values[i][j] = min(values[i][j], v)
    graph[i].add(j)
f, t = map(int, input().split())
nodes = [1e9 for _ in range(n+1)]
nodes[f] = 0
def dijkstra():
    hq = []
    heapq.heappush(hq, [0, f])
    while hq:
        v, node = heapq.heappop(hq)
        if nodes[node] < v:
            continue
        for ch in graph[node]:
            dist = nodes[node] + values[node][ch]
            if nodes[ch] > dist:
                nodes[ch] = dist
                heapq.heappush(hq, [dist, ch])
dijkstra()
print(nodes[t])