n, m, k = map(int, input().split())
length = n + m
dp = [[0] * (i+1) for i in range(201)]
for i in range(201):
    for j in range(i+1):
        if i == j == 0:
            continue
        elif i == 0 or j == 0 or i == j:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][min(j, i-1-j)]
def solution():
    global n, m, k
    if dp[length][m] < k:
        return -1
    pos, pset = 0, set()
    while m > 0:
        if k == 1: break
        for i in range(m, length-pos+1):
            if dp[i][m] >= k and i - 1 >= m:
                k -= dp[i-1][m]
                m -= 1
                pos = length - (i)
                pset.add(pos)
                break
    answer = ['z' if i in pset else 'a' for i in range(length)]
    if not pset: pset.add(-1)
    answer[max(pset)+1:] = ['a'] * (length-(max(pset)+1)-(m)) + ['z'] * m
    return ''.join(answer)
print(solution())