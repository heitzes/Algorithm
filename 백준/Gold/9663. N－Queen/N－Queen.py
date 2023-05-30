n = int(input())
answer = 0
def backtracking(ind, nums):
    global answer
    for i, v in enumerate(nums[:-1]):
        if abs(i-(ind-1)) == abs(v-nums[-1]):
            return
    if len(nums) == n:
        answer += 1
    for i in range(1, n+1):
        if i in nums: continue
        if nums and abs(nums[-1]-i) == 1: continue
        nums.append(i)
        backtracking(ind+1, nums)
        nums.pop()
    return answer
print(backtracking(0, []))