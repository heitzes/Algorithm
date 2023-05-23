import heapq
from collections import defaultdict
def solution(n, paths, gates, summits):
    answer = []
    nodes = [1e9] * (n+1)
    values = defaultdict(int)
    routes = defaultdict(set)
    gates, summits = set(gates), set(summits)
    for i, j, k in paths:
        if not values[i]:
            values[i] = dict()
        if not values[j]:
            values[j] = dict()
        values[i][j] = k
        values[j][i] = k
        routes[i].add(j)
        routes[j].add(i)
    def dijkstra():
        hq = []
        for g in gates:
            heapq.heappush(hq, [0, g, 0])
            nodes[g] = 0
        while hq:
            val, node, f = heapq.heappop(hq)
            if nodes[node] < val:
                continue
            for ch in routes[node]:
                if ch in gates:
                    continue
                node_maxi = max(val, values[ch][node])
                if nodes[ch] > node_maxi and not f:
                    nodes[ch] = node_maxi
                    if f and ch in cummits:
                        continue
                    if not f and ch in summits:
                        heapq.heappush(hq, [node_maxi, ch, 1])
                    else:
                        heapq.heappush(hq, [node_maxi, ch, f])
    dijkstra()
    ind, minimum = 0, 1e9
    for s in sorted(summits):
        if nodes[s] < minimum:
            minimum = min(minimum, nodes[s])
            ind = s
    return [ind, minimum]