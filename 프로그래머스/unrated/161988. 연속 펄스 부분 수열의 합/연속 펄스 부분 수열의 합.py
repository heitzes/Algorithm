def solution(sequence):
    """
    시간 초과 풀이:
        k번째 인덱스에서 시작하고 길이가 n인 연속 부분수열의 합이 DP[n][k]에 저장되어 있다고 가정한다
        점화식: DP[n][k] = DP[n-1][k] + sequence[k+n-1] (단, 0 <= k <= sequence 길이 - n)
    ...
    for n in range(2, slen+1):
        for k in range(slen-n+1):
            dp[n-1][k] = dp[n-2][k] + sequence[k+n-1]
        maxi = max(max([abs(i) for i in dp[n-1]]), maxi)
    return maxi
    """
    
    """
    n번째 index까지 탐색 했을 때 가장 큰 연속 부분 수열의 합이 DP[n]에 저장되어 있다
    점화식: DP[n] = max(DP[n-1] + sequence[n], sequence[n]) (단, n >= 1)
    """
    slen = len(sequence)
    seq1 = [(-1)**(i%2) * sequence[i] for i in range(slen)]
    seq2 = [(-1)**((i+1)%2) * sequence[i] for i in range(slen)]
    dp1, dp2 = seq1[:], seq2[:]
    for i in range(1, slen):
        dp1[i] = max(dp1[i-1] + dp1[i], dp1[i])
        dp2[i] = max(dp2[i-1] + dp2[i], dp2[i])
    return max(max(dp1), max(dp2))