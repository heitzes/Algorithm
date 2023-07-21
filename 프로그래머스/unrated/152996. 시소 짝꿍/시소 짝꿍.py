from collections import defaultdict
def solution(weights):
    answer = 0
    wdict = defaultdict(int)
    for w in weights:
        wdict[w] += 1
    for i in wdict:
        for j in wdict:
            if i == j:
                answer += (wdict[i] * (wdict[j]-1)) / 2
            else:
                if j in [1.5*i, 2*i, 4*i/3]:
                    answer += wdict[i] * wdict[j]
    return answer