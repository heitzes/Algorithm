n = int(input())
nlist = sorted([int(input()) for _ in range(n)], reverse=True)
ans = 0
for i, w in enumerate(nlist, 1):
    ans = max(ans, w*i)
print(ans)