n, m = map(int, input().split())
roads = sorted([list(map(int, input().split())) for _ in range(m)], key= lambda x: x[-1])
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
maxi, ans, cnt = 0, 0, 0
for a, b, cost in roads:
    if union(a, b):
        maxi = max(maxi, cost)
        ans += cost
        cnt += 1
    if cnt == n-1: break
print(ans - maxi)