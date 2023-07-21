def solution(n, m, section):
    prev = section[0]
    answer = 1
    for sec in section:
        if sec >= prev + m:
            answer += 1
            prev = sec
    return answer