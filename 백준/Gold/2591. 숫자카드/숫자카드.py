n = input()
nlist = ['0']
dp = [0] * (41)
dp[1], dp[2] = 1, 2
for i in range(3, 41):
    dp[i] = dp[i-1] + dp[i-2] 
for i in range(len(n)):
    if '1' <= nlist[-1][-1]+n[i] <= '34':
        if nlist[-1][-1]+n[i] in ['10', '20', '30']:
            npop = nlist.pop()
            if len(npop[:-1]) > 0:
                nlist.append(npop[:-1])
            nlist.append(npop[-1]+n[i])
        else:
            nlist[-1] += n[i]
    else:
        nlist.append(n[i])
nlist = nlist[1:]
ans = 1
for num in nlist:
    if int(num) == 0:
        print(0)
        break
    if num[-1] == '0':
        ans *= dp[len(str(int(num)))-1]
    else:
        ans *= dp[len(str(int(num)))]
else:
    print(ans)