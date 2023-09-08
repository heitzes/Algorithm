def solution(n, arr1, arr2):
    answer = []
    d = {'1': '#', '0': ' '}
    for i in range(n):
        a, b = arr1[i], arr2[i]
        string = bin(a | b)[2:]
        string = '0'*(n-len(string))+string
        answer.append(''.join([d[j] for j in string]))
    return answer