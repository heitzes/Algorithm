def solution(arr1, arr2):
    r, c = len(arr1), len(arr2[0])
    answer = [[0]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            answer[i][j] += sum([arr1[i][k]*arr2[k][j] for k in range(len(arr1[0]))])
    return answer