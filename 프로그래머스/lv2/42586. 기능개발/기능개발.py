import math
def solution(progresses, speeds):
    answer = [0]
    baepo = [math.ceil((100-progresses[i])/speeds[i]) for i in range(len(speeds))]
    now = baepo[0]
    for b in baepo:
        if b <= now:
            answer[-1] += 1
        else:
            now = b
            answer.append(1)
    return answer