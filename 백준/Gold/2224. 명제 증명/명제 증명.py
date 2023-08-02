from collections import deque
n = int(input())
alpha = dict()
for _ in range(n):
    x, y = input().split(" => ")
    if x not in alpha:
        alpha[x] = [set(), set()]
    if y not in alpha:
        alpha[y] = [set(), set()]
    alpha[y][0].add(x)
    alpha[x][1].add(y)
anslist = []
def bfs(k):
    dq = deque(alpha[k][1])
    vi = set(alpha[k][1])
    while dq:
        x = dq.popleft()
        for ch in alpha[x][1]:
            if ch not in vi:
                dq.append(ch)
                vi.add(ch)
    for u in sorted(vi):
        if u == k: continue
        anslist.append([k, u])
for k in sorted(alpha):
    bfs(k)
print(len(anslist))
for x, y in anslist:
    print('{} => {}'.format(x, y))