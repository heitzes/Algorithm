def solution(a, b, n):
    answer = 0
    while n >= a:
        earned = n // a * b
        n += earned - (n - n % a)
        answer += earned
    return answer
