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
uv = u_d[1] + v_d[n] + u_d[v]
uu = u_d[1] + u_d[n] + u_d[v]*2
vu = v_d[1] + u_d[n] + u_d[v]
vv = v_d[1] + v_d[n] + u_d[v]*2
mini = min([uv, uu, vv, vu])
if mini >= 1e9:
    print(-1)
else:
    print(mini)