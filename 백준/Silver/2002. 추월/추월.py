from collections import deque
n = int(input())
into, out = deque([]), deque([])
for _ in range(n):
    into.append(input())
for _ in range(n):
    out.append(input())
forward = []
while out:
    car = out.popleft()
    while into and into[0] in forward:
        into.popleft()
    if into[0] != car:
        forward.append(car)
    else:
        into.popleft()
print(len(forward))