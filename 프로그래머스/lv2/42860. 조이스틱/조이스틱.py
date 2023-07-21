def solution(name):
    answer = 0
    last = 0
    for i in range(len(name)):
        if name[i] != 'A':
            last = max(last, i)
        a, z = abs(ord(name[i])-ord('A')), abs(ord('Z')-ord(name[i])) + 1
        answer += min(a, z)
    part1 = name[:len(name)//2+1]
    part2 = name[len(name)//2+1:]

    first, max1, max2 = 1e9, 0, 0
    for i in range(1, len(part1)):
        if part1[i] != 'A':
            max1 = max(max1, i)
            first = min(first, i)
    if first == 1e9:
        first = 0
    for i in range(len(part2)):
        if part2[i] != 'A':
            max2 = max(max2, len(part2)-i)
    right, left = max1, max2
    traversal = [right*2 + left, left*2 + right, last, len(name)-first]
    return answer + min(traversal)