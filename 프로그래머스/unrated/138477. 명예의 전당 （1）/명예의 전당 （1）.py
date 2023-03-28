from heapq import heappush, heappushpop

def solution(k, score):
    answer = []
    heap = []
    for i in range(k if k <= len(score) else len(score)):
        heappush(heap, score[i])
        answer.append(heap[0])

    for i in range(k, len(score)):
        heappushpop(heap, score[i])
        answer.append(heap[0])

    return answer