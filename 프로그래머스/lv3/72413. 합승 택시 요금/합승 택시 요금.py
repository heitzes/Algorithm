import heapq
def solution(n, s, a, b, fares):
    answer = 0
    
    graph = [[] for _ in range(n+1)]
    cost = [[0]*(n+1) for _ in range(n+1)]
    for i, j, k in fares:
        graph[i].append(j)
        graph[j].append(i)
        cost[i][j] = k
        cost[j][i] = k

    def daijkstra(start):
        pq = []
        dist = [-1] * (n + 1)
        for i in range(1, n+1):
            if i == start: 
                heapq.heappush(pq, [0, i])
                dist[i] = 0
            else: 
                dist[i] = 1e9

        while pq:
            cur, node = heapq.heappop(pq)
            for ch in graph[node]:
                if dist[ch] > cur + cost[node][ch]:
                    dist[ch] = cur + cost[node][ch]
                    heapq.heappush(pq, [dist[ch], ch])
        return dist
    answer = 1e9
    for i in range(1, n+1):
        dist = daijkstra(i)
        answer = min(answer, dist[s] + dist[a] + dist[b])
    return answer