n = int(input())
answer = 0
nlist = sorted([[int(input()), i] for i in range(n)])
for i in range(n):
    answer = max(answer, nlist[i][1] - i)
print(answer + 1)