from collections import defaultdict
def solution(k, tangerine):
    answer = 0
    cnt = defaultdict(int)
    for t in tangerine:
        cnt[t] += 1
    scnt = sorted(cnt.items(), key=lambda x: x[-1])
    while k > 0:
        k -= scnt.pop()[-1]
        answer += 1
    return answer