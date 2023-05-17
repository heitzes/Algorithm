def solution(n, costs):
    answer = 0
    uf = [-1] * n
    costs = sorted(costs, key=lambda x: x[-1])
    def find(node):
        if uf[node] < 0: 
            return node
        uf[node] = find(uf[node])
        return uf[node]
    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        uf[rb] = ra
        return True
    for cost in costs:
        if union(cost[0], cost[1]):
            answer += cost[-1]
    return answer 