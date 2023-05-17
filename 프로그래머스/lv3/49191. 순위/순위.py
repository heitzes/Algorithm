from collections import deque
def solution(n, results):
    answer = 0
    scores = dict()
    for i in range(1, n+1):
        scores[i] = [set(), set()]
    for win, lose in results:
        scores[win][0].add(lose)
        scores[lose][1].add(win)
    def bfs(m, node):
        vi = set([node])
        dq = deque([node])
        while dq:
            dpop = dq.popleft()
            for ch in scores[dpop][m]:
                if ch in vi:
                    continue
                vi.add(ch)
                dq.append(ch)
                scores[node][m].add(ch)
    for i in range(1, n+1):
        bfs(0, i)
        bfs(1, i)
    for pw, pl in scores.values():
        if len(pw) + len(pl) == n-1:
            answer += 1
    return answer