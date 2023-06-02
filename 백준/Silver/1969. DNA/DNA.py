from collections import Counter
n, m = map(int, input().split())
nlist = [input() for _ in range(n)]
counter = []
ans, dist = '', 0
for i in range(m):
    cnt = [dna[i] for dna in nlist]
    counter.append(Counter(cnt))
for c in counter:
    c = sorted(list(c.items()), key=lambda x: (-x[1], x[0]))
    ans += c[0][0]
    dist += sum([i[1] for i in c]) - c[0][1]
print(ans)
print(dist)