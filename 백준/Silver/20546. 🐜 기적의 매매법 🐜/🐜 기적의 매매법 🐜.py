n = int(input())
nlist = list(map(int, input().split()))
updown = [0, 0]
jmoney, jstock = n, 0
smoney, sstock = n, 0
cnt = 2
for stock in nlist:
    if jmoney == 0: break
    jbuy = jmoney // stock
    jstock += jbuy
    jmoney -= jbuy * stock
for i in range(1, len(nlist)):
    cnt += 1
    stock = nlist[i]
    if stock > nlist[i-1]:
        updown[0] += 1
        updown[1] = 0
    elif stock < nlist[i-1]:
        updown[1] += 1
        updown[0] = 0
    else:
        updown[0], updown[1] = 0, 0
    if updown[0] >= 3:
        smoney += sstock * stock
        sstock = 0
    elif updown[1] >= 3:
        sbuy = smoney // stock
        sstock += sbuy
        smoney -= sbuy * stock
jval = (jmoney + jstock * nlist[-1])
sval = (smoney + sstock * nlist[-1])
if jval > sval:
    print("BNP")
elif jval < sval:
    print("TIMING")
else:
    print("SAMESAME")