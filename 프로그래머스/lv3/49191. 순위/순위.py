from collections import deque
def solution(n, results):
    answer = 0
    scores = [[set(), set()] for _ in range(n+1)]
    for win, lose in results:
        scores[win][0].add(lose)
        scores[lose][1].add(win)
    # 2중 for문으로도 해결 가능
    for i in range(1, n+1):
        for loser in scores[i][0]:
            scores[loser][1].update(scores[i][1])
        for winner in scores[i][1]:
            scores[winner][0].update(scores[i][0])
    for i in range(1, n+1):
        if len(scores[i][0]) + len(scores[i][1]) == n-1: answer += 1
    return answer