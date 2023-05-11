def solution(priorities, location):
    answer = 0
    pq = list(map(list, zip(priorities, range(len(priorities)))))
    while pq:
        ppop = pq.pop(0)
        if pq and ppop[0] < max(pq)[0]:
            pq.append(ppop)
            continue
        answer += 1
        if ppop[1] == location:
            break
    return answer