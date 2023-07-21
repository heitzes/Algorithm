import bisect
num = int(input())
n, slist = 1, [1]
while slist[-1] < num:
    n += 1
    six = slist[-1] + (n)*2 + (n-1) + (n-2)
    slist.append(six)
dp = [i for i in range(slist[-1]+1)]
for s in slist:
    dp[s] = 1

def dp_maker(num):
    global dp
    for k in range(2, num+1):
        ind = bisect.bisect_right(slist, k)
        for i in range(ind-1, 0, -1):
            dp[k] = min(dp[k], dp[k-slist[i]] + dp[slist[i]])
    return dp
dp_maker(num)
print(dp[num])