from collections import deque
def solution(n, results):
    answer = 0
    scores = [[[], []] for _ in range(n+1)]
    for win, lose in results:
        scores[win][0].append(lose)
        scores[lose][1].append(win)
    def bfs(m, node):
        vi = set(scores[node][m])
        dq = deque(scores[node][m])
        while dq:
            dpop = dq.popleft()
            for ch in scores[dpop][m]:
                if ch in vi:
                    continue
                vi.add(ch)
                dq.append(ch)
        return len(vi)
    for i in range(1, n+1):
        win = bfs(0, i)
        lose = bfs(1, i)
        if win + lose == n-1: answer += 1
    return answer