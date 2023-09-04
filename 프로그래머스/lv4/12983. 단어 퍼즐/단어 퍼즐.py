def solution(strs, t):
    answer = 0
    '''
    1 <= k <= 5
    dp[i] = max(dp[i], dp[i-k] + 1)
    '''
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    dp = [1e9] * (len(t)+1)
    dp[0] = 0
    for i in range(1, len(t)+1):
        for k in range(1, 6):
            if i - k < 0: break
            if t[i-k:i] in strs:
                dp[i] = min(dp[i], dp[i-k] + 1)
    return dp[-1] if dp[-1] != 1e9 else -1