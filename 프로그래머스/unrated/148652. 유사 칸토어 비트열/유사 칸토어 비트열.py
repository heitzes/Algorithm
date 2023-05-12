def solution(n, l, r):
    answer = r - l + 1
    for i in range(l-1, r):
        while i >= 1:
            m, n = divmod(i, 5)
            if m == 2 or n == 2:
                answer -= 1
                break
            i = m
    return answer