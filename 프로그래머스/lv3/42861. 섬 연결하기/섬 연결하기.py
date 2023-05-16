def solution(n, costs):
    answer, cnt = 0, n-1
    nset = set([i for i in range(n)])
    costs = sorted(costs, key = lambda x: (-x[-1], x[0], x[1]))
    n1, n2, c = costs.pop()
    answer += c
    cnt -= 1
    nset -= set([n1, n2])
    while nset and cnt > 0:
        for i in range(len(costs)-1, -1, -1):
            n1, n2, c = costs[i]
            if n1 in nset and n2 in nset:
                continue
            if n1 not in nset and n2 not in nset:
                continue
            break
        nset -= set([n1, n2])
        cnt -= 1
        answer += c
        costs.remove([n1,n2,c])
    return answer