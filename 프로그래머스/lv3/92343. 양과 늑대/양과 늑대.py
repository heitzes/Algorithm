def solution(info, edges):
    answer = 0
    graph = [set() for _ in range(17)]
    for p, ch in edges: graph[p].add(ch)
    def dfs(node, sheep, wolf, nxt):
        nonlocal answer
        if wolf >= sheep: return
        answer = max(answer, sheep)
        nxt = (nxt - set([node])) | graph[node]
        for ch in nxt:
            if not info[ch]: dfs(ch, sheep+1, wolf, nxt)
            else: dfs(ch, sheep, wolf+1, nxt)
    dfs(0, 1, 0, graph[0])
    return answer