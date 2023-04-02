def solution(n, times):    
    """
    최악의 경우: 심사관 1명, 심사시간 1,000,000,000분, 사람 1,000,000,000명
    -> 최소 심사 시간은 10**18
    심사 시간(x)을 이분탐색 대상으로 잡는다
    -> x시간 안에 심사 할 수 있는 사람의 수 y가 n명 이상이면 x를 줄이고 n명 미만이면 x를 늘린다
    """
    left, right = 1, 10**18
    while left <= right:
        y = 0
        x = (left + right) // 2
        for t in times:
            y += (x // t)
        if y >= n:
            right = x - 1
            answer = x # 가능한 경우 기록!
        else:
            left = x + 1
    return answer