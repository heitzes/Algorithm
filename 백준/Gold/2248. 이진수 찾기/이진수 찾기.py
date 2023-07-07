import sys
sys.setrecursionlimit(10**6)
n, l, i = map(int, input().split())
dp = [[-1]*(l+1) for _ in range(n+1)]
def call_dp(idx, cnt):
    if idx == n:
        dp[idx][cnt] = 1
        return 1
    if cnt == 0:
        return 1
    if dp[idx][cnt] != -1:
        return dp[idx][cnt]
    dp[idx][cnt] = call_dp(idx+1, cnt) + call_dp(idx+1, cnt-1)
    return dp[idx][cnt]
call_dp(0, l)
answer = ''
def dfs(idx, cnt, nums, order):
    global answer
    if idx < n and cnt == 0:
        nums.extend(['0']*(n-idx))
        answer = ''.join(nums)
        return
    if idx == n:
        answer = ''.join(nums)
        return
    left = dp[idx+1][cnt]
    if i > order + left:
        dfs(idx+1, cnt-1, nums + ['1'], order + left)
    else:
        dfs(idx+1, cnt, nums + ['0'], order)
dfs(0, l, [], 0)
print(answer)