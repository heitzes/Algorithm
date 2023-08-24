def solution(n, left, right):
    answer = []
    lr, lc = left // n, left % n
    rr, rc = right // n, right % n
    for i in range(lr, rr+1):
        row = [i+1] * (i+1) + [j for j in range(i+2, n+1)]
        if i == lr == rr:
            answer.extend(row[lc:rc+1])
        elif i == lr:
            answer.extend(row[lc:])
        elif i == rr:
            answer.extend(row[:rc+1])
        else:
            answer.extend(row)
    return answer