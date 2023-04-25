from bisect import bisect_left
from collections import deque
def solution(n, m, section):
    answer = 1
    start = 0
    section = deque(section)
    while True:
        sec = section[start]
        ind = bisect_left(section, sec+m)
        if ind == len(section):
            break
        answer += 1
        start = ind

    return answer