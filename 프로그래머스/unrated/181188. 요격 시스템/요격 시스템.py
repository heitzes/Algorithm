from collections import deque
def intersect(t1, t2):
    if t1[1] > t2[0]:
        return (t2[0], min(t1[1], t2[1]))
    return ()
def solution(targets):
    answer = 1
    inter = [-1, 1e9+1]
    targets = deque(sorted(targets))
    while targets:
        tg = targets.popleft()
        inter = intersect(inter, tg)
        if not inter:
            answer += 1
            inter = tg
    return answer