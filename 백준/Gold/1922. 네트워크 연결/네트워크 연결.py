n, m = int(input()), int(input())
costs = []
for _ in range(m):
    costs.append(list(map(int, input().split())))
costs = sorted(costs, key=lambda x: x[-1])
uf = [-1] * (n+1)
def find(k):
    if uf[k] < 0:
        return k
    uf[k] = find(uf[k])
    return uf[k]
def union(a, b):
    ra, rb = find(a), find(b)
    if ra == rb:
        return False
    if rb > ra:
        uf[ra] = rb
    else:
        uf[rb] = ra
    return True
answer, cnt = 0, 0
for a, b, c in costs:
    if union(a, b):
        answer += c
        cnt += 1
    if cnt == n-1:
        break
print(answer)