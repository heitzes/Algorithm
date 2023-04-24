import math
def solution(r1, r2):
    answer = 0
    for i in range(1, r2+1):
        maxy = int(math.sqrt(r2**2 - i**2))
        miny = math.ceil(math.sqrt(r1**2 - i**2)) if r1 > i else 0
        answer += (maxy-miny+1)
    return answer*4