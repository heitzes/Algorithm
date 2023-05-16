from itertools import permutations
def solution(numbers):
    answer = 0
    nlist = list(map(int, list(numbers)))
    permset = set()
    for i in range(1, len(nlist)+1):
        for p in permutations(nlist, i):
            permset.add(int(''.join(map(str, p))))
    def isPrime(num):
        if number < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    for number in permset:
        if isPrime(number):
            answer += 1
    return answer