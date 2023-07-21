def solution(n, lost, reserve):
    answer = 0
    reserve, lost = set(reserve)-set(lost), set(lost)-set(reserve)
    cant = len(lost)
    for l in sorted(lost):
        if l-1 in reserve:
            reserve -= set([l-1])
            cant -= 1
        elif l+1 in reserve:
            reserve -= set([l+1])
            cant -= 1
    return n - cant