n = int(input())
nlist = list(map(int, input().split()))
av = set([i for i in range(100000*20+1)])
def dfs(idx, cnt):
    global n
    if idx == n:
        if cnt in av:
            av.remove(cnt)
        return
    dfs(idx+1, cnt + nlist[idx])
    dfs(idx+1, cnt)
    return
dfs(0, 0)
print(min(av))