from collections import defaultdict
import heapq
n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    i, j, v = map(int, input().split())
    graph[i].append([j, v])
    graph[j].append([i, v])
u, v = map(int, input().split())

def dijkstra(k):
    hq = [[0, k]]
    nodes = [1e9] * (n+1)
    nodes[k] = 0
    while hq:
        val, node = heapq.heappop(hq)
        if nodes[node] < val:
            continue
        for ch, cost in graph[node]:
            dist = nodes[node] + cost
            if nodes[ch] > dist:
                nodes[ch] = dist
                heapq.heappush(hq, [dist, ch])
    return nodes
u_d = dijkstra(u)
v_d = dijkstra(v)
one = u_d[1] + u_d[v] + v_d[n]
two = v_d[1] + v_d[u] + u_d[n]
mini = min(one, two)
if mini >= 1e9:
    print(-1)
else:
    print(mini)