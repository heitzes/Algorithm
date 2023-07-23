from collections import deque
n, k = map(int, input().split())
sq = deque([i for i in range(1, n+1)])
ref = deque([])
while len(ref) + len(sq) >= k:
    ref.append(sq.popleft())
    for _ in range(k-1): sq.popleft()
    if len(ref) + len(sq) < k:
        break
    if len(sq) == 0: 
        sq, ref = ref, deque([])
    elif len(sq) < k:
        ref.append(sq.popleft())
        for _ in range(k-1-len(sq)): ref.popleft()
        sq, ref = ref, deque([])
if sq:
    print(sq[0])
else:
    print(ref[0])