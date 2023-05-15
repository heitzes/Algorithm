from bisect import bisect_left
def solution(citations):
    answer = 0
    citations = sorted(citations)
    for i in range(max(citations)):
        ind = bisect_left(citations, i)        
        if len(citations) - ind >= i:
            answer = max(answer, i)
    return answer