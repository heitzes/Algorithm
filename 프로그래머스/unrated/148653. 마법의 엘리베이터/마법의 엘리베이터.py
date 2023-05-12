def solution(storey):
    answer = 0
    for i in range(1, len(str(storey))):
        ref = round(storey/(10**i)) * (10**i)
        answer += abs(ref-storey)/(10**(i-1))
        storey = ref
    ref = round(storey/(10**len(str(storey)))) * (10**len(str(storey)))
    if ref != 0:
        ref -= storey
        ref = str(ref).replace('0', '')
        return answer + int(ref) + 1
    storey = str(storey).replace('0', '')
    return answer + int(storey)