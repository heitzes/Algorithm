from itertools import product
n, s = map(int, input().split())
nlist = list(map(int, input().split()))
pd = list(product(range(2), repeat=n))
answer = 0
pd.pop(0)
for p in pd:
    summ = 0
    for i in range(n):
        if p[i] == 1:
            summ += nlist[i]
    if summ == s:
        answer += 1
print(answer)