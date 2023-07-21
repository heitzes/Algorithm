def solution(storey):
    answer = 0
    for i in range(1, len(str(storey))+1):
        ref = round(storey/(10**i)) * (10**i)
        answer += abs(ref-storey)/(10**(i-1))
        storey = ref
    if storey != 0:
        answer += 1
    return answer