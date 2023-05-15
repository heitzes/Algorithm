import heapq
def solution(operations):
    nums = []
    for op in operations:
        mode, n = op.split(" ")
        if mode == "I":
            heapq.heappush(nums, int(n))
        elif nums:
            if int(n) == 1:
                nums.pop()
            else:
                heapq.heappop(nums)
    if not nums:
        return [0, 0]
    return [max(nums), nums[0]]