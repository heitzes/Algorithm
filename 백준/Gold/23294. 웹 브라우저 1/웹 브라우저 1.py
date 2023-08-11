from collections import deque
backSpace = deque([])
frontSpace = deque([])
now, cap = -1, 0
n, q, maxCap = list(map(int, input().split()))
nlist = list(map(int, input().split()))
dcap = {i+1: nlist[i] for i in range(n)}

def backward():
    global now
    frontSpace.append(now)
    now = backSpace.pop()
def forward():
    global now
    backSpace.append(now)
    now = frontSpace.pop()
def access(new):
    global frontSpace, cap, now
    for page in frontSpace:
        cap -= dcap[page]
    frontSpace = deque([])
    if now != -1:   
        backSpace.append(now)
    cap += dcap[new]
    now = new
    while cap > maxCap:
        old = backSpace.popleft()
        cap -= dcap[old]
def compress():
    global cap, backSpace
    newBackwardSpace = deque([])
    while backSpace:
        if not newBackwardSpace:
            newBackwardSpace.append(backSpace.popleft())
            continue
        while backSpace and newBackwardSpace[-1] == backSpace[0]:
            remove = backSpace.popleft()
            cap -= dcap[remove]
        if backSpace:
            newBackwardSpace.append(backSpace.popleft())
    backSpace = newBackwardSpace

for _ in range(q):
    cmd = input().split()
    if cmd[0] == "B":
        if len(backSpace) >=1: backward()
    elif cmd[0] == "F":
        if len(frontSpace) >=1: forward()
    elif cmd[0] == "A":
        access(int(cmd[-1]))
    else:
        compress()
print(now)
if backSpace:
    print(' '.join([str(i) for i in list(backSpace)[::-1]]))
else:
    print(-1)
if frontSpace:
    print(' '.join([str(i) for i in list(frontSpace)[::-1]]))
else:
    print(-1)