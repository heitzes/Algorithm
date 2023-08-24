def solution(arr1, arr2):
    answer = [[sum([a * b for a, b in zip(ra, rb)]) for rb in zip(*arr2)] for ra in arr1]
    return answer