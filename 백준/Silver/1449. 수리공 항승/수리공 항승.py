from collections import deque
n, tape = map(int, input().split())
dq = deque(sorted(list(map(int, input().split()))))
ans = 0
while dq:
    dpop = dq.popleft()
    e = dpop-0.5+tape
    ans += 1
    while dq and dq[0]+0.5 <= e:
        dq.popleft()
print(ans)