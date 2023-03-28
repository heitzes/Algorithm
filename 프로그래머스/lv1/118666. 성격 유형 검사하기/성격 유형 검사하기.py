def solution(survey, choices):
    result = []
    table = {k:0 for k in "RTCFJMAN"}
    for i in range(len(choices)):
        amount = choices[i] - 4
        if amount > 0:
            table[survey[i][-1]] += amount
        elif amount < 0:
            table[survey[i][0]] += -amount
    
    for u, v in zip("RCJA", "TFMN"):
        if table[u] > table[v]:
            result.append(u)
        elif table[u] < table[v]:
            result.append(v)
        else:
            result.append(u if u < v else v)

    return "".join(result)