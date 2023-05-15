def solution(citations):
    answer = 0
    citations = sorted(citations)
    for h in range(citations[-1]+1):
        count = 0
        for paper in citations:
            if paper >= h:
                count += 1
        if count >= h:
            answer = max(h, answer)
    return answer