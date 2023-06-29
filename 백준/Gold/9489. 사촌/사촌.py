from collections import deque, defaultdict

def countSibling(tree, nlist, dq):
    while dq:
        cnt = len(dq)
        if k in dq: 
            answer = cnt
            break
        dq = deque(sorted(dq))
        for _ in range(cnt):
            p = dq.popleft()
            while len(nlist) >= 2 and nlist[0] == nlist[1]-1:
                ch = nlist.popleft()
                tree[ch] = p
                dq.append(ch)
            if nlist:
                ch = nlist.popleft()
                tree[ch] = p
                dq.append(ch)
while True:
    n, k = map(int, input().split())
    if n == 0 and k == 0: break
    nlist = deque(list(map(int, input().split())))
    if k == nlist[0]:
        print(0)
        continue
    tree = dict()
    root = nlist.popleft()
    dq = deque([root])
    countSibling(tree, nlist, dq)
    answer = 0
    tree[root] = 0
    parentK = tree[k]
    grandK = tree[parentK]
    for node in tree:
        if tree[node] not in tree: continue
        if tree[node] != parentK and tree[tree[node]] == grandK:
            answer += 1
    print(answer)