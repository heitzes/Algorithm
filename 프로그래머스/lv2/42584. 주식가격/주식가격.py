def solution(prices):
    answer, stack = [0], [[prices.pop(), 0]]
    while prices:
        ppop, val = prices.pop(), 0
        while stack and ppop <= stack[-1][0]:
            val += stack[-1][1]
            stack.pop()
        answer.append(val+1)
        stack.append([ppop, val+1])     
    return answer[::-1]