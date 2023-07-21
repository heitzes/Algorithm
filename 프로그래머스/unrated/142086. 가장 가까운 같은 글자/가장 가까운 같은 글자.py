def solution(s):
    answer = []
    wdict = dict()
    for ind, ch in enumerate(s):
        if ch not in wdict:
            answer.append(-1)
        else:
            answer.append(ind-wdict[ch])
        wdict[ch] = ind
    return answer