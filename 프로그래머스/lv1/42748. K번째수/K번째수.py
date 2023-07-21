def solution(array, commands):
    answer = []
    for comm in commands:
        i, j, k = comm
        answer.append(sorted(array[i-1:j])[k-1])
    return answer