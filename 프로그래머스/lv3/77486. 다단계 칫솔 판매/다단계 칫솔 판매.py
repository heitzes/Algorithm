import sys
sys.setrecursionlimit(10**6)
from collections import defaultdict
def solution(enroll, referral, seller, amount):
    answer = []
    parent = defaultdict(list)
    res = defaultdict(int)
    for name, p in zip(enroll, referral):
        parent[name] = p
    def toothbrush(name, money):
        res[name] += money - money//10
        if name == "-" or money == 0: return 
        toothbrush(parent[name], money//10)
        return 
    for sell, money in zip(seller, amount):
        toothbrush(sell, money*100)
    return [res[i] for i in enroll]