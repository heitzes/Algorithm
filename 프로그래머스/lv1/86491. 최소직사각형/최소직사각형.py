def solution(sizes):
    answer = 0
    new_sizes = [sorted(size) for size in sizes]
    max_w = max([i[0] for i in new_sizes])
    max_h = max([i[1] for i in new_sizes])    
    
    return max_w * max_h