from collections import deque
n, k = map(int, input().split())
def bfs(x):
    dq = deque([x])
    vi = [-1] * 100001 # +1, *2 한 값은 100000보다 작아야함
    route = [-1] * 100001
    vi[x] = 0
    while dq:
        now = dq.popleft()
        for nxt in [now-1, now+1, now*2]:
            if 0 <= nxt <= 100000 and vi[nxt] == -1:
                vi[nxt] = vi[now] + 1
                route[nxt] = now
                dq.append(nxt)
        if vi[k] != -1:
            print(vi[k])
            break
    res = [k]
    for _ in range(vi[k]):
        res.append(route[res[-1]])
    print(*res[::-1], ' ')
bfs(n)