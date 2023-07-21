from collections import deque
n = int(input())
vi, dq = set([n]), deque([[n, 0]])
while dq:
    dpop, cnt = dq.popleft()
    if dpop == 1:
        print(cnt)
        break
    if dpop % 3 == 0: 
        if dpop // 3 not in vi:
            vi.add(dpop//3)
            dq.append([dpop//3, cnt+1])
    if dpop % 2 == 0:
        if dpop // 2 not in vi:
            vi.add(dpop//2)
            dq.append([dpop//2, cnt+1])
    if dpop -1 not in vi:
        vi.add(dpop-1)
        dq.append([dpop-1, cnt+1])