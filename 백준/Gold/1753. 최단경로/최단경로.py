import heapq
v, e = map(int, input().split())
k = int(input())
distances = [float('inf')] * (v+1)
distances[k] = 0
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a, b, w = map(int, input().split())
    graph[a].append([b, w])
def daijkstra(graph, start):
    pq = [[0, start]]
    while pq:
        dist, node = heapq.heappop(pq)
        if distances[node] < dist: continue
        for ch, d in graph[node]:
            if dist + d < distances[ch]:
                distances[ch] = dist + d
                heapq.heappush(pq, [dist + d, ch])
    return distances
distances = daijkstra(graph, k)
for i in range(1, v+1):
    print(distances[i] if distances[i]!=float('inf') else "INF")