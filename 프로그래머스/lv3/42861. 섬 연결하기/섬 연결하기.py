def solution(n, costs):
    answer, cnt = 0, n-1
    costs = sorted(costs, key = lambda x: (x[-1], x[0], x[1]))
    nset = set()
    while cnt != 0:
        for cost in costs:
            if not nset:
                break
            if cost[0] in nset and cost[1] in nset:
                continue
            if cost[0] in nset or cost[1] in nset:
                break
        nset.update(cost[:-1])
        answer += cost[-1]
        costs.remove(cost)
        cnt -= 1
    return answer