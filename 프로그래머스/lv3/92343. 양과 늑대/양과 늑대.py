def solution(info, edges):
    answer = 0
    graph = [set() for _ in range(17)]
    for p, ch in edges: graph[p].add(ch)
    cnt = 0
    def dfs(node, sheep, wolf, nxt):
        nonlocal answer,cnt
        if wolf >= sheep: return
        answer = max(answer, sheep)
        nxt |= graph[node]
        for ch in nxt:
            if not info[ch]: dfs(ch, sheep+1, wolf, (nxt - set([ch])))
            else: dfs(ch, sheep, wolf+1, (nxt - set([ch])))
    dfs(0, 1, 0, set())
    return answer