from collections import defaultdict
n = int(input())
answer = 0
nlist, nset = [], set()
weight = defaultdict(int)
change = defaultdict(int)
for _ in range(n):
    word = input()
    nlist.append(word)
for w in nlist:
    for i, v in enumerate(w):
        weight[v] += 10 ** (len(w)-i-1)
weight = sorted(weight, key=lambda x: -weight[x])
for alpha, val in zip(weight, range(9, 9-len(weight), -1)):
    change[alpha] = val
for w in nlist:
    cnt = ''
    for a in w:
        cnt += str(change[a])
    answer += int(cnt)
print(answer) 