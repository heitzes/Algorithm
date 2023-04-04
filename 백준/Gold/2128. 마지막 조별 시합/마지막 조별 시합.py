from itertools import combinations
n, d, k = map(int, input().split())
student, comb = [[] for _ in range(n)], []
pbs = [i+1 for i in range(d)]
for i in range(n):
    pb = list(map(int, input().split()))
    for j in range(pb[0]):
        student[i].append(pb[j+1])
for k in range(1, k+1):
    comb.extend(map(list, combinations(pbs, k)))

def bit_maker(problem):
    bit = 0
    for p in problem:
        bit |= (1 << (d-p))
    return bit

maxi = 0
for c in comb:
    c_bit = bit_maker(c)
    cnt = 0
    for s in student:
        s_bit = bit_maker(s)
        if c_bit | s_bit == c_bit:
            cnt += 1
    maxi = max(maxi, cnt)
print(maxi)