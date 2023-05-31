n, m = map(int, input().split())
nlist = sorted(list(map(int, input().split())))
nset = set()
def backtracking(nums, idx):
    global n, m
    if len(nums) == m:
        if tuple(nums) not in nset:
            nset.add(tuple(nums))
            print(' '.join(map(str, nums)))
        return
    for i in range(n):
        if i in idx: continue
        if nums and int(nums[-1]) > nlist[i]:
            continue
        backtracking(nums + [nlist[i]], idx + [i])
backtracking([], [])