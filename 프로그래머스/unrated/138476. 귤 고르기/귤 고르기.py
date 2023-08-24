from collections import Counter
def solution(k, tangerine):
    answer = 0
    cnt = Counter(tangerine)
    scnt = sorted(cnt.values(), key=lambda x: x)
    while k > 0:
        k -= scnt.pop()
        answer += 1
    return answer