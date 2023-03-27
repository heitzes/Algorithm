def solution(sizes):
    n, m = 0, 0
    for a, b in sizes:
        if a < b:
            a, b = b, a
        n = max(n, a)
        m = max(m, b)
    return n * m