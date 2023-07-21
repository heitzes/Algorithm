def solution(play_time, adv_time, logs):
    answer, adv = [], 0
    def make_time(string):
        time = list(map(int, string.split(":")))
        return time[0]*3600 + time[1]*60 + time[2]
    pt = make_time(play_time)
    at = make_time(adv_time)
    dp = [0] * (pt + 1)
    logs.sort()
    for log in logs:
        s, e = log.split("-")
        st, et = make_time(s), make_time(e)
        dp[st] += 1
        dp[et] -= 1
    for i in range(1, pt+1):
        dp[i] += dp[i-1]
    for i in range(1, pt+1):
        dp[i] += dp[i-1]    
    start = 0  
    adv = dp[at-1]
    for i in range(1, pt+1):
        if i + at <= pt:
            if dp[i+at-1] - dp[i-1] > adv:
                start = i
                adv = dp[i+at-1] - dp[i-1]
    answer.append(str(start // 3600))
    start %= 3600
    answer.append(str(start // 60))
    start %= 60
    answer.append(str(start))
    return ':'.join(['0'*(2-len(t)) + t for t in answer])