test = []
while True:
    nlist = list(map(int, input().split()))
    if len(nlist) == 1:
        break
    test.append([nlist[0], nlist[1:]])

def bruteforce(nums, k):
    if len(nums) == 6:
        print(' '.join(map(str, nums)))
        return
    for i in range(k):
        if t[i] in nums: continue
        if nums and t[i] < int(nums[-1]): continue
        bruteforce(nums + [t[i]], k)
    
for i, case in enumerate(test):
    k, t = case
    bruteforce([], k)
    if i != len(test)-1:
        print()