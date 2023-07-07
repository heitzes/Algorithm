import sys
sys.setrecursionlimit(10**6)
n, l, i = map(int, input().split())
dp = [[-1]*(l+1) for _ in range(n+1)]
def call_dp(idx, cnt):
    if idx == n or cnt == 0:
        dp[idx][cnt] = 1
        return 1
    if dp[idx][cnt] != -1:
        return dp[idx][cnt]
    dp[idx][cnt] = call_dp(idx+1, cnt)
    if cnt > 0: dp[idx][cnt] += call_dp(idx+1, cnt-1)
    return dp[idx][cnt]
call_dp(0, l)
def dfs(idx, cnt, nums, order):
    if idx == n: 
        return nums
    if cnt == 0:
        nums.extend(['0']*(n-idx))
        return nums
    left = dp[idx+1][cnt]
    if i > order + left:
        return dfs(idx+1, cnt-1, nums + ['1'], order + left)
    else:
        return dfs(idx+1, cnt, nums + ['0'], order)
answer = dfs(0, l, [], 0)
print(''.join(answer))