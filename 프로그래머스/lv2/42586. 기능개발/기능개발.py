def solution(progresses, speeds):
    answer = [0]
    timeline = []
    for p, s in zip(progresses, speeds):
        timeline.append(-int(-(100-p)//s))
    cur = timeline[0]
    while timeline:
        tpop = timeline.pop(0)
        if tpop <= cur:
        	answer[-1] += 1
        else:
            answer.append(1)
            cur = tpop
    return answer