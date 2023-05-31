n, m = map(int, input().split())
nlist = sorted(list(map(int, input().split())))

def backtracking(nums):
    global n, m
    if len(nums) == m:
        print(' '.join(map(str, nums)))
    for i in range(n):
        if nlist[i] not in nums:
            if nums and nlist[i] <= int(nums[-1]):
                continue
            backtracking(nums + [nlist[i]])
backtracking([])