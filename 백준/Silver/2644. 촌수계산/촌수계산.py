from collections import defaultdict, deque
n = int(input())
a, b = map(int, input().split())
k = int(input())
chon = defaultdict(list)
for _ in range(k):
    i, j = map(int, input().split())
    chon[i].append(j)
    chon[j].append(i)
    
def bfs(a, b):
    que = deque([[a, 0]])
    vi = [0] * (n+1)
    vi[a] = 1
    while que:
        q, cnt = que.popleft()
        if q == b:
            return cnt
        for ch in chon[q]:
            if not vi[ch]:
                vi[ch] = 1
                que.append([ch, cnt+1])
    return -1

print(bfs(a, b))