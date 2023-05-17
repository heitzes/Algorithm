from collections import deque, defaultdict
def solution(n, edge):
    cnt = 0
    graph = defaultdict(list)
    answer = defaultdict(int)
    vi, dq = set([1]), deque([[1, 0]])
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    while dq:
        dpop, cnt = dq.popleft()
        answer[dpop] = cnt
        for ch in graph[dpop]:
            if ch not in vi:
                vi.add(ch)
                dq.append([ch, cnt + 1])
    maxi = max(answer.values())
    return sum([1 for i, k in answer.items() if k == maxi])