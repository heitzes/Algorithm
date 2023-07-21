from collections import defaultdict
from itertools import combinations
def solution(clothes):
    wears = defaultdict(int)
    for cloth in clothes:
        wears[cloth[1]] += 1
    cnt = 1
    for k in wears.values():
        cnt *= (k+1)        
    return cnt - 1