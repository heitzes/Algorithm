n = int(input())
nlist = list(map(int, input().split()))
dp1, dp2 = [1] * n, [1] * n
for i in range(n):
    for j in range(i+1, n):
        if nlist[j] > nlist[i]:
            dp1[j] = max(dp1[j], dp1[i]+1)
for i in range(n-1, -1, -1):
    for j in range(i):
        if nlist[j] > nlist[i]:
            dp2[j] = max(dp2[j], dp2[i]+1)
print(max([dp1[i]+dp2[i] for i in range(n)])-1)