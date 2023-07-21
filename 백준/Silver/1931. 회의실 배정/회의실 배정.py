from collections import deque
n = int(input())
ans = 0
dq = deque(sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: (x[-1], x[0])))
while dq:
    start, end = dq.popleft()
    ans += 1
    while dq and dq[0][0] < end:
        dq.popleft()
print(ans)