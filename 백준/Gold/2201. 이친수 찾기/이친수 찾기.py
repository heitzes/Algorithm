from bisect import bisect_left
n = int(input())
dp = [[0, 0], [0, 1], [1, 0]]
ndp = [0, 1, 2]
for i in range(3, 90):
    dp.append([[], []])
    dp[i][0] = dp[i-1][0] + dp[i-1][1]
    dp[i][1] = dp[i-1][0]
    ndp.append(ndp[-1]+dp[i][0] + dp[i][1])
bit = bisect_left(ndp, n)
def dfs(n, rem, order):
    if n == 0:
        return order
    if n == 1:
        return order + ['0' if rem == 1 else '1']
    if ndp[n-1] + 1 >= rem:
        return dfs(n-1, rem, order + ['0'])
    else:
        return dfs(n-2, rem-(ndp[n-1]+1), order + ['1', '0'])
if n == 1:
    print('1')
elif n == 2:
    print('10')
elif n == 3:
    print('100')
elif n == 4:
    print('101')
else:
    print(''.join(dfs(bit-2, n-ndp[bit-1], ['1', '0'])))