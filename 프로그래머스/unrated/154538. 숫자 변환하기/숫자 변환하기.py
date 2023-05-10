from collections import deque
def solution(x, y, n):
    vi = set([x])
    dq = deque([[x, 0]])
    while dq:
        cur, cnt = dq.popleft()
        if cur == y:
            return cnt
        if cur < y:
            if cur + n not in vi:
                if cur + n == y:
                    return cnt + 1
                vi.add(cur + n)
                dq.append([cur + n, cnt + 1])
            if cur * 2 not in vi:
                if cur * 2 == y:
                    return cnt + 1
                vi.add(cur * 2)
                dq.append([cur * 2, cnt + 1])
            if cur * 3 not in vi:
                if cur * 3 == y:
                    return cnt + 1
                vi.add(cur * 3)
                dq.append([cur * 3, cnt + 1])
    return -1