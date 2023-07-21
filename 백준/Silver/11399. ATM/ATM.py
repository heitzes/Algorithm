n = int(input())
nlist = sorted(list(map(int, input().split())))
dp = [0]
for i in nlist:
    dp.append(dp[-1] + i)
print(sum(dp))