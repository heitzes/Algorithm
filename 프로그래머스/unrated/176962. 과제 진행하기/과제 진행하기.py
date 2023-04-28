def solution(plans):
    remain = []
    plans = sorted(map(lambda x: [x[0], int(x[1][:2])*60 + int(x[1][3:]), int(x[-1])], plans), key=lambda x:x[1])
    for plan in plans:
        subject, start, need = plan
        for i, rem in enumerate(remain):
            end, _ = rem
            if end > start:
                remain[i][0] += need
        remain.append([start+need, subject])
    return [i[1] for i in sorted(remain)]