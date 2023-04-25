def solution(n):
    answer = 0
    nlist = sorted(list(str(n)), reverse=True)
    return int(''.join(nlist))