n, m = map(int, input().split())
nlist = sorted(list(map(int, input().split())))

def backtracking(nums):
    global n, m
    if len(nums) == m:
        print(' '.join(map(str, nums)))
        return
    for i in range(n):
        if nums and int(nums[-1]) > nlist[i]:
            continue
        backtracking(nums + [nlist[i]])
backtracking([])