n, e = map(int, input().split())
elist = sorted([list(map(int, input().split())) for _ in range(e)], key = lambda x: x[-1])

p = [i for i in range(n+1)]
def find(node):
    if p[node] == node: return node
    p[node] = find(p[node])
    return p[node]
def union(a, b):
    ra, rb = find(a), find(b)
    if ra != rb:
        p[ra] = rb
        return True
    return False
cnt, ans = 0, 0
for a, b, cost in elist:
    if union(a, b):
        cnt += 1
        ans += cost
    if cnt == n: break
print(ans)