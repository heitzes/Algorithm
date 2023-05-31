n, m = map(int, input().split())
nlist = sorted(list(map(int, input().split())))
nset = set()
def backtracking(nums):
    global n, m
    if len(nums) == m:
        if tuple(nums) not in nset:
            nset.add(tuple(nums))
            print(' '.join(map(str, nums)))
        return
    for i in range(n):
        backtracking(nums + [nlist[i]])
backtracking([])