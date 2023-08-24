import math
def solution(n,a,b):
    answer = 0
    a, b = a-1, b-1
    leng = int(math.log(n, 2))
    ab = bin(a ^ b)[2:]
    ab = '0'*(leng-len(ab)) + ab
    ind = ab.index('1')
    return leng-ind