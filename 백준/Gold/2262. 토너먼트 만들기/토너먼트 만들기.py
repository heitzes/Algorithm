n = int(input())
nlist = list(map(int, input().split()))
order = sorted(nlist)[::-1]
answer = 0
for i in order[:-1]:
    ind = nlist.index(i)
    if ind == 0:
        answer += abs(nlist[1] - i)
    elif ind == len(nlist) - 1:
        answer += abs(nlist[-2] - i)
    else:
        answer += min(abs(nlist[ind-1]-i), abs(nlist[ind+1]-i))
    nlist.remove(i)
print(answer)