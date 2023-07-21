from collections import defaultdict
from itertools import combinations
n, d, k = map(int, input().split())
pbs = defaultdict(list)
std = defaultdict(str)
answer = 0
combination = list(combinations([i+1 for i in range(d)], k))

def bitmask(it):
    global d
    bit = 0
    for v in it:
        bit |= (1 << (v-1))
    return bit

for i in range(n):
    student = list(map(int, input().split()))
    std[i] = bitmask(student[1:])

for comb in combination:
    problem = bitmask(comb)
    cnt = 0
    for student in std.values():
        if student | problem == problem:
            cnt += 1
    answer = max(cnt, answer)
print(answer)