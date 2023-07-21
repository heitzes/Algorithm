def change(num, n):
    string = ''
    alpha = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    for i in range(10):
        alpha[i] = str(i)
    while num > 0:
        string += alpha[num % n]
        num = num // n
    return list(string[::-1])
def solution(n, t, m, p):
    """
    change: k라는 수를 n진법으로 바꾸는 함수
    nlist: 사람들이 말하는 숫자를 담은 리스트
    모든 사람이 한번씩 말 했을 때 리스트 안의 수는 m개
    -> 튜브가 t개의 수를 말해야 한다면 리스트 안의 수는 최소 m*t개
    """
    num, nlist = 0, ['0']
    while len(nlist) < m * t:
        nlist.extend(change(num, n))
        num += 1
    ans = [nlist[i*m + p-1] for i in range(t)]
    return ''.join(ans)