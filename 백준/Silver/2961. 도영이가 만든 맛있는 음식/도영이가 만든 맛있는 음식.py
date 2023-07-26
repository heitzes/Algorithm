n = int(input())
nlist = []
for i in range(n):
    a, b = map(int, input().split())
    nlist.append([a, b])
answer = float('inf')
def dfs(idx, s, b):
    global answer, n
    if idx == n:
        if s!=1 and b !=0:
            answer = min(answer, abs(s-b))
        return 
    dfs(idx + 1, s * nlist[idx][0], b + nlist[idx][1])
    dfs(idx + 1, s, b)
dfs(0, 1, 0)
print(answer)