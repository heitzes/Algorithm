def solution(sizes):
    answer = 0
    current = sizes.pop()
    for size in sizes:
        comp1 = [max(size[0], current[0]), max(size[1], current[1])]
        comp2 = [max(size[1], current[0]), max(size[0], current[1])]
        if comp1[0]*comp1[1] > comp2[0]*comp2[1]:
            current = comp2
        else:
            current = comp1
    return current[0] * current[1]