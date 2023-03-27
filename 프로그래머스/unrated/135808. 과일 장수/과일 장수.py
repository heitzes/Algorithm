def solution(k, m, score):
    answer = 0
    if len(score) < m:
        return answer

    score.sort()
    while len(score) >= m:
        local_min = 20
        for _ in range(m):
            local_min = min(local_min, score.pop())
        answer += local_min * m
    return answer