def solution(elements):
    answer = 0
    nums = set()
    ref = elements * 2
    for i in range(len(elements)):
        for n in range(1, len(elements)+1):
            nums.add(sum(ref[i:i+n]))
    return len(nums)