import heapq
def solution(k, score):
    answer = []
    honor = []
    for s in score:
        if len(honor) < k:
            heapq.heappush(honor, s)
        else:
            heapq.heappushpop(honor, s)
        answer.append(honor[0])
    return answer