n, m = map(int, input().split())
nlist = sorted(list(map(int, input().split())))
def backtracking(nums):
    if len(nums) == m:
        print(' '.join(map(str, nums)))
        return
    for i in range(n):
        if nlist[i] in nums: continue
        nums.append(nlist[i])
        backtracking(nums)
        nums.pop()
backtracking([])
