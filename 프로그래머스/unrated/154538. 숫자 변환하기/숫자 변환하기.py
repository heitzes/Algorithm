from collections import deque
def solution(x, y, n):
    vi = set([x])
    dq = deque([[x, 0]])
    while dq:
        cur, cnt = dq.popleft()
        if cur == y:
            return cnt
        for nxt in [cur + n, cur * 2, cur * 3]:
            if nxt <= y and nxt not in vi:
                vi.add(nxt)
                dq.append([nxt, cnt + 1])
    return -1