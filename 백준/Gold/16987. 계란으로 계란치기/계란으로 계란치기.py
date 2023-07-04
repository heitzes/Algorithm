n = int(input())
orders = []
ans = 0
eggs = [list(map(int, input().split())) for _ in range(n)]

def calc(hit, ref):
    global n
    ref = [row[:] for row in ref]
    for i in range(n):
        a, b = i, hit[i]
        if ref[a][0] <=0 or ref[b][0] <=0: continue 
        ref[a][0] -= ref[b][1]
        ref[b][0] -= ref[a][1]
    answer = 0
    for egg in ref:
        if egg[0] <= 0: answer += 1
    return answer

def order(idx, olist):
    global n, ans
    if idx == n:
        ans = max(ans, calc(olist, eggs))
        return
    for i in range(n):
        if i != idx:
            order(idx+1, olist + [i])
order(0, [])
print(ans)