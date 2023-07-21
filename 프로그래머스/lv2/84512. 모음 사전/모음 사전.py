from itertools import product
def solution(word):
    alpha = ['A', 'E', 'I', 'O', 'U']
    permlist = []
    for i in range(1, 6):
        for perm in product(alpha, repeat=i):
            permlist.append(''.join(perm))
    permlist.sort()
    return permlist.index(word) + 1