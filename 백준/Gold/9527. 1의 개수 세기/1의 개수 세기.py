n, m = map(int, input().split())
dp, ndp = [0, 1], [1, 2]
for i in range(1, 64):
    dp.append(dp[-1]+dp[-1]+2**(i))
    ndp.append(2 ** (i+1))
bn, bm = bin(n-1)[2:], bin(m)[2:]
def count(binary):
    ans = 0
    for i in range(len(binary)):
        if binary[i] == '1':
            ans += (dp[len(binary)-1-i]) + binary[:i].count('1') * ndp[len(binary)-1-i]
    ans += binary.count('1')
    return ans
print(count(bm)-count(bn))