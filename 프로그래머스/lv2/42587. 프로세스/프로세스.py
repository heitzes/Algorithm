from collections import deque
def solution(priorities, location):
    answer = 0
    maxi = deque(sorted(priorities, reverse=True))
    pq = deque(list(enumerate(priorities)))
    while priorities:
        ind, ppop = pq.popleft()
        if ppop < maxi[0]:
            pq.append([ind, ppop])
            continue
        answer += 1
        if ind == location:
            return answer
        maxi.popleft()
    return answer