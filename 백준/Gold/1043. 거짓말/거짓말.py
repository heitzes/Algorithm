n, m = map(int, input().split())
p = [i for i in range(n+1)]
know = set(list(map(int, input().split()))[1:])

def find(node):
    if p[node] == node:
        return node
    p[node] = find(p[node])
    return p[node]

def union(a, b):
    ra, rb = find(a), find(b)
    if ra != rb:
        p[ra] = rb
    return
parties, answer = [], 0
for i in range(m):
    _, *party = list(map(int, input().split()))
    parties.append(party)
    for j in range(1, len(party)):
        union(party[0], party[j])
pknow = set([find(k) for k in know])
for party in parties:
    for pa in party:
        if find(pa) in pknow:
            break
    else:
        answer += 1
print(answer)