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

# set 풀이
# bonus = 0
# student = defaultdict(set)
# for i in range(n):
#     pbs = list(map(int, input().split()))
#     if pbs[0] == 0:
#         bonus += 1
#     for p in range(pbs[0]):
#         student[i].add(pbs[p+1])
# comb = []
# for i in range(1, k+1):
#     comb.extend(list(map(set, combinations(dlist, i))))
# maxi = 0
# for c in comb:
#     count = 0
#     for st, pb in student.items():
#         if len(pb - c) == 0:
#             count += 1
#     maxi = max(maxi, count)
# print(maxi + bonus)
