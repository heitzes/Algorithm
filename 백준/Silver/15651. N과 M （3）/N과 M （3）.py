n, m = map(int, input().split())
nlist = [i for i in range(1, n+1)]
def backtracking(nums):
    if len(nums) == m:
        print(' '.join(map(str, nums)))
        return
    for i in range(n):
        backtracking(nums + [nlist[i]])
backtracking([])