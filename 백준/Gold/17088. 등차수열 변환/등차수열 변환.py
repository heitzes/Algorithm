n = int(input())
nlist = list(map(int, input().split()))

def isArithmetic(x, y, cnt):
    d = y - x
    for i in range(2, len(nlist)):
        an = x + i * d
        diff = abs(nlist[i] - an)
        if diff <= 1:
            if diff == 1:
                cnt += 1
            continue
        return -1
    return cnt

def solution():
    answer = 1e9
    if len(nlist) <= 2:
        return 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            a, b = nlist[0] + i, nlist[1] + j
            cnt = abs(i) + abs(j)
            ans = isArithmetic(a, b, cnt)
            if ans != -1: answer = min(answer, ans)
    return answer if answer != 1e9 else -1
print(solution())