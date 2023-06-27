def solution():
    n = int(input())
    nlist = list(map(int, input().split()))
    m = int(input())
    left, right = 0, m
    if sum(nlist) <= m: return max(nlist)
    while left + 1 < right:
        mid = (left + right) // 2
        cnt = sum([min(i, mid) for i in nlist])
        if cnt <= m:
            left = mid
        else:
            right = mid
    return left
print(solution())