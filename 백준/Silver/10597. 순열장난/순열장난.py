kri = input()
if len(kri) <= 9:
    klen = len(kri)
else:
    klen = (len(kri) - 9)/2 + 9
def backtracking(ind, nums):
    global klen
    if ind >= len(kri):
        print(' '.join(nums))
        exit(0)
    for i in range(1,3):
        num = kri[ind:ind+i]
        if num[0] != '0' and 0 < int(num) <= klen and num not in nums:
            nums.append(num)
            backtracking(ind+i, nums)
            nums.pop()
backtracking(0, [])