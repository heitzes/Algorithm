from itertools import product
ans = list(map(int, input().split()))
nlist = [1, 2, 3, 4, 5]
answer = 0
def compare(perm):
    global answer
    for i in range(8):
        if perm[i] == perm[i+1] == perm[i+2]:
            break
    else:
        cnt = sum([1 if perm[i] == ans[i] else 0 for i in range(10)])
        if cnt >= 5: answer += 1
for a in product(nlist, repeat=10):
    compare(a)
print(answer)